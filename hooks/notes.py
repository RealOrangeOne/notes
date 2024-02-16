import jinja2
from mkdocs.structure.nav import Navigation, Section
from collections import defaultdict
from mkdocs.utils import meta
from mkdocs.plugins import event_priority

@jinja2.pass_context
def get_page(context, slug):
    nav = context["nav"]
    for page in nav.pages:
        if page.file.src_uri == slug:
            return page

    raise ValueError("Unable to find page for '%s'", slug)


def get_notes_from_nav(nav: Navigation):
    notes_section = next(item for item in nav if item.is_section and item.title == "Notes")

    notes = [item for item in nav.pages if item.is_page and notes_section in item.ancestors and item.file.src_uri != "notes/index.md"]

    return notes_section, notes


@jinja2.pass_context
def get_notes(context):
    notes_section, notes = get_notes_from_nav(context["nav"])

    return sorted(notes, key=lambda p: p.meta["git_creation_date_localized_raw_iso_date"], reverse=True)


def on_env(env, config, files):
    env.tests["startswith"] = str.startswith
    env.globals["get_page"] = get_page
    env.globals["get_notes"] = get_notes


class TagSection(Section):
    """
    A modified section which is active if any of its children are active
    (regardless of what mkdocs tells it).
    """
    @property
    def active(self):
        return any(c.active for c in self.children)

    @active.setter
    def active(self, value: bool):
        pass


@event_priority(100)
def on_nav(nav: Navigation, config, files):
    """
    Structure the nav sections by
    """
    notes_section, notes = get_notes_from_nav(nav)

    notes_page = notes_section.children[0]

    pages_to_tag = defaultdict(list)

    orphan_pages = []

    for note in notes:
        with open(note.file.abs_src_path) as f:
            _, metadata = meta.get_data(f.read())

        if tags := metadata.get("tags"):
            for tag in tags:
                pages_to_tag[tag].append(note)
        else:
            orphan_pages.append(note)

    tag_sections = [
        TagSection(tag, pages)
        for tag, pages in pages_to_tag.items()
    ]

    notes_section.children = tag_sections + orphan_pages + [notes_page]

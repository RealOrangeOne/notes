import jinja2
from mkdocs.structure.nav import Navigation

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

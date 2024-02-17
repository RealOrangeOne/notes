import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from notes import get_notes_from_nav
from mkdocs.structure.nav import Navigation, Section
from collections import defaultdict
from mkdocs.utils import meta
from mkdocs.plugins import event_priority


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
    Structure the nav sections by tag
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

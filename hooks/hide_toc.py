from mkdocs.structure.toc import TableOfContents

def flatten_toc(item):
    yield item
    children = item.items if isinstance(item, TableOfContents) else item.children
    for subitem in children:
        yield from flatten_toc(subitem)


def on_page_content(html, page, config, files):
    if not page.url.startswith("notes/") or page.file.src_uri == "notes/index.md":
        return

    toc = list(flatten_toc(page.toc))

    if len(toc) <= 4:
        hidden_items = page.meta.setdefault("hide", [])
        if "toc" not in hidden_items:
            hidden_items.append("toc")

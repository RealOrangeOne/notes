import jinja2

@jinja2.pass_context
def get_page(context, slug):
    nav = context["nav"]
    for page in nav.pages:
        if page.file.src_uri == slug:
            return page

    raise ValueError("Unable to find page for '%s'", slug)


@jinja2.pass_context
def get_notes(context):
    notes = []
    for page in context["nav"].pages:
        if not page.file.src_uri.startswith("notes/"):
            continue

        if page.file.src_uri == "notes/index.md":
            continue

        notes.append(page)
    return sorted(notes, key=lambda p: p.meta["git_creation_date_localized_raw_iso_date"], reverse=True)


def on_env(env, config, files):
    env.tests["startswith"] = str.startswith
    env.globals["get_page"] = get_page
    env.globals["get_notes"] = get_notes

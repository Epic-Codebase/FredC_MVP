from fasthtml import ft


def page(request, exception):
    info = ft.Titled("Oh, no!", ft.Div("We could not find that page :("))

    return info

from fasthtml import common as fh

from view.auth import page as auth_page

DEV_MODE = True


app, rt = fh.fast_app(live=DEV_MODE)


@rt("/")
def get():
    return fh.H1("WebApp")


app.get("/login")(auth_page)
app.get("/register")(auth_page)


fh.serve()

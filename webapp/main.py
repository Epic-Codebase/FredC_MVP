from fasthtml import common as fh

from view.auth import login, logout
from view.auth import page as auth_page
from view.auth import register

DEV_MODE = True


app, rt = fh.fast_app(live=DEV_MODE)


@rt("/")
def get():
    return fh.H1("WebApp")


# Register routes
app.get("/register")(auth_page)
app.post("/register")(register)
# Login routes
app.get("/login")(auth_page)
app.post("/login")(login)
app.post("/logout")(logout)


fh.serve()

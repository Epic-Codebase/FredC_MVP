from fasthtml import common as fh

import view.auth
from view.notfound import page as notfound_page

DEV_MODE = True


def beforeware():

    return fh.Beforeware(
        view.auth.beforeware,
        skip=[
            r"/favicon\.ico",
            r"/static/.*",
            r".*\.css",
            "/register",
            "/login",
        ],
    )


app, rt = fh.fast_app(
    live=DEV_MODE, exception_handlers={404: notfound_page}, before=beforeware()
)


@rt("/")
def get():
    return fh.H1("WebApp")


# Register routes
app.get("/register")(view.auth.page)
app.post("/register")(view.auth.register)
# Login routes
app.get("/login")(view.auth.page)
app.post("/login")(view.auth.login)
app.get("/logout")(view.auth.logout)


fh.serve()

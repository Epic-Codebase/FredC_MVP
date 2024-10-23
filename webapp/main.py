from fasthtml import common as fh

DEV_MODE = True


app, rt = fh.fast_app(live=DEV_MODE)


@rt("/")
def get():
    return fh.H1("WebApp")


fh.serve()

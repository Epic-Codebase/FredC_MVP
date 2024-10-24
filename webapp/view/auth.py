from hmac import compare_digest

from fasthtml import ft
from fasthtml.common import NotFoundError, RedirectResponse

from model.user import User
from store.user import users

# Status code 303 can change POST to GET
login_redirection = RedirectResponse("/login", status_code=303)


def page():

    return ft.Titled("Test")


def register(user: User, session):

    if not user.name or not user.password:
        return login_redirection

    try:
        user = users[user.name]
        # User found. Can't register again.
        return login_redirection
    except NotFoundError:
        users.insert(user)

    session["auth"] = user.name
    return RedirectResponse("/", status_code=303)


def login(user: User, session):

    if not user.name or not user.password:
        return login_redirection

    try:
        local_user = users[user.name]
    except NotFoundError:
        # User not found. Try again.
        return login_redirection

    # Match passwords
    if not compare_digest(
        user.password.encode("utf-8"), local_user.password.encode("utf-8")
    ):
        return login_redirection

    session["auth"] = user.name
    return RedirectResponse("/", status_code=303)


def logout(session):

    del session["auth"]
    return login_redirection


def beforeware(request, session):

    auth = request.scope["auth"] = session.get("auth", None)

    if not auth:
        return login_redirection

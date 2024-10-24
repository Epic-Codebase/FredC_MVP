from model.user import User
from store.db import db

users = db.create(User, pk="id")

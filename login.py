import hashlib

from ORM_db import Database
from admin import Admin


def login(username, password, db):
    hash_password = hashlib.sha256(str.encode(password)).hexdigest()
    admins = db.select_from_table("admins")
    for row in admins:
        if username == row[1] and hash_password == row[2]:
            return Admin(row[0], row[3])
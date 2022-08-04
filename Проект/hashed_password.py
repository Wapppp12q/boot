from werkzeug.security import generate_password_hash, check_password_hash


def set_password(password):
    hashed_password = generate_password_hash(password)
    return hashed_password


def check_password(hashed_password, password):
    value = check_password_hash(hashed_password, password)
    return value
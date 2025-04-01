def validate_password(str):
    return password == str

def crack_password(valid_chars: str):
    min = 1
    max = 20
    password_iter = password_gen(valid_chars, min, max)
    for password in password_iter:
        if validate_password(password):
            return password
    return None

def password_gen(valid_chars: str, min: int, max: int) -> str:
    password = "".join([valid_chars[0] for _ in range(min)])
    yield password
    for i in range(min, max + 1):
        for j in range(len(password)):
            for k in valid_chars:
                password = f"{password[:j]}{k}{password[j+1:]}"
                yield password
        if (len(password) < max):
            password = f"{valid_chars[0]}{password}"

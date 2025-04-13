from itertools import product
from typing import Optional

def validate_password(password_guess: str) -> bool:
    """
    Replace this with some way of getting the password from the other file
    """
    password = "gbcgef"  
    return password == password_guess

def crack_password(valid_chars: str, min:int = 1, max:int = 20) -> Optional[str]:
    password_iter = password_gen(valid_chars, min, max)
    for password in password_iter:
        if validate_password(password):
            return password
    return None

def password_gen(valid_chars: str, min: int, max: int) -> str:
    for length in range(min, max+1):
        for password_guess in product(valid_chars, repeat=length):
            yield "".join(password_guess)

if __name__ == '__main__':
    print(f"The password is: {crack_password(valid_chars = "abcdefg")}");

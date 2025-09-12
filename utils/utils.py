import random

def generate_email(base_name = "vitaliigr_31qafs_"):
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(3))
    return f"{base_name}{random_digits}@ya.ru"

def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    all_chars = letters + digits
    password = ''.join(random.choice(all_chars) for _ in range(6))
    return password

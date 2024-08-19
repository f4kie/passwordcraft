def validate_password(password, length, use_uppercase, use_numbers, use_special):
    if len(password) < length:
        return False
    if use_uppercase and not any(c.isupper() for c in password):
        return False
    if use_numbers and not any(c.isdigit() for c in password):
        return False
    if use_special and not any(c in string.punctuation for c in password):
        return False
    return True

import random
import string


def generate_random_string(text_length: int = 10) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(characters, k=text_length))

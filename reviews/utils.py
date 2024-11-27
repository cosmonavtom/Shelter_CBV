import string
import random


def slug_generator():
    ''' Генератор слага из латинских букв и цифр. Длина = 20 '''
    return ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=20))

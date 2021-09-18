import string
import random

# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '').replace('#', "")

SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(100)])

print(SECRET_KEY)

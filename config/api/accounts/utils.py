import random

def generate_token():

    return ''.join(random.choices([chr(i) for i in range(27,127)],k=10))
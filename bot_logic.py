import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Cruz"
def comands():

    waos = "```Los Comandos disponibles son: \n $gen para generar una clave \n $moneda para un cara o sello \n $tuki que es sorpresa ```"
    return waos
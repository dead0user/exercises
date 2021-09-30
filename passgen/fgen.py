import random


def string_to_list(word):
    return [char for char in word]

def password_generator(pass_len, pass_dict):
    password = ''
    counter = 0
    for sign in random.sample(pass_dict, pass_len):
        password += sign
        counter += 1
        if counter == pass_len:
            print(password)


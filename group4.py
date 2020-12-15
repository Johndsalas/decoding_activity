import string

def alpha_shift_decryption(message,shift):    

    alpha = string.ascii_lowercase
    alpha = alpha * 2

    new_message = ''

    for char in message:

        if char in alpha:

            char_index = alpha.index(char)

            shift_num = char_index + (shift * -1)

            new_message += alpha[shift_num]

        else:

            new_message += ' '

    return new_message
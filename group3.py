def reverse_letters_decryption(message):

    message = message.split(' ')

    message.reverse()

    return ' '.join(message)
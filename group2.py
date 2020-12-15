def multiply_letters_decryption(message, multiplier = 5):

    count = 0

    new_message =''

    for letter in message:

        if letter.isalpha():

            count += 1

            if count % multiplier == 0:

                new_message += letter

        else:

            new_message += ' '

    return new_message
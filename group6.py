def swap_every_two_words_decryption(message):

    encrypted_message =''

    message_list = message.split(' ')

    duo = []

    for word in message_list:

        duo.append(word)   

        if len(duo) == 2:

            duo.reverse()

            for word in duo:

                encrypted_message += word + ' '

            duo = []

    if len(message_list) % 2 != 0:

        encrypted_message += duo[0]

    return encrypted_message.strip()
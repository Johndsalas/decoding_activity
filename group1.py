def add_special_characters_decryption(message):

    new_message =''

    for character in message:
        
        if character.isalpha():
            
            new_character = character

        elif character in '!#$%^&*':

            new_character = ''

        elif character == '@':

            new_character = ' '

        new_message += new_character

    return new_message
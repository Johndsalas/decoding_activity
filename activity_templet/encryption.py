''' Encrypts a message for the decoding activity'''
import string
import random

def swap_first_and_last_letter(message):  
    
    # create empty string
    encrypted_message = ''  
    
    # convert message string to list of words in string 
    message_list = message.split(' ')
    
    # for each word in the list get the start and end letter
    for word in message_list:
    
        start_letter = word[0]
        
        end_letter = word[-1]
        
        # if the word is grater than 2 letters capture other letters in the string 
        # then assign last_letter plus other_letters plus start_letter plus 'space' to new_word
        if len(word) > 2:
        
            other_letters = word[1:-1]
            
            new_word = end_letter + other_letters + start_letter + ' '
            
        # if the word is two letters long add end_letter plus start_letter plus 'space' to new_word
        elif len(word) == 2:
            
            new_word = end_letter + start_letter + ' '
            
        # if word is one letter add word plus space to new_word
        else:
            
            new_word = word + ' '
        
        # add new_word to encrypted_message
        encrypted_message += new_word

    return encrypted_message.strip() # remove ' ' at end of message


def swap_every_two_words(message):

    # define empty string and empty list
    encrypted_message =''

    duo = []
    
    # change message to list of words
    message_list = message.split(' ')

    
    # add each word in the list to duo
    for word in message_list:

        duo.append(word)   

        # if there are two words in duo 
        # reverse the list 
        # add each word plus a space to encrypted_message 
        # and remove the words from duo
        
        if len(duo) == 2:

            duo.reverse()

            for word in duo:

                encrypted_message += word + ' '

            duo = []

    # if the mwssage has an odd number of words add the last word added to duo to encrypted_message
    if len(message_list) % 2 != 0:

        encrypted_message += duo[0]

    return encrypted_message.strip()


def swap_first_and_last_words(message):

    # split message into list of words
    li = message.split(' ')

    # get length of first and last word
    first_word_index = len(li[0])

    last_word_index = len(li[-1])

    # use length and index to get first word, last word, and other words 
    first_word = message[:first_word_index]

    last_word = message[(last_word_index*-1):]

    other_words = message[(first_word_index):(last_word_index*-1)]

    # return first word plus other words plus last word
    return last_word + other_words + first_word


def alpha_shift(message,shift=3):    

    # get string with alphabet repeated twice and empty string
    alpha = string.ascii_lowercase
    alpha = alpha * 2

    new_message = ''

    #For each character in message if that character is in alph
    for char in message:

        # if that character is in alpha
        if char in alpha:

            # get that characer's first index in alpha
            char_index = alpha.index(char)

            # get the index number that is 'shift' lower than the index number
            shift_num = char_index + (shift * -1)

            # add the letter found at the index of shift_num to new message
            new_message += alpha[shift_num]

        # if character is not in alpha (is a space)
        else:

            # add space to new message
            new_message += ' '

    return new_message


def reverse_letters(message):

    # get list of words
    message = message.split(' ')

    # reverse order of list
    message.reverse()

    # return joined list of reversed words 
    return ' '.join(message)


def multiply_letters(message, multiplier = 5):

    new_message =''
    
    # for each letter in the message
    for letter in message:
    
        # if the letter is an alphabet character
        if letter.isalpha():
        
            # multiply the character and add it to new message
            new_message += (letter * multiplier)
        
        # if it is not 
        else:
            
            # add a ' ' to new message
            new_message += ' '

    return new_message


def add_special_characters(message):

    # get empty list
    new_message =''

    # for each character in the message
    for character in message:

        # if the character is an alpha character
        if character.isalpha():

            # add a random symble after that character in new_character
            new_character = character + random.choice(['!','#','$','%','^','&','*'])

        # if it is not an alpha character    
        else:

            # set new_character to '@' 
            new_character = '@'

         # add new character to new message   
        new_message += new_character

    return new_message

def encrypt_message():

    message = "the answer to life the universe and everything is forty two"

    message = swap_first_and_last_letter(message)
    message = swap_every_two_words(message)
    message = swap_first_and_last_words(message)
    message = alpha_shift(message,shift=3)
    message = reverse_letters(message)
    message = multiply_letters(message, multiplier = 5)
    message = add_special_characters(message)
    return message

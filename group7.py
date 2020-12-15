def swap_first_and_last_letter_decryption(message):  
    
    encrypted_message = ''
    
    message_list = message.split(' ')
    
    for word in message_list:
    
        start_letter = word[0]
        
        end_letter = word[-1]
        
        if len(word) > 2:
        
            other_letters = word[1:-1]
            
            new_word = end_letter + other_letters + start_letter + ' '
            
        elif len(word) == 2:
            
            new_word = end_letter + start_letter + ' '
            
        else:
            
            new_word = word + ' '
            
        encrypted_message += new_word

    return encrypted_message.strip()
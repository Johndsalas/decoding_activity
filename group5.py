def swap_first_and_last_words_decryption(message):

    li = message.split(' ')

    first_word_index = len(li[0])

    last_word_index = len(li[-1])

    first_word = message[:first_word_index]

    last_word = message[(last_word_index*-1):]

    other_words = message[(first_word_index):(last_word_index*-1)]

    return last_word + other_words + first_word
# Decoding Activity

In this activity Students will collaborate on a series of ‘decrypting’ functions that when chained together will decrypt a message from a string of seeming gibberish. The activity illustrates that when a function returns a value it makes that value accessible to code that is outside of the returning function and can serve as a way to introduce the concept of imports.

Steps for the activity are as follows:

1) Instructors choose phrase to be encoded. (phrase should include all lowercase letters to work with examples in the notebook)

2) Instructors run the phrase through a number of encryption functions, provided in the notebook, to get the encoded phrase.

3) Students are split into a number of teams equal to the number of encoding functions used.

4) Each student team is then tasked with creating a decryption function that would undo one of the encryption functions. Example: Write a function that takes in a string of characters and returns a string of characters with the first letter and last letter of each word swapped. 

5) Functions should be submitted to the instructor and copied into separate .py files in the same folder. The instructor can then import each of the .py files into a main .py or notebook file. 

6) Once everything is assembled the instructor can decrypt the original message by Running each of the matching decryption functions in the reverse order that the encryption functions were run during the activity preparation. The input for the first function should be the fully encoded message, then use the output of the first function as the input for the next and so on. should undo the encryption revealing the message. (See notebook for example) The Instructor could also print each function’s output to further illustrate how the message is being changed by ‘filtering’ it through each the functions.

6) The Instructor could also, demonstrate encrypting and decrypting different messages to illustrate function repeatability.

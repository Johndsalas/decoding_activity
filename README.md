# Decoding Activity

In this activity Students will collaborate on a series of ‘decoding’ functions. When chained together the functions will ‘decode’ a message from a string of seeming gibberish. This Activity is intended to illustrate that functions take in a value and then return a value, granting the rest of the code access to the returned value only. This Activity will also introduce the concept of imports. 

Steps for the activity are as follows:

1) Instructors choose phrase to be encoded.

2) Instructors run the phrase through a number of encoding functions, provided in the notebook, to get the encoded phrase.

3) Students are split into a number of teams equal to the number of encoding functions used.

4) Each student team is then tasked with creating a function that would undo one of the encryption functions. Example: Write a function that takes in a string of characters and returns a string of characters with the first letter and last letter of each word swapped. Functions should be submitted or copied into separate .py files.

5) Instructors can then import each of the .py files into a main .py or notebook file. Running the functions in the reverse order beginning with the encrypted message as the first imput and using the output of the first function as the input for the next and so on should undo the encryption revealing the message. Instructors could also print the encrypted message after each function to further illustrate how the message is being changed by ‘filtering’ it through each the functions.

6) Instructors could also use different messages to illustrate repeatability.

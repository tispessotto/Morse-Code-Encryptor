import pandas as pd

data = pd.read_csv("morse_code.txt")

code_dict = {}
for i in data.iterrows():
    code_dict[i[1].LETTER] = i[1].CODE

machine_on = True
while machine_on:
    print("Welcome to Morse Code Encryptor.")
    user_input = input("What sentence would you like encrypted into Morse Code? Letters/Numbers only.").upper()
    words_in_sentence = user_input.split(" ")
    coded_sentence_list = []

    for word in words_in_sentence:
        for letter in word:
            coded_sentence_list += (value for key, value in code_dict.items() if letter == key)
        coded_sentence_list += " "

    coded_sentence = ""
    space_between_letters = "   "
    space_between_words = "       "

    for i in coded_sentence_list[:-1]:
        if i == " ":
            coded_sentence += space_between_words
        else:
            coded_sentence += i
        coded_sentence += space_between_letters

    final_coded_sentence = (coded_sentence[:-3])
    print(f"Your coded sentence is: {final_coded_sentence}")
    keep_asking = True
    while keep_asking:
        keep_going = input("Would you like to encrypt another sentence? Y/N ").upper()
        if keep_going == "N":
            machine_on = False
            keep_asking = False
        elif keep_going == "Y":
            keep_asking = False
        else:
            print("Sorry. Invalid response.")







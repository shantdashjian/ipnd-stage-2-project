# IPND Stage 2 Final Project
# Developer: Shaun Dashjian

import os
import random

#############
# Quiz Data #
#############

########
# Easy #
########
# Numbered blanks and correct inputs
easy_list_numbered_blanks  = [["___1___", "___2___", "___3___", "___4___"],["___1___", "___2___", "___3___"]]
easy_list_correct_inputs = [["function", "parameters", "None", "list"],["boxes", "boxify", "box"]]
# Questions
easy_list_strings = ['''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.''', '''In the DOM, elements are contained in ___1___. Everything in your web page is in ___1___. The term
___2___ is what you do when you break down a design mock into its visual design elements, by
drawing a ___3___ around each element.''']

##########
# Medium #
##########
# Numbered blanks and correct inputs
medium_list_numbered_blanks  = [["___1___", "___2___"],["___1___", "___2___", "___3___"]]
medium_list_correct_inputs = [["DRY", "once"],["why", "what", "how"]]
# Questions
medium_list_strings = ['''___1___ or Don't Repeat Yourself is an important programming concept. It means that you should do
things ___2___ and be able to reuse them. This means more effective development by easier
maintenance, less bugs, and faster expandability. Using CSS rules is a great way to stay ___1___.
''', '''As an expert, use comments to explain ___1___ you did something. Beginners comment to explain
___2___ they did and more advanced developers use comments to explain ___3___ they did it.
''']

########
# Hard #
########
# Numbered blanks and correct inputs.
hard_list_numbered_blanks  = [["___1___", "___2___"],["___1___", "___2___"]]
hard_list_correct_inputs = [["randint", "random"],["mutation", "memory"]]
# Questions
hard_list_strings = ['''To generate random numbers, use the ___1___ function by importing the ___2___ module.
''', '''Lists support ___1___. ___1___ means you can change the value of the variable while keeping
it referring to the same location in ___2___.
''']

def clear_screen():
    # To have a cleaner output
    os.system('cls||clear')

def word_in_numbered_blanks(word, numbered_blanks):
    # To checks if a numbered blank is a substring of the word passed in.
    for blank in numbered_blanks:
        if blank in word:
            return blank
    return None

def guess(quiz_string, numbered_blanks, correct_inputs):
    # To try to guess once
    print "Read the following sentence carefully: "
    print
    print quiz_string
    quiz_string = quiz_string.split()
    # To get user input
    user_inputs = [""] * len(numbered_blanks)
    for index, blank in enumerate(numbered_blanks):
        if blank in "".join(quiz_string):
            user_input = raw_input("Type in a word to replace " + blank + " : ")
            user_inputs[index] = user_input

    # To prepare user answer
    replaced = []
    for word in quiz_string:
        replacement = word_in_numbered_blanks(word, numbered_blanks)
        if replacement != None:
            user_input =  user_inputs[numbered_blanks.index(replacement)]
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    user_replaced = " ".join(replaced)

    # To prepare correct answer
    replaced = []
    for word in quiz_string:
        replacement = word_in_numbered_blanks(word, numbered_blanks)
        if replacement != None:
            correct_input =  correct_inputs[numbered_blanks.index(replacement)]
            word = word.replace(replacement, correct_input)
            replaced.append(word)
        else:
            replaced.append(word)
    correctly_replaced = " ".join(replaced)

    # To show result
    clear_screen()
    if user_replaced == correctly_replaced:
        print "Brilliant! You passed the quiz!"
    else:
        print "You didn't pass the quiz."
    print
    print "Your answer was: "
    print user_replaced
    return user_replaced == correctly_replaced

def play():
    print
    level =""
    print "Please select a game difficulty by typing it in!"
    while level not in ["easy", "medium", "hard"]:
        print "Possible choices include 'easy', 'medium', and 'hard'."
        level = raw_input()
    if level == "easy":
        index = random.randint(0, len(easy_list_strings) - 1)
        quiz_string = easy_list_strings[index]
        numbered_blanks = easy_list_numbered_blanks[index]
        correct_inputs = easy_list_correct_inputs[index]
    if level == "medium":
        index = random.randint(0, len(medium_list_strings) - 1)
        quiz_string = medium_list_strings[index]
        numbered_blanks = medium_list_numbered_blanks[index]
        correct_inputs = medium_list_correct_inputs[index]
    if level == "hard":
        index = random.randint(0, len(hard_list_strings) - 1)
        quiz_string = hard_list_strings[index]
        numbered_blanks = hard_list_numbered_blanks[index]
        correct_inputs = hard_list_correct_inputs[index]
    print "You've chosen " + level + "!"
    print
    print "You will get 5 guesses per problem"
    for guess_no in range (1, 6):
        print "This is guess No. " + str(guess_no)
        print
        result = guess(quiz_string, numbered_blanks, correct_inputs)
        if result == True:
            break
    if result == True:
        print "You win!"
    else:
        print "Try harder next time."

# Main loop
while True:
    play()
    play_again = ""
    while play_again != 'y' and play_again != 'n':
        play_again = raw_input("Play again? (y/n) ")
    if play_again == 'n':
        break
print "Have a nice day!"

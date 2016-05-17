# IPND Stage 2 Final Project
# Developer: Shaun Dashjian

import os
import random

ATTEMPTS = 5

#############
# Quiz Data #
#############

########
# Easy #
########
# Numbered blanks and correct inputs
easy_list_numbered_blanks = [["___1___", "___2___", "___3___", "___4___"],
                             ["___1___", "___2___", "___3___", "___4___"]]
easy_list_correct_inputs = [["function", "parameters", "None", "list"],
                            ["boxes", "boxify", "box", "element"]]
# Questions
easy_list_strings = ['''
A ___1___ is created with the def keyword. You specify the inputs a ___1___
takes by adding ___2___ separated by commas between the parentheses. ___1___s
by default return ___3___ if you don't specify the value to return. ___2___
can be standard data types such as string, number, dictionary, tuple, and
___4___ or can be more complicated such as objects and lambda functions.''',
                     '''
In the DOM, elements are contained in ___1___. Everything in your web page is
in ___1___. The term ___2___ is what you do when you break down a design mock
into its visual design elements, by drawing a ___3___ around each ___4___.''']

##########
# Medium #
##########
# Numbered blanks and correct inputs
medium_list_numbered_blanks = [["___1___", "___2___", "___3___", "___4___"],
                               ["___1___", "___2___", "___3___", "___4___"]]
medium_list_correct_inputs = [["DRY", "concept", "once", "bugs"],
                              ["why", "what", "comments", "how"]]
# Questions
medium_list_strings = ['''
___1___ or Don't Repeat Yourself is an important programming ___2___. It means
that you should do things only ___3___ and be able to reuse them. This means
more effective development by easier maintenance, less ___4___, and faster
expandability. Using CSS rules is a great way to stay ___1___. ''',
                       '''
As an expert, use comments to explain ___1___ you did something. Beginners
comment to explain ___2___ they did and more advanced developers use ___3___
to explain ___4___ they did it. ''']

########
# Hard #
########
# Numbered blanks and correct inputs.
hard_list_numbered_blanks = [["___1___", "___2___", "___3___", "___4___"],
                             ["___1___", "___2___", "___3___", "___4___"]]
hard_list_correct_inputs = [["randint", "random", "two", "upper"],
                            ["mutation", "memory", "return", "append"]]
# Questions
hard_list_strings = ['''
To generate random numbers, use the ___1___ function by importing the ___2___
module. For ___1___, you need ___3___ parameters, one for the lower limit and
the other for the ___4___ limit. ''',
                     '''
Lists support ___1___. ___1___ means you can change the value of the variable
while keeping it referring to the same location in ___2___. Because of
mutation, when you send a list reference to a function, you don't need to
___3___ it when you ___4___ a new item to the end of the list.''']


def clear_screen():
    # To have a cleaner output
    os.system('cls||clear')


def word_in_numbered_blanks(word, numbered_blanks):
    """
    Checks if a numbered blank is a substring of the word passed in.
    :param word: the word.
    :param numbered_blanks: the list of numbered blanks.
    :return: the blank or None.
    """
    for blank in numbered_blanks:
        if blank in word:
            return blank
    return None


def get_level():
    """
    Asks the user which level she want to play and get her preference.
    :return: the level
    """
    clear_screen()
    level = ""
    print "Please select a game difficulty by typing it in!"
    while level not in ["easy", "medium", "hard"]:
        print "Possible choices include 'easy', 'medium', and 'hard'."
        level = raw_input()
    print "You've chosen " + level + "!"
    print
    return level


def get_level_data(level):
    """
    Get level data based on the level the player picked.
    Given the level, a question is picked randomly from a list of possible
    questions.
    :param level: the level
    :return: the apporpriate data
    """
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
    user_inputs = [""] * len(correct_inputs)
    return index, quiz_string, numbered_blanks, correct_inputs, user_inputs


def get_user_input(index, numbered_blanks):
    """
    Get user inputs to replace the numbered blanks.
    :param index: the index of the current blank in question.
    :param numbered_blanks: the list of numbered blanks.
    :return: the user's answer for this blank.
    """
    return raw_input("Type in a word to replace " +
                     numbered_blanks[index] + " : ")


def prepare_solution(index, quiz_string_words, numbered_blanks, inputs):
    """
    Prepare a solution by replacing the blanks with inputs.
    :param index: the index of the current blank in question.
    :param quiz_string_words: the question broken into words.
    :param numbered_blanks: the list of numbered blanks.
    :param inputs: all inputs.
    :return: the question with the answers in place.
    """
    replaced = []
    for word in quiz_string_words:
        replacement = word_in_numbered_blanks(word, numbered_blanks)
        if ((replacement) and
                (numbered_blanks.index(replacement) <= index)):
            the_input = inputs[numbered_blanks.index(replacement)]
            word = word.replace(replacement, the_input)
            replaced.append(word)
        else:
            replaced.append(word)
    return " ".join(replaced)


def result(user_solution, correct_solution):
    """
    Evaluates the player's solution and display it.
    :param user_solution: the user's solution.
    :param correct_solution: the correct solution.
    :return: a boolean showing whether they are the same.
    """
    clear_screen()
    if user_solution == correct_solution:
        print "Correct!"
        print "Here's your answer in place:"
        print user_solution
    else:
        print "Incorrect."
    print
    return user_solution == correct_solution


def guess(index, quiz_string, numbered_blanks, correct_inputs, user_inputs):
    """
    Gets the player to try to guess once.
    :param index: the index of the current blank in question.
    :param numbered_blanks: the list of numbered blanks.
    :param correct_inputs: all correct inputs.
    :param user_inputs: all user inputs.
    :return: the result of the guess and the correct solution.
    """
    print "Read the following sentence carefully: "
    print
    print quiz_string
    print
    quiz_string_words = quiz_string.split()
    # To get user inputs, prepare user solution and correct solution
    user_inputs[index] = get_user_input(index, numbered_blanks)
    user_solution = prepare_solution(index, quiz_string_words,
                                     numbered_blanks, user_inputs)
    correct_solution = prepare_solution(index, quiz_string_words,
                                        numbered_blanks, correct_inputs)
    # To show result
    return result(user_solution, correct_solution), correct_solution


def play():
    """
    Gets the player to play one round.
    """
    level = get_level()
    (index, quiz_string, numbered_blanks, correct_inputs,
     user_inputs) = get_level_data(level)
    print "You will get 5 guesses per blank"
    for index, numbered_blank in enumerate(numbered_blanks):
        for guess_no in range(1, ATTEMPTS + 1):
            (player_answered_correctly,
             correct_solution) = guess(index, quiz_string, numbered_blanks,
                                       correct_inputs, user_inputs)
            if player_answered_correctly:
                quiz_string = correct_solution
                break
            if ATTEMPTS - guess_no > 0:
                print ("You have " + str(ATTEMPTS - guess_no) +
                       " attempts left!")
        if player_answered_correctly is False:
            break
    if player_answered_correctly:
        print "**** You win! ****"
    else:
        print "You ran out of attempts. Good luck next time."


# Main loop
while True:
    play()
    play_again = ""
    while play_again != 'y' and play_again != 'n':
        play_again = raw_input("Play again? (y/n) ")
    if play_again == 'n':
        break
print "Have a nice day!"

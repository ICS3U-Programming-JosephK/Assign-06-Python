#!/usr/bin/env python3
# Created by: Joseph Kwon
# Created on: Dec 21, 2022
# This program asks the user for sentences and translates them to pig latin, frames them, and shuffles the words

import random


def translate_to_pig_latin(sentence):
    # parsing, string to list
    words = sentence.split()
    # setting the list
    pig_latin_words = []

    # pig latin process through for each loop
    for word in words:
        # move the first index, and add "ay"
        pig_latin_word = word[1:] + word[0] + "ay"
        # add the transformed word to the rest
        pig_latin_words.append(pig_latin_word)
    # return the pig latin sentence to main function
    return pig_latin_words


def frame(lst):
    # Find the longest string in the list, this will calculate the frame border
    max_len = 0
    for string in lst:
        max_len = max(max_len, len(string))

    # Create the top and bottom border of the frame
    border = "*" * (max_len + 4)

    # Create the framed list
    framed_list = []
    framed_list.append(border)
    for string in lst:
        framed_list.append("* " + string.center(max_len) + " *")
    framed_list.append(border)

    return framed_list


def shuffle_words(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    # Use the shuffle function from the random module to shuffle the list of words
    random.shuffle(words)
    # Return the shuffled list of words
    return words


def main():
    # Inform the user about their FIRST program
    print("Pig Latin Program:")

    # getting the sentence/word from user
    sentence = input("Enter a sentence: ")
    pig_latin_words = translate_to_pig_latin(sentence)
    # output final result to the user
    print("Translated to Pig Latin:", pig_latin_words)
    print("")

    # Inform the user about their NEXT program
    print("Rectangular Frame Program:")

    # Get the list of strings from the user
    lst = input("Enter a sentence to be framed: ").split()

    # Frame the list of strings
    framed_list = frame(lst)

    # Print the framed list
    print("The framed list is:")
    for string in framed_list:
        print(string)
        print("")

    # Inform the user about their third program
    print("Sentence Mixer Program")
    print("PS: I came up with this program idea (not on the problem list")
    print("")

    # Get the sentence from user
    sentence = input("Enter a sentence: ")
    # Call the shuffle_words function and pass the value of the sentence variable as an argument
    shuffled_words = shuffle_words(sentence)
    # Use the join method to create a string from the shuffled_words list, separated by spaces
    # Then print the resulting string with a message
    print("Shuffled sentence:", " ".join(shuffled_words))


if __name__ == "__main__":
    main()

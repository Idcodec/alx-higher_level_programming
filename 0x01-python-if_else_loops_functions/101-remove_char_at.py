#!/usr/bin/python3
def remove_char_at(str, n):
    New_word = ""

    for i in range(len(str)):
        if i != n:
            New_word += str[i]

	return New_word

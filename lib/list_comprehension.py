#!/usr/bin/env python3

def return_evens(num_list):
    just_evens = [n for n in num_list if (n %2 == 0)]
    print(just_evens)
    return just_evens

def make_exclamation(sentence_list):
    add_exlams = [(n + '!') for n in sentence_list]
    print(add_exlams)
    return add_exlams
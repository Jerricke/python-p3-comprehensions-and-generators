#!/usr/bin/env python3

def return_evens(num_list):
    even = list();
    for num in num_list:
        if num%2 == 0:
            even.append(num)
    return even
    pass

def make_exclamation(sentence_list):
    newArray = list()
    for index in sentence_list:
        newArray.append(index + "!")
        print(newArray)
    return newArray
    pass

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:33:33 2023

@author: ofekd
"""
def revword(file: str):
    return file.lower()[::-1]


def countword():
    file = open("text.txt","r")
    count = 1
    for line in file:
        words = line.split(" ")
        if len(words)==1:
            word = words[0].lower().strip()
        else:
            for j in words :
                word1 = revword(j).strip()
                if word1 == word:
                    count += 1
    print(count)

countword()









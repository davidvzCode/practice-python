from hashlib import new
from operator import le
import random
import os
import re


def game_over():
    return  """ 
    ********      GAME OVER     ********
    ▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
    ▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
    ▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
    ▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
    ▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    █████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    █████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
    ████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
    """

def read():
    word = []
    with open('./files/data.txt','r', encoding='utf-8') as f:
        for line in f:
            word.append(line);
    return word


def verify(word, letter, word_correct):
    if word_correct:
        aux = list(filter(lambda x: x == letter, word_correct))
        if aux:
            return word_correct
    for l in word:
        if l == letter:
            word_correct.append(l)
            break
    return word_correct


def menu():
    data = read()
    word = random.choice(data)
    word_correct = []
    life = 9
    print(word)
    while True:
        print(""" ***   HANGMAN GAME    ***""" + "\n")
        win = 0
        quiz = ""
        for i in word:
            aux = False
            for j in word_correct:
                if j == i:
                    quiz += i + " "
                    aux = True
                    win += 1
                    break 
            if aux == False:
                quiz += "_ "
        if win == len(word)-1:
            break
        print(quiz + "\n")
        letter = input("enter a letter: ")
        bad = word_correct
        word_correct = verify(word, letter, word_correct)
        if len(bad) == len(word_correct):
            life -= 1
        os.system('clear')
        if life == 0:
            break
    if life > 0:
        print("WIN!!!!")
    else:
        print(game_over())


def run():
    menu()


if __name__ == '__main__':
    run()
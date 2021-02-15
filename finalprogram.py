# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:03:09 2021

@author: iceti
"""
menu1 = """

You have selected :"""

menu2 = """
What would you like to do?

1) Test if formula
2) List Atoms
3) List Constants
4) List Variables
5) List Relations
6) Test if satisfiable
7) Add formula to file
8) End"""

from predicate import *

with open("formulae.txt", "r+") as formulae:
    textlist = formulae.readlines()
    print("What formula would you like to examine?")
    count = 0
    formulist = []
    for text in textlist:
        formula = Formula(text)
        formulist.append(formula)
        print(str(count)+"): "+str(formula))
        count += 1
    print(str(count)+"): Enter own formula")
    choice = input("Please input your selection: ")
    if choice == str(len(formulist)):
        text = input("Please input your formula: ")
        formula = Formula(text)
    else:
        formula = formulist[int(choice)]
    done = False
    while not done:
        print(menu1 + str(formula) + menu2)
        choice = input("Please input your selection: ")
        if choice == "1":
            print(formula.isformula())
        elif choice == "2":
            print(formula.listatoms())
        elif choice == "3":
            print(formula.listconstants())
        elif choice == "4":
            print(formula.listvariables())
        elif choice == "5":
            print(formula.listrelations())
        elif choice == "6":
            print(formula.issatisfiable())
        elif choice == "7":
            formulae.write("\n"+formula.getrawtext())
            print(formula.getrawtext())
        else:
            done = True
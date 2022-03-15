# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import csv
import math
import matplotlib.pyplot as plp
import tkinter as tk
from tkinter import ttk

file = open('bazaDanych.csv')

type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
header
rows = []
for row in csvreader:
    rows.append(row)

file.close()

max_cena = 200

# zmienne sztuczna

# HM = [[],[]] #harmony memory
HMS = 10  # harmony memory size
HM = [[0] * 3 for i in range(HMS)]
# petla wypelnia pamiec losowymi rozwiazami
# losowe rozwiazanie do pamieci
# hm rozwiazania

odl = 400
i = 0
while i < HMS:
    first = random.randrange(1, len(rows), 1)
    second = random.randrange(1, len(rows), 1)
    # print("Wartosci R:G:B pierwszego przedmiotu")
    tab1 = str(rows[first]).split(";")
    # print(tab1[2])
    # print(tab1[3])
    tab1[0] = (tab1[0][2:])
    sliced = slice(-2)
    # print(rows[first])
    tab1[4] = (tab1[4][sliced])

    # print(tab1[0])
    # print(tab1[4])

    tab2 = str(rows[second]).split(";")
    # print(i)
    # print("Wartosci R:G:B drugiego przedmiotu")
    # print(tab2[2])
    # print(tab2[3])
    tab2[0] = (tab2[0][2:])
    sliced = slice(-2)
    tab2[4] = (tab2[4][sliced])
    # print(tab2[4])

    odl = math.sqrt(pow((int(tab1[2]) - int(tab2[2])), 2) + pow((int(tab1[3]) - int(tab2[3])), 2) + pow(
        (int(tab1[4]) - int(tab2[4])), 2))
    # print(odl)
    if (max_cena >= int(tab1[1]) + int(tab2[1])):
        HM[i][0] = tab1[0]
        HM[i][1] = tab2[0]
        HM[i][2] = odl
        i = i + 1


def _putInHM(where):
    first = random.randrange(1, len(rows), 1)
    second = random.randrange(1, len(rows), 1)

    tab1 = str(rows[first]).split(";")
    tab1[0] = (tab1[0][2:])
    sliced = slice(-2)
    tab1[4] = (tab1[4][sliced])

    tab2 = str(rows[second]).split(";")
    tab2[0] = (tab2[0][2:])
    sliced = slice(-2)
    tab2[4] = (tab2[4][sliced])

    odl = math.sqrt(pow((int(tab1[2]) - int(tab2[2])), 2) + pow((int(tab1[3]) - int(tab2[3])), 2) + pow(
        (int(tab1[4]) - int(tab2[4])), 2))
    if (max_cena >= int(tab1[1]) + int(tab2[1])):
        HM[i][0] = tab1[0]
        HM[i][1] = tab2[0]
        HM[i][2] = odl

    # print("=============================================")


ftab11 = int(tab1[2])
ftab12 = int(tab1[3])
ftab13 = int(tab1[4])

ftab21 = int(tab2[2])
ftab22 = int(tab2[3])
ftab23 = int(tab2[4])


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


print(HM)

# root window
root = tk.Tk()
root.geometry("960x600")
root.title('1111')

username_label = tk.Label(root, text="", width=20, height=10, bg=_from_rgb((ftab11, ftab12, ftab13)))
username_label.grid(column=0, row=0)
username_label = tk.Label(root, text="", width=20, height=10, bg=_from_rgb((ftab21, ftab22, ftab23)))
username_label.grid(column=1, row=0)
# set window background color
# left_frame = Frame(main_frame, bg=_from_rgb((ftab11, ftab12, ftab13)))
# right_frame = Frame(main_frame, bg=_from_rgb((ftab21, ftab22, ftab23)))
root.mainloop()






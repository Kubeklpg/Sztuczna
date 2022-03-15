# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import csv
import math
import matplotlib.pyplot as plp
from tkinter import *

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


odl = 400
while odl>85:
    first = random.randrange(1, len(rows), 1)
    second = random.randrange(1, len(rows), 1)
    print("Wartosci R:G:B pierwszego przedmiotu")
    tab1 = str(rows[first]).split(";")
    print(tab1[2])
    print(tab1[3])
    sliced = slice(-2)
    tab1[4]=(tab1[4][sliced])
    print(tab1[4])
    
    tab2 = str(rows[second]).split(";")
    print("-------")
    print("Wartosci R:G:B drugiego przedmiotu")
    print(tab2[2])
    print(tab2[3])
    sliced = slice(-2)
    tab2[4]=(tab2[4][sliced])
    print(tab2[4])
    
    odl = math.sqrt(pow((int(tab1[2])-int(tab2[2])),2)+pow((int(tab1[3])-int(tab2[3])),2)+pow((int(tab1[4])-int(tab2[4])),2))
    print(odl)
    print("=============================================")
ftab11 = int(tab1[2])
ftab12 = int(tab1[3])
ftab13 = int(tab1[4])

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb   



# declare the window
window = Tk()
# set window title
window.title("Python GUI App11111")
# set window width and height
window.configure(width=500, height=300)
# set window background color
window.configure(bg=_from_rgb((ftab11, ftab12, ftab13))) 
window.mainloop()

    



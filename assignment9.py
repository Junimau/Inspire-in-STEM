#!usr/bin/python
#############
#  Name :maureen june
#  date :06/08/2022
#  gui_examples using ktinker
#####################


#draw a digital and analog clock using graphical user interface 
#indicating the time

'''
Creation of the Digital Clock in Python
'''
from tkinter import *
from tkinter.ttk import *

from time import strftime

main = Tk()

main.title('The Digital clock in Python')

def clock():
	tick = strftime('%H:%M:%S %p')

	clock_label .config(text =tick)

	clock_label .after(1000, clock)

clock_label = Label(main, font =('sans', 80), background = 'white', foreground = 'purple')

clock_label.pack(anchor= 'center')

clock()
mainloop()
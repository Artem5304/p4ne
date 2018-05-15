#!/usr/bin/python3

from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x): return x.value

wb = load_workbook('/home/velikan/PycharmProjects/p4ne/Lab1.2/data_analysis_lab.xlsx')
sheet = wb['Data']
list_x = list(map(getvalue, sheet['A'][1:]))
list_y1 = list(map(getvalue, sheet['C'][1:]))
list_y2 = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(list_x,list_y1,label="Temp")
pyplot.plot(list_x,list_y2,label="Sun")

pyplot.show()

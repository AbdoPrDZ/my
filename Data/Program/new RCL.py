# -*- coding:Utf-8 -*-
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile
from math import *
from numpy import *
from matplotlib.pyplot import figure,  show
from matplotlib.widgets import MultiCursor
from turtle import *
from time import *

position = os.getcwd()
# print('Run Program:\n')
# print('{}\RCL.exe'.format(position))

root = Tk()
Title = 'RCL Show Graph and Frensel Draw'
root.title(Title)
root.iconbitmap('Icon.ico')
Error1 = 'Not found this circuit...?! '
Error2 = 'Your project is empty...?! '

Um, Ue = "", ""
Im, Ie = "", ""
F, P, T = "", "", ""
Fi, rdFi, EP = "", "", ""
enter, ZR, ZC, ZL, Z = [], "", "", "", ""
U, I, UR, UC, UL, fi, fiward = "", "", "", "", "", "", ""

def Save(event):
	global Um, Ue, Im, Ie, F, P, T, enter, ZR, ZC, ZL, Z, Fi, rdFi, EP, UR, UC, UL
	# print('Save Project')
	if(Um == Ue == Im == Ie == F == P == T == Fi == rdFi == EP == U == I == UR == UC == UL == fi == fiward == ZR == ZC == ZL == ""):
		messagebox.showerror('Error', Error2)
	else:
		txt = 		'{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}\n{8}\n{9}\n{10}\n{11}\n{12}\n{13}\n{14}\n{15}\n{16}\n{17}'.format(Um, Ue, Im, Ie, F, P, T, enter, ZR, ZC, ZL, Z, rdFi, Fi, EP, UR, UC, UL)
		file = asksaveasfile(initialdir = "Documents/RCl Project", title = "Save RCL Project", filetype = [("RCL Project", "*.RCLP"), ("RCL Project", "*.RCLP")])
		# print(file)
		file.write(txt)
		file.close()
	
def Open(event):
	# print('Open Project')
	result = askopenfile(initialdir = "Documents/RCl Project", title = "Open RCL Project", filetypes = (("RCL Project", ".RCLP"), ("Text Documents", ".txt")))
	Link = result.name
	file = open(r'{}'.format(result.name), 'r')
	
	List = file.read().split("\n")
	
	Name = list(Link)
	OTitle = Link.split(".")[0].split("/")[-1]
	root.title('{0} open project: {1}'.format(Title, OTitle))
	Open_chvar(List)
	
def Open_chvar(X):
	global Um, Ue, Im, Ie, F, P, T, enter, ZR, ZC, ZL, Z, Fi, rdFi, EP, UR, UC, UL
	Um, Ue, Im, Ie, F, P, T, enter, ZR, ZC, ZL, Z, rdFi, Fi, EP, UR, UC, UL = float(X[0]), float(X[1]), float(X[2]), float(X[3]), float(X[4]), float(X[5]), float(X[6]), str(X[7]), float(X[8]), float(X[9]), float(X[10]), float(X[11]), float(X[12]), float(X[13]), float(X[14]), float(X[15]), float(X[16]), float(X[17])
	lblrUm.configure(text = round(Um, 2))
	lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
	lblrUe.configure(text = round(Ue, 2))
	lblrIm.configure(text = round(Im, 2))
	lblFI.configure(text = '{} Sin'.format(round(Im,  2)))
	lblrIe.configure(text = round(Ie, 2))
	lblrF.configure(text = round(F, 2))
	lblrP.configure(text = round(P, 2))
	lblrT.configure(text = round(T, 2))
	Enter = ['None', 'RCL', 'RC', 'RL', 'CL', 'R', 'C', 'L']
	I = 0
	while not(Enter[I] == enter):I = I+1
	combo.current(I)
	lblrZ.configure(text = round(Z, 2))
	lblrZR.configure(text = round(ZR, 2))
	lblrZC.configure(text = round(ZC, 2))
	lblrZL.configure(text = round(ZL, 2))
	lblrFI.configure(text = round(Fi, 2))
	lblrEP.configure(text = round(EP, 2))
	lblrrdFI.configure(text = ' = > Radians {} rd'.format(round(rdFi, 2)))
	lblFUFI.configure(text = '+ {})'.format(round(rdFi, 2)))
	lblFIFI.configure(text = '+ {})'.format('0'))
	if(enter == 'None'):
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['disabled'])
		eZC.configure(state = ['disabled'])
		eZL.configure(state = ['disabled'])
		eZ.configure(state = ['enabled'])
		eZ.insert(0, round(Z, 2))
		eFi.configure(state = ['enabled'])
		eFi.insert(0, round(Fi, 2))
	elif(enter == 'RCL'):
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['enabled'])
		eZR.insert(0, round(ZR, 2))
		eZC.configure(state = ['enabled'])
		eZC.insert(0, round(ZC, 2))
		eZL.configure(state = ['enabled'])
		eZL.insert(0, round(ZL, 2))
		eZ.configure(state = ['disabled'])
		eFi.configure(state = ['disabled'])
	elif(enter == 'RC'):
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['enabled'])
		eZR.insert(0, round(ZR, 2))
		eZC.configure(state = ['enabled'])
		eZC.insert(0, round(ZC, 2))
		eZL.configure(state = ['disabled'])
		eZ.configure(state = ['disabled'])
		eFi.configure(state = ['disabled'])
	elif(enter == 'RL'):
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['enabled'])
		eZR.insert(0, round(ZR, 2))
		eZC.configure(state = ['disabled'])
		eZL.configure(state = ['enabled'])
		eZL.insert(0, round(ZL, 2))
		eZ.configure(state = ['disabled'])
		eFi.configure(state = ['disabled'])
	elif(enter == 'CL'):
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['disabled'])
		eZC.configure(state = ['enabled'])
		eZC.insert(0, round(ZC, 2))
		eZL.configure(state = ['enabled'])
		eZL.insert(0, round(ZL, 2))
		eZ.configure(state = ['disabled'])
		eFi.configure(state = ['disabled'])
	elif(enter == 'R'):
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['enabled'])
		eZR.insert(0, round(ZR, 2))
		eZC.configure(state = ['disabled'])
		eZL.configure(stLate = ['disabled'])
		eZ.configure(state = ['disabled'])
		eFi.configure(state = ['disabled'])
	elif(enter == 'C'):
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['disabled'])
		eZC.configure(state = ['enabled'])
		eZC.insert(0, round(ZC, 2))
		eZL.configure(state = ['disabled'])
		eZ.configure(state = ['disabled'])
		eFi.configure(state = ['disabled'])
	elif(enter == 'L'):
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['disabled'])
		eZC.configure(state = ['disabled'])
		eZL.configure(state = ['enabled'])
		eZL.insert(0, round(ZL, 2))
		eZ.configure(state = ['disabled'])
		eFi.configure(state = ['disabled'])

def Examples():
	def Open_Ex(x):
		Cr = ['None', 'RCL', 'RC', 'RL', 'CL', 'R', 'C', 'L']
		# print(Cr[x])
		os.chdir("..")
		os.chdir("Get")
		File = open('UserName.get', 'r')
		User = File.readline()
		User = list(User)
		i = 0
		while not(User[i] == '"'):i = i+1
		User[i] = ""
		while not(User[i] == '"'):i = i+1
		User[i] = ""
		while not(User[i] == '\n'):i = i+1
		User[i] = ""
		User = "".join(User)
		OEx = r"C:/Users/{0}/Documents/RCl Project/Examples/{1}.RCLP".format(User, Cr[x])
		file = open(OEx, 'r')
		
		i1, List = 1, []
		while(i1 <= 18):
			Line = file.readline()
			List.append(Line)
			i1 = i1+1
		Name = list(OEx)
		i2 = 0
		while not(Name[i2] == '.' and Name[i2+1] == 'R' and Name[i2+2] == 'C' and Name[i2+3] == 'L' and Name[i2+4] == 'P'):i2 = i2+1
		A = i2-2
		while not(Name[i2] == "/"):i2 = i2-1
		B = i2
		r = arange(B, A, 1)
		X = []
		while(B <= A):
			B = B+1
			X.append(Name[B])
		OTitle = "".join(X)
		root.title('{0} open project: {1}'.format(Title, OTitle))
		Open_chvar(List)
	
	SpanGenderEx = StringVar()
	shows = Tk()
	ttk.Button(shows, text = 'None',  command = lambda : Open_Ex(0)).pack()
	ttk.Button(shows, text = 'RCL',  command = lambda : Open_Ex(1)).pack()
	ttk.Button(shows, text = 'RC',  command = lambda : Open_Ex(2)).pack()
	ttk.Button(shows, text = 'RL',  command = lambda : Open_Ex(3)).pack()
	ttk.Button(shows, text = 'CL',  command = lambda : Open_Ex(4)).pack()
	ttk.Button(shows, text = 'R',  command = lambda : Open_Ex(5)).pack()
	ttk.Button(shows, text = 'C',  command = lambda : Open_Ex(6)).pack()
	ttk.Button(shows, text = 'L',  command = lambda : Open_Ex(7)).pack()

def RCL_Help(event):
	os.chdir(position)
	os.system('..\\Help\\Help_English.ppsx')

menubar = Menu(root)
filemenu = Menu(menubar,  tearoff = 0)
filemenu.add_command(label = "Open",  command = Open)

filemenu.add_command(label = "Save",  command = Save)

filemenu.add_separator()

filemenu.add_command(label = "Exit",  command = root.quit)
menubar.add_cascade(label = "File",  menu = filemenu)

aboutmenu = Menu(menubar,  tearoff = 0)
aboutmenu.add_command(label = "Examples", command = Examples)
aboutmenu.add_command(label = "Help", command = RCL_Help)
menubar.add_cascade(label = "About",  menu = aboutmenu)

root.config(menu = menubar)

SpanGenderU = StringVar()# U(volt)
SpanGenderI = StringVar()# I(Ampere)
SpanGenderFPT = StringVar()# Frequency(Hz) and Pulse(rd/s) and Tour(ms)

svUm = StringVar()# Umax
svUe = StringVar()# Ueff
svIm = StringVar()# Imax
svIe = StringVar()# Ieff
svF = StringVar()# Frequency(Hz) 
svP = StringVar()# Pulse(rd/s)
svT = StringVar()# Tour(ms)
svZR = StringVar()# Z Resistance
svUR = StringVar()# U Resistance
svZC = StringVar()# Z C
svC = StringVar()# C
svUC = StringVar()# UC
svZL = StringVar()# Z L
svL = StringVar()# L
svUL = StringVar()# UL
svZ = StringVar()# Z
svFi = StringVar()# FI

def callbackUm(svUm):# Umax
	global Um, Ue, Im, Z, rdFi, EP
	Um = float(svUm.get())
	lblrUm.configure(text = Um)
	lblFU.configure(text = '{} Sin'.format(Um))
	Ue = Um/sqrt(2)
	lblrUe.configure(text = round(Ue,  2))
	Z = Um/Im
	lblrZ.configure(text = round(Z,  2))
	cosFi = cos(rdFi)
	EP = Um*Im*cosFi
	lblrEP.configure(text = round(EP, 2))

def callbackUe(svUe):# Ueff
	global Ue, Um, Im, Z, rdFi, EP
	Ue = float(svUe.get())
	lblrUe.configure(text = Ue)
	Um = Ue*sqrt(2)
	lblrUm.configure(text = round(Um,  2))
	lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
	Z = Um/Im
	lblrZ.configure(text = round(Z,  2))
	cosFi = cos(rdFi)
	EP = Um*Im*cosFi
	lblrEP.configure(text = round(EP, 2))

def callbackIm(svIm):# Imax
	global Im, Ie, Um, Z, rdFi, EP
	Im = float(svIm.get())
	lblrIm.configure(text = Im)
	Ie = Im/sqrt(2)
	lblFI.configure(text = '{} Sin'.format(round(Im,  2)))
	lblrIe.configure(text = round(Ie,  2))
	Z = Um/Im
	lblrZ.configure(text = round(Z,  2))
	cosFi = cos(rdFi)
	EP = Um*Im*cosFi
	lblrEP.configure(text = round(EP, 2))

def callbackIe(svIe):# Ieff
	global Ie, Im, Um, Z, rdFi, EP
	Ie = float(svIe.get())
	lblrIe.configure(text = Ie)
	Im = Ie*sqrt(2)
	lblrIm.configure(text = round(Im,  2))
	lblFI.configure(text = '{} Sin'.format(round(Im,  2)))
	Z = Um/Im
	lblrZ.configure(text = round(Z,  2))
	cosFi = cos(rdFi)
	EP = Um*Im*cosFi
	lblrEP.configure(text = round(EP, 2))

def callbackF(svF):# Frequency
	global F, P, T
	F = float(svF.get())
	lblrF.configure(text = F)
	P = int(2*pi*F)
	lblrP.configure(text = round(P,  2))
	lblFUP.configure(text = '({} t'.format(round(P,  2)))
	lblFIP.configure(text = '({} t'.format(round(P,  2)))
	T = 1/F
	lblrT.configure(text = round(T,  2))

def callbackP(svP):# Pulse
	global F, P, T
	P = float(svP.get())
	lblrP.configure(text = P)
	lblFUP.configure(text = '({} t'.format(round(P,  2)))
	lblFIP.configure(text = '({} t'.format(round(P,  2)))
	F = P/(2*pi)
	lblrF.configure(text = round(F,  2))
	T = 1/F
	lblrT.configure(text = round(T,  2))

def callbackT(svT):# Tour
	global F, P, T
	T = float(svT.get())
	lblrT.configure(text = T)
	F = float(1/T)
	lblrF.configure(text = round(F,  2))
	P = float(2*pi*F)
	lblrP.configure(text = round(P,  2))
	lblFUP.configure(text = '({} t'.format(round(P,  2)))
	lblFIP.configure(text = '({} t'.format(round(P,  2)))

def callbackRCL(x):# RCL
	global enter, Fi, rdFi, P, ZR, ZC, ZL, Z, UR, UC, UL, Um, Ue, Im, EP
	enter = combo.get()
	if(enter == "None"):
		Z = float(svZ.get())
		lblrZ.configure(text = Z)
		Fi = float(svFi.get())
		lblrFI.configure(text = Fi)
		rdFi = radians(Fi)
		lblrrdFI.configure(text = ' = > Radians {} rd'.format(round(rdFi, 2)))
		lblFUFI.configure(text = '+ {})'.format(round(rdFi, 2)))
		lblFIFI.configure(text = '+ {})'.format('0'))
		Um = Z*Im
		lblrUm.configure(text = round(Um, 2))
		lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
		Ue = Um/sqrt(2)
		lblrUe.configure(text = round(Ue,  2))
		cosFi = cos(rdFi)
		EP = Um*Im*cosFi
		lblrEP.configure(text = round(EP, 2))
	elif(enter == "RCL"):
		ZR = float(svZR.get())
		lblrZR.configure(text = ZR)
		UR = ZR*Im
		lblrUR.configure(text = ' = > UR {} v'.format(round(UR,  2)))
		ZC = float(svZC.get())
		lblrZC.configure(text = ZC)
		C = 1/(ZC*P)
		lblrC.configure(text = ' = > C {} uF'.format(round(C*10e5)))
		UC = ZC*Im
		lblrUC.configure(text = ' = > UC {} v'.format(round(UC, 2)))
		ZL = float(svZL.get())
		lblrZL.configure(text = ZL)
		L = ZL/P
		lblrL.configure(text = ' = > L {} H'.format(round(L,  2)))
		UL = ZL*Im
		lblrUL.configure(text = ' = > UL {} v'.format(round(UL,  2)))
		Z = sqrt(ZR**2+(ZL-ZC)**2)
		lblrZ.configure(text = round(Z,  2))
		Um = Z*Im
		lblrUm.configure(text = round(Um, 2))
		lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
		Ue = Um/sqrt(2)
		lblrUe.configure(text = round(Ue,  2))
		rdFi = atan((ZL-ZC)/ZR)
		Fi = degrees(rdFi)
		lblrFI.configure(text = round(Fi,  2))
		lblrrdFI.configure(text = ' = > Radians {} rd'.format(round(rdFi, 2)))
		lblFUFI.configure(text = '+ {})'.format(round(rdFi, 2)))
		lblFIFI.configure(text = '+ {})'.format(0))
		cosFi = cos(rdFi)
		EP = Um*Im*cosFi
		lblrEP.configure(text = round(EP, 2))
	elif(enter == "RC"):
		ZR = float(svZR.get())
		lblrZR.configure(text = ZR)
		UR = ZR*Im
		lblrUR.configure(text = ' = > UR {} v'.format(round(UR,  2)))
		ZC = float(svZC.get())
		lblrZC.configure(text = ZC)
		C = 1/(ZC*P)
		lblrC.configure(text = ' = > C {} uF'.format(round(C*10e5)))
		UC = ZC*Im
		lblrUC.configure(text = ' = > UC {} v'.format(round(UC,  2)))
		Z = sqrt(ZR**2+(ZC**2))
		lblrZ.configure(text = round(Z, 2))
		Um = Z*Im
		lblrUm.configure(text = round(Um, 2))
		lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
		Ue = Um/sqrt(2)
		lblrUe.configure(text = round(Ue,  2))
		rdFi = atan(-ZC/ZR)
		Fi = degrees(rdFi)
		lblrFI.configure(text = round(Fi,  2))
		lblrrdFI.configure(text = ' = > Radians {} rd'.format(round(rdFi, 2)))
		lblFUFI.configure(text = '+ {})'.format(round(rdFi, 2)))
		lblFIFI.configure(text = '+ {})'.format(0))
		cosFi = cos(rdFi)
		EP = Um*Im*cosFi
		lblrEP.configure(text = round(EP, 2))
	elif(enter == "RL"):
		ZR = float(svZR.get())
		lblrZR.configure(text = ZR)
		UR = ZR*Im
		lblrUR.configure(text = ' = > UR {} v'.format(round(UR,  2)))
		ZL = float(svZL.get())
		lblrZL.configure(text = ZL)
		L = ZL/P
		lblrL.configure(text = ' = > L {} H'.format(round(L,  2)))
		UL = ZL*Im
		lblrUL.configure(text = ' = > UL {} v'.format(round(UL,  2)))
		Z = sqrt(ZR**2+(ZL**2))
		lblrZ.configure(text = round(Z,  2))
		Um = Z*Im
		lblrUm.configure(text = round(Um, 2))
		lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
		Ue = Um/sqrt(2)
		lblrUe.configure(text = round(Ue,  2))
		rdFi = atan(ZL/ZR)
		Fi = degrees(rdFi)
		lblrFI.configure(text = round(Fi,  2))
		lblrrdFI.configure(text = ' = > Radians {} rd'.format(round(rdFi, 2)))
		lblFUFI.configure(text = '+ {})'.format(round(rdFi, 2)))
		lblFIFI.configure(text = '+ {})'.format(0))
		cosFi = cos(rdFi)
		EP = Um*Im*cosFi
		lblrEP.configure(text = round(EP, 2))
	elif(enter == "CL"):
		ZC = float(svZC.get())
		lblrZC.configure(text = ZC)
		C = 1/(ZC*P)
		lblrC.configure(text = ' = > C {} uF'.format(round(C*10e5)))
		UC = ZC*Im
		lblrUC.configure(text = ' = > UC {} v'.format(round(UC,  2)))
		ZL = float(svZL.get())
		lblrZL.configure(text = ZL)
		L = ZL/P
		lblrL.configure(text = ' = > C {} H'.format(round(L, 2)))
		UL = ZL*Im
		lblrUL.configure(text = ' = > UL {} v'.format(round(UL,  2)))
		Z = sqrt((ZL-ZC)**2)
		lblrZ.configure(text = round(Z, 2))
		Um = Z*Im
		lblrUm.configure(text = round(Um, 2))
		lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
		Ue = Um/sqrt(2)
		lblrUe.configure(text = round(Ue,  2))
		rdFi = atan(ZL-ZC)
		Fi = degrees(rdFi)
		lblrFI.configure(text = round(Fi,  2))
		lblrrdFI.configure(text = ' = > Radians {} rd'.format(round(rdFi, 2)))
		lblFUFI.configure(text = '+ {})'.format(round(rdFi, 2)))
		lblFIFI.configure(text = '+ {})'.format(0))
		cosFi = cos(rdFi)
		EP = Um*Im*cosFi
		lblrEP.configure(text = round(EP, 2))
	elif(enter == "R"):
		ZR = float(svZR.get())
		lblrZR.configure(text = ZR)
		UR = ZR*Im
		lblrUR.configure(text = ' = > UR {} v'.format(round(UR,  2)))
		Z = ZR
		lblrZ.configure(text = Z)
		Um = Z*Im
		lblrUm.configure(text = round(Um, 2))
		lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
		Ue = Um/sqrt(2)
		lblrUe.configure(text = round(Ue,  2))
		Fi = 0
		rdFi = radians(rdFi)
		lblrFI.configure(text = round(Fi,  2))
		lblrrdFI.configure(text = ' = > Radians {} rd'.format(round(rdFi, 2)))
		lblFUFI.configure(text = '+ {})'.format(round(rdFi, 2)))
		lblFIFI.configure(text = '+ {})'.format(0))
		cosFi = cos(rdFi)
		EP = Um*Im*cosFi
		lblrEP.configure(text = round(EP, 2))
	elif(enter == "C"):
		ZC = float(svZC.get())
		lblrZC.configure(text = ZC)
		C = 1/(ZC*P)
		lblrC.configure(text = ' = > C {} uF'.format(round(C*10e5)))
		UC = ZC*Im
		lblrUC.configure(text = ' = > UC {} v'.format(round(UC,  2)))
		Z = ZC
		lblrZ.configure(text = Z)
		Um = Z*Im
		lblrUm.configure(text = round(Um, 2))
		lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
		Ue = Um/sqrt(2)
		lblrUe.configure(text = round(Ue,  2))
		rdFi = atan(-ZC)
		Fi = degrees(rdFi)
		lblrFI.configure(text = round(Fi,  2))
		lblrrdFI.configure(text = ' = > Radians {} rd'.format(round(rdFi, 2)))
		lblFUFI.configure(text = '+ {})'.format(round(rdFi, 2)))
		lblFIFI.configure(text = '+ {})'.format(0))
		cosFi = cos(rdFi)
		EP = Um*Im*cosFi
		lblrEP.configure(text = round(EP, 2))
	elif(enter == "L"):
		ZL = float(svZL.get())
		lblrZL.configure(text = ZL)
		UL = ZL*Im
		lblrUL.configure(text = ' = > UL {} v'.format(round(UL,  2)))
		Z = ZL
		lblrZ.configure(text = Z)
		L = ZL/P
		lblrL.configure(text = ' = > L {} H'.format(round(L, 2)))
		Um = Z*Im
		lblrUm.configure(text = round(Um, 2))
		lblFU.configure(text = '{} Sin'.format(round(Um,  2)))
		Ue = Um/sqrt(2)
		lblrUe.configure(text = round(Ue,  2))
		rdFi = atan(ZL)
		Fi = degrees(rdFi)
		lblrFI.configure(text = round(Fi,  2))
		lblrrdFI.configure(text = ' = > Radians {} rd'.format(round(rdFi, 2)))
		lblFUFI.configure(text = '+ {})'.format(round(rdFi, 2)))
		lblFIFI.configure(text = '+ {})'.format(0))
		cosFi = cos(rdFi)
		EP = Um*Im*cosFi
		lblrEP.configure(text = round(EP, 2))

svUm.trace("w", lambda name, index, mode, svUm = svUm:callbackUm(svUm))
svUe.trace("w", lambda name, index, mode, svUe = svUe:callbackUe(svUe))
svIm.trace("w", lambda name, index, mode, svIm = svIm:callbackIm(svIm))
svIe.trace("w", lambda name, index, mode, svIe = svIe:callbackIe(svIe))
svF.trace("w", lambda name, index, mode, svF = svF:callbackF(svF))
svP.trace("w", lambda name, index, mode, svP = svP:callbackP(svP))
svT.trace("w", lambda name, index, mode, svT = svT:callbackT(svT))
svZR.trace("w", lambda name, index, mode, svZR = svZR:callbackRCL(svZR))
svUR.trace("w", lambda name, index, mode, svUR = svUR:callbackRCL(svUR))
svZC.trace("w", lambda name, index, mode, svZC = svZC:callbackRCL(svZC))
svC.trace("w", lambda name, index, mode, svC = svC:callbackRCL(svC))
svUC.trace("w", lambda name, index, mode, svUC = svUC:callbackRCL(svUC))
svZL.trace("w", lambda name, index, mode, svZL = svZL:callbackRCL(svZL))
svL.trace("w", lambda name, index, mode, svL = svL:callbackRCL(svL))
svUL.trace("w", lambda name, index, mode, svUL = svUL:callbackRCL(svUL))
svZ.trace("w", lambda name, index, mode, svZ = svZ:callbackRCL(svZ))
svFi.trace("w", lambda name, index, mode, svFi = svFi:callbackRCL(svFi))

def RbClicked1():# U(volt)
	global Um, Ue
	if(SpanGenderU.get() == "Umax"):
		Ue = 0
		eUe.delete(0, END)
		eUe.configure(state = ['disabled'])
		lblrUe.configure(text = '0.00')
		eUm.configure(state = ['enabled'])
		# print("Umax")
	elif(SpanGenderU.get() == "Ueff"):
		Um = 0
		eUm.delete(0, END)
		eUm.configure(state = ['disabled'])
		lblrUm.configure(text = '0.00')
		eUe.configure(state = ['enabled'])
		# print("Ueff")
		
def RbClicked2():# I(Ampere)
	global Im, Ie
	if(SpanGenderI.get() == "Imax"):
		Ie = 0
		eIm.configure(state = ['enabled'])
		eIe.delete(0, END)
		eIe.configure(state = ['disabled'])
		lblrIe.configure(text = '0.00')
		# print("Imax")
	elif(SpanGenderI.get() == "Ieff"):
		Im = 0
		eIm.delete(0, END)
		eIm.configure(state = ['disabled'])
		lblrIm.configure(text = '0.00')
		eIe.configure(state = ['enabled'])
		# print("Ieff")
		
def RbClicked3():# Frequency and Pulse and Tour
	global F, P, T
	if(SpanGenderFPT.get() == "Frequency"):
		P, T = 0, 0
		eP.delete(0, END)
		eT.delete(0, END)
		lblrP.configure(text = '0.00')
		lblrT.configure(text = '0.00')
		lblFUP.configure(text = '(P t')
		lblFIP.configure(text = '(P t')
		eF.configure(state = ['enabled'])
		eP.configure(state = ['disabled'])
		eT.configure(state = ['disabled'])
		# print("Frequency")
	elif(SpanGenderFPT.get() == "Pulse"):
		F, T = 0, 0
		eF.delete(0, END)
		eT.delete(0, END)
		lblrF.configure(text = '0.00')
		lblrT.configure(text = '0.00')
		lblFUP.configure(text = '(P t')
		lblFIP.configure(text = '(P t')
		eF.configure(state = ['disabled'])
		eP.configure(state = ['enabled'])
		eT.configure(state = ['disabled'])
		# print("Pulse")
	elif(SpanGenderFPT.get() == "Tour"):
		F, P = 0, 0
		eF.delete(0, END)
		eP.delete(0, END)
		lblrF.configure(text = '0.00')
		lblrP.configure(text = '0.00')
		lblFUP.configure(text = '(P t')
		lblFIP.configure(text = '(P t')
		eF.configure(state = ['disabled'])
		eP.configure(state = ['disabled'])
		eT.configure(state = ['enabled'])
		# print("Tour")	

def EnterEntryRCL():# RCL
	global enter, Um, Ue, Im, Ie, F, P, T, Z, ZR, ZC, C, ZL, L, Fi, rdFi, EP
	enter = combo.get()
	if(enter == "None"):
		ZR, ZC, C, ZL, L, Z, Fi, rdFi, EP = 0, 0, 0, 0, 0, 0, 0, 0, 0
		lblrZR.configure(text = '0.00')
		lblrUR.configure(text = ' = > UR 0.00 v')
		lblrZC.configure(text = '0.00')
		lblrC.configure(text = ' = > C 0.00 uF')
		lblrUC.configure(text = ' = > UC 0.00 v')
		lblrZL.configure(text = '0.00')
		lblrZ.configure(text = '0.00')
		lblrL.configure(text = ' = > L 0.00 H')
		lblrUL.configure(text = ' = > UL 0.00 v')
		lblrFI.configure(text = '0.00')
		lblrrdFI.configure(text = ' = > Radians 0.00 rd')
		lblrEP.configure(text = '0.00')
		lblFUFI.configure(text = '+ Fi)')
		lblFIFI.configure(text = '+ Fi)')
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['disabled'])# ZR
		eZC.configure(state = ['disabled'])# ZC
		eZL.configure(state = ['disabled'])# ZL
		eZ.configure(state = ['enabled'])# Z
		eFi.configure(state = ['enabled'])# Fi
		# print(enter)
	elif(enter == "RCL"):# RCL
		ZR, ZC, C, ZL, L, Z, Fi, rdFi, EP = 0, 0, 0, 0, 0, 0, 0, 0, 0
		lblrZR.configure(text = '0.00')
		lblrUR.configure(text = ' = > UR 0.00 v')
		lblrZC.configure(text = '0.00')
		lblrC.configure(text = ' = > C 0.00 uF')
		lblrUC.configure(text = ' = > UC 0.00 v')
		lblrZL.configure(text = '0.00')
		lblrZ.configure(text = '0.00')
		lblrL.configure(text = ' = > L 0.00 H')
		lblrUL.configure(text = ' = > UL 0.00 v')
		lblrFI.configure(text = '0.00')
		lblrrdFI.configure(text = ' = > Radians 0.00 rd')
		lblrEP.configure(text = '0.00')
		lblFUFI.configure(text = '+ Fi)')
		lblFIFI.configure(text = '+ Fi)')
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['enabled'])# ZR
		eZC.configure(state = ['enabled'])# ZC
		eZL.configure(state = ['enabled'])# ZL
		eZ.configure(state = ['disabled'])# Z
		eFi.configure(state = ['disabled'])# Fi
		# print(enter)
	elif(enter == "RC"):# RC
		ZR, ZC, C, ZL, L, Z, Fi, rdFi, EP = 0, 0, 0, 0, 0, 0, 0, 0, 0
		lblrZR.configure(text = '0.00')
		lblrUR.configure(text = ' = > UR 0.00 v')
		lblrZC.configure(text = '0.00')
		lblrC.configure(text = ' = > C 0.00 uF')
		lblrUC.configure(text = ' = > UC 0.00 v')
		lblrZL.configure(text = '0.00')
		lblrZ.configure(text = '0.00')
		lblrL.configure(text = ' = > L 0.00 H')
		lblrUL.configure(text = ' = > UL 0.00 v')
		lblrFI.configure(text = '0.00')
		lblrrdFI.configure(text = ' = > Radians 0.00 rd')
		lblrEP.configure(text = '0.00')
		lblFUFI.configure(text = '+ Fi)')
		lblFIFI.configure(text = '+ Fi)')
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['enabled'])# ZR
		eZC.configure(state = ['enabled'])# ZC
		eZL.configure(state = ['disabled'])# ZL
		eZ.configure(state = ['disabled'])# Z
		eFi.configure(state = ['disabled'])# Fi
		# print(enter)
	elif(enter == "RL"):# RL
		ZR, ZC, C, ZL, L, Z, Fi, rdFi, EP = 0, 0, 0, 0, 0, 0, 0, 0, 0
		lblrZR.configure(text = '0.00')
		lblrUR.configure(text = ' = > UR 0.00 v')
		lblrZC.configure(text = '0.00')
		lblrC.configure(text = ' = > C 0.00 uF')
		lblrUC.configure(text = ' = > UC 0.00 v')
		lblrZL.configure(text = '0.00')
		lblrZ.configure(text = '0.00')
		lblrL.configure(text = ' = > L 0.00 H')
		lblrUL.configure(text = ' = > UL 0.00 v')
		lblrFI.configure(text = '0.00')
		lblrrdFI.configure(text = ' = > Radians 0.00 rd')
		lblrEP.configure(text = '0.00')
		lblFUFI.configure(text = '+ Fi)')
		lblFIFI.configure(text = '+ Fi)')
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['enabled'])# ZR
		eZC.configure(state = ['disabled'])# ZC
		eZL.configure(state = ['enabled'])# ZL
		eZ.configure(state = ['disabled'])# Z
		eFi.configure(state = ['disabled'])# Fi
		# print(enter)
	elif(enter == "CL"):# CL
		ZR, ZC, C, ZL, L, Z, Fi, rdFi, EP = 0, 0, 0, 0, 0, 0, 0, 0, 0
		lblrZR.configure(text = '0.00')
		lblrUR.configure(text = ' = > UR 0.00 v')
		lblrZC.configure(text = '0.00')
		lblrC.configure(text = ' = > C 0.00 uF')
		lblrUC.configure(text = ' = > UC 0.00 v')
		lblrZL.configure(text = '0.00')
		lblrZ.configure(text = '0.00')
		lblrL.configure(text = ' = > L 0.00 H')
		lblrUL.configure(text = ' = > UL 0.00 v')
		lblrFI.configure(text = '0.00')
		lblrrdFI.configure(text = ' = > Radians 0.00 rd')
		lblrEP.configure(text = '0.00')
		lblFUFI.configure(text = '+ Fi)')
		lblFIFI.configure(text = '+ Fi)')
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['disabled'])# ZR
		eZC.configure(state = ['enabled'])# ZC
		eZL.configure(state = ['enabled'])# ZL
		eZ.configure(state = ['disabled'])# Z
		eFi.configure(state = ['disabled'])# Fi
		# print(enter)
	elif(enter == "R"):# R
		ZR, ZC, C, ZL, L, Z, Fi, rdFi, EP = 0, 0, 0, 0, 0, 0, 0, 0, 0
		lblrZR.configure(text = '0.00')
		lblrUR.configure(text = ' = > UR 0.00 v')
		lblrZC.configure(text = '0.00')
		lblrC.configure(text = ' = > C 0.00 uF')
		lblrUC.configure(text = ' = > UC 0.00 v')
		lblrZL.configure(text = '0.00')
		lblrZ.configure(text = '0.00')
		lblrL.configure(text = ' = > L 0.00 H')
		lblrUL.configure(text = ' = > UL 0.00 v')
		lblrFI.configure(text = '0.00')
		lblrrdFI.configure(text = ' = > Radians 0.00 rd')
		lblrEP.configure(text = '0.00')
		lblFUFI.configure(text = '+ Fi)')
		lblFIFI.configure(text = '+ Fi)')
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['enabled'])# ZR
		eZC.configure(state = ['disabled'])# ZC
		eZL.configure(state = ['disabled'])# ZL
		eZ.configure(state = ['disabled'])# Z
		eFi.configure(state = ['disabled'])# Fi
		# print(enter)
	elif(enter == "C"):# C
		ZR, ZC, C, ZL, L, Z, Fi, rdFi, EP = 0, 0, 0, 0, 0, 0, 0, 0, 0
		lblrZR.configure(text = '0.00')
		lblrUR.configure(text = ' = > UR 0.00 v')
		lblrZC.configure(text = '0.00')
		lblrC.configure(text = ' = > C 0.00 uF')
		lblrUC.configure(text = ' = > UC 0.00 v')
		lblrZL.configure(text = '0.00')
		lblrZ.configure(text = '0.00')
		lblrL.configure(text = ' = > L 0.00 H')
		lblrUL.configure(text = ' = > UL 0.00 v')
		lblrFI.configure(text = '0.00')
		lblrrdFI.configure(text = ' = > Radians 0.00 rd')
		lblrEP.configure(text = '0.00')
		lblFUFI.configure(text = '+ Fi)')
		lblFIFI.configure(text = '+ Fi)')
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['disabled'])# ZR
		eZC.configure(state = ['enabled'])# ZC
		eZL.configure(state = ['disabled'])# ZL
		eZ.configure(state = ['disabled'])# Z
		eFi.configure(state = ['disabled'])# Fi
		# print(enter)
	elif(enter == "L"):# L
		ZR, ZC, C, ZL, L, Z, Fi, rdFi, EP = 0, 0, 0, 0, 0, 0, 0, 0, 0
		lblrZR.configure(text = '0.00')
		lblrUR.configure(text = ' = > UR 0.00 v')
		lblrZC.configure(text = '0.00')
		lblrC.configure(text = ' = > C 0.00 uF')
		lblrUC.configure(text = ' = > UC 0.00 v')
		lblrZL.configure(text = '0.00')
		lblrZ.configure(text = '0.00')
		lblrL.configure(text = ' = > L 0.00 H')
		lblrUL.configure(text = ' = > UL 0.00 v')
		lblrFI.configure(text = '0.00')
		lblrrdFI.configure(text = ' = > Radians 0.00 rd')
		lblrEP.configure(text = '0.00')
		lblFUFI.configure(text = '+ Fi)')
		lblFIFI.configure(text = '+ Fi)')
		eZR.delete(0, END)
		eZC.delete(0, END)
		eZL.delete(0, END)
		eZ.delete(0, END)
		eFi.delete(0, END)
		eZR.configure(state = ['disabled'])# ZR
		eZC.configure(state = ['disabled'])# ZC
		eZL.configure(state = ['enabled'])# ZL
		eZ.configure(state = ['disabled'])# Z
		eFi.configure(state = ['disabled'])# Fi
		# print(enter)
	else:# Else Enter is Error
		# print("ERROR")
		msg = messagebox.showerror('Error', Error1)
		combo.current(0)

def ShowGraph():# Show Graph to U and I
	global Um, Im, Fi, P, T, Z
	t = arange(0,  100,  T)
	fig = figure(0)
	axU = fig.add_subplot(211)
	axU.spines['right'].set_color('none')
	axU.spines['top'].set_color('none')
	axU.xaxis.set_ticks_position('bottom')
	axU.spines['bottom'].set_position(('data', 0))
	axU.yaxis.set_ticks_position('left')
	axU.spines['left'].set_position(('data', 0))
	axU.set_title('Show Graph to Imax, Umax',  fontsize = 25)
	axU.plot(t, Um*sin(P*t+Fi), color = "blue", linewidth = 2.5, linestyle = "-", Label = "U(t)")# U(t)
	axU.grid(True)
	axU.legend(["Umax"])
	axU.set_xlim(0, 40)
	axI = fig.add_subplot(212, sharex = axU)
	axI.spines['right'].set_color('none')
	axI.spines['top'].set_color('none')
	axI.xaxis.set_ticks_position('bottom')
	axI.spines['bottom'].set_position(('data', 0))
	axI.yaxis.set_ticks_position('left')
	axI.spines['left'].set_position(('data', 0))
	axI.plot(t, Im*sin(P*t), color = "green", linewidth = 2.5, linestyle = "-", Label = "I(t)")# I(t)
	axI.grid(True)
	axI.legend(["Imax"])
	axI.set_xlim(0, 40)
	multi = MultiCursor(fig.canvas,  (axU,  axI),  color = 'r',  lw = 1)
	show()

def ShowFrenselDraw():# Show Frensel Draw to U and I to RCL
	global enter, Um, Im, Fi, rdFi, ZR, ZC, ZL, U, I, UR, UC, UL, fi, fiward
	U = Um/2
	# print(U)
	I = Im
	# print(I)
	UR = (ZR*Im)/2
	# print(UR)
	UC = (ZC*Im)/2
	# print(UC)
	UL = (ZL*Im)/2
	# print(UL)
	fi = Fi
	# print(fi)
	fiward = int(fi)
	# print(fiward)
	title('Frensel Draw')
	reset()
	width(5)
	if(enter == "None"):
		# print("None")
		I = I/2
		up()
		backward(I)
		down()
		# I
		color('black')
		forward(I)
		write('I')
		forward(I)
		sleep(1)
		
		up()
		backward(I*2)
		down()
		
		# fi
		left(fi)
		# U
		color('green')
		forward(U*2)
		write('U')
		sleep(1)
		
		up()
		backward(U*2)
		right(fi)
		forward(I+I/2)
		down()
		
		# Fi
		color('red')
		if(fi>0):left(90)
		elif(fi<0):right(90)
		i = 0
		if(fiward>0):fiward = fiward*1
		elif(fiward<0):fiward = fiward*(-1)
		while(i<fiward):
			i = i+1
			if(fi>0):
				forward(2)
				left(1)
			elif(fi<0):
				forward(2)
				right(1)
			if(i == fiward):write('  Fi')
	elif(enter == "RCL"):
		# print("RCL")
		up()
		backward(UR)
		down()
		
		# I
		color('black')
		forward(I)
		write('I')
		sleep(1)
		
		up()
		backward(I)
		down()
		# fi
		left(fi)
		# U
		color('green')
		forward(U*2)
		write('U')
		sleep(1)
		
		up()
		backward(U*2)
		down()
		# UR
		width(2.5)
		color('red')
		right(fi) # Fi
		forward(UR)
		write('  UR')
		forward(UR)
		sleep(1)
		# UL
		color('blue')
		left(90)
		forward(UL)
		write('  UL')
		forward(UL)
		
		up()
		left(-90)
		forward(1.5)
		down()
		
		# UC
		sleep(1)
		color('dark red')
		left(-90)
		forward(UC)
		write('  UC')
		forward(UC)
		sleep(1)
		
		up()
		backward(UC*2)
		right(90)
		backward(2)
		right(90)
		backward(UL*2)
		right(90)
		backward(UR+UR/2)
		down()
		
		# Fi
		color('black')
		if(fi>0):left(90)
		elif(fi<0):right(90)
		i = 0
		if(fiward>0):fiward = fiward*1
		elif(fiward<0):fiward = fiward*(-1)
		while(i<fiward):
			i = i+1
			if(fi>0):
				forward(1)
				left(1)
			elif(fi<0):
				forward(1)
				right(1)
			if(i == fiward):write('  Fi')
	elif(enter == "RC"):
		# print("RC")
		up()
		backward(UR)
		down()
		# I
		color('black')
		forward(I)
		write('I')
		sleep(1)
		
		up()
		backward(I)
		down()
		# fi
		left(fi)
		# U
		color('green')
		forward(U*2)
		write('U')
		sleep(1)
		
		up()
		backward(U*2)
		down()
		# UR
		width(2.5)
		color('red')
		right(fi) # Fi
		forward(UR)
		write('  UR')
		forward(UR)
		sleep(1)
		# UC
		color('dark red')
		left(-90)
		forward(UC)
		write('  UC')
		forward(UC)
		sleep(1)
		
		up()
		backward(UC*2)
		left(90)
		backward(UR)
		down()
		# Fi
		color('black')
		if(fi>0):left(90)
		elif(fi<0):right(90)
		i = 0
		if(fiward>0):fiward = fiward*1
		elif(fiward<0):fiward = fiward*(-1)
		while(i<fiward):
			i = i+1
			if(fi>0):
				forward(2)
				left(1)
			elif(fi<0):
				forward(2)
				right(1)
			if(i == fiward):write('  Fi')
	elif(enter == "RL"):
		# print("RL")
		up()
		backward(UR)
		down()
		# I
		color('black')
		forward(I)
		sleep(1)
		
		up()
		backward(I)
		down()
		# Fi
		left(fi)
		color('green')
		forward(U*2)
		write('U')
		sleep(1)
		
		up()
		backward(U*2)
		down()
		# UR
		width(2.5)
		color('red')
		right(fi) # Fi
		forward(UR)
		write('  UR')
		forward(UR)
		sleep(1)
		# UL
		color('blue')
		left(90)
		forward(UL)
		write('  UL')
		forward(UL)
		
		up()
		backward(UL*2)
		right(90)
		backward(UR)
		down()
		# Fi
		color('black')
		if(fi>0):left(90)
		elif(fi<0):right(90)
		i = 0
		if(fiward>0):fiward = fiward*1
		elif(fiward<0):fiward = fiward*(-1)
		while(i<fiward):
			i = i+1
			if(fi>0):
				forward(2)
				left(1)
			elif(fi<0):
				forward(2)
				right(1)
			if(i == fiward):write('  Fi')
	elif(enter == "CL"):
		up()
		backward(I/2)
		down()
		# I
		color('black')
		forward(I)
		write('I')
		up()
		backward(I)
		sleep(1)
		left(fi) # Fi
		down()
		# U
		color('green')
		forward(U)
		write('U')
		forward(U)
		sleep(1)
		up()
		backward(U*2)
		down()
		right(fi)# -Fi
		left(90)
		width(2.5)
		# UL
		color('blue')
		forward(UL)
		write('  UL')
		forward(UL)
		sleep(1)
		
		up()
		left(-90)
		forward(1.5)
		left(-90)
		down()
		# UC
		color('dark red')
		forward(UC)
		write('  UC')
		forward(UC)
		sleep(1)
	elif(enter == "R"):
		up()
		backward(U)
		down()
		# I
		color('black')
		forward(I)
		write('I')
		sleep(1)
		up()
		backward(I)
		down()
		# U
		color('green')
		forward(U*2)
		write('U')
		sleep(1)
		up()
		backward(U*2)
		down()
		# UR
		color('red')
		forward(UR)
		write('UR')
		forward(UR)
		up()
		backward(UR)
	elif(enter == "C"):
		up()
		backward(I/2)
		down()
		# I
		color('black')
		forward(I)
		write('I')
		sleep(1)
		up()
		backward(I)
		left(fi)
		down()
		# U
		color('green')
		forward(U*2)
		write('U')
		sleep(1)
		up()
		backward(U*2)
		down()
		# UC
		color('dark red')
		forward(UC)
		write('UC')
		forward(UC)
	elif(enter == "L"):
		up()
		backward(I/2)
		down()
		# I
		color('black')
		forward(I)
		write('I')
		sleep(1)
		up()
		backward(I)
		left(fi)
		down()
		# U
		color('green')
		forward(U*2)
		write('   U')
		sleep(1)
		up()
		backward(U*2)
		down()
		# UL
		color('blue')
		forward(UL)
		write('   UL')
		forward(UL)

root.bind("<Control-o>", Open)
root.bind("<Control-s>", Save)
root.bind("<Key-F1>", RCL_Help)

F1 = ttk.Frame(root)
F1.grid(row = 0,  column = 0,  padx = 10,  pady = 10)

# U(volt)
ttk.Label(F1, text = 'U (volt)').grid(row = 0, column = 0, columnspan = 2)
rbUm = ttk.Radiobutton(F1, text = 'Umax', variable = SpanGenderU, value = 'Umax', command = RbClicked1)
rbUm.grid(row = 1, column = 0)
eUm = ttk.Entry(F1, textvariable = svUm, state = ['disabled'])
eUm.grid(row = 1, column = 1)

rbUe = ttk.Radiobutton(F1, text = 'Ueff', variable = SpanGenderU, value = 'Ueff', command = RbClicked1)
rbUe.grid(row = 2, column = 0)
eUe = ttk.Entry(F1, textvariable = svUe, state = ['disabled'])
eUe.grid(row = 2, column = 1)

# I(Ampere)
ttk.Label(F1, text = 'I (Ampere)').grid(row = 3, column = 0, columnspan = 2)
rbIm = ttk.Radiobutton(F1, text = 'Imax', variable = SpanGenderI, value = 'Imax', command = RbClicked2)
rbIm.grid(row = 4, column = 0)
eIm = ttk.Entry(F1, textvariable = svIm, state = ['disabled'])
eIm.grid(row = 4, column = 1)

rbIe = ttk.Radiobutton(F1, text = 'Ieff', variable = SpanGenderI, value = 'Ieff', command = RbClicked2)
rbIe.grid(row = 5, column = 0)
eIe = ttk.Entry(F1, textvariable = svIe, state = ['disabled'])
eIe.grid(row = 5, column = 1)

# Frequency(Hz) and Pulse(rd/s) and Tour(ms)
txt = "    Frequency(Hz)\nPulse(rd/s)tour(ms)"
ttk.Label(F1, text = txt).grid(row = 8, column = 0, columnspan = 2, pady = 2)
rbF = ttk.Radiobutton(F1, text = 'Frequency', variable = SpanGenderFPT, value = 'Frequency', command = RbClicked3)
rbF.grid(row = 9, column = 0)
eF = ttk.Entry(F1, textvariable = svF, state = ['disabled'])
eF.grid(row = 9, column = 1)
rbP = ttk.Radiobutton(F1, text = 'Pulse', variable = SpanGenderFPT, value = 'Pulse', command = RbClicked3)
rbP.grid(row = 10, column = 0)
eP = ttk.Entry(F1, textvariable = svP, state = ['disabled'])
eP.grid(row = 10, column = 1)
rbT = ttk.Radiobutton(F1, text = 'Tour', variable = SpanGenderFPT, value = 'Tour', command = RbClicked3)
rbT.grid(row = 11, column = 0)
eT = ttk.Entry(F1, textvariable = svT, state = ['disabled'])
eT.grid(row = 11, column = 1)

# RCL
F2 = ttk.Frame(root)
F2.grid(row = 0, column = 1,  padx = 10,  pady = 10)

combo = ttk.Combobox(F2)
combo.grid(row = 0, column = 0, columnspan = 2)
combo['values'] = ("None", "RCL", "RC", "RL", "CL", "R", "C", "L")
combo.current(0)

ttk.Button(F2, text = 'Enter', command = EnterEntryRCL).grid(row = 1, column = 1)

ttk.Label(F2, text = 'ZR').grid(row = 2, column = 0)
eZR = ttk.Entry(F2, textvariable = svZR, state = ['disabled'])
eZR.grid(row = 2, column = 1)

ttk.Label(F2, text = 'ZC').grid(row = 3, column = 0)
eZC = ttk.Entry(F2, textvariable = svZC, state = ['disabled'])
eZC.grid(row = 3, column = 1)

ttk.Label(F2, text = 'ZL').grid(row = 4, column = 0)
eZL = ttk.Entry(F2, textvariable = svZL, state = ['disabled'])
eZL.grid(row = 4, column = 1)

ttk.Label(F2, text = 'Z').grid(row = 5, column = 0)
eZ = ttk.Entry(F2, textvariable = svZ)
eZ.grid(row = 5, column = 1)

# FI
ttk.Label(F2, text = 'Fi').grid(row = 6, column = 0)
eFi = ttk.Entry(F2, textvariable = svFi)
eFi.grid(row = 6, column = 1)

# EP
ttk.Label(F2, text = 'EP').grid(row = 7, column = 0)

# Result
ttk.Label(F1, text = ' Result ').grid(row = 0, column = 3)

# Result U(volt)
ttk.Label(F1, text = ' = ').grid(row = 1, column = 2)
lblrUm = ttk.Label(F1, text = '0.00')
lblrUm.grid(row = 1, column = 3)
ttk.Label(F1, text = ' v').grid(row = 1, column = 4)
ttk.Label(F1, text = ' = ').grid(row = 2, column = 2)
lblrUe = ttk.Label(F1, text = '0.00')
lblrUe.grid(row = 2, column = 3)
ttk.Label(F1, text = ' v').grid(row = 2, column = 4)

# Result I(Ampere)
ttk.Label(F1,  text = ' = ').grid(row = 4, column = 2)
lblrIm = ttk.Label(F1, text = '0.00')
lblrIm.grid(row = 4, column = 3)
ttk.Label(F1, text = ' A').grid(row = 4, column = 4)
ttk.Label(F1, text = ' = ').grid(row = 5, column = 2)
lblrIe = ttk.Label(F1, text = '0.00')
lblrIe.grid(row = 5, column = 3)
ttk.Label(F1, text = ' A').grid(row = 5, column = 4)

# Result Frequency and Pulse and Tour
ttk.Label(F1, text = ' = ').grid(row = 9, column = 2)
lblrF = ttk.Label(F1, text = '0.00')
lblrF.grid(row = 9, column = 3)
ttk.Label(F1, text = ' Hz').grid(row = 9, column = 4)
ttk.Label(F1, text = ' = ').grid(row = 10, column = 2)
ttk.Label(F1, text = ' rd/s').grid(row = 10, column = 4)
lblrP = ttk.Label(F1, text = '0.00')
lblrP.grid(row = 10, column = 3)
ttk.Label(F1, text = ' = ').grid(row = 11, column = 2)
lblrT = ttk.Label(F1, text = '0.00')
lblrT.grid(row = 11, column = 3)
ttk.Label(F1, text = ' s').grid(row = 11, column = 4)

# Result RCL
ttk.Label(F2, text = 'Result').grid(row = 1, column = 2, columnspan = 2, padx = 10)

ttk.Label(F2, text = ' = ').grid(row = 2, column = 2)
lblrZR = ttk.Label(F2, text = '0.00')
lblrZR.grid(row = 2, column = 3)
ttk.Label(F2, text = ' Ohom').grid(row = 2, column = 4)
lblrUR = ttk.Label(F2, text = ' = > UR 0.00 v')
lblrUR.grid(row = 2, column = 5)

ttk.Label(F2, text = ' = ').grid(row = 3, column = 2)
lblrZC = ttk.Label(F2, text = '0.00')
lblrZC.grid(row = 3, column = 3)
ttk.Label(F2, text = 'Ohom').grid(row = 3, column = 4)
lblrC = ttk.Label(F2, text = ' = > C 0.00 uF')
lblrC.grid(row = 3, column = 5)
lblrUC = ttk.Label(F2, text = ' = > UC 0.00 v')
lblrUC.grid(row = 3, column = 6)

ttk.Label(F2, text = ' = ').grid(row = 4, column = 2)
lblrZL = ttk.Label(F2, text = '0.00')
lblrZL.grid(row = 4, column = 3)
ttk.Label(F2, text = 'Ohom').grid(row = 4, column = 4)
lblrL = ttk.Label(F2, text = ' = > L 0.00 H')
lblrL.grid(row = 4, column = 5)
lblrUL = ttk.Label(F2, text = ' = > UL 0.00 v')
lblrUL.grid(row = 4, column = 6)

ttk.Label(F2, text = ' = ').grid(row = 5, column = 2)
lblrZ = ttk.Label(F2, text = '0.00')
lblrZ.grid(row = 5, column = 3)
ttk.Label(F2, text = ' Ohom').grid(row = 5, column = 4)

# Result FI
ttk.Label(F2, text = ' = ').grid(row = 6, column = 2)
lblrFI = ttk.Label(F2, text = '0.00')
lblrFI.grid(row = 6, column = 3)
ttk.Label(F2, text = 'Degrees').grid(row = 6, column = 4)
lblrrdFI = ttk.Label(F2, text = ' = > Radians 0.00 rd')
lblrrdFI.grid(row = 6, column = 5)

# Result EP
lblrEP = ttk.Label(F2, text = '0.00')
lblrEP.grid(row = 7, column = 1)
ttk.Label(F2, text = 'Watt').grid(row = 7, column = 2)

# Final
F3 = ttk.Frame(root)
F3.grid(row = 1, column = 0, columnspan = 2, pady = 20)

# U(t)
ttk.Label(F3, text = 'Final U(t):').grid(row = 0, column = 0)
lblFU = ttk.Label(F3, text = 'Umax Sin')
lblFU.grid(row = 0, column = 1)
lblFUP = ttk.Label(F3, text = '(P t')
lblFUP.grid(row = 0, column = 2)
lblFUFI = ttk.Label(F3, text = '+ Fi)')
lblFUFI.grid(row = 0, column = 3)

# I(t)
ttk.Label(F3, text = 'Final I(t):').grid(row = 1, column = 0)
lblFI = ttk.Label(F3, text = 'Imax Sin')
lblFI.grid(row = 1, column = 1)
lblFIP = ttk.Label(F3, text = '(P t')
lblFIP.grid(row = 1, column = 2)
lblFIFI = ttk.Label(F3, text = '+ Fi)')
lblFIFI.grid(row = 1, column = 3)

# Create a Graph
buG = ttk.Button(F3, text = 'Show a Graph')
buG.grid(row = 0, column = 4, rowspan = 2, padx = 20)
buG.config(command = ShowGraph)

# Create a Fresnel representation
buF = ttk.Button(F3, text = 'Show Fresnel Draw')
buF.grid(row = 0, column = 5, rowspan = 2, padx = 20)
buF.config(command = ShowFrenselDraw)

root.mainloop()
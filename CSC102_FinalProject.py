#!/usr/bin/env python3.6
# First line is for Linux/UNIX compatibility
# Calls Python3.6 for those not versed in Linux
######
# This is a substitute assignment for the Stock portfolio 1 & 2
# and NASCAR programs, as well as final discussion.
# This is pre-alpha of the final product which will host a suite of tools
# that can be used in the NETSEC world.
######
#Coming up:
#	Finishing the Port scanner
#	Cleaning up the code
#   Aesthetic touches
#   Anything else I can think of
#	This project will have it's own repo on GitHub shortly
######
#
# Huge thanks to StackOverflow, without that, this would not have gotten done!!
#
######
# Adam Morris
# CSC102
# Substitute assignment
# Professor Gose
######
#Library - Scapy needs to be installed
from scapy.all import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import os, sys, time, threading, socket, subprocess
######
#Basic window
root = Tk()
root.title("CSC102 Final Project")	#Window title
root.geometry("400x300")     		#Basic window size
root.resizable(False, False) 		#Prevents resising
######
#Button functions
def netInfo():
	def linuxNet():
		net = os.system('ifconfig')

	def windowsNet():
		net = os.system('ipconfig /all')

	main = Tk()
	main.title('Network Information')
	main.geometry('300x100')
	b1 = Button(main, text='Linux', command=linuxNet)
	b2 = Button(main, text='Windows', command=windowsNet)
	b1.place(x = 0, y = 50)
	b2.place(x = 0, y = 0)
	main.mainloop()

#done
def ping():
	ping = sr1(IP(dst="www.google.com")/ICMP()/"XXXXXXXXXXX")	#Pings google to test for network connectivity
	ping.show()													#Breakdown of the ICMP request
	
#mostly done - To do: add contrast to the menu
def fileHandling():
	#A way to open files to view their contents in the terminal
	filename = filedialog.askopenfilename(parent=root)	#starting location
	f = open(filename)									#opens the file 
	f.read
	for line in f:
		print (line)									#Prints each line that is in the file

#done
def screenClear():
	if sys.platform.startswith('linux'):    #Linux Detection
		os.system('clear') 					#clear screen command for Linux

	if sys.platform.startswith('win32'):	#Windows Detection
		os.system('cls') 					#clear screen command for Linux

###################################################################
#class for the port scanner
class PortScannerGUI(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		#Building the GUI
		self.main = Tk()
		self.main.geometry("550x500")
		self.main.title("Port Scanner")
		self.buttons()
		self.stop = False

	#building out the buttons
	def buttons(self):
		main = self.main

		#Default input frame
		inFrame = Frame(main, width="250")
		inFrame.pack(pady=15, padx=15)

		#some labels
		start =  Label(inFrame, text="Start:")
		end   =  Label(inFrame, text="End:")
		port  =  Label(inFrame, text="Port:")
		self.rangeStartEntry = Entry(inFrame)
		self.rangeEndEntry = Entry(inFrame)


		#placing the buttons
		start.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        end.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.rangeStartEntry.grid(row=0, column=1, padx=5, pady=5)
        self.rangeEndEntry.grid(row=0, column=3, padx=5, pady=5)
        portLabel.grid(row=1, column=2, padx=5, pady=5, sticky=W)
		
		#console
        self.consoleFrame = Frame(root)
        self.consoleFrame.pack(expand=1, pady=15, padx=15, fill= BOTH)
        self.consoleText = Text(self.consoleFrame, fg="green", bg="black",state=DISABLED)
        self.consoleText.pack(expand=1, fill= BOTH)


    #The main portion of the tool
	def netScan(self):
		# Tells the user what to do
		#a = messagebox.showinfo("Port Scan", "Click 'ok' to start the scan")
		#print(a)
		#Dictionary with the common ports and their associated services
		commonPorts = {

		'21' : 'FTP', \
		'22' : 'SSH', \
		'23' : 'TELNET', \
		'25' : 'SMTP', \
		'53' : 'DNS', \
		'69' : 'TFTP', \
		'80' : 'HTTP', \
		'110' : 'POP3', \
		'123' : 'NTP', \
		'137' : 'NETBIOS-NS', \
		'138' : 'NETBIOS-DGM', \
		'139' : 'NETBIOS-SSN', \
		'143' : 'IMAP', \
		'389' : 'LDAP', \
		'443' : 'HTTPS', \
		'995' : 'POP3-SSL', \
		'993' : 'IMAP-SSL', \
		'3306' : 'MYSQL',
	
		}
		#empty list for storing open ports
		openPorts = []

###################################################################

class HexConverterGUI():
	def __init__(self):
																									#Designing the GUI
		self.main_window = Tk()
		self.main_window.title("HEX Converter")
		self.topFrame = tk.Frame(self.main_window)
		self.bottomFrame = tk.Frame(self.main_window)
																									#User input for hex values
		self.hexPrompt = tk.Label(self.topFrame, text="Enter the HEX value")
		self.hexEntry = tk.Entry(self.topFrame, width=10)
																									#Packs the label and entry widgets
		self.hexPrompt.pack(side='left')
		self.hexEntry.pack(side='left')
																									#Buttons
		self.hexCalc = tk.Button(self.bottomFrame, text='Convert', command=self.convert)
		self.hexQuit = tk.Button(self.bottomFrame, text='QUIT', command=self.main_window.destroy)
																									#packs the buttons
		self.hexCalc.pack(side='left')
		self.hexQuit.pack(side='left')
																									#packs the frame
		self.topFrame.pack()
		self.bottomFrame.pack()

		tk.mainloop()																				#Starts the GUI

	def convert(self):																				#Conversion function
		hexes = self.hexEntry.get()																	#Gets hex values

		hexx = str(hexes).lstrip("0x")																#Strips the "0x" from the HEX so the user can enter either "0x63" or "63" and get the same result

		convert = bytearray.fromhex(hexx).decode()													#decodes the hex value
																									#Prints the results
		tk.messagebox.showinfo('Results',\
			str(hexes) + ' in ASCII is ' + \
			str(convert))

##################################################################################################
#buttons

button1 = Button(root, text= "Net Information", fg = 'green', bg = 'black', command = netInfo)
button1.place(x = 0, y = 0)

button2 = Button(root, text= "Test network connection", fg = 'green', bg = 'black', command = ping)
button2.place(x = 0, y = 50)

button3 = Button(root, text= "Clear Terminal screen", fg = 'green', bg = 'black', command = screenClear)
button3.pack(side=BOTTOM)

button4 = Button(root, text= "Port Scan (Still in development)", fg = 'green', bg = 'black', command = PortScannerGUI)
button4.place(x = 0, y = 100)

button5 = Button(root, text= "HEX converter", fg = 'green', bg = 'black', command = HexConverterGUI)
button5.place(x = 0, y = 150)

##################################################################################################
#Menubar
menubar = Menu(root)
##############################################
#this builds out the 'file' menu tab or exit from the program
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=fileHandling)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
#Configures the main window
root.config(background='black', menu=menubar)

#Main loop
root.mainloop()

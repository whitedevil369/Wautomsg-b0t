import pyautogui 
import time
import sys
from pyfiglet import Figlet
import argparse
#from positionfinder import positions
#from pynput.mouse import Listener          


parser = argparse.ArgumentParser()
parser.add_argument("-s","--senderNumber", help="Enter your whatsapp number in the format <country_code><your_number> without starting with +/0 and without any spaces in between")
parser.add_argument("-r","--recipientFile", help="Enter the path of the .txt file containing the list of recipient phone numbers in the same format as the sender number")
parser.add_argument("-m","--mode", help="Set the mode of entry of the messege (file/cli)")
parser.add_argument("-f","--fileMessege", help="enter the path of file containing the messege")
args = parser.parse_args()



def br():
	pyautogui.hotkey('shift', 'enter')

def exit_timer():
	t=0
	cl=3
	print("Quitting in 3 seconds...")
	time.sleep(1)
	for t in range(0,3):
		print(cl)
		time.sleep(1)
		t=t+1
		cl=cl-1
	print("Quiting...")

def alert():
	t=0
	cl=3
	print("ALERT! The b0t will start in 3 seconds.")
	time.sleep(1)
	for t in range(0,3):
		print(cl)
		time.sleep(1)
		t=t+1
		cl=cl-1
	print("b0t STARTED...")	

'''
def on_click(x, y, button, pressed):       
	if pressed:
		global pos_x
		pos_x = x
		
		global pos_y
		pos_y = y
	if not pressed:
		return False
'''

def home():
	f1 = Figlet(font='rounded')
	f2 = Figlet(font='digital')
	print ("Name: Wautomsg-b0t")
	print ("version: 1.0")
	print ("@whitedevil369")
	print (f1.renderText('Wautomsg-b0t'))
	print (f2.renderText("Made by Poornesh Adhithya"))
	print ("\nWELCOME TO Wautomsg-b0t\nWautomsg-b0t is a WHATSAPP MASS/BULK MESSAGE SENDER\n(WITHOUT SAVING THE PHONE NUMBERS IN CONTACTS)\n")
	input("\nPRESS ENTER TO CONTINUE.\n\nb0t:~#> ")

home()

if(args.senderNumber==None):
	print ("\nENTER SENDER PHONE NUMBER: ")
	print ("format: <country_code><phone_number> (without + or 00 or spaces)")
	print ("Eg. 911234567890\nWhere 91 is the Country Code and 1234567890 is phone number")
	sender_ph = input("\nb0t:~#> ")
	print("\n")
else:
    sender_ph = args.senderNumber


if not sender_ph.isdigit() or '\n' in sender_ph:
	print("PHONE NUMBER SHOULD CONTAIN ONLY DIGITS")
	exit_timer()
	exit()
if(args.recipientFile==None):
	print ("\nENTER THE SOURCE LOCATION OF THE PHONE NUMBERS LIST: ")
	print ("Eg. /root/Desktop/contacts.txt\nIf it exists in the same dirctory of the file then,\nEg. contacts.txt")
	src = input("\nb0t:~#> ")
	print("\n")
else:
    src = args.recipientFile
try:
	phone_file=open(src)
	phone=phone_file.readlines()

except:
	print("RECIPIENT FILE DOESN'T EXIST!")
	exit_timer()		
	exit()


if not src.endswith('.txt'):
	print("ONLY .txt FILE FORMAT IS ACCEPTED")
	exit_timer()
	exit()

counter=0
for p in phone: 
	x=p.split('\n')
	p=x[0]
	if p and p.isdigit(): 
		counter += 1
	else:
		print("PHONE NUMBERS SHOULD CONTAIN ONLY DIGITS")
		exit_timer()
		exit()

if(args.mode == None):
	print ("\nENTER YOUR MODE OF MESSAGING (cli/file): ")
	print ("cli to enter Message in the terminal.\nfile to import the location of the file")
	c = input("\nb0t:~#> ")
	print("\n")
else:
    c = args.mode
if c=='file':
	if(args.fileMessege==None):
		print ("\nENTER THE SOURCE LOCATION OF THE MESSAGE: ")
		print ("Eg. /root/Desktop/samplemsg.txt\nIf it exists in the same dirctory of the file then,\nEg. samplemsg.txt")
		loc = input("\nb0t:~#> ")
	else:
		loc = args.fileMessege
	if not loc.endswith('.txt'):
		print("ONLY .txt FILE FORMAT IS ACCEPTED")
		exit_timer()		
		exit()
	try:
		msg_file=open(loc)
		msg=msg_file.readlines()
		message=''
	except:
		print("FILE DOESN'T EXIST!")
		exit_timer()		
		exit()

elif c=='cli':
	print ("\nTYPE THE MESSAGE: ")
	print ("Once you are done, Press ENTER and then Ctrl+D to end the Message")
	print ("\nb0t:~#> ")
	message=sys.stdin.read()
	msg=''
	m=''

else:
	print("INVALID CHOICE!")
	exit_timer()
	exit()
'''
print("Place your mouse pointer on the text of latest/recent message from the WhatsApp chatbox and click on it")   
print("(Eg. place your mouse pointer on the text of 'Hi' message which was entered earlier during the setup phase)")
input("\nPRESS ENTER AND THEN CLICK THE MESSAGE. AFTER CLICKING IT PRESS ENTER AGAIN! (MAKE SURE TO CLICK AFTER 3 Seconds)\n\nb0t:~#> ")

with Listener(
        on_click=on_click,
        ) as listener:
    listener.join()
'''
#<----------------------------------------------------->

#positions
pos_x = 1441	# value of x in positionfinder.py
pos_y = 959	# value of y in positionfinder.py
#THIS IS FOR 1600x900 RESOLUTION, VALUES MAY CHANGE ACCORDING TO YOUR PCs RESOLUTION. (use positionfinder.py tool to find your mouse position)
#Change These Values Before Executing

#<----------------------------------------------------->

input("\nPRESS Enter To Start The b0t and then Switch to WhatsApp Web.\n\nb0t:~#> ")
print("\nYou have 5 seconds to switch to WhatsApp Web.....")
time.sleep(5)
print("Switch to WhatsApp Web, Your running out of time...\n")
alert()
time.sleep(1)
pyautogui.typewrite('Wa.me/'+sender_ph)
pyautogui.press('enter')
position = pos_x,pos_y
pyautogui.click(position)
time.sleep(1)
pyautogui.press('esc')
time.sleep(2)
pyautogui.press('esc')
time.sleep(1)
pyautogui.typewrite('Test Message')
pyautogui.press('enter')

i=0
try:
	for number in phone:
		time.sleep(2)
		pyautogui.typewrite('Wa.me/'+number)
		pyautogui.press('enter')	
		pyautogui.click(position)
		time.sleep(1)
		pyautogui.press('esc')
		time.sleep(2)
		pyautogui.press('esc')
		time.sleep(1)
		#pyautogui.typewrite('Write Something')
		#br() #Use This to go to new line without sending the message 
		for m in msg:
			pyautogui.typewrite(m)	
		pyautogui.typewrite(message)
		time.sleep(1)
		pyautogui.press('enter')
		time.sleep(3)
		pyautogui.press('tab')
		pyautogui.press('tab')		
		pyautogui.typewrite(sender_ph)
		pyautogui.press('enter')
		i=i+1
		print ("Message has been sent to "+str(i)+" of "+str(counter)+" Recipients")
	time.sleep(2)
	pyautogui.typewrite("Messages Sent Successfully!")
	br()
	pyautogui.typewrite("Thank-You! See You Next Time.")
	br() 
	pyautogui.typewrite("Good Bye!")	
	pyautogui.press('enter')
	print ("\nMessages Sent Successfully!")
	print("\nHOPE THIS TOOL HELPED YOU!\nTHANKS FOR USING THIS TOOL.")

except:
	print("\nProcess Terminating...")
	msg_file.close()
	phone_file.close()
	exit()

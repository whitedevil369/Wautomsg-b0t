# Wautomsg-b0t
Easy to use, Whatsapp Web Mass/Bulk Messaging b0t (without saving the numbers in contacts, No APIs, No Additional Downloads required)

# Compatibility
Tested and Works on Debian based Linux, Windows and (MAC OS (yet to be tested)), etc. <br />
Works on Browsers like Google Chrome, Firefox, (Safari(yet to be tested)), etc. <br />

# Setup
1. Install WhatsApp Application on your mobile phone (iOS/Android/Any) (If you don't have) <br />
2. Register your account with your phone number. <br />
3. Open your native browser through your mobile (Safari/Chrome) and type the following Wa.me/<country_code><your_phone_number> without (+/00/spaces)
and you will be Redirected to your WhatsApp Chatbox, To keep the chat alive, just send a message "Hi" (or any other message) <br />
4. Open your native Browser on your PC and open this <a href="https://web.whatsapp.com/">link</a>. <br />
5. You will get a QR Code in that webpage, Scan that QR Code using your WhatsApp mobile Application (Settings>WhatsApp Web/Desktop>Scan QR Code) <br />
6. Go to Your Chatbox (Your Phone Number) and Now your good to go.

# Requirements
<b>git (for git clone method):<br /></b>
Click This <a href="https://git-scm.com/downloads">Link</a> for Downloading & This <a href="https://git-scm.com/book/en/v2/Getting-Started-Installing-Git">Link</a> for Installation. <br />
For Debian based Linux, <br /> 
$ sudo apt-get install git <br /><br />
<b>python & pip:<br /></b>
Click This <a href="https://www.python.org/downloads/">Link</a> for Downloading Python & Installing pip
  
# Installation
You can either Download the zip file and extract it or
Open your Terminal and type the following: <br />
git clone https://github.com/whitedevil369/Wautomsg-b0t.git <br />
cd Wautomsg-b0t/ <br /><br />

<b>Python version: 3:<br /></b>
python3 -m pip install -r requirements.txt <br /><br />
If it's not working, then try, <br />
pip install -r requirements.txt

<b>Python version: 2:<br /></b>
pip install -r requirements.txt

# Usage
To find the mouse pointer Position, place your mouse pointer on the text of latest/recent message from the WhatsApp chatbox (Eg. place your mouse pointer on the text of "Hi" message which was entered earlier during the setup phase) <br />
Now execute this program through your terminal. <br />
python positionfinder.py <br /><br />
It will Print the values of x and y positions of your mouse pointer. (Eg. Point(x=1229, y=781)). Note down these values. <br />
Open the Wautomsg-b0t using any (editor/notepad) and then find (Ctrl+F) pos_x and pos_y and change the existing positions to the noted position accordingly. <br />
Save this file. <br /><br />
You can either parse arguements directly along with the command or enter the parameters using the command line wizard.<br />
to understand how to parse arguements directly use <br />
python Wautomsg-b0t.py --help<br /><br />
To run the program using the CLI wizard Type the following in your terminal, <br />
python Wautomsg-b0t.py <br /><br />
1. Enter your WhatsApp Phone Number <br />
2. Import the file containing Phone Number List in .txt file format <br />
3. Enter the mode of Messaging (importing from file (or) input the message in terminal/cli) <br />
4. Now Type the Message and Press Enter then Ctrl+D or else Import the File containing the Message to be sent according to the mode. <br />
5. Press Enter To Start the b0t and Switch to logged in WhatsApp Web, and make sure that the cursor is in your chat. <br />
6. Don't do anything until the b0t completes the execution, When It Completes, You will be notified through WhatsApp as well as in Terminal. <br />

# Additional Information
b0t can send upto 5 messages per minute. If the b0t is slow, you can remove/reduce the values of time.sleep() function. <br />
b0t has time.sleep() function just to avoid accounts from getting banned by WhatsApp for sending too many Requests. <br />
b0t nicely handles most of the scenarios like even if the account doesn't exist in WhatsApp, It escapes the alert and continue with other existing accounts. <br /><br />
If you have any issues/If you find any bugs, Feel free to open an issues thread/Pull Request. <br />
If you like this tool and if it helped you, Please Do Star the repo.

# Limitation
You can not use your PC for any other purpose/multitask during the execution of the tool. 

# Disclaimer
<b>This tool is made only for constructive purposes with a good intention, Please Use this tool Responsibly and don't try to Message bomb or Spam any unknown people.</b> <br />
Feel free to fork/publish this tool, but just make sure that you give credits to @whitedevil369 or Poornesh Adhithya.<br />

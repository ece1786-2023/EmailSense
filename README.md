# EmailSense
2023-Fall ECE 1786: Creative Applications of Natural Language Processing <br/>
University of Toronto <br/>
Authored by: Isabella Hao & Weizhou Wang <br/>

## Email accounts used in this project
**Server Email:** ```emailsense.1786@gmail.com```<br/>
**Server Password:** ```emailsense666``` (the one used in email_monitor.py is a specific device password for accessing the IMAP server)<br/>
**Testing User Email:** ```user.emailsense.1786@gmail.com```<br/>
**Server Password:** ```emailsense666``` (the one used in email_monitor.py is a specific device password for accessing the IMAP server)<br/>

## Repository Structure
```src/:``` Stores all source code (please see a specific README under this folder)<br/>
```emails/:``` Stores all incoming emails (Email Buffer)<br/>
```dataset/:``` Dataset used in training & testing the model<br/>

## Apple Shortcuts
Note: After downloading the Shortcuts, users need to modify the paths to their absolute paths & change the SSH settings <br/>
Note: Since Shortcuts on Macs do not support running bash script, these Shortcuts can only be used on iPhones <br/>
**EmailSense On:** https://www.icloud.com/shortcuts/c4951bf446db4c10a8e2c8ed370023ec <br/>
**EmailSense Off:** https://www.icloud.com/shortcuts/fc6fea52b2084da895bbe24f23b0fdff <br/>

## Usage
You can start EmailSense on your computer by:
```
python3 EmailSense.py [-h] [--name NAME] [--email EMAIL] [--password PASSWORD]

EmailSense - Professor's email assistant

options:
  -h, --help           show this help message and exit
  --name NAME          Please type the user's name, default to Alex
  --email EMAIL        Please type the user's email, default to Testing User Email
  --password PASSWORD  Please type the user email's **APP** password```, default to Testing User Email's App password
```

## Setup Guide & Apple Focus Automation
1. Please set up an APP password for your email. You can follow: https://support.google.com/mail/answer/185833?hl=en <br/>
   This APP password is the one you should use in the PASSWORD parameter above
2. Please put your iPhone and Mac on the same wifi, then modify the SSH settings in the Shortcut scripts by following https://dougbeal.com/2019/11/02/remote-control-your-mac-with-your-iphone-and-ssh-key-shortcuts/ <br/>
3. On your iPhone, please create the "EmailSense" Focus mode and the following two Automation: <br/>
   <img src="https://github.com/ece1786-2023/EmailSense/assets/59983226/567a3de4-31b6-43d6-be73-82b031de17ea" width="300" height="350">
   <img src="https://github.com/ece1786-2023/EmailSense/assets/59983226/bdc4bc9e-fa6e-4163-bb3a-4c041830f89b" width="300" height="350"> <br/>
4. If everything goes well, then the EmailSense should automatically start when you turn on the focus mode
   

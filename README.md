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
```src/:``` Stores all source code<br/>
```emails/:``` Stores all incoming emails (Email Buffer)<br/>
```dataset/:``` Dataset used in training & testing the model<br/>

## Apple Shortcuts
Note: After downloading the Shortcuts, users need to modify the paths to their absolute paths & change the SSH settings <br/>
**EmailSense On:** https://www.icloud.com/shortcuts/c4951bf446db4c10a8e2c8ed370023ec <br/>
**EmailSense Off:** https://www.icloud.com/shortcuts/fc6fea52b2084da895bbe24f23b0fdff <br/>

## Usage
```
python3 EmailSense.py [-h] [--name NAME] [--email EMAIL] [--password PASSWORD]

EmailSense - Professor's email assistant

options:
  -h, --help           show this help message and exit
  --name NAME          Please type the user's name, default to Alex
  --email EMAIL        Please type the user's email, default to Testing User Email
  --password PASSWORD  Please type the user email's **APP** password```, default to Testing User Email's App password

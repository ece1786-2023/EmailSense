import email_listener
import classifier
import atexit
import pystache
import argparse

PROF_NAME = ''
CURRICULUM = 0
COLLAB = 0
RECOM = 0
ADMIN = 0
OTHER = 0
SUMMARY = []

# Parse raw emails, save to files, and analyze them
def process_email(email_listener, msg_dict: dict()):
    global CURRICULUM, COLLAB, RECOM, ADMIN, OTHER
    for email in list(msg_dict.keys()):
        ''' Email Format
            Subject: xxx
            Content:
            xxx
        '''
        email_text = ""
        email_text += "Subject: " + msg_dict[email]['Subject'] + "\n"
        email_text += "Content:\n" + msg_dict[email]['Plain_Text']
        
        ''' File Name Format
            EmailSense/emails/<UID>_<sender_address>.txt
        '''
        with open("../emails/"+email+".txt", "w") as text_file:
            text_file.write(email_text)

        # Execute GPT classifier
        print("Analyzing Email:", msg_dict[email]['Subject'])
        pred, reason = classifier.classifier(email_text)

        # Count the number of categories, used for result generator
        if (pred == 'CURRICULUM'):
            CURRICULUM += 1
        elif (pred == 'COLLAB'):
            COLLAB += 1
        elif (pred == 'RECOM'):
            RECOM += 1
        elif (pred == 'ADMIN'):
            ADMIN += 1
        else:
            OTHER += 1

        print("Prediction Result:", pred)
        print("Reason:", reason)

        # Move the email to the corresponding folder
        uid = str(email).split('_')[0]
        try:
            email_listener.server.move(uid, pred)
        except:
            # Create the folder and move the message to the folder
            email_listener.server.create_folder(pred)
            email_listener.server.move(uid, pred)
        print("Email has been moved to", pred)

# Activate when the system exits
def result_generator(server_email, server_password, user_email):
    global CURRICULUM, COLLAB, RECOM, ADMIN, OTHER, PROF_NAME
    renderer = pystache.Renderer()
    # Calculate the total num of emails received
    sum = CURRICULUM + COLLAB + RECOM + ADMIN + OTHER
    # Use Mustache to generate the final email
    email = renderer.render_path('./email_template.mustache' \
                         , {'NAME': PROF_NAME,
                            'CURRICULUM': CURRICULUM,
                            'COLLAB': COLLAB,
                            'RECOM': RECOM,
                            'ADMIN': ADMIN,
                            'OTHER': OTHER,
                            'TOTAL': sum,
                            'SUMMARY': 'no summary yet!'})

    # Initialize the email responder
    responder = email_listener.email_responder.EmailResponder(server_email, server_password)
    # Login
    responder.login()
    # The recipient for the email
    recipient = user_email
    # The subject of the emails
    # TODO: Add time
    subject = "[EmailSense] Your Email Inbox Activity Report"
    # Plain text version of the email
    text = email
    # Sends a plain text email
    # TODO: HTML format of email?
    responder.send_singlepart_msg(recipient, subject, text)

    print("System exited. Summary has been sent back to user.")

if __name__ == "__main__":
    # Parge argvs
    parser = argparse.ArgumentParser(description="EmailSense - Your email's assistant")
    parser.add_argument('name', type=str, help="Please type the user's name")
    parser.add_argument('email', type=str, help="Please type the user's email")
    parser.add_argument('password', type=str, help="Please type the user email's 'device' password")
    args = parser.parse_args()
    PROF_NAME = args.name

    # Set your email, password, what folder you want to listen to, and where to save attachments
    user_email = args.email
    user_password = args.password
    server_email = "emailsense.1786@gmail.com"
    server_password = "jwqknoywuvxlteua"
    # Set the result generator to generate email when exit
    atexit.register(result_generator, server_email, server_password, user_email)

    folder = "Inbox"
    attachment_dir = "../attachment/"
    el = email_listener.EmailListener(user_email, user_password, folder, attachment_dir)

    # Log into the IMAP server
    el.login()

    # Get the emails currently unread in the inbox
    msg_dict = el.scrape()
    process_email(None, msg_dict=msg_dict)

    # Start listening to the inbox (set default timeout to 10 hours)
    el.listen(600, process_func=process_email)
import email_listener

def process_email(email_listener, msg_dict: dict()):
    for email in list(msg_dict.keys()):
        email_text = ""
        email_text += "From: " + email.split("_")[-1] + "\n"
        email_text += "Subject: " + msg_dict[email]['Subject'] + "\n"
        email_text += "Content:\n" + msg_dict[email]['Plain_Text']
        with open("../emails/"+email+".txt", "w") as text_file:
            text_file.write(email_text)

if __name__ == "__main__":
    # Set your email, password, what folder you want to listen to, and where to save attachments
    email = "emailsense.1786@gmail.com"
    password = "jwqknoywuvxlteua"
    folder = "Inbox"
    attachment_dir = "../attachment/"
    el = email_listener.EmailListener(email, password, folder, attachment_dir)

    # Log into the IMAP server
    el.login()

    # Get the emails currently unread in the inbox
    msg_dict = el.scrape()
    process_email(None, msg_dict=msg_dict)

    # Start listening to the inbox (set default timeout to 10 hours)
    el.listen(600, process_func=process_email)
import os

# Change this to the corresponding category
category = "recommendation"

count = 11
for filename in os.listdir("../../dataset/" + category):
    if ("emails" in filename):
        with open(os.path.join("../../dataset/" + category, filename), 'r') as f: # open in readonly mode
            # do your stuff
            emails = f.read()
            emails = ["Subject"+e for e in emails.split("Subject") if e][1:]
            for i, email in enumerate(emails):
                with open(os.path.join("../../dataset/" + category, "synthetic_"+str(count)+".txt"), "w+") as newfile:
                    email = email.strip()
                    email = email.strip("-")
                    email = email.strip("`")
                    email = email.strip()
                    email = email.strip("`")
                    email = email.strip("-")
                    email = email.strip()
                    newfile.writelines(email)
                    count += 1

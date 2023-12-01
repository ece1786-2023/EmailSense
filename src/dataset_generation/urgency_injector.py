# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
import os
client = OpenAI()

prompt = '''I will give you an email. You need to understand the content of the email and its background. Then, you need to add one or two sentences of time-sensitive messages to the email's content. The time-sensitive messages are defined as messages that are urgent or information that needs the recipient's immediate attention, meaning that the email expects a reply immediately or by the next day.

Please note that your task is to inject time-sensitive messages into the original email, instead of writing a reply to the email. Also note that, please keep the email format as:

Subject: XXX
Content:
XXX
'''

# Modify to the corresponding category & email number
category = "administrative"
candidates = [22, 46]

email = str()
path = str()
for i in candidates:
    try:
        filename = "synthetic_" + str(i) + ".txt"
        path = os.path.join("../../dataset/" + category, filename)
        with open(path) as f:
            email = f.read()
    except:
        filename = str(i) + ".txt"
        path = os.path.join("../../dataset/" + category, filename)
        with open(path) as f:
            email = f.read()

    response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {
        "role": "system",
        "content": prompt
        },
        {
        "role": "user",
        "content": email
        }
    ],
    temperature=1.1,
    max_tokens=512,
    top_p=0.9,
    frequency_penalty=0,
    presence_penalty=0
    )

    with open(path, "w+") as f:
        f.writelines(response.choices[0].message.content)
        print("Writed to:", path)
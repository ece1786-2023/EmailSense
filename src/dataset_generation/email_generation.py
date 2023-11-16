# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
client = OpenAI()

# Change this to the corresponding category
category = "recommendation"

prompt = str()
with open("./prompt/" + category + ".txt") as f:
    prompt = f.read()

for i in range(8):
    with open("../../dataset/" + category + "/emails"+str(i)+".txt", "w+") as file:
        response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {
            "role": "system",
            "content": prompt
            }
        ],
        temperature=1.1,
        max_tokens=4096,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0
        )

        file.writelines(response.choices[0].message.content)
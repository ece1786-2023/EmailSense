# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI

client = OpenAI()

prompt = str()
with open("./prompt.txt") as f:
    prompt = f.read()

#function to call openai api from Isabella's A4
def call_openai_api(statement):
  response = client.chat.completions.create(
    model="gpt-4",
    messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": "" }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )
  return response.choices[0].message.content
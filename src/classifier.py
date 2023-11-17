# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
import pandas as pd
import os
import sys

client = OpenAI(api_key="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")

categories = ['RECOM', 'COLLAB', 'CURRICULUM', 'ADMIN', 'OTHER']

classifier_prompt = str()
with open("./classifier_prompt.txt") as f:
    classifier_prompt = f.read()

#function to call openai api from Isabella's A4
def classifier(statement):
  response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
    {"role": "system", "content": classifier_prompt},
    {"role": "user", "content": statement}
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )

  output_class = str()
  output_reason = str()
  output = response.choices[0].message.content

  for category in categories:
     if category in output:
        output_class = category
        break

  output_reason = output[len(output_class):]

  return output_class, output_reason.strip(', ')

# Testing classification performance on dataset
if __name__ == "__main__":
  dataset_path = sys.argv[1]

  predict_classes = []
  predict_reasons = []
  corrects = []
  correct = 0
  count = 0
  dataset = pd.read_csv(dataset_path)
  for row_id, row in dataset.iterrows():
    filename = row['filename']
    print("Classifying email:", os.path.join('../dataset/', filename))
    label = row['category']
    email = str()
    with open(os.path.join('../dataset/', filename)) as f:
        email = f.read()
    output_class, output_reason = classifier(email)

    predict_classes.append(output_class)
    predict_reasons.append(output_reason)
    count += 1
    if output_class == label:
        correct += 1
        corrects.append(1)
    else:
        corrects.append(0)
  
  dataset['prediction'] = predict_classes
  dataset['reason'] = predict_reasons
  dataset['correct'] = corrects

  print("Results written to:", dataset_path[:-4]+'_result.csv')
  dataset.to_csv(dataset_path[:-4]+'_result.csv', index=False)

  accuracy = correct / count
  print(accuracy)
    

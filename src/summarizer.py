# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
import pandas as pd
import os
import sys

client = OpenAI(api_key="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")

summarizer_prompt = str()
with open("C:\\Users\\haois\\Documents\\GitHub\\EmailSense\\src\\summarizer_prompt.txt",'r',encoding="utf-8") as f:
   summarizer_prompt = f.read()

def split_by_newline(sentence):
    split_sentences = []
    parts = sentence.split('\n',1)  # Split by the first period
    split_sentences.append(parts)
    return parts

#function to call openai api from Isabella's A4
def summarizer(statement):
  response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
    {"role": "system", "content": summarizer_prompt},
    {"role": "user", "content": statement}
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )

  output_class = str()
  output_summary = str()
  output_reasoning = str()
  output = response.choices[0].message.content

  output_class = output[0]

  if output_class == '0':
    output_reasoning = output[len(output_class):]
  else:
    output_summary,output_reasoning=split_by_newline(output[len(output_class):])



  return output_class, output_summary.strip().strip(',').strip(), output_reasoning

# Testing classification performance on dataset
if __name__ == "__main__":
  dataset_path = sys.argv[1]

  predict_classes = []
  predict_summary = []
  predict_reasoning = []
  corrects = []
  correct = 0
  count = 0
  dataset = pd.read_csv(dataset_path)
  for row_id, row in dataset.iterrows():
    filename = row['filename']
    print("Summarizing email:", os.path.join('../dataset/', filename))
    label = row['time_sensitive']
    email = str()
    with open(os.path.join('c:/Users/haois/Documents/GitHub/EmailSense/dataset/', filename),'r',encoding="utf-8") as f:
      email = f.read()

    temp = summarizer(email)

    print(temp)
    
    output_class, output_summary ,output_reasoning= temp
   
       
    if output_class == '1':
       output_class = 'YES'
    else:
       output_class = 'NO'

    predict_classes.append(output_class)
    predict_summary.append(output_summary)
    predict_reasoning.append(output_reasoning)
   
    count += 1

    if output_class == label:
        correct += 1
        corrects.append(1)
    else:
        corrects.append(0)
  
  dataset['urgent'] = predict_classes
  dataset['summary'] = predict_summary
  dataset['correct_urgency'] = corrects
  dataset['reasoning'] = predict_reasoning

  print("Results written to:", dataset_path[:-4]+'_summarizer_result.csv')
  dataset.to_csv(dataset_path[:-4]+'_summarizer_result.csv', index=False)

  accuracy = correct / count
  print(accuracy)
    

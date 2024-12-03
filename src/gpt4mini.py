import openai
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='src/openai.env')
import json

openai.api_key = os.getenv("OPENAIKEY")



def get_chatgpt_response(prompt, model="gpt-4o-mini", temperature=0.7, max_tokens=2048):
    completion = openai.ChatCompletion.create(
      model="gpt-4o-mini",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
      ],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return (completion.choices[0].message.content)



input_file = "src/article_text.json"

with open(input_file, 'r') as file:
    input_data = json.load(file)


prompt = """
    Provide the sentiment of the below article as either positive, negative or neutral. Just return the sentiment as a string. 
    {}
"""


output_file = "src/article_text_gt.json"
output_gt = []
for article in input_data:
    input_prompt = prompt.format(article)
    output_text = get_chatgpt_response(input_prompt)
    output_gt.append(output_text)


with open(output_file, 'w') as file:
    json.dump(output_gt, file, indent=4)  
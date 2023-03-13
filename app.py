# https://chatgpt-lab.com/n/nda0de0be1774
import os
import openai

openai.api_key = os.environ.get('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {'role': 'system', 'content': 'あなたは優秀なITエンジニアです。'},
        {'role': 'user', 'content': 'どのプログラミング言語でも役に立つ、意外と知られていないITエンジニアの豆知識を1つ教えてください。'}
    ],
    temperature=0.0,
)
res_content = response['choices'][0]['message']['content'] 
print(res_content)
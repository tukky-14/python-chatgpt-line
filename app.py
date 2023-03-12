# https://chatgpt-lab.com/n/nda0de0be1774
import openai

openai.api_key = 'OpenAI API シークレットキー'

response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {'role': 'system', 'content': 'You are a helpful assisant.'},
                    {'role': 'user', 'content': '開発に便利な、みんなが知らない知識を1つ教えてください。'}
                ],
                temperature=0.0,
)
res_content = response['choices'][0]['message']['content'] 
print(res_content)
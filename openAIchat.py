#import os
#import openai
####
#from openai import OpenAI
#import openai
#client = OpenAI()
#client = OpenAI(api_key="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")
#client.api_key = ("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")
#OpenAI.api_key.encode.__get__ = ("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")
#client.models.list()

#message = client.beta.threads.messages.create(
#thread_id = thread.id,
#role = "user",
#content = “what is the biggest and most expensive villa in bali”
#)
# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
#client = OpenAI()
client = OpenAI(api_key="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")
response = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[
    {
      "role": "user",
      "content": "who won the cricket world cup in 2023"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
#return response.choices[0].message.content
#from dotenv import load_dotenv, find_dotenv

#load_dotenv(find_dotenv())
#openai.api_key = ("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")

#model_engine = "text-davinci-003"
#model="gpt-3.5-turbo"
#temperature = 0.9
#max_tokens = 150

#prompt = "Write a haiku about large language models."
#messages = [{"role": "user", "content": prompt}]
#response = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": prompt}], temperature=temperature)
#response = openai.completions.create(model="gpt-3.5-turbo-0613", prompt="Write a haiku about large language models.", temperature=0.9, max_tokens=150)
#response = openai.completions.create(model="gpt-3.5-turbo-0613", prompt="Write a haiku about large language models.", temperature=0.9, max_tokens=150)
#response = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": prompt}], temperature=temperature, max_tokens=150)
#print(response)
#print(response["choices"][0]["message"]["content"])
#print(response["usage"])
#print(response["usage"]["total_tokens"])

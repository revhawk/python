from openai import OpenAI
#import openai
#client = OpenAI()
client = OpenAI(api_key="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")
#client.api_key = ("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")
#OpenAI.api_key.encode.__get__ = ("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")
# Reg - Key2 - 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
client.models.list()
print(client.models.list())
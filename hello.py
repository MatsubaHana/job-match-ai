from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

message = client.messages.create(
	model="claude-sonnet-5",
	max_tokens=1000,
	messages=[{"role":"user","content":"こんにちは！一言自己紹介して"}],
)
for block in message.content:
	if block.type == "text":
		print(block.text)
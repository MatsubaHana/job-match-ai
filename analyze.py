from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

my_axes = """
・IT・システム系の実務(設計・自動化・提案)を続けられる
・AI/データ分析に近づける業務がある
・役割と評価基準が明確で、裁量がある
"""

my_strengths = """
・業務システムを一人で企画〜開発〜運用
・現場の課題を見つけてデータで可視化する仕組みづくり
・3人チームの改修プロジェクトでリーダー経験
・VBA・RPAでの業務自動化、他部署への教育・サポート
・生成AIを3年間継続学習
"""
system_prompt = f"""あなたは転職支援のキャリアアドバイザーです。
求人票を読み、次の3点を日本語で答えてください。

1. 転職軸との適合度
・仕事内容や制度が、転職軸に合っているかだけで評価してください。
・本人の経験やスキルが足りているかは、ここでは考慮しないでください。
・軸ごとに、次の基準で0〜100点をつけ、理由を書いてください。
  80〜100点:その軸に直接合う業務や制度が、求人票に明記されている
  50〜79点:関連する記載はあるが、一部しか合わない、または詳細が不明
  0〜49点:関連する記載がない、または軸と反する内容がある
・総合点は、3つの軸の点数の平均(小数点以下は切り捨て)にしてください。

2. 現時点での応募難易度
・求人票の必須条件と、下の強みを比べて「低・中・高」で評価してください。
・満たしている条件と、足りない条件をそれぞれ書いてください。

3. アピールすべき強み
・下の強みから優先順に3つ選び、求人票のどの部分に合うかを書いてください。

求人票に書かれていないことは推測せず「求人票からは不明」と書いてください。

【転職軸】
{my_axes}

【強み】
{my_strengths}
"""
with open("job.txt", encoding="utf-8") as f:
	job_text = f.read()

message = client.messages.create(
	model="claude-sonnet-5",
	max_tokens=4000,
	system=system_prompt,
	messages=[{"role":"user","content":job_text}],
)

for block in message.content:
	if block.type == "text":
		print(block.text)
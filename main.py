# imports
import random
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# load env variables
load_dotenv(".env")
PPLX_KEY = os.environ.get("PPLX_KEY")

team1 = "Golden State Warriors"
team2 = "Denver Nuggets"

# test random winner
def determineWinner(team1, team2):
    odds = random.randint(0,1)
    if odds > 0.5:
        winner = team2
    else:
        winner = team1

    return winner

# test perplexity
messages = [
    {
        "role": "system",
        "content": """ 
            You are an expert in basketball and statistics.
            You are tasked with researching two teams and determining the most likely winner in a matchup.
            Please return your response in JSON format, with the following fields:
            ```
            {
                "reasoning": ,
                "winner": ,
            }
            ```
            Return ONLY THE JSON AND NOTHING ELSE.
            """,

    },
    {
        "role": "user",
        "content": "Denver Nuggets vs. Golden State Warriors",
    }
]

client = OpenAI(api_key=PPLX_KEY, base_url="https://api.perplexity.ai")

response = client.chat.completions.create(
    model="sonar-pro",
    messages=messages,
)

# grab content string
content = response.choices[0].message.content

# convert to JSON
content_json = json.loads(content, strict=False)
winner = content_json["winner"]
reasoning = content_json["reasoning"]

print(winner)
print(reasoning)


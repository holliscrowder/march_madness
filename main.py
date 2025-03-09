# Take two team names and determine the winner
import random
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
PPLX_KEY = os.environ.get("PPLX_KEY")

team1 = "Golden State Warriors"
team2 = "Denver Nuggets"

def determineWinner(team1, team2):
    odds = random.randint(0,1)
    if odds > 0.5:
        winner = team2
    else:
        winner = team1

    return winner

#test perplexity

messages = [
    {
        "role": "system",
        "content": "You are an expert in basketball and statistics. You are tasked with researching two teams and determining the most likely winner in a matchup.",

    },
    {
        "role": "user",
        "content": "Denver Nuggets vs. Golden State Warriors",
    }
]
print(PPLX_KEY)
client = OpenAI(api_key=PPLX_KEY, base_url="https://api.perplexity.ai")

response = client.chat.completions.create(
    model="sonar-pro",
    messages=messages,
)

# payload = {
#     "model": "sonar",
#     "messages": messages,
# }

# headers = {
#     "Authorization": f'Bearer {PPLX_KEY}',
#     "Content-Type": "application/json"
# }

# response = requests.post(url="https://api.perplexity.ai/chat/completions", json=payload, headers=headers)
print(response.content)


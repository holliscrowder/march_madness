# imports
from openai import OpenAI
from dotenv import load_dotenv
import os
import json


# load env variables
load_dotenv(".env")
PPLX_KEY = os.environ.get("PPLX_KEY")

team1 = "Golden State Warriors"
team2 = "Denver Nuggets"

# load teams
with open("first_four.json", "r") as f:
    matchups = json.load(f)

print(matchups)

# determine winner given matchup
def determineWinner(team1: str, team2: str):

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
            "content": f"{team1} vs. {team2}",
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

    return [winner, reasoning]

# test llm winner function
# [winner, reasoning] = determineWinner("Denver Nuggets", "Golden State Warriors")

# print(winner)
# print(reasoning)

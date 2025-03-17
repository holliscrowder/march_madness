# imports
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# load env variables
load_dotenv(".env")
PPLX_KEY = os.environ.get("PPLX_KEY")

# load teams
with open("pplx_round_64.json", "r") as f:
    matchups = json.load(f)

# determine winner given matchup
def determineWinner(team1: str, team2: str):

    # test perplexity
    messages = [
        {
            "role": "system",
            "content": """ 
                You are an expert in college basketball and statistics.
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
    content = content.strip()

    # convert to JSON
    try:
        content_json = json.loads(content, strict=False)
        winner = content_json["winner"]
        reasoning = content_json["reasoning"]
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        return ["ERROR", "Invalid JSON response"]

    return [winner, reasoning]

# test llm winner function
winners = {}
for match in matchups:
    team1 = match[0]
    team2 = match[1]
    [winner, reasoning] = determineWinner(team1, team2)
    winners[winner] = reasoning

print(winners)

# write to output json
with open ("round_64_output.json", "w") as f:
    json.dump(winners, f)

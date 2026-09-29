import json
import random
from datetime import date

def get_daily_prompt():
    with open("prompts.json", encoding="utf-8") as f:
        prompts = json.load(f)
    rng = random.Random(date.today().isoformat())
    return rng.choice(prompts)

if __name__ == "__main__":
    p = get_daily_prompt()
    print(p["prompt"])
    for h in p["hints"]:
        print(f" {h['es']} - {h['en']}")
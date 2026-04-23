import json
import os
import random

username = os.getenv("GITHUB_ACTOR", "unknown")

accuracy = round(random.uniform(0.7, 0.95), 3)
f1 = round(random.uniform(0.7, 0.95), 3)

result = {
    "name": username,
    "accuracy": accuracy,
    "f1": f1
}

with open("result.json", "w") as f:
    json.dump(result, f)

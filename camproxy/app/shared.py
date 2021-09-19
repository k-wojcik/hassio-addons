import json
import os

options_path = os.environ.get("OPTIONS_PATH", "/data/options.json")
with open(options_path) as f:
    options = json.load(f)
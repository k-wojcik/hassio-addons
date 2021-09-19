import json
import os
import logging
import sys

options_path = os.environ.get("OPTIONS_PATH", "/data/options.json")
with open(options_path) as f:
    options = json.load(f)


# Log to stdout
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(handler)    
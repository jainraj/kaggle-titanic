from program.transformers import Transformer
import json

with open('config.json') as f:
    config = json.load(f)


transformer = Transformer(config)

a = 0

import json

class StringUtils:

    def prety_json(text):
        # json_ob = json.loads(str(text))
        return json.dumps(text, indent=2)
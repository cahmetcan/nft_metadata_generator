import json

for i in range(7777):
    y = i+1
    data = {
        "name": "Number #{}".format(y),
        "symbol": "BONKTICKET",
        "description": "THAT BONK TICKET WAITS TO GET YOU RICH.",
        "image": "{}.png".format(i),
        "attributes": [
            {
                "trait_type": "Number",
                "value": str(i)
            }
        ],
        "properties": {
            "files": [
                {
                    "uri": "{}.png".format(i),
                    "type": "image/png"
                }
            ]
        }
    }

    with open("{}.json".format(i), "w") as f:
        json.dump(data, f)

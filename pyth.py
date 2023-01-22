
import json

size = input("Enter the size of your collection: ")

name = input("Enter the the name of your collection: ")

symbol = input("Enter the symbol of your collection: ")

description = input("Enter the description of your collection: ")
for i in range(int(size)):
    y = i+1
    data = {
        "name": "{} {}".format(name, y),
        "symbol": symbol,
        "description": description,
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

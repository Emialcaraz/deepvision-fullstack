# This a dummy module
# This gets called in the module_main.py file

import random
from typing import Dict
import json, os
import time
from indexer.indexer import db


def vehicleapi():
    # json.loads() will throw a ValueError if JSON is invalid
    try:
        with open('events.json') as raw_data:
            json_docs = json.loads(raw_data.read())
            for json_doc in json_docs:

                if db.exists(index="vehicle"):
                    return db.search('vehicle')

                db.index('vehicle', json.dumps(json_doc))
                return db.search('vehicle')

    except ValueError as error:
        print("Error type:", type(error))
        print("json.loads() ValueError for JSON object:", error)
        return 500

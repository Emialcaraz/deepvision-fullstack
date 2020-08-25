from elasticsearch import Elasticsearch
import json


class Database:
    def __init__(self):
        self.__es = Elasticsearch('database', port=9200)

    def index(self, index, body):
        try:
            return self.__es.index(
                index=index,
                body=body
            )

        except Exception:
            return None

    def exists(self, index):
        try:
            return self.__es.indices.exists(index=index)
        except Exception:
            return None

    def search(self, index, body={'query': {'match_all': {}}}):
        try:
            self.__es.indices.refresh(index=index)
            return self.__es.search(
                index=index,
                body=body
            )

        except Exception:
            return None

    def searchanomalies(self, index):

        search_param = json.dumps({
            "query": {
                "match_all": {
                    "module": "dv-traffic",
                    "events": [
                        {
                            "alerts": [
                                {
                                    "type": "trafficAnomaly",
                                }],
                        }],
                }
            }
        })

        try:
            self.__es.indices.refresh(index=index)
            return self.__es.search(
                index=index,
                body=search_param,
                size=999
            )

        except Exception:
            return None


db = Database()

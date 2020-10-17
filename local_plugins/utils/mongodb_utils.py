import pymongo

class MongoDBUtil:

    def execute_mongodb(dbHost, database_name, query_collection, script):
        try:
            mongo_client = pymongo.MongoClient(dbHost, 27017)
            db = mongo_client[database_name]
            col = db[query_collection]
            results = col.find(script)
            return ([r for r in results])
        except:
            return 'There are some problems to connect to Test-Data-Service'



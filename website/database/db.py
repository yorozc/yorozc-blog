from pymongo import MongoClient
from pymongo.errors import ConfigurationError
import certifi
import os

try:
    def _uri():
        uri = os.getenv("MONGODB_URI")
        if not uri:
            raise ConfigurationError("MONGODB_URI not set")
        return uri

    def get_client() -> MongoClient:
        return MongoClient(
            _uri(),
            tls=True,
            tlsCAFile=certifi.where()
        )

    try:
        get_client().admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    def get_db():
        return get_client()[os.getenv("DB")]

    def get_blog_collection():
        return get_db()[os.getenv("BLOG_COLLECTION")]
    
    def get_users_collection():
        return get_db()[os.getenv("USER_COLLECTION")]

except Exception as e:
    print("Unable to make connection to DB")
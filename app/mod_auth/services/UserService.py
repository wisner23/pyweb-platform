from .interfaces.IUserService import IUserService
from pymongo import MongoClient
import config


class UserService(IUserService):

    # This method will do some change and apply all business logic
    @staticmethod
    def registry_user(user):
        con_cfg = config.get_database_configurations()

        client = MongoClient(con_cfg['host'], con_cfg['port'])
        database = client[con_cfg['database']]
        collection = database.get_collection("canonical-datalake")

        collection.insert(user)
        client.close()

    @staticmethod
    def retrieve_users():
        con_cfg = config.get_database_configurations()

        client = MongoClient(con_cfg['host'], con_cfg['port'])
        database = client[con_cfg['database']]
        collection = database.get_collection("canonical-datalake")

        docs = [doc for doc in collection.find()]
        return docs
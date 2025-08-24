from pymongo import MongoClient
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()

class Logs:
    def __init__(self, interface: str, ip: str, status: str, protocol: str):
        self.interface = interface
        self.ip = ip
        self.status = status
        self.protocol = protocol
        self.createdAt = datetime.now(timezone.utc) 

    def to_dict(self):
        return {
            "interface": self.interface,
            "ip": self.ip,
            "status": self.status,
            "protocol": self.protocol,
            "createdAt": self.createdAt
        }

class LogsModel:
    def __init__(self, db_name: str, collection_name: str):
        self.client = MongoClient(os.getenv('MONGO_URI')) 
        self.db = self.client[db_name]
        self.collection = self.db[collection_name] 

    def create_logs(self, logs: Logs):
        logs_dict = logs.to_dict()
        result = self.collection.insert_one(logs_dict) 
        return str(result.inserted_id)

    def get_logs(self, ip: str):
        return self.collection.find_one({"ip": ip})

from pymongo.errors import DuplicateKeyError

import proto.entities.demo_pb2 as demo_pb
from base import Base
from dao.mongodb import MongoDBHelper
from errors import PopupError
from submodules.utils.logger import Logger

logger = Logger()


class DemoDA(MongoDBHelper, Base):

    coll = "___demo_db___demos___"

    def add_demo(self, demo):
        json_data = self.PH.to_dict(demo)
        try:
            self.insert_one(json_data)
        except DuplicateKeyError as ex:
            logger.error(ex)
            raise PopupError("Already add this demo")

    def update_demo(self, demo):
        matcher = {"id": demo.id}
        json_data = self.PH.to_dict(demo)
        self.update_one(matcher, json_data)

    def delete_demo(self, demo):
        matcher = {"id": demo.id}
        return self.delete_one(matcher)

    def query_demo(self, demo):
        matcher = {"id": demo.id}
        return self.find_one(matcher)

    def list_demo(self):
        matcher = {}
        demos = self.find_many(matcher)
        return demos

    def get_demo_by_id(self, id):
        matcher = {"id": id}
        demo = self.find_one(matcher)
        return self.PH.to_obj(demo, demo_pb.Demo)

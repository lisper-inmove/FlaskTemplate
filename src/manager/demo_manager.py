import proto.entities.demo_pb2 as demo_pb
from manager.base_manager import BaseManager
from dao.demo_dao import DemoDA
from errors import PopupError


class DemoManager(BaseManager):

    @property
    def dao(self):
        if self._dao is None:
            self._dao = DemoDA()
        return self._dao

    def create_demo(self, request):
        obj = self.create_obj(demo_pb.Demo)
        obj.name = request.name
        return obj

    def delete_demo(self, request):
        demo = demo_pb.Demo()
        demo.id = request.id
        self.dao.delete_demo(demo)
        return demo

    def query_demo(self, request):
        return self.dao.get_demo_by_id(request.id)

    def update_demo(self, request):
        demo = self.dao.get_demo_by_id(request.id)
        if not demo:
            raise PopupError("Demo Not Exists")
        demo.name = request.name
        return demo

    def list_demo(self, request):
        for demo in self.dao.list_demo():
            yield self.PH.to_obj(demo, demo_pb.Demo)

    def add_demo(self, demo):
        return self.dao.add_demo(demo)

    def do_update_demo(self, demo):
        return self.dao.update_demo(demo)

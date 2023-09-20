# -*- coding: utf-8 -*-

import proto.api.api_demo_pb2 as api_demo_pb

from ctrl.base_ctrl import BaseCtrl
from manager.demo_manager import DemoManager


class DemoCtrl(BaseCtrl):

    def _init(self, *args, **kargs):
        self._manager = DemoManager()

    def create(self):
        request = self.get_request_obj(api_demo_pb.DemoCreateRequest)
        demo = self._manager.create_demo(request)
        self._manager.add_demo(demo)
        return self.__create_demo_response(demo)

    def update(self):
        request = self.get_request_obj(api_demo_pb.DemoUpdateRequest)
        demo = self._manager.update_demo(request)
        self._manager.do_update_demo(demo)
        return self.__create_demo_response(demo)

    def list(self):
        request = self.get_request_obj(api_demo_pb.DemoListRequest)
        demos = self._manager.list_demo(request)
        result = api_demo_pb.DemoListResponse()
        for demo in demos:
            result.demos.add().CopyFrom(self.__create_demo_response(demo))
        return result

    def query(self):
        request = self.get_request_obj(api_demo_pb.DemoQueryRequest)
        demo = self._manager.query_demo(request)
        return self.__create_demo_response(demo)

    def delete(self):
        request = self.get_request_obj(api_demo_pb.DemoDeleteRequest)
        demo = self._manager.query_demo(request)
        self._manager.delete_demo(request)
        return self.__create_demo_response(demo)

    def __create_demo_response(self, demo):
        if demo is None:
            return None
        obj = api_demo_pb.DemoCommonResponse()
        obj.id = demo.id
        obj.name = demo.name
        obj.createTime = demo.createTime
        obj.updateTime = demo.updateTime
        return obj

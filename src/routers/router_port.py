# -*- coding: utf-8 -*-

from flask import Blueprint
from submodules.utils.protobuf_helper import ProtobufHelper as PH
from unify_response import UnifyResponse
from routers.router_helper import RouterHelper

name = "router-port"
_router_port = Blueprint(name, name, url_prefix="/<string:source>")

router_helper = RouterHelper("ctrl")


@_router_port.route("/<string:operate>", methods=["POST", "GET", "DELETE", "PUT", "HEAD"])
def router_port(source, operate):
    """视图层."""
    if '-' in operate:
        operate = operate.replace('-', '_')
    if '-' in source:
        source = source.replace('-', '_')
    ctrl = router_helper.ctrls[source](operate=operate)
    result = ctrl.do_operate()
    return UnifyResponse.R(PH.to_json(result))


router_helper.load_ctrl()

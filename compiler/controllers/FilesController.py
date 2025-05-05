from errors.ErrorsServer import *
from flask import request, jsonify
from conf import BaseConf

URL_PUBLISHER = BaseConf.PUBLISHER_URL
CODE_URL_API_COMPILATOR = BaseConf.CODE_URL_API_COMPILATOR


def post(code):
    return jsonify({
        'data': "",
        'message' : 'OK',
        'status' : 200
    })
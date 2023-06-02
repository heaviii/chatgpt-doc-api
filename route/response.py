import json


class BaseRoute:
    @staticmethod
    def success(data):
        code = 9999
        msg = 'Success'
        #Response.headers['Content-Type'] = 'application/json;charset=utf-8'
        return {'code': code, 'data': data, 'msg': msg} 
        #return jsonify({'code': code, 'data': data, 'msg': msg})
    @staticmethod
    def error(code,data,msg):
        return {'code': code, 'data': data, 'msg': msg}

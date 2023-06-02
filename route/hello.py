# 定义参数解析器
import json

from route.response import BaseRoute



# 定义路由类
class Hello():
    @staticmethod
    def post():
        # 如果参数校验失败，则返回 400 状态码和错误信息
        raw_data = request.data

        # 反序列化 json 数据
        data = json.loads(raw_data)

        # 获取需要的数据
        name = '啊啊啊'
        age = data.get('age')
        print(name)

        return BaseRoute.success({'name': name, 'age': int(age)})
        #return jsonify({'code': 0, 'msg': 'success', 'data': {'name': name, 'age': int(age)}})
        #return f'Hello, {name}! You are {age} years old!'
    @staticmethod
    def get():
        name = 'hi'
        return BaseRoute.success({'name': name})

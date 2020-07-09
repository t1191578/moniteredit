from  flask import Flask ,request
from flask_restful import Resource, Api

app =Flask(__name__)
api = Api(app)
cluster = []
class Student(Resource):
    def get(self, name):
        node = next(filter(lambda x:x['name'] ==name, cluster), None)
        #for node in cluster:
         #   if node['name'] == name:
          #      return node
        return {'node': node},200 if node else 404
    def post(self, name):
        if next(filter(lambda x:x['name'] ==name, cluster), None) is not None:
            return {'message':"An item with name'{}' already exist".format(name)}, 400
        data= request.get_json()
        new_node ={'ip': data['ip'], 'name': name, 'port':data['port']}
        cluster.append(new_node)
        return cluster , 201
class allnodes(Resource):
    def get(self):
        return {'nodes': cluster}

api.add_resource(Student, '/student/<string:name>')
api.add_resource(allnodes, '/allnodes')
app.run(port=5000)
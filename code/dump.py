---------------------------------------------------

from flask import Flask, request
from flask_restful import Resource, Api
import requests
from multipledispatch import dispatch
from Metricsource import Source

app = Flask(__name__)
api = Api(app)

uri = "http://35.154.106.147:9090/api/v1/"
query = "query?query=slurm_"
clsval = Source(uri, query)


class Cluster(Resource):

    def get(self, metric):
        uri = "http://35.154.106.147:9090/api/v1/"
        query = "query?query=slurm_"
        clsval = Source(uri, query)
        val = clsval.inputoutput(metric)
        result = {}
        # val = Source.inputoutput(metric)
        for i in range(len(val)):
            cluster = val[i]
            if cluster['metric']['__name__'] == 'slurm_' + metric:
                result[i + 1] = {'cluster': cluster['metric']['instance'],
                                 cluster['metric']['__name__'][6:]: cluster['value'][1]}
        if result:
            return result, 200
        else:
            return None, 404

    def get(self, clustername, metric):
        uri = "http://35.154.106.147:9090/api/v1/"
        query = "query?query=slurm_"
        clsval = Source(uri, query)
        val = clsval.inputoutput(clustername, metric)
        result = {}
        # val = Source.inputoutput(metric)
        for i in range(len(val)):
            cluster = val[i]
            if cluster['metric']['__name__'] == 'slurm_' + metric:
                result[i + 1] = {'cluster': cluster['metric']['instance'],
                                 cluster['metric']['__name__'][6:]: cluster['value'][1]}
        if result:
            return result, 200
        else:
            return None, 404


api.add_resource(Cluster,
                 '/<string:metric>')  # details from all clusters: end point for cpu - 2(idel,total) , node-1(idel,down) , memory-1(available)
# api.add_resource(Cluster, '/cluster/<string:clustername>/<string:metric>')
# api.add_resource(Cluster, '/cluster/<string:name>/<string:cpus_idle>')
# api.add_resource(Cluster, '/cluster/<string:name>/<string:memory_available>')
app.run(port=5000)
------------------------------------------------
import requests

class Source:
    def  __init__(self,required_metric,ur):
        self.required_metric = required_metric
        self.ur=ur

    def getfromdb(self):
        #establish conn to db,   query according to request and return details in the formate required
        #
        pass
    url ="http://35.154.106.147:9090/api/v1/"
    query= "query?query="+metricreq
    def inputoutput(metricreq):
        url = "http://35.154.106.147:9090/api/v1/"
        query = "query?query=" + metricreq

        input= {"cpus_idle" :url+query,
        "cpus_total":"http://35.154.106.147:9090/api/v1/query?query=slurm_cpus_total",
        "nodes_down" : "http://35.154.106.147:9090/api/v1/query?query=slurm_nodes_down",
        "nodes_idle":"http://35.154.106.147:9090/api/v1/query?query=slurm_nodes_idle",
        "Memory_alloc" :"http://35.154.106.147:9090/api/v1/query?query=slurm_Memory_alloc",
        "cluster_list": "http://35.154.106.147:9090/api/v1/query?query=go_info"
        }
        #nodes_total=Source("cpu_idle","http://15.206.250.89:9090/api/v1/query?query=slurm_cpus_idle{job=%22slurm2%22}")
        #memory_avaialble=Source("cpu_idel","http://15.206.250.89:9090/api/v1/query?query=slurm_cpus_idle{job=%22slurm2%22}")
        mt = next(filter(lambda i: i == metricreq, input), None)
        print('mt val is ', mt)
        resp = requests.get(input[mt])
        if resp.status_code != 200:
                    # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        val= resp.json()
                #cluster = val['data']['result']['metric']['job']
                #slurm_nodes_idle= val['data']['result']['value']['1']
        cluster = val['data']['result']
        return cluster


val=Source.inputoutput("Memory_alloc")
print('final val',val)
-----------------------------------------------------------------

from  flask import Flask ,request
from flask_restful import Resource, Api
import requests
from Metricsource import Source
app =Flask(__name__)
api = Api(app)


class Cluster(Resource):

    def get(self, metric):
        result={}
        val = Source.inputoutput(metric)
        for i in range(len(val)):
            cluster = val[i]
            if cluster['metric']['__name__'] == 'slurm_'+metric:
                result[i+1] = {'cluster': cluster['metric']['instance'], cluster['metric']['__name__'][6:]: cluster['value'][1]}
        return result

api.add_resource(Cluster, '/<string:metric>')
#api.add_resource(Cluster, '/cluster/<string:name>/<string:metric>')
#api.add_resource(Cluster, '/cluster/<string:name>/<string:cpus_idle>')
#api.add_resource(Cluster, '/cluster/<string:name>/<string:memory_available>')
app.run(port=5000)
-----------------------------------
import requests
class Prom:
    def node(self):
        resp = requests.get('http://15.206.250.89:9090/api/v1/query?query=slurm_nodes_idle')
        if resp.status_code != 200:
    # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        val= resp.json()
        cluster = val['data']['result']
        return cluster


cluster = Prom()
print(cluster.node())

------------------------------
import requests

resp = requests.get('http://15.206.250.89:9090/api/v1/query?query=slurm_nodes_idle')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
print(resp.json())
val= resp.json()

cluster = val['data']['result']
print(cluster)


---------------------------------------------------------------

from  flask import Flask ,request
from flask_restful import Resource, Api

app =Flask(__name__)
api = Api(app)

cluster = {'metric': {'name':"slurm_nodes_idle" ,'instance':"35.209.219.226:8080",'job':"slurm2"},
           'value':{0:1593766788.942, '1':"3"}}


class Cluster(Resource):
    def get(self, name,nodes_idle):

        if cluster['metric']['job'] == name:
            return {'cluster': cluster['metric']['job'],'slurm_nodes_idle': cluster['value']['1']},200

        else: return None, 404

api.add_resource(Cluster, '/cluster/<string:name>/<string:nodes_idle>')
#api.add_resource(Cluster, '/cluster/<string:name>/<string:cpus_idle>')
#api.add_resource(Cluster, '/cluster/<string:name>/<string:memory_available>')
app.run(port=5000)
----------------------------------------------------------------------------------
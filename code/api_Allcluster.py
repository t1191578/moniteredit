from  flask import Flask ,request
import json
from flask_restful import Resource, Api
import requests
from multipledispatch import dispatch
from Metricsource import Source
app =Flask(__name__)
api = Api(app)

uri = "http://35.154.106.147:9090/api/v1/"
#query = "query?query="
clsval = Source(uri)


class Allcluster(Resource):

    def get(self, metric):
        mquery="slurm_"+metric
        val = clsval.inputoutput(mquery)
        result={}
        for i in range(len(val)):
            cluster = val[i]
            if cluster['metric']['__name__'] == 'slurm_'+metric:
                result[i+1] = {'cluster name': cluster['metric']['job'], cluster['metric']['__name__'][6:]: cluster['value'][1]}
        if result: return result ,  200
        else: return None, 404

class Onecluster(Resource):
    def get(self, clustername, metric):
        mquery = "slurm_" + metric
        val = clsval.inputoutput(clustername, mquery)
        print('value is ',val)
        result={}
        for i in range(len(val)):
            cluster = val[i]
            if cluster['metric']['__name__'] == 'slurm_'+metric:
                return {'cluster name': cluster['metric']['job'], cluster['metric']['__name__'][6:]: cluster['value'][1]}, 200
        #if result: return result ,  200
            else: return None, 404

class Clusterlist(Resource):

    def get(self, clustercmd):
        val = clsval.inputoutput(clustercmd)
        result=[]
        for i in range(len(val)):
            cluster = val[i]
            if cluster['metric']['__name__'] == clustercmd:
                result.append(cluster['metric']['job'])
        if result: return  {'clusters':result},  200
        else: return None, 404


api.add_resource(Allcluster, '/cluster/<string:metric>')# details from all clusters: end point for cpu - 2(idel,total) , node-1(idel,down) , memory-1(available)
api.add_resource(Onecluster, '/cluster/<string:clustername>/<string:metric>')# details of new requested cluster with name
api.add_resource(Clusterlist, '/<string:clustercmd>')# details of new requested cluster with name


app.run(port=5000)
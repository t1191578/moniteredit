import requests
# scheduler reqyuet with cluster name and metrics name>
class Source:

    Type = ("cpu_alloc", "cpu_idle", "cpu_Total")
    def  __init__(self,required_metric,ur):
        self.required_metric = required_metric
        self.ur=ur
    def __repr__(self):
        pass #return f"<Metric {self.required_metric}>"
    def cpu_total(self, required_metric,ur ):
        val = resp.json()
        print(val)
        # cluster = val['data']['result']['metric']['job']
        # slurm_nodes_idle= val['data']['result']['value']['1']
        cluster = val['data']['result']



    def savetodb(self):
        #establish conn to db
        #save data in data base
        pass
#for now check the out put
source =Source("cpu_idel","http://15.206.250.89:9090/api/v1/query?query=slurm_nodes_alloc{job=%22slurm2%22}")
resp = requests.get(source.ur)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
#print(resp.json())
val= resp.json()
print(val)
#cluster = val['data']['result']['metric']['job']
#slurm_nodes_idle= val['data']['result']['value']['1']
cluster = val['data']['result']

print(cluster)

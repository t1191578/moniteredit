import requests

class Source:
    def  __init__(self,required_metric,ur):
        self.required_metric = required_metric
        self.ur=ur

    def getfromdb(self):
        #establish conn to db,   query according to request and return details in the formate required
        #
        pass

    def inputoutput(input):
        cpus_idel =Source("cpu_idel","http://15.206.122.250:9090/api/v1/query?query=slurm_cpus_idle")
        cpus_total=Source("cpu_total","http://15.206.122.250:9090/api/v1/query?query=slurm_cpus_total")
        Allc_nodes_idle=Source("nodes_idel","http://15.206.122.250:9090/api/v1/query?query=slurm_nodes_idle")
        #nodes_total=Source("cpu_idle","http://15.206.250.89:9090/api/v1/query?query=slurm_cpus_idle{job=%22slurm2%22}")
        nodes_down=Source("nodes_down","http://15.206.122.250:9090/api/v1/query?query=slurm_nodes_down")
        #memory_avaialble=Source("cpu_idel","http://15.206.250.89:9090/api/v1/query?query=slurm_cpus_idle{job=%22slurm2%22}")
        cluster_list=Source("cluster_list","http://15.206.122.250:9090/api/v1/query?query=go_info")

        print(input)
        resp = requests.get(input.ur)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        #print(resp.json())`
        val= resp.json()
        print(val)
        #cluster = val['data']['result']['metric']['job']
        #slurm_nodes_idle= val['data']['result']['value']['1']
        cluster = val['data']['result'][0],val['data']['result'][1]

        print(cluster[0])
        print(cluster[1])

val=Source.inputoutput("cpus_idel")
print(val)
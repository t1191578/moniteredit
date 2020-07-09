from Metricsource import Source
import json
class Cluster():
    def __init__(self,metricname):
        self.metricname=metricname


    def get(self, name):
        return f"{'name', {self.metricname}}"

#def describe_task(task_id):
#    return requests.get(_url('/tasks/{:d}/'.format(task_id)))

    val=Source.inputoutput("nodes_down")
    print('final val',val)
    print('length val', len(val))
    val1={}
    val1= val[0]
    print('val 1 is ',val1['metric'])


    for i in range (len(val)):
        val1 = val[i]
        print(val1)


        if val1['metric']['__name__'] == 'slurm_nodes_down':


            print("cluster1:",val1['metric']['job'])
            print("nodes_down:", val1['value'][1])
            print("substring:", val1['metric']['__name__'][6:])

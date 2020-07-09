import requests
from multipledispatch import dispatch


class Source:
    def __init__(self,url,query):
        self.url = url
        self.query= query
    def url(self):
        #form url
        pass

    @dispatch(str)
    def inputoutput(self, metricreq):
        Aurl = self.url+self.query+metricreq
        print(Aurl)
        resp = requests.get(Aurl)
        if resp.status_code != 200:
                    # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        val= resp.json()
        cluster = val['data']['result']
        return cluster
    @dispatch(str,str)
    def inputoutput(self, name, metricreq):
        Aurl = self.url + self.query + metricreq+'{job="'+name+'"}'
        resp = requests.get(Aurl)
        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        val = resp.json()
        cluster = val['data']['result']
        return cluster

uri="http://35.154.106.147:9090/api/v1/"
query= "query?query="
val=Source(uri,query)
val.inputoutput( "go_info")
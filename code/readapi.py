import requests

resp = requests.get('http://15.206.250.89:9090/api/v1/query?query=slurm_nodes_idle')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
print(resp.json())

node= {'ip': '10.3', 'name': 'cluster name33', 'port': '2000'}
resp = requests.post('http://127.0.0.1:5000/student/cluster name33', json=node)
#if resp.status_code != 201:
 #   raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print(resp.json())
dic={}
dic=resp.json()
print(dic)
#fin = open("out.txt", "wt")

textToSearch = input( "dd" )
textToReplace = input( "10.2 " )
fileToSearch = 'events.txt'
tempFile = open( fileToSearch, 'r+' )


with open('events.txt','w') as fd:
    for line in fd:
         fdw= fd.write()
         fdw = fdw.replace('dd', 'python')

    fd.close()



#with open('events.txt','w') as fd:
 #   fd.write(r.text)
############################
#for todo_item in resp.json():
    #for subitem in todo_item.json():
    #print('{} {}'.format(todo_item['ip']))
 #   print('{}'.format(todo_item))

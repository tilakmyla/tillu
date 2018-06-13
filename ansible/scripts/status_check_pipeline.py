from elasticsearch import Elasticsearch
import requests
import sys
import time
apache_url = "http://34.238.151.235:80"
es = Elasticsearch(['http://log-es-767366264.us-east-1.elb.amazonaws.com:80'])


## Generate the load to the apache server so that it will generate the logs
for i in range(50):
	r = requests.get(url = apache_url)
	if r.status_code != 200:
		print "server unreachable"
		sys.exit()


time.sleep(10)
## Check for the Elasticsearch cluster status
if es.ping():
    read = es.cluster.health()
    if read['status'] == "green":
        #time.sleep(10)
    	print "elasticsearch cluster status check passed and searching for the documents"
    	response_single = es.search(index="log-*", q='python-requests AND @timestamp:[now-2m TO now]', size=10000)
    	if response_single['hits']['total'] >= 50:
                print response_single['hits']['hits'][0]
    		print "documents found and status check passed"
    	elif response_single['hits']['total'] == 0:
    		print "No documents found in Elasticsearch, Status check failed"
                sys.exit()
    elif read['status'] == "yellow":
    	print "Cluster status is yellow"
    elif read['status'] == "red":
    	print "Cluster status is red, Status check failed.. exited"
    	sys.exit()
else:
	print "cluster Unreachable"
	sys.exit()

from elasticsearch import Elasticsearch
import sys
es = Elasticsearch(['http://log-es-767366264.us-east-1.elb.amazonaws.com:80'])
if es.ping():
    read = es.cluster.health()
    if read['status'] == "green":
        print "Status check passed"
    elif read['status'] == "yellow":
        print "Cluster status is yellow"
    elif read['status'] == "red":
        print "Cluster status is red, Status check failed.. exited"
        sys.exit()
else:
        print "cluster Unreachable"
        sys.exit()

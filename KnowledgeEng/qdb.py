__author__ = 'colinmoore-hill'


from py2neo import Graph


graphdb = Graph("http://ParaDroid_KE:mKDMaaAPthbgqzAMuysE@paradroidke.sb04.stations.graphenedb.com:24789/db/data/")


def executeCypher(qry):
    resp = graphdb.cypher.execute(qry)
    return resp


def getNode(lbl, ref):
    pass

def mergeNode(lbl, args):
    qry = "MERGE (n :"+lbl+" "+args+") RETURN n.name"
    print(qry)
    resp = executeCypher( qry)
    print(resp)

def mergeRel(qry):
    pass



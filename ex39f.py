import numpy as np
def Dag_graph(adj_list):
   DAG = {}
   for edge in adj_list:
      source_d , w = edge.split(':')
      source,d = map(int,source_d.split('->'))
      w = int(w)
      if source not in DAG:
         DAG[source]=[]
      DAG[source].append((d,w))
   if d not in DAG:
      DAG[d] = []
   return DAG
def topological_sort(DAG):
   node_visted = []
   order = []
   def searchnodes(source):
      node_visted.append(source)
      if source in DAG.keys():
         for neighbor in DAG[source]:
            if neighbor[0] not in node_visted:
               searchnodes(neighbor[0])
      order.append(source)
   for source in DAG.keys():
      if source not in node_visted:
         searchnodes(source)
   return order[::-1]

def Longestpath(graph,source,sink):
   order = topological_sort(graph)
   score = {node: -float("Inf") for node in order}
   score[source]=0
   parent = {}
   for node in order:
      if node==sink:
         break
      if node in graph.keys():
            for i in range(len(graph[node])):
               neighbor = graph[node][i][0]
               w = graph[node][i][1]
               if score[node]+w > score[neighbor]:
                  score[neighbor]=score[node]+w
                  parent[neighbor]=node
   path = []
   current = sink
   while current != source:
      path.append(current)
      if current in parent:
         current=parent[current]
      else:
         break

   path.append(source)
   path.reverse()
   return score[sink],path
if __name__ =="__main__":

   source = np.loadtxt( 'rosalind_ba5d.txt',max_rows=1,dtype=int)
   sink = np.loadtxt('rosalind_ba5d.txt',skiprows=1, max_rows=1, dtype=int)
   source = int(source)
   sink = int(sink)
   adj_list = np.loadtxt('rosalind_ba5d.txt',skiprows=2,dtype=str)
   graph = Dag_graph(adj_list)
   #print(graph)
   #print(topological_sort(graph))
   ans = Longestpath(graph,source,sink)[0]
   ans2 = Longestpath(graph,source, sink)[1]
   ans2=[str(x) for x in ans2]
   ans2 = '->'.join(ans2)
   print(ans)
   print(ans2)

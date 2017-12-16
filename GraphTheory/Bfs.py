import sys
from queue import *

def bfs(g, s):
	n = len(g)-1

	# setup a list to store the distances from s.
	d = [-1] * (n+1)
	d[s] = 0

	# setup the queue for bfs
	q = Queue(maxsize=0)
	q.put(s)

	# setup array to note visited vertices.
	v = [False] * (n+1)
	v[s] = True

	# compute the distances.
	while not q.empty():
		curr = q.get()
		for u in g[curr]:
			if not v[u]:
				q.put(u)
				d[u] = d[curr] + 6
				v[u] = True

	# return the distances.
	return d

def main():
	q = int(input())

	for _ in range(q):
		[n, m] = [int(i) for i in input().strip().split(' ')]
		
		# Make a graph of the required size
		graph = []
		for _ in range(0, n+1):
			graph.append([])

		for _ in range(m):
			[u, v] = [int(i) for i in input().strip().split(' ')]
			graph[u].append(v)
			graph[v].append(u)

		src = int(input())

		d = bfs(graph, src)

		for i in range(len(d)):
			if i != 0 and i != src:
				print(d[i], end=' ')
		print()

if __name__ == "__main__":
	main()
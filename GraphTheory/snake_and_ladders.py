from queue import *

def replace(g, this, that):
	for (k, v) in g.items():
		for i in range(len(v)):
			if v[i] == this:
				v[i] = that
	del g[this]

def bfs(g, s):
	d = [-1] * 101
	d[s] = 0
	q = Queue(maxsize=0)
	q.put(s)
	v = [False] * 101
	v[s] = True

	while not q.empty():
		curr = q.get()

		for u in g[curr]:
			if not v[u]:
				d[u] = d[curr] + 1
				v[u] = True
				q.put(u)

	return d

def print_graph(g):
	for (k, v) in g.items():
		print(k, end=': ')
		for i in v:
			print(i, end=' ')
		print()

def main():
	t = int(input())
	for _ in range(t):
		
		# construct the graph
		graph = {}
		for i in range(1, 101):
			graph[i] = list(range(i+1, (i+7) if (i+7) <= 101 else 101))
		
		this = []
		that = []
		n = int(input())
		for _ in range(n):
			[i, j] = [int(i) for i in input().strip().split(' ')]
			this.append(i)
			that.append(j)
		m = int(input())
		for _ in range(m):
			[i, j] = [int(i) for i in input().strip().split(' ')]
			this.append(i)
			that.append(j)

		assert len(this) == len(that)

		for i in range(len(this)):
			replace(graph, this[i], that[i])

		dist = bfs(graph, 1)

		print(dist[100])

if __name__ == "__main__":
	main()
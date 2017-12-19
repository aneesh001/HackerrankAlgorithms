from queue import *

def make_tree(g, t, p):
	n = len(g)
	visited = [False] * (n+1)
	visited[1] = True

	q = Queue(maxsize=0)
	q.put(1)

	while not q.empty():
		curr = q.get()
		for v in g[curr]:
			if not visited[v]:
				visited[v] = True
				p[v] = curr
				t[curr].append(v)
				q.put(v)

def compute_sizes(tree, size, root):
	s = 1
	for v in tree[root]:
		compute_sizes(tree, size, v)
		s += size[v]
	size[root] = s		

def main():
	[n, m] = [int(i) for i in input().strip().split(' ')]

	graph = {}
	for i in range(1, n+1):
		graph[i] = []
	for _ in range(m):
		[u, v] = [int(i) for i in input().strip().split(' ')]
		graph[u].append(v)
		graph[v].append(u)
	
	tree = {}
	for i in range(1, n+1):
		tree[i] = []
	parent = list(range(n+1))

	make_tree(graph, tree, parent)

	size = [0] * (n+1)
	compute_sizes(tree, size, 1)

	ans = 0
	for i in range(2, n+1):
		if size[i] % 2 == 0:
			ans += 1
	print(ans)

if __name__ == "__main__":
	main()
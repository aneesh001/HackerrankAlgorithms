from collections import defaultdict
from heapq import *

def djikstra(graph, src):
	# Keep track of the vertices accounted for.
	visited = {src}

	# setup list to hold closest distances
	dist = [-1] * (len(graph) + 1)
	dist[src] = 0

	verts = []
	for (k, v) in graph[src]:
		verts.append((v, k))
	heapify(verts)

	while len(visited) != len(graph) and len(verts) > 0:
		top = heappop(verts)

		if top[1] not in visited:
			visited.add(top[1])

			if dist[top[1]] == -1 or dist[top[1]] > top[0]:
				dist[top[1]] = top[0]

			for (k, v) in graph[top[1]]:
				if k not in visited:
					heappush(verts, (v + dist[top[1]], k))

	# return the list of smallest distances from src
	return dist

def main():
	t = int(input())
	for _ in range(t):
		[n, m] = [int(i) for i in input().strip().split(' ')]
		g = defaultdict(list)
		for i in range(1, n+1):
			g[i] = []
		for _ in range(m):
			[x, y, r] = [int(i) for i in input().strip().split(' ')]
			g[x].append((y, r))
			g[y].append((x, r))
		s = int(input())

		d = djikstra(g, s)

		for i in range(1, len(d)):
			if i != s:
				print(d[i], end=' ')
		print()

if __name__ == "__main__":
	main()
from functools import cmp_to_key

class union_find(object):
	def __init__(self, n):
		self.parent = []
		self.rank = [0] * (n+1)
		self.c = n

		for i in range(0, n+1):
			self.parent.append(i)

	def count(self):
		return self.c

	def find(self, i):
		if self.parent[i] != i:
			self.parent[i] = self.find(self.parent[i])
		return self.parent[i]

	def connected(self, i, j):
		return self.find(i) == self.find(j)

	def union(self, i, j):
		pi = self.find(i)
		pj = self.find(j)

		if pi == pj:
			return

		if self.rank[pi] < self.rank[pj]:
			self.parent[pi] = pj
		else:
			self.parent[pj] = pi

			if self.rank[pi] == self.rank[pj]:
				self.rank[pi] += 1

		self.c -= 1


def edge_comp(e1, e2):
	if e1[2] < e2[2]:
		return -1
	elif e1[2] > e2[2]:
		return 1
	else:
		return -1 if sum(e1) <= sum(e2) else 1

def main():
	[n, m] = [int(i) for i in input().strip().split(' ')]
	edges = []
	for _ in range(m):
		[x, y, r] = [int(i) for i in input().strip().split(' ')]
		edges.append((x, y, r))
	edges.sort(key=cmp_to_key(edge_comp))
	uf = union_find(n)

	i = 0
	t = 0
	while uf.count() >= 2 and i < len(edges):
		if not uf.connected(edges[i][0], edges[i][1]):
			uf.union(edges[i][0], edges[i][1])
			t += edges[i][2]
		i += 1

	print(t)

if __name__ == "__main__":
	main()
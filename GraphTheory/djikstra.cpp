#include <vector>
#include <map>
#include <cstdio>
#include <queue>
#include <utility>
#include <set>

using std::vector;
using std::map;
using std::priority_queue;
using std::set;
using std::pair;

struct vert_comp {
	bool operator()(const pair<int, int> &f, const pair<int, int> &s) {
		return !(f.first < s.first);
	}
};

vector<int> distance(map<int, vector<pair<int, int>>> g, int s) {
	vector<int> dist(g.size() + 1, -1);

	set<int> visited;
	visited.insert(s);

	priority_queue<pair<int, int>, vector<pair<int, int>>, vert_comp> verts;
	for(auto &i: g[s]) {
		verts.push({i.second, i.first});
	}

	while(visited.size() != g.size() && !verts.empty()) {
		auto t = verts.top();
		verts.pop();

		if(visited.find(t.second) == visited.end()) {
			visited.insert(t.second);

			if(dist[t.second] == -1 || dist[t.second] > t.first) {
				dist[t.second] = t.first;
			}

			for(auto &i: g[t.second]) {
				if(visited.find(i.first) == visited.end()) {
					verts.push({dist[t.second] + i.second, i.first});
				}
			}
		}
	}

	return dist;
}

int main(void) {
	int t;
	scanf("%d", &t);

	while(t--) {
		int n, m;
		scanf("%d %d", &n, &m);

		map<int, vector<pair<int, int>>> graph;
		for(int i = 1; i <= n; ++i) {
			graph.insert({i, vector<pair<int, int>>()});
		}
		for(int i = 0; i < m; ++i) {
			int x, y, r;
			scanf("%d %d %d", &x, &y, &r);

			graph[x].push_back({y, r});
			graph[y].push_back({x, r});
		}

		int src;
		scanf("%d", &src);

		vector<int> dist = distance(graph, src);

		for(int i = 1; i <= n; ++i) {
			if(i != src)
				printf("%d ", dist[i]);
		}
		printf("\n");
	}

	return 0;
}
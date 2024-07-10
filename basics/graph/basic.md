# graph based problems

## The graph problems

Differences between BFS and DFS in python is trival, depending on which node to take in one iteration, either the first one by `q.pop(0)` for BFS or the last one by `q.pop()` for DFS.

Normally we need a variable `seen` to store the visited nodes to avoid the unnecessary reprocessing, just remember to use a `set()` instead of a `list`, cause there are repeated failures of TLE due to the use of a list.

### Bellman-Ford vs. Dijkstra Algorithms

1. **Use Case**:
   - Bellman-Ford: Handles negative weights and detects negative cycles.
   - Dijkstra: Efficient for non-negative weights.

2. **Time Complexity**:
   - Bellman-Ford: \(O(V \cdot E)\)
   - Dijkstra: 
     - \(O(V^2)\) (simple implementation)
     - \(O((V + E) \log V)\) (binary heap)
     - \(O(E + V \log V)\) (Fibonacci heap)

3. **Algorithm Type**:
   - Bellman-Ford: Dynamic Programming
   - Dijkstra: Greedy Algorithm

4. **Process**:
   - Bellman-Ford: Relaxes all edges \(V-1\) times.
   - Dijkstra: Uses priority queue to extend shortest known path.

5. **Initialization**:
   - Both: Distances initialized to \(\infty\), source set to 0.

6. **Negative Weight Cycles**:
   - Bellman-Ford: Detects negative cycles.
   - Dijkstra: Cannot handle negative weights.

**Summary**:

- **Bellman-Ford**: Versatile, suitable for financial modeling.

- **Dijkstra**: Efficient for routing and road networks.

### Cycle problems

|Link|Comment|Date|
|---|---|---|
|[LC 1971 Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)| Disjoint set, BFS and DFS will be TLE, only if the seen is using a list instead of a set. |05/01/2024|
|[LC 2065 Maximum Path Quality of a Graph](https://leetcode.com/problems/maximum-path-quality-of-a-graph/description/)|DFS, Recursion, set: {0}, |05/01/2024|

```python
    def validPath(self, n: int, edges: List[List[int]], s: int, d: int) -> bool:
        graph = defaultdict(list)
        for e in edges:
            u,v = e
            graph[u].append(v)
            graph[v].append(u)
        
        q,seen = [], set()
        seen.add(s)
        q.append(s)
        while q:
            #This defines BFS pop(0) or DFS pop().
            cur = q.pop(0)
            if cur == d:
                return True
            for nxt in graph[cur]:
                if nxt in seen:
                    continue
                seen.add(nxt)
                q.append(nxt)
        return False
```

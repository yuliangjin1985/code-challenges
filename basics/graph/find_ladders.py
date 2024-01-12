from collections import defaultdict

class Solution:
    def findLadders(self, b: str, e: str, wl: list[str]) -> list[list[str]]:
        graph = defaultdict(list)
        N, L = len(wl), len(b)
        for w in wl:
            for i in range(L):
                key = w[:i] + '*' + w[i+1:]
                graph[key].append(w)
        
        print(graph)
        
        queue = []
        queue.append(b)
        temp = defaultdict(list)
        temp[b] = [[b]]
        visited = set()

        while queue:
            cur = queue.pop(0)
            if cur == e:
                return temp[cur]
            # Explore next level
            paths = temp[cur]
            for i in range(L):
                key = cur[:i] + '*' + cur[i+1:]
                for next in graph[key]:
                    # if next in temp: continue
                    if next == cur: continue
                    if next in visited: continue
                    updated_paths = temp[next]
                    for path in paths:
                        new_path = []
                        for k in path:
                            new_path.append(k)
                        new_path.append(next)
                        if updated_paths and len(new_path) > len(updated_paths[-1]):
                            continue
                        if new_path in updated_paths: continue
                        updated_paths.append(new_path)
                    if next not in queue: queue.append(next)
            visited.add(cur)
        
        return []















if __name__ == "__main__":
    # test cases
    # b = "hit", e = "cog", wl = ["hot","dot","dog","lot","log","cog"]
    ret = Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    print(ret)
from heapq import *
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # the id starts at 1
        graph = [[] for _ in range(n+1)]
        # construct the graph
        for edge in times:
            f, t, w = edge[0], edge[1], edge[2]
            graph[f].append([t, w])
        # call dijkstra function
        # Given a graph and a start point
        # return a list of the minimun distance from the start point to other nodes.
        distTo = self.dijkstra(k ,graph)
        # Find the longest minimun distance
        res = 0
        for i in range(1, len(distTo)):
            if distTo[i] == float('inf'):
                # There is at least a node can be reached
                return -1
            res = max(res, distTo[i])
        return res
    
    def dijkstra(self, start:int, graph:List[List[int]]) -> List[int]:
        distTo = [float('inf') for _ in range(len(graph))]
        distTo[start] = 0
        heap = []
        heappush(heap, (0, list([start, 0])))
        while heap:
            cur_state = heappop(heap)[1]
            cur_node_id, cur_dist_from_start = cur_state[0], cur_state[1]
            if distTo[cur_node_id] < cur_dist_from_start:
                continue
            for neighbor in graph[cur_node_id]:
                next_node_id = neighbor[0]
                dist_to_next_node = distTo[cur_node_id] + neighbor[1]
                # Update the dp table
                if dist_to_next_node < distTo[next_node_id]:
                    distTo[next_node_id] = dist_to_next_node
                    heappush(heap, (dist_to_next_node, list([next_node_id, dist_to_next_node])))

        return distTo

class State:
    def __init__(self, id:int, distFromStart:int) -> None:
        # node's id
        self.id = id
        # The distance from start point to this node
        self.distFromStart = distFromStart


class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 鄰接表建圖
        graph = [[] for _ in range(n+1)]
        for edge in times:
            from_node, to_node, weight = edge
            graph[from_node].append([to_node, weight])
        # 距離數組
        distance = [float('inf') for _ in range(n+1)]
        distance[k] = 0
        # 記錄是否訪問過的數組
        visited = [False for _ in range(n+1)]
        # heap
        heap = []
        heappush(heap, [0, k]) # [weight, source]
        # 遍歷
        while heap:
            _, cur_node = heappop(heap)
            if visited[cur_node]: continue
            visited[cur_node] = True
            # 考察每一條邊
            for edge in graph[cur_node]:
                to_node, weight = edge
                if not visited[to_node] and distance[cur_node] + weight < distance[to_node]:
                    distance[to_node] = distance[cur_node] + weight
                    heappush(heap, [distance[to_node], to_node])

        ans = float('-inf')
        for i in range(1, n+1):
            if distance[i] == float('inf'):
                return -1
            ans = max(ans, distance[i])

        return ans
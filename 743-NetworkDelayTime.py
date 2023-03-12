import heapq
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
        pq = []
        #heapq.heappush(pq, (0, State(start, 0)))
        heapq.heappush(pq, (0, list([start, 0])))
        while pq:
            cur_state = heapq.heappop(pq)[1]
            #cur_node_id, cur_dist_from_start = cur_state.id, cur_state.distFromStart
            cur_node_id, cur_dist_from_start = cur_state[0], cur_state[1]
            if distTo[cur_node_id] < cur_dist_from_start:
                continue
            for neighbor in graph[cur_node_id]:
                next_node_id = neighbor[0]
                dist_to_next_node = distTo[cur_node_id] + neighbor[1]
                # Update the dp table
                if dist_to_next_node < distTo[next_node_id]:
                    distTo[next_node_id] = dist_to_next_node
                    #heapq.heappush(pq, (dist_to_next_node, State(next_node_id, dist_to_next_node)))
                    heapq.heappush(pq, (dist_to_next_node, list([next_node_id, dist_to_next_node])))

        return distTo

class State:
    def __init__(self, id:int, distFromStart:int) -> None:
        # node's id
        self.id = id
        # The distance from start point to this node
        self.distFromStart = distFromStart
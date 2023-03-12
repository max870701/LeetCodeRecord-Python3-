import heapq
from typing import List, Any
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        # construct the graph
        for i in range(len(edges)):
            f, t = edges[i][0], edges[i][1]
            w = succProb[i]
            graph[f].append([t, w])
            graph[t].append([f, w])
        
        return self.dijkstra(start, end, graph)

    def dijkstra(self, start:int, end:int, graph:List[List[Any]]) -> float:
        # Definition: proTo[i] is the maximum probability from the start node to the node i
        # Set the initial value as -1
        probTo = [-1 for _ in range(len(graph))]
        # Base case, the probability from start to start is 1
        probTo[start] = 1
        # Priority Queue, the priority order is the bigger prob_from_start
        # Definition of State: [id, prob_from_start]
        pq = []
        heapq.heappush(pq, (1, [start, 1]))
        while pq:
            cur_state = heapq.heappop(pq)[1]
            cur_node_id, cur_prob_from_start = cur_state[0], cur_state[1]
            # Return cur_prob_from_start if reach the end point
            if cur_node_id == end:
                return cur_prob_from_start
            # Continue, if there is already a bigger probability
            if probTo[cur_node_id] > cur_prob_from_start:
                continue
            # Push adjacent nodes into the Priority Queue
            for neighbor in graph[cur_node_id]:
                next_node_id = neighbor[0]
                # Check if there is a bigger probability from cur_node_id to next_node_id
                prob_to_next_node = probTo[cur_node_id] * neighbor[1]
                if prob_to_next_node > probTo[next_node_id]:
                    probTo[next_node_id] = prob_to_next_node
                    # By the default in Python, the heap queue is a min heap.
                    # If we want to order the heap queue as max heap, add a negative symbol in your priority order
                    heapq.heappush(pq, (-prob_to_next_node, [next_node_id, prob_to_next_node]))
        return 0.0
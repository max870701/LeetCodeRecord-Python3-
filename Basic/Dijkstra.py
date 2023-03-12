import heapq
from typing import List

class State:
    def __init__(self, id:int, distFromStart:int) -> None:
        # node's id
        self.id = id
        # The distance from start point to this node
        self.distFromStart = distFromStart

# Input a frome node id and a to node id, return the weight
def weight(f:int, t:int) -> int:
    pass

# Input a node s id< return all adjacent nodes of it
def adj(s:int) -> List[int]:
    pass

# Input a graph and a start point
# return a list of the minimun distance from the start point to other nodes. 
def dijkstra(start:int, graph:List[List[int]]) -> List[int]:
    # The number of nodes in the graph
    len_graph = len(graph)
    # Record the weight of the minimum distance. A kind of dp table
    # Definition: distTo[i] is the weight of the minimum distance
    #             from the start point to the node i
    # The initial value in distTo is a positive infinity integar
    distTo = [[float('inf') for _ in range(len_graph)]]
    # Base case: start to start, the minimum distance is zero
    distTo[start] = 0
    # Priority Queue, the priority order is the distFromStart
    # BFS from the start point
    pq = []
    heapq.heappush(pq, (0, State(start, 0)))
    while pq:
        cur_state = heapq.heappop(pq)
        cur_node_id = cur_state.id
        cur_distfromstart = cur_state.distFromStart
        # If there is already a shorter path to the current node
        if distTo[cur_node_id] < cur_distfromstart:
            continue
        # Push adjacent nodes of the current node into the Priority Queue
        for next_node_id in adj(cur_node_id):
            # Check if there is a shorter path from curNode to nextNode
            dist_to_next_node = distTo[cur_node_id] + weight(cur_node_id, next_node_id)
            if dist_to_next_node < distTo[next_node_id]:
                # Update the dp table
                distTo[next_node_id] = dist_to_next_node
                # Push this node and the distance into the Priority Queue
                # In Python, we cannot prioritize between to State instance
                # We can replace the State instance as a list
                heapq.heappush(pq, (dist_to_next_node, State(next_node_id, dist_to_next_node)))
    return distTo
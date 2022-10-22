graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

def BFS(graph, s):
    # First come, first out
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)

    while (len(queue) > 0):
        vertex = queue.pop(0) # pop the first element
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w) # add to the last position
                seen.add(w)
        print(vertex)

if __name__ == "__main__":
    BFS(graph, "A")
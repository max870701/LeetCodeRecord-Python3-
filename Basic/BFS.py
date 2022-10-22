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
    parent = {s: None}

    while (len(queue) > 0):
        vertex = queue.pop(0) # pop the first element
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w) # add to the last position
                seen.add(w)
                parent[w] = vertex
        #print(vertex)
    
    return parent

if __name__ == "__main__":
    parent = BFS(graph, "E")
    #for key in parent:
    #    print(key, parent[key])
    v = "B"
    count = 0
    while v:
        print(v)
        v = parent[v]
        count += 1
    print("The shortest steps is {}".format(count))
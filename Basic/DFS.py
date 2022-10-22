graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}

def DFS(graph, s):
    # First in, last out
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)

    while (len(stack) > 0):
        vertex = stack.pop() # pop the last element
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w) # add to the last position
                seen.add(w)
        print(vertex)

if __name__ == "__main__":
    DFS(graph, "A")
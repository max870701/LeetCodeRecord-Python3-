function findOrder(numCourses: number, prerequisites: number[][]): number[] {
    // Build a directed graph (Adajency List, Indegree List)
    var graph: number[][] = Array.from({ length: numCourses }, () => [])
    var indegree: number[] = new Array(numCourses).fill(0)

    for (let i = 0; i < prerequisites.length; i++) {
        var [to_node, from_node] = prerequisites[i]
        graph[from_node].push(to_node)
        indegree[to_node]++
    }
    // Add vertices with 0 indegree into a queue
    var queue: number[] = new Array(numCourses).fill(0)
    var left: number = 0
    var right: number = 0

    for (let i = 0; i < numCourses; i++) {
        if (indegree[i] === 0) {
            queue[right++] = i
        }
    }
    // BFS
    var cnt = 0
    while (left < right) {
        var cur_node = queue[left++]
        cnt++
        for (let neighbor of graph[cur_node]) {
            if (--indegree[neighbor] == 0) {
                queue[right++] = neighbor
            }
        }
    }

    return cnt === numCourses ? queue : []
};
function wallsAndGates(rooms: number[][]): void {
    const row: number = rooms.length
    const col: number = rooms[0].length
    let queue: Array<[number, number]> = []
    let visited: Set<string> = new Set()

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (rooms[i][j] === 0) {
                const pos = `${i},${j}`;
                queue.push([i, j])
                visited.add(pos)
            }
        }
    }

    function bfs(x: number, y: number): void {
        if (x < 0 || x >= row || y < 0 || y >= col || visited.has(`${x},${y}`) || rooms[x][y] === -1)
            return
        queue.push([x, y])
        visited.add(`${x},${y}`)
    };

    var dist: number = 0
    while (queue.length > 0) {
        let currentLevelSize = queue.length;
        for (let k = 0; k < currentLevelSize; k++) {
            const [x, y] = queue.shift()!;
            rooms[x][y] = dist
            bfs(x + 1, y)
            bfs(x - 1, y)
            bfs(x, y + 1)
            bfs(x, y - 1)
        }
        dist++
    }
}
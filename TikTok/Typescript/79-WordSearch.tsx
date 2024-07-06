function exist(board: string[][], word: string): boolean {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (f(board, i, j, word, 0)) return true
        }
    }
    return false
};

function f(board: string[][], i: number, j: number, word: string, k: number): boolean {
    if (k === word.length) return true
    if (i < 0 || i === board.length || j < 0 || j === board[0].length || board[i][j] !== word.charAt(k)) return false

    var tmp: string = board[i][j]
    board[i][j] = "0"
    var ans: boolean = f(board, i + 1, j, word, k + 1) || f(board, i - 1, j, word, k + 1) || f(board, i, j + 1, word, k + 1) || f(board, i, j - 1, word, k + 1)
    board[i][j] = tmp

    return ans
};

function exist1(board: string[][], word: string): boolean {
    const find = (i: number, j: number, k: number) => {
        if (k === word.length) return true
        if (i < 0 || i === row || j < 0 || j === col || board[i][j] !== word.charAt(k)) return false
        let tmp: string = board[i][j]
        board[i][j] = "0"
        let ans: boolean = find(i-1, j, k+1) || find(i+1, j, k+1) || find(i, j-1, k+1) || find(i, j+1, k+1)
        board[i][j] = tmp

        return ans
    }
    // Start from all positions to serach the word
    let row = board.length, col = board[0].length
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (find(i, j, 0)) return true
        }
    }
    return false
};
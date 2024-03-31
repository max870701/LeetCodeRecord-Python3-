// Time Complexity: O(n)
// Space Complexity: O(n)
function validateStackSequences(pushed: number[], popped: number[]): boolean {
    var res: number[] = []
    var p: number = 0
    // When push
    for (let n of pushed) {
        res.push(n)
        // When pop
        while (res.length && res[res.length - 1] === popped[p]) {
            res.pop()
            p++
        }
    }

    return res.length === 0
};

// Time Complexity: O(n)
// Space Complexity: O(1)
function validateStackSequences2(pushed: number[], popped: number[]): boolean {
    var i: number = 0
    var j: number = 0

    for (let n of pushed) {
        pushed[i++] = n
        while (i > 0 && pushed[i-1] === popped[j]) {
            i--
            j++
        }
    }

    return i === 0
};
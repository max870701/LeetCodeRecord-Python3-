function longestPalindrome(s: string): string {
    var res: string = ""

    for (var i = 0; i < s.length; i++) {
        // Find the palindrome which the center is s[i]
        var p1 = palindrome(s, i, i)
        // Find the palindrome which the center is s[i] and s[i+1]
        var p2 = palindrome(s, i, i+1)
        // Update the res
        res = res.length > p1.length ? res : p1
        res = res.length > p2.length ? res : p2
    }

    return res
};

function palindrome(s: string, l: number, r: number): string {
    while (l >= 0 && r < s.length && s.charAt(l) === s.charAt(r)) {
        l--
        r++
    }
    return s.substring(l+1, r)
};
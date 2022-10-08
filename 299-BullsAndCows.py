class Solution(object):
    def generate_dict(self, l):
        tmp = collections.defaultdict(int)
        for s in l:
            tmp[s] += 1
        return tmp

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # guess number 1A2B game
        # Time O(N)
        # Space O(1)
        secret_dict = self.generate_dict(secret)
        guess_dict = self.generate_dict(guess)

        bulls = cows = 0

        for key, value in guess_dict.items():
            if key in secret_dict:
                cows += min(value, secret_dict[key])

        i = 0
        while i < len(guess):
            if guess[i] == secret[i]:
                cows -= 1
                bulls += 1
            i += 1

        return "{}A{}B".format(bulls, cows)

    def getHint1(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # guess number 1A2B game
        # Time O(N)
        # Space O(1)
        tmp = collections.defaultdict(int)
        bulls = cows = 0

        for index, s in enumerate(secret):
            g = guess[index] # value in guess
            if s == g:
                bulls += 1
            else:
                #cows += int(tmp[s] < 0) + int(tmp[g] > 0)
                if tmp[s] < 0: # can find in guess
                    cows += 1
                if tmp[g] > 0: # can find in seceret
                    cows += 1                
                tmp[s] += 1
                tmp[g] -= 1
                
        return "{}A{}B".format(bulls, cows)
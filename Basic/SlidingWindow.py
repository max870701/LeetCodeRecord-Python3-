# Frame of Sliding Window
def slidingWindow(s);
    window = dict()
    left = right = 0
    
    while right < len(s):
        # char c is the character moved into the window
        c = s[right]
        # increase the window
        right += 1
        # Update your data below

        # Debugging output
        print("Window: [{}, {})\n".format(left, right))

        # Determine if the left side of window need be shrinked
        while (condition):
            # char d will be removed from the window
            d = s[left]
            # Shrink the window
            left += 1
            # Update the data in the window


def flip(ch):
    return '1' if (ch == '0') else '0'

def minFlipsWith(s, start_char):
    c = 0
    for i in range(len(s)):
        if (s[i] != start_char):
            c += 1
        start_char = flip(start_char)
    return c


def minFlips(s):
    return min(minFlipsWith(s, '0'),
               minFlipsWith(s, '1'))


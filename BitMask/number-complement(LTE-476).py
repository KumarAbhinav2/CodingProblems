class Solution:

    """
    xor of bit with 1 will flip the bits
    xor of bit with 0 will result in same bit
    """
    def findComplement(self, num: int) -> int:
        # This algo follows the openJDK algorithm implementation
        # Will create the bitmask by propagating the highest bit into lower bits
        # then xor with num will result in complement
        bitmask = num
        bitmask |= bitmask >> 1
        bitmask |= bitmask >> 2
        bitmask |= bitmask >> 4
        bitmask |= bitmask >> 8
        bitmask |= bitmask >> 16
        return bitmask ^ num


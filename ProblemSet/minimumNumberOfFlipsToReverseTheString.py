class Solution:
    def minimumFlips(self, n: int) -> int:
        # convert decimal to binary string
        binary = ""
        num = n
        
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        
        # reverse the binary string
        rev = binary[::-1]
        
        # count mismatches between binary and reversed version
        count = 0
        for i in range(len(binary)):
            if binary[i] != rev[i]:
                count += 1
        
        return count

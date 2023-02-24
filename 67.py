
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a,b = a[::-1],b[::-1] # reverse the strings
        for i in range(max(len(a),len(b))):
            # here i subtract ord('0') to get the int from ascii val
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            print(digitA)
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0
            total = digitB + digitA + carry
            char = str(total % 2)
            res += char + res
            carry = total // 2

            if carry: # edge case: if carry is not 0
                res += '1' + res
        return res
print(Solution().addBinary('10','11'))

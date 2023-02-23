
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        a,b = a[::-1],b[::-1] # reverse the strings
        for i in range(max(len(a),len(b))):
            print(i)
            if int(a[i])+int(b[i])+carry==0:
                res += '0'
                carry = 0
                print(res)
            elif int(a[i])+int(b[i])+carry==1:
                res += '1'
                carry = 0
                print(res)
            elif int(a[i])+int(b[i])+carry==3:
                res += '0'
                carry = 1
                print(res)
        print(res[::-1])
print(Solution().addBinary('10','1101011'))

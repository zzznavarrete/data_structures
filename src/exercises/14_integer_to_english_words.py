class Solution:
    def __init__(self):
        self.ones = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine', ' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        self.tens = ['', ' Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        self.thousands = ['', ' Thousand', ' Million', ' Billion']

    def recursive_helper(self, n:int) -> str:
        if n < 20:
            return self.ones[n]
        elif n < 100:
            return self.tens[n // 10] + self.recursive_helper(n % 10)
        elif n < 1000:
            return self.recursive_helper(n // 100) + ' Hundred' +self.recursive_helper(n % 100)
        else:
            for i in range(3, 0, -1):
                if n >= 1000**i:
                    return self.recursive_helper(n // (1000 ** i)) + self.thousands[i] + self.recursive_helper(n % (1000 ** i)) 
            
        return ""

    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        return self.recursive_helper(n=num).lstrip()

if __name__ == "__main__":
    sol = Solution()
    print(sol.numberToWords(num=9900900))

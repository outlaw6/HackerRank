class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        lists = []
        for num in range(1,n+1):
            if n % num == 0:
                lists.append(num)
	       
        return str(sum(lists))
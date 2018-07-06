class Calculator():
    
    def power(self, n, p):
        if p == 0:
            return 1
        if n == 0:
            return 0
        assert n > 0,"n and p should be non-negative"
        assert p > 0, "n and p should be non-negative"
        return n**p
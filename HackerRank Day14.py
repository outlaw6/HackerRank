class Difference:

    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        container = []
        
        for x in self.__elements:
            for y in self.__elements:
                container.append(abs(x-y))
                
        print(max(container))
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
            
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = 0
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90 and avg <= 100:
            return "O"            
        if avg >= 80 and avg < 90:
            return "E"
        if avg >= 70 and avg < 80:
            return "A"
        if avg >= 55  and avg < 70:
            return "P"
        if avg >= 40 and avg < 55:
            return "D"
        if avg < 40:
            return "T"
        
        
        
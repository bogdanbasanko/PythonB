class NumberAnalyzer:
    def __init__(self, number):
        self.number = number
        self.is_even = IsEven(number).check()
        self.is_positive = IsPositive(number).check()

    def analyze(self):
      
        return {
            "number": self.number,
            "is_even": self.is_even,
            "is_positive": self.is_positive 
        }
class IsEven:
    def __init__(self, number): 
        self.number = number

    def check(self):
        return self.number % 2 == 0
class IsPositive:
    def __init__(self, number):
        self.number = number

    def check(self):
        return self.number > 0
class Summary:
    def __init__(self, numbers):
        self.numbers = numbers
        self.even_count = 0
        self.odd_count = 0
        self.positive_count = 0
        self.negative_count = 0
        self.process_numbers()

    def process_numbers(self):
        
        for number in self.numbers:
            analysis = NumberAnalyzer(number).analyze()
            if analysis["is_even"]:
                self.even_count += 1
            else:
                self.odd_count += 1

            if analysis["is_positive"]:
                self.positive_count += 1
            else:
                self.negative_count += 1

    def get_summary(self):
        
        return {
            "even_count": self.even_count,
            "odd_count": self.odd_count,
            "positive_count": self.positive_count,
            "negative_count": self.negative_count
        }



numbers = [10, -5, 7, 0, -2, 8, -9]
summary = Summary(numbers)
print(summary.get_summary())

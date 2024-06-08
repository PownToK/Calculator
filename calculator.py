class Calculator:

    def __init__(self):
        self.sum = 0
        self.count = 0

    def add(self, n):
        self.sum += n
        self.count += 1

    def mean(self):
        return self.sum / self.count

    def reset(self):
        self.sum = 0
        self.count = 0        

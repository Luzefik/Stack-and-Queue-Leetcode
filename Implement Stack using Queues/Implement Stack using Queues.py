class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        self.queue2.append(x)

        while self.queue1:
            self.queue2.append(self.queue1.pop(0))

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue1:
            return self.queue1.pop(0)
        return None

    def top(self):
        if self.queue1:
            return self.queue1[0]
        return None

    def empty(self):
        return len(self.queue1) == 0
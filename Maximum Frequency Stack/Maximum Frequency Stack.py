class FreqStack:
    def __init__(self):
        self.freq_map = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val):
        freq = self.freq_map.get(val, 0) + 1
        self.freq_map[val] = freq

        if freq > self.max_freq:
            self.max_freq = freq

        if freq not in self.group:
            self.group[freq] = []
        self.group[freq].append(val)

    def pop(self):
        val = self.group[self.max_freq].pop()

        self.freq_map[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val
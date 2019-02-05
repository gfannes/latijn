class Score:
    def __init__(self):
        self.ok = 0
        self.ko = 0
    def update(self, b):
        if b:
            self.ok += 1
        else:
            self.ko += 1
    def __str__(self):
        return f"{self.ok}/{self.ok+self.ko}"


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

def input_int(msg, min, max):
    while True:
        v = input(msg+" ")
        try:
            v = int(v)
            assert(min < max)
            if min <= v and v <= max:
                #OK: input is accepted
                return v
            print(f"Je kan enkel een getal tussen {min} en {max} opgeven")
        except ValueError:
            print("Dit is geen getal! Probeer opnieuw.")

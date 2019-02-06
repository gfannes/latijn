from Log import error
import gubg.naft
import random

class Word:
    def __init__(self, attrs):
        self.id = int(attrs["id"])
        self.latin = attrs["latin"]
        self.dutch = attrs["dutch"]
        self.extra = attrs.get("extra", None)
        self.tip = attrs.get("tip", None)
        self.gender = attrs.get("gender", None)

    def __repr__(self):
        return f"{self.id}: {self.latin} => {self.dutch}"

    def create_from(r):
        if not r.pop_node("word"):
            return None
        return Word(r.pop_attrs())

class Book:
    def __init__(self, attrs):
        self.ary = []
        self.grade = int(attrs["grade"])
        self.name = attrs["name"]

    def __len__(self):
        return len(self.ary)

    def add(self, word):
        self.ary.append(word)

    def prune(self, six, eix):
        self.ary = self.ary[six:eix]

    def select_subset(self, size):
        return random.sample(self.ary, size)

    def load(fn):
        with open(fn, "r") as fi:
            r = gubg.naft.Range(fi.read())

        if not r.pop_node("book"):
            error(f"{fn} does not contain the [book] node")
        book = Book(r.pop_attrs())

        b = r.pop_block()
        while True:
            word = Word.create_from(b)
            if not word:
                break
            book.add(word)

        print(f"Loaded {len(book)} words from {fn}")
        return book

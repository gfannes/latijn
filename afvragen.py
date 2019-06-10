import sys
sys.path.append("gubg.io/src")

import word
import util

book = word.Book.load("vestibulum.naft")

print("Hallo Tibe, ben je er klaar voor?")

six = util.input_int(f"Van waar wil je beginnen?", 1, len(book))
eix = util.input_int(f"Tot waar wil je gaan?", 1, len(book))
book.prune(six-1, eix)

nr = util.input_int(f"Hoeveel woorden wil je afvragen? Maximum is {len(book)}.", 1, len(book))

score = util.Score()

subset = book.select_subset(nr)
for ix, word in enumerate(subset):
    print(f"\n{ix+1}/{nr}: {word.latin}")
    input("Duw op <enter> voor het antwoord")
    def hr(v, fill=" "):
        str = v if v else ""
        return str.ljust(20, fill)
    def gender(v):
        if v == "m":
            return "m."
        if v == "f":
            return "vr."
        if v == "s":
            return "onz."
        if v == "m/f":
            return "m./vr."
        return v
    print(f"{hr('Extra')} | {hr('Geslacht')} | {hr('Vertaling')} | {hr('tip')}")
    print(f"{hr('', '-')} | {hr('', '-')} | {hr('', '-')} | {hr('', '-')}")
    print(f"{hr(word.extra)} | {hr(gender(word.gender))} | {hr(word.dutch)} | {hr(word.tip)}")
    while True:
        answer = input("Had je het juist? (j,n): ")
        if answer == "j" or answer == "n":
            correct = (answer == "j")
            score.update(correct)
            with open("log.naft", "a") as fo:
                fo.write(f"[{'ok' if correct else 'ko'}](id:{word.id})\n")
            break
        print("Ik kon je antwoord niet begrijpen")

print(f"\nJe score is {score}")

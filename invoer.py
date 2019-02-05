id = input("Start id: ")
id = int(id)
with open("tmp.naft", "w") as fo:
    while True:
        print(f"id: {id}")
        latin = input("Latin: ")
        if not latin:
            break
        extra = input("Extra: ")
        gender = input("Gender: ")
        dutch = input("Dutch: ")
        tip = input("Tip: ")
        fo.write(f"\n    [word]")
        fo.write(f"(id:{id})")
        fo.write(f"(latin:{latin})")
        fo.write(f"(dutch:{dutch})")
        if extra:
            fo.write(f"(extra:{extra})")
        if gender:
            fo.write(f"(gender:{gender})")
        if tip:
            fo.write(f"(tip:{tip})")
        id += 1

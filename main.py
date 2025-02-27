def guestBook():
    name = input("sinu nimi: ")
    comment = input("sinu sõnum: ")
    text = f"nimi: "{name}, "Sõnum: " {comment}
    file = open("guestBook.txt", "a")
    fil.write(text)
    file.close()
    print("sõnum oli salvestatu edukalt")
import datetime
print(datetime.datetime.now())

def guesrBook1().
name = input("Sinu tegevus: ")
comment = input("Sinu kool: ")
text = f"Tegin: {name} Kool: {comment}\n"
file = open("guestBook1.txt", "a", encoding="utf-8")
file.write(text)
file.close()
print("Sinu tegevus")

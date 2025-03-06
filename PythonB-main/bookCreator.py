import bookCreator as bookCreator
import LogCreator as log
import fileReader as reader

def main():
    print("1 - küalisteraamat")
    print("2 - Luua loogid")
    print("3 - Lugeda faili")
    userInput = input("sinu valik: ")
    if userInput == "1":
        bookCreator.guestBook()
    elif userInput == "2":
        log.createLog()
    elif userInput =="3":
        userFile = input("Milline file as tahad lugeda?")
        reader.readFile(userFile)
    
    else:
        print("vale valik")
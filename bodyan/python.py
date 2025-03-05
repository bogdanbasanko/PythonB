with open('example.txt', 'r') as file:

    content = file.read()

if not content:  
    print("Файл пустой.")
else:
    print("Содержимое файла:")
    print(content)
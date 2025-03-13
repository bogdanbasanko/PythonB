i = 0
lines = []

# Чтение данных из файла
with open('data.txt', 'r') as file:
    lines = file.readlines()

while i < len(lines) - 1:
    line1 = lines[i].strip().split()
    line2 = lines[i + 1].strip()

    try:
       
        number1, number2 = float(line1[0]), float(line1[1])

    
        if line2 == "addition":
            result = number1 + number2
        elif line2 == "subtraction":
            result = number1 - number2
        else:
            
            raise NameError("Unsupported operation encountered")

    except NameError as e:
        
        print(f"\033[31m{NameError}: {e}\033[0m")
        i += 2
        continue
    except ValueError as e:
       
        print(f"Error: {e} in line: {lines[i]}")
        i += 2
        continue

    print(f"Result of {line2}: {result}")
    i += 2

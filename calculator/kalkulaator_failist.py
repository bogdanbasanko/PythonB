def perform_operation_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        i = 0
        while i < len(lines):
            line1 = lines[i].strip().split()
            line2 = lines[i + 1].strip()

            try:
                number1, number2 = float(line1[0]), float(line1[1])
            except ValueError:
                print(f"Error: Invalid data in line: {lines[i]}")
                i += 2
                continue

            operation = line2

            try:
                if operation == "+":
                    result = number1 + number2
                elif operation == "-":
                    result = number1 - number2
                elif operation == "*":
                    result = number1 * number2
                elif operation == "/":
                    if number2 == 0:
                       
                      ZeroDivisionError("Error: Division by zero!")
                    result = number1 / number2
                else:
                      Exception("Error: Unsupported operation!")
                
                print(f"Result for {number1} {operation} {number2}: {result}")

            except ZeroDivisionError as e:
                print(e)

            except Exception as e:
                print(f"Error: {e}")
            
            i += 2

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found!")
    except Exception as e:
        print(f"Error: {e}")


perform_operation_from_file('arvud.txt')

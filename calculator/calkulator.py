def calculate_average_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            numbers = []
            for line in file:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(f'Error in line "{line.strip()}": not a number, skipping.')
            
            if numbers:
                average = sum(numbers) / len(numbers)
                print(f'Average of numbers: {average:.2f}')
            else:
                print("No numbers found in the file.")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

calculate_average_from_file('data.txt')

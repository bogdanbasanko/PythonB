def check_username_from_file(file_name):
    forbidden_characters = "!@#$%^&*()"
    
    try:
        with open(file_name, 'r', encoding='utf-8-sig') as file:
            for line in file:
                username = line.strip()  
                
                if any(character in username for character in forbidden_characters):
                    print(f'{username} – invalid username') 
                else:
                    print(f'{username} – valid username')  
            
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}") 

check_username_from_file('kasutajad.txt')

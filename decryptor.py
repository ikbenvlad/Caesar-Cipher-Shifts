def caesar_decrypt(encrypted_message, key=1):
    decrypted = ""
    for char in encrypted_message:
        if char.isalpha():
            char_code = ord(char)
            char_code -= key
            if char.isupper():
                if char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code < ord('a'):
                    char_code += 26
            
            decrypted += chr(char_code)
        else:
            decrypted += char
    
    return decrypted

robot_name = "Spcpu"

print(robot_name + ": " + "Hi! My name is " + robot_name + ". I can decrypt Caesar ciphers for you.")

while True:
    encrypted_message = input("Enter your message ('q' to quit): ")
    
    if encrypted_message == 'q':
        decrypted_message = caesar_decrypt(encrypted_message) == False
        print(robot_name + ": " + "Thank you for using my program!")
        break
    
    else:
        decrypted_message = caesar_decrypt(encrypted_message)
    print(robot_name + ": " + "Here's your decrypted message: ", decrypted_message)

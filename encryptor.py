def caesar_encrypt(message, key=1):
    encrypted = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            char_code += key
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26 
                elif char_code < ord('a'):
                    char_code += 26

            encrypted += chr(char_code)
        else:
            encrypted += char
    
    return encrypted

robot_name = "Spcpu"

print(robot_name + ": " + "Hi! My name is " + robot_name + ". I can encrypt messages using a Caesar cipher for you.")

while True:
    decrypted_message = input("Enter your message ('q' to quit): ")
    
    if decrypted_message == 'q':
        print(robot_name + ": " + "Thank you for using my program!")
        break

    encrypted_message = caesar_encrypt(decrypted_message)
    print(robot_name + ": " + "Here's your encrypted message: ", encrypted_message)

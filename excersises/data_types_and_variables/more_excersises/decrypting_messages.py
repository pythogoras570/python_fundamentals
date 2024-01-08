key = int(input())
number_of_lines = int(input())

message = ''

for crypted_message in range(number_of_lines):
    crypt = input()
    decrypt = ord(crypt) + key
    message += chr(decrypt)

print(message)

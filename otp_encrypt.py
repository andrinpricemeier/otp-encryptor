print(b"01100110".decode("ascii"))

print("Welcome to OTP encryptor")
message_to_encrypt = input("Enter your sensitive message: ")
key = input("Now enter your secret as a string of 0 and 1: ")
message_binary = ''.join(format(ord(i), '08b') for i in message_to_encrypt)
print("Length message in bits: ")
print(len(message_binary))
print("Length key: ")
print(len(key))
if len(message_binary) != len(key):
    print("Message is not the same length as key, pad it.")
    exit(1)
encrypted = ''.join([str((ord(a) ^ ord(b))) for a, b in zip(message_binary, key)])
print("Here is your encrypted message:")
print(encrypted)
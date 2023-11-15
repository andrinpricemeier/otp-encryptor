print("Welcome to OTP encryptor")
encrypted = input("Enter your encrypted string of 0 and 1: ")
key = input("Now enter your secret as a string of 0 and 1: ")
decrypted = ''.join([str((ord(a) ^ ord(b))) for a, b in zip(encrypted, key)])
print("Here is your decrypted message")
n = 8
chunks = [decrypted[i:i+n] for i in range(0, len(decrypted), n)]
result = []
for chunk in chunks:
    print(chunk)
    result.append(chr(int(chunk, 2)))
print(''.join(result))

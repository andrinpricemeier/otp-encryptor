# OTP encryptor

One Time Pad encryption for sensitive messages

## Exchange OTPs

1. Exchange OTPs in a secure manner
2. Run script to encrypt on side A
3. Send over email
4. Run script to decrypt on side B

* Use a quantum random number generator
* One OTP per day, do not reuse
* Handwritten notes in person only

Downsides: Have to trust OS and Python interpreter.

For the truly paranoid, calculate XOR manually:

1. Convert message into binary
2. Compare message and key bits
3. If 1 and 0 or 0 and 1, then output is 1, otherwise 0

## Encryption

1. python otp_encrypt.py
2. Enter your message in ASCII
3. Enter your key in 0 and 1
4. They both have to match, ASCII is 8 bits per char, just pad it with some random char to match key length

## Decryption

1. python otp_decrypt.py
2. Enter your encrypted message in 0 and 1
3. Enter your key in 0 and 1
4. Output is decrypted message

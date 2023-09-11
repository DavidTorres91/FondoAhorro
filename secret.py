import os
import binascii

secret_key = binascii.hexlify(os.urandom(24)).decode('utf-8')
print(secret_key)

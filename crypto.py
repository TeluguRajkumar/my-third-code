#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 19:18:44 2020

@author: rajkumar
"""


#############ENCRYPTED CODE########

pip install cryptography
from cryptography.fernet import Fernet
gen_key = Fernet.generate_key()
fer=Fernet(gen_key)
message= "my deep dark secret"
encrypted=fer.encrypt(message.encode())
print(encrypted)



###########DECRYPTED CODE########

from cryptography.fernet import Fernet
gen_key=Fernet.generate_key()
fer= Fernet(gen_key)
message="encrypted text"
decrypted=fer.decrypt("my deep dark secret")
print(decyrpted)


 from cryptography.fernet import Fernet
 key = Fernet.generate_key()
 f = Fernet(key)
 token = f.encrypt(b"my deep dark secret")
 token
 f.decrypt(token)

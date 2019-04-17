#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 11:47:13 2018

@author: Yeahia Sarker

"""

import os
import pyaes
import hashlib, binascii
import shutil
import sys
import zipfile

class aescrypt:
    def __init__(self):
        """To initilize something """
        print("##### WELCOME #####")
        password = input("Enter The Password : ")
        dk = hashlib.pbkdf2_hmac('sha512', password.encode(), b'md5', 1000, dklen = 256)
        self.key = binascii.hexlify(dk)
        self.key = self.key[:32]
        self.mode = pyaes.AESModeOfOperationCTR(self.key)

    def create_file(self):
        """ It will create a file if the file doesn't exists"""
        if sys.argv[1].endswith(".encrypted"):
            self.decrypt()
        else:
            self.encrypt()

    def encrypt(self):
        shutil.make_archive(((str(sys.argv[1]))),"zip",".",str(sys.argv[1]))
        input_file_name = (str(sys.argv[1]) + ".zip")
        with open(input_file_name, encoding = "utf-8", errors = "ignore") as input_file:
            with open((input_file_name + ".encrypted"), 'wb+') as output_file:
                pyaes.encrypt_stream(self.mode, input_file, output_file)

    def decrypt(self):
        output_file_name = str(sys.argv[1].split(".")[0])
        try:
            with open(str(sys.argv[1])) as input_file:
                with open((str(output_file_name)), 'wb+') as output_file:
                    pyaes.decrypt_stream(self.mode, input_file, output_file)
        except FileNotFoundError as e:
            print(e)
nabcrypt = aescrypt()
nabcrypt.create_file()
## Ended Up with a encoding error
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 11:47:13 2018

@author: Yeahia Sarker

"""
import sys
import os
import pyaes
#import subprocess
import hashlib, binascii
class nabcrypt:
    def __init__(self):
        """To initilize something """
        password = ("Enter Password : ")
        dk = hashlib.pbkdf2_hmac('sha512', password.encode(), b'md5', 100000, dklen = 256)
        self.key = binascii.hexlify(dk)
        self.key = self.key[:32]
        self.mode = pyaes.AESModeOfOperationCTR(self.key)
        print("WELCOME")
    def create_file(self):
        """ It will create a file if the file doesn't exists"""
        if sys.argv[1].endswith(".nab"):
            self.decrypt()
        else:
            self.encrypt()
    def encrypt(self):
        with open(str(sys.argv[1])) as input_file:
            with open(str(sys.argv[1]) + "nab") as output_file:
                pyaes.encrypt_stream(self.mode, input_file, output_file)
    def decrypt(self):
        output_file_name = str(sys.argv[1].split(".")[0])
        with open(str(sys.argv[1])) as input_file:
            with open(str(output_file_name)) as output_file:
                pyaes.decrypt_stream(self.mode, input_file, output_file)
nabcrypt = nabcrypt()
nabcrypt.create_file()

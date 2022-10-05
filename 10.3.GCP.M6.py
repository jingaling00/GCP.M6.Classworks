# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:13:43 2022

@author: jingy
"""

cipher_1 = {'A': 'Z', 'B': 'A', 'C': 'V',  
              'D': 'K',  'E': 'F',  'F': 'D',  
              'G': 'X',  'H': 'C',  'I': 'G',  
              'J': 'E',  'K': 'W',  'L': 'L',  
              'M': 'I',  'N': 'P', 'O': 'Y',  
              'P': 'H', 'Q': 'R', 'R': 'B',  
              'S': 'N',  'T': 'S',  'U': 'J',
              'V': 'M',  'W': 'O',  'X': 'Q',  
              'Y': 'U',  'Z': 'T',' ':' '}

def encrypt(message,cipher):
    message = message.upper()
    encrypted = []
    for letter in message:
        letter = cipher[letter]
        encrypted.append(letter)
    encrypted = ''.join(encrypted)
    return encrypted

def decrypt(message,cipher): # this is the dumb way. flip the dictionary.
    decrypted = []
    for letter in message:
        for i in cipher_1.keys():
            if cipher[i]==letter:
                decrypted.append(i)
    decrypted = ''.join(decrypted)
    decrypted = decrypted.lower()
    return decrypted

if __name__ == '__main__':
    print(decrypt('XZSFOZU VYIHJSGPX HUSCYP GN BFZLLU DJP!',cipher_1))
        
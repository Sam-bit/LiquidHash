'''
Author  : Sambit Samal
This program is used to create a hash string by using multiple hash function.

You can change the order of the hash function used OR can omit some of the hash function OR you can add some more OR repeat the used hash function of your choice as per your requirement.

You Can also add SALT words to strengthen your Source String
It is just for a sample

USES
* Creates an UNBREAKABLE AND UNCRACKABLE, STILL UNIQUE hash string of variable digest size and length based on the outermost hash algorithm used (In our case the message length, the digest size and block size is equal to that of sha512). Thus it becomes unpredictable for the crackers if SENSITIVE PASSWORDS are stored using MY FullStopHash

PUBLIC FUNCTION USED :
1) hexdigest - Creates an hexadecimal representation of the liquidhash (WITHOUT SALT STRING)
2) digest - Creates an digested version of the liquidhash (WITHOUT SALT STRING)
3) hexdigest_encoded - Encoded Hexadecimal representation of the liquidhash (WITHOUT SALT STRING)
4) digest_encoded - Encoded digested version of the liquidhash (WITHOUT SALT STRING)
5) hexdigest_crypted - Creates an hexadecimal representation of the liquidhash (WITH SALT STRING)
6) digest_crypted - Creates an digested version of the liquidhash (WITH SALT STRING)
7) hexdigest_encrypted - Base64 encoded Hexadecimal representation of the liquidhash (WITH SALT STRING)
8) digest_encrypted - Base64 encoded digested version of the liquidhash (WITH SALT STRING)

'''

import hashlib
import base64
from base91 import base91
class liquidhash:
    @staticmethod
    def mainhexcrypter(SrcString,salt = ""):
       DestHash = bytes(str(SrcString), encoding="ascii")
       DestHash = bytes(hashlib.md5(DestHash).hexdigest(), encoding="ascii")
       DestHash = bytes(hashlib.sha1(DestHash).hexdigest(), encoding="ascii")
       DestHash = bytes(hashlib.sha224(DestHash).hexdigest(), encoding="ascii")
       DestHash = bytes(hashlib.sha384(DestHash).hexdigest(), encoding="ascii")
       DestHash = bytes(hashlib.sha256(DestHash).hexdigest(), encoding="ascii")
       DestHash = bytes(hashlib.sha512(DestHash).hexdigest(), encoding="ascii")
       return str(DestHash)
    @staticmethod
    def maincrypter(SrcString,salt = ""):
       DestHash = bytes(str(SrcString + salt), encoding="ascii")
       DestHash = hashlib.md5(DestHash).digest()
       DestHash = hashlib.sha1(DestHash).digest()
       DestHash = hashlib.sha224(DestHash).digest()
       DestHash = hashlib.sha384(DestHash).digest()
       DestHash = hashlib.sha256(DestHash).digest()
       DestHash = hashlib.sha512(DestHash).digest()
       return str(DestHash)
    @staticmethod
    def maincoder(SrcString):
       DestCode = SrcString.encode('ascii')
       DestCode = base91.b91encode(DestCode).encode('ascii')
       DestCode = base64.b64encode(DestCode)
       return str(DestCode)
#BEGINS NORMAL ENCRYPTION
    @staticmethod
    def hexdigest(SrcString):
       DestHash = liquidhash.mainhexcrypter(SrcString)
       return str(DestHash)

    @staticmethod
    def digest(SrcString):
       DestHash = liquidhash.maincrypter(SrcString)
       return str(DestHash)
#ENDS NORMAL ENCRYPTION
#BEGINS NORMAL ENCODER (ENCRYPTION + ENCODER WITHOUT SALT)
    @staticmethod
    def digest_encoded(SrcString):
       DestHash = liquidhash.maincrypter(SrcString)
       DestHash = liquidhash.maincoder(DestHash)
       return str(DestHash)
    
    @staticmethod
    def hexdigest_encoded(SrcString):
       DestHash = liquidhash.maincrypter(SrcString)
       DestHash = liquidhash.maincoder(DestHash)
       return str(DestHash)
#ENDS NORMAL ENCODER (ENCRYPTION + ENCODER WITHOUT SALT)
#BEGINS SALTED ENCRYPTION
    @staticmethod
    def digest_crypted(SrcString):
       salt = liquidhash.digest(SrcString)
       DestHash = liquidhash.digest(SrcString + salt)
       return str(DestHash)
    
    @staticmethod
    def hexdigest_crypted(SrcString):
       salt = liquidhash.hexdigest(SrcString)
       DestHash = liquidhash.hexdigest(SrcString + salt)
       return str(DestHash)
#ENDS SALTED ENCYPTION
#BEGINS ENCODED + ENCRYPTED + SALTED
    @staticmethod
    def digest_encrypted(SrcString):
       salt = liquidhash.digest(SrcString)
       salt = liquidhash.maincoder(salt)
       DestHash = liquidhash.digest(SrcString + salt)
       DestHash = liquidhash.maincoder(DestHash)
       return str(DestHash)
       
    @staticmethod
    def hexdigest_encrypted(SrcString):
       salt = liquidhash.hexdigest(SrcString)
       salt = liquidhash.maincoder(salt)
       DestHash = liquidhash.maincrypter(SrcString + salt)
       DestHash = liquidhash.maincoder(DestHash)
       return str(DestHash)
#ENDS ENCODED + ENCRYPTED + SALTED

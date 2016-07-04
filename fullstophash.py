'''
Author  : Sambit Samal
This program is used to create a hash string by using multiple hash function.

You can change the order of the hash function used OR can omit some of the hash function OR you can add some more OR repeat the used hash function of your choice as per your requirement.

You Can also add SALT words to strengthen your Source String
It is just for a sample

USES
* Creates an UNBREAKABLE AND UNCRACKABLE, STILL UNIQUE hash string of variable digest size and length based on the outermost hash algorithm used (In our case the message length, the digest size and block size is equal to that of sha512). Thus it becomes unpredictable for the crackers if SENSITIVE PASSWORDS are stored using MY FullStopHash

PUBLIC FUNCTION USED :
1) hexdigest - Creates an hexadecimal representation of the fullstophash (WITHOUT SALT STRING)
2) digest - Creates an digested version of the fullstophash (WITHOUT SALT STRING)
3) hexdigest_encoded - Encoded Hexadecimal representation of the fullstophash (WITHOUT SALT STRING)
4) digest_encoded - Encoded digested version of the fullstophash (WITHOUT SALT STRING)
5) hexdigest_crypted - Creates an hexadecimal representation of the fullstophash (WITH SALT STRING)
6) digest_crypted - Creates an digested version of the fullstophash (WITH SALT STRING)
7) hexdigest_encrypted - Base64 encoded Hexadecimal representation of the fullstophash (WITH SALT STRING)
8) digest_encrypted - Base64 encoded digested version of the fullstophash (WITH SALT STRING)

'''

import hashlib
import base64
import base91
class fullstophash:
	@staticmethod
	def mainhexcrypter(SrcString):
		DestHash = str(SrcString)
		DestHash = hashlib.md5(DestHash).hexdigest()
		DestHash = hashlib.sha1(DestHash).hexdigest()
		DestHash = hashlib.sha224(DestHash).hexdigest()
		DestHash = hashlib.sha384(DestHash).hexdigest()
		DestHash = hashlib.sha256(DestHash).hexdigest()
		DestHash = hashlib.sha512(DestHash).hexdigest()
		return str(DestHash)
	@staticmethod
	def maincrypter(SrcString):
		DestHash = str(SrcString)
		DestHash = hashlib.md5(DestHash + salt).digest()
		DestHash = hashlib.sha1(DestHash + salt).digest()
		DestHash = hashlib.sha224(DestHash + salt).digest()
		DestHash = hashlib.sha384(DestHash + salt).digest()
		DestHash = hashlib.sha256(DestHash + salt).digest()
		DestHash = hashlib.sha512(DestHash + salt).digest()
		return str(DestHash)
	@staticmethod
	def maincoder(SrcString):
		DestCode = str(SrcString)
		DestCode = base91.b91encode(DestCode)
		DestCode = base64.b64encode(DestCode)
		return str(DestCode)
#BEGINS NORMAL ENCRYPTION
	@staticmethod
	def hexdigest(SrcString):
		DestHash = fullstophash.mainhexcrypter(SrcString)
		return str(DestHash)

	@staticmethod
	def digest(SrcString):
		DestHash = fullstophash.maincrypter(SrcString)
		return str(DestHash)
#ENDS NORMAL ENCRYPTION
#BEGINS NORMAL ENCODER (ENCRYPTION + ENCODER WITHOUT SALT)
	@staticmethod
	def digest_encoded(SrcString):
		DestHash = fullstophash.maincrypter(SrcString)
		DestHash = fullstophash.maincoder(DestHash)
		return str(DestHash)
	
	@staticmethod
	def hexdigest_encoded(SrcString):
		DestHash = fullstophash.maincrypter(SrcString)
		DestHash = fullstophash.maincoder(DestHash)
		return str(DestHash)
#ENDS NORMAL ENCODER (ENCRYPTION + ENCODER WITHOUT SALT)
#BEGINS SALTED ENCRYPTION
	@staticmethod
	def digest_crypted(SrcString):
		salt = fullstophash.maindigest(SrcString)
		DestHash = fullstophash.maindigest(SrcString + salt)
		return str(DestHash)
	
	@staticmethod
	def hexdigest_crypted(SrcString):
		salt = fullstophash.mainhexdigest(SrcString)
		DestHash = fullstophash.mainhexdigest(SrcString + salt)
		return str(DestHash)
#ENDS SALTED ENCYPTION
#BEGINS ENCODED + ENCRYPTED + SALTED
	@staticmethod
	def digest_encrypted(SrcString):
		salt = fullstophash.maindigest(SrcString)
		salt = fullstophash.maincoder(salt)
		DestHash = fullstophash.maindigest(SrcString + salt)
		DestHash = fullstophash.maincoder(DestHash)
		return str(DestHash)
		
	@staticmethod
	def hexdigest_encrypted(SrcString):
		salt = fullstophash.mainhexdigest(SrcString)
		salt = fullstophash.maincoder(salt)
		DestHash = fullstophash.maincrypter(SrcString + salt)
		DestHash = fullstophash.maincoder(DestHash)
		return str(DestHash)
#ENDS ENCODED + ENCRYPTED + SALTED

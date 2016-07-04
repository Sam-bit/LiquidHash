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
3) hexdigest_encoded - Base64 encoded Hexadecimal representation of the fullstophash (WITHOUT SALT STRING)
4) digest_encoded - Base64 encoded digested version of the fullstophash (WITHOUT SALT STRING)
5) hexdigest_crypted - Creates an hexadecimal representation of the fullstophash (WITH SALT STRING)
6) digest_crypted - Creates an digested version of the fullstophash (WITH SALT STRING)
7) b64hexdigest_encrypted - Base64 encoded Hexadecimal representation of the fullstophash (WITH SALT STRING)
8) b64digest_encrypted - Base64 encoded digested version of the fullstophash (WITH SALT STRING)

'''

import hashlib
import base64
class fullstophash:
	@staticmethod
	def mainhexdigest(SrcString):
		DestHash = str(SrcString)
		DestHash = hashlib.md5(DestHash).hexdigest()
		DestHash = hashlib.sha1(DestHash).hexdigest()
		DestHash = hashlib.sha224(DestHash).hexdigest()
		DestHash = hashlib.sha384(DestHash).hexdigest()
		DestHash = hashlib.sha256(DestHash).hexdigest()
		DestHash = hashlib.sha512(DestHash).hexdigest()
		return str(DestHash)
	@staticmethod
	def maindigest(SrcString):
		DestHash = str(SrcString)
		DestHash = hashlib.md5(DestHash + salt).digest()
		DestHash = hashlib.sha1(DestHash + salt).digest()
		DestHash = hashlib.sha224(DestHash + salt).digest()
		DestHash = hashlib.sha384(DestHash + salt).digest()
		DestHash = hashlib.sha256(DestHash + salt).digest()
		DestHash = hashlib.sha512(DestHash + salt).digest()
		return str(DestHash)
		
	@staticmethod
	def hexdigest_encrypt(SrcString):
		salt = fullstophash.mainhexdigest(SrcString)
		DestHash = fullstophash.mainhexdigest(SrcString + salt)
		return str(DestHash)
	
	@staticmethod
	def digest_encrypt(SrcString):
		salt = fullstophash.maindigest(SrcString)
		DestHash = fullstophash.maindigest(SrcString + salt)
		return str(DestHash)
		
	@staticmethod
	def b64digest_encrypt(SrcString):
		salt = fullstophash.maindigest(SrcString)
		salt = base64.b64encode(salt)
		DestHash = fullstophash.maindigest(SrcString + salt)
		DestHash = base64.b64encode(DestHash)
		return str(DestHash)
		
	@staticmethod
	def b64hexdigest_encrypt(SrcString):
		salt = fullstophash.mainhexdigest(SrcString)
		salt = base64.b64encode(salt)
		DestHash = fullstophash.mainhexdigest(SrcString + salt)
		DestHash = base64.b64encode(DestHash)
		return str(DestHash)

	@staticmethod
	def hexdigest(SrcString):
		DestHash = fullstophash.mainhexdigest(SrcString)
		return str(DestHash)

	@staticmethod
	def digest(SrcString):
		DestHash = fullstophash.maindigest(SrcString)
		return str(DestHash)

	@staticmethod
	def b64digest(SrcString):
		DestHash = fullstophash.maindigest(SrcString)
		DestHash = base64.b64encode(DestHash)
		return str(DestHash)

	@staticmethod
	def b64hexdigest(SrcString):
		DestHash = fullstophash.mainhexdigest(SrcString)
		DestHash = base64.b64encode(DestHash)
		return str(DestHash)
 

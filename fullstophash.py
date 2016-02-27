'''
Author  : Sambit Samal
This program is used to create a hash string by using multiple hash function.

You can change the order of the hash function used OR can omit some of the hash function OR you can add some more OR repeat the used hash function of your choice as per your requirement.

You Can also add SALT words to strengthen your Source String
It is just for a sample

USES
* Creates an UNBREAKABLE AND UNCRACKABLE, STILL UNIQUE hash string of variable digest size and length based on the outermost hash algorithm used (In our case the message length, the digest size and block size is equal to that of sha512). Thus it becomes unpredictable for the crackers if SENSITIVE PASSWORDS are stored using MY FullStopHash

'''

import hashlib
import base64
class fullstophash:
	@staticmethod
	def hexdigest(SrcString):
		return hashlib.sha512(hashlib.sha256(hashlib.sha384(hashlib.sha224(hashlib.sha1(hashlib.md5(SrcString).hexdigest()).hexdigest()).hexdigest()).hexdigest()).hexdigest()).hexdigest()
	@staticmethod
	def digest(SrcString):
		return hashlib.sha512(hashlib.sha256(hashlib.sha384(hashlib.sha224(hashlib.sha1(hashlib.md5(SrcString).digest()).digest()).digest()).digest()).digest()).digest()
	@staticmethod
	def b64digest(SrcString):
		return base64.b64encode(hashlib.sha512(hashlib.sha256(hashlib.sha384(hashlib.sha224(hashlib.sha1(hashlib.md5(SrcString).digest()).digest()).digest()).digest()).digest()).digest())
	@staticmethod
	def b64hexdigest(SrcString):
		return base64.b64encode(hashlib.sha512(hashlib.sha256(hashlib.sha384(hashlib.sha224(hashlib.sha1(hashlib.md5(SrcString).hexdigest()).hexdigest()).hexdigest()).hexdigest()).hexdigest()).hexdigest())

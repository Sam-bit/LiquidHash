# LiquidHash
* Create a single hash string by using multiple hash function.
This program is used to create a hash string by using multiple hash function.

You can change the order of the hash function used OR can omit some of the hash function OR you can add some more OR repeat the used hash function of your choice as per your requirement.

You Can also add SALT words to strengthen your Source String
It is just for a sample

## USES

* Creates an UNBREAKABLE AND UNCRACKABLE, STILL UNIQUE hash string of variable digest size and length based on the outermost hash algorithm used (In our case the message length, the digest size and block size is equal to that of sha512). Thus it becomes unpredictable for the crackers if SENSITIVE PASSWORDS are stored using MY FullStopHash

* You can change the order of the hash function used OR can omit some of the hash function OR you can add some more OR repeat the used hash function of your choice as per your requirement.


## PUBLIC FUNCTION USED :
1) hexdigest - Creates an hexadecimal representation of the fullstophash (WITHOUT SALT STRING)  
2) digest - Creates an digested version of the fullstophash (WITHOUT SALT STRING)  
3) hexdigest_encoded - Base64 encoded Hexadecimal representation of the fullstophash (WITHOUT SALT STRING)  
4) digest_encoded - Base64 encoded digested version of the fullstophash (WITHOUT SALT STRING)  
5) hexdigest_crypted - Creates an hexadecimal representation of the fullstophash (WITH SALT STRING)  
6) digest_crypted - Creates an digested version of the fullstophash (WITH SALT STRING)  
7) hexdigest_encrypted - Base64 encoded Hexadecimal representation of the fullstophash (WITH SALT STRING)  
8) digest_encrypted - Base64 encoded digested version of the fullstophash (WITH SALT STRING)  

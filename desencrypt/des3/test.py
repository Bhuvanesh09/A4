from Crypto.Cipher import DES

key1 = b'helloWorld'
key2 = b'Helloworld'

crypter1 = DES.new(key , DES.MODE_OFB)
crypter2 = DES.new(key2, DES.MODE_OFB)

text = b'I will encrypt t'

msg = crypter1.encrypt(key1,)
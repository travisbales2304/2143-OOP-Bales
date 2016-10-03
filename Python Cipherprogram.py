"""
Travis Bales
Program 01 EasyCipher
10/03/2016
Object Oriented Programming
MT 1:00pm - 2:20pm
"""



"""
@ Name: ShiftCipher
@ Description: Simple class to do a shift cipher
"""
class ShiftCipher(object):
	
	"""
	@ Name: __init__
	@ Description: 
	@ Params:
	     None
	"""
	def __init__(self):
		
		self.plainText = None
		self.cipherText = None
		self.cleanText = None
		self.decText = None
		self.shift = 3
		
	def __str__(self):
		return "plainText: %s\ncipherText: %s\ncleanText: %s\nshift: %d\n" % (self.plainText,self.cipherText,self.cleanText,self.shift)
	
	"""
	@ Name: promptUserMessage
	@ Description: Prompts user for message from standard in
	@ Params:
	     None
	"""
	def promptUserMessage(self):
		temp = input("Message: ")
		self.setMessage(temp)

	"""
	@ Name: setMessage
	@ Description: sets plaintext and then cleans and calls encrypt.
	@ Params:
	     message {string}: String message
	     encrypted {bool}: False = plaintext True=ciphertext
	"""
	def setMessage(self,message,encrypted=False):
		if(not encrypted):
			self.plainText = message
			self.cleanData()
			self.__encrypt()
		#	self.__decrypt() #ADDED THIS
		else:
			self.cipherText = message
			self.__decrypt()
	
	def getCipherText(self):
		return self.cipherText
		
	def getPlainText(self):
		return self.plainText

	def setShift(self,shift):
		self.shift = shift
	
	def getShift(self):
		return self.shift
		
		"""
	@ Name: cleanDate
	@ Description: sets plaintext and then cleans and calls encrypt.
		Removes any characters that are not alphanumeric
	"""
		
	def cleanData(self):
		self.cleanText = ''
		for letter in self.plainText:
			if ord(letter) < 48:
				continue
			elif ord(letter) > 57 and ord(letter) < 65:
				continue
			elif ord(letter) > 90 and ord(letter) < 97:
				continue
			if ord(letter) > 96:
				self.cleanText += chr(ord(letter)-32)
			else:
				self.cleanText += letter
			
		
	"""
	Encrypts plaintext not ciphertext
	"""
	def __encrypt(self):
		self.cipherText = ''
		if(not self.cleanText):
			return
		for letter in self.cleanText:
			if ord(letter) > 57:
				self.cipherText += chr((((ord(letter)-65) + self.shift) % 26)+65)
			else:
				self.cipherText += letter
		    
		
	
	"""
	Decrypts ciphertext not plaintext
	Does not add spaces between words for the plain text
	"""
	def __decrypt(self):
		self.decText = ''
		if (not self.cipherText):
			return
		for letter in self.cipherText:
			if ord(letter) > 57:
				self.decText += chr((((ord(letter)-65) - self.shift) % 26)+65)
			else:
				self.decText += letter
		self.cleanText = self.decText



#person = input('Enter your name: ')
alice = ShiftCipher()
alice.setMessage('Hello World')
print(alice)
alice.setMessage('@th   e g#oo---d th(e b&ad an )d th_)e ug&%$ly((')
print(alice)
alice.setMessage('       good morn*ing,viet()nam ---1+-9*6 9')
print(alice)

bob = ShiftCipher()
bob.setMessage(alice.getCipherText(),True)
print(bob)

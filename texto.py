from screenEntity import *

class Text( ScreenEntity ):
	textString = ""
	fontArray = []
	caracterSpace = 1

	def setFontArray( self, fA ):
		self.fontArray = fA	
	
	def setText( self, text ):
		self.textString = text
		self.initBitmap()		
		i = 0
		for letra in self.textString:
			self.addCaracterToBitMap( self.fontArray[ letra ], i )
			i += 1
			
	def initBitmap( self ):
		self.bitMap = []		
		#Se define la altura en base a la altura de la letra
		for y in range(0, len(self.fontArray[" "])):
			self.bitMap.append([])
			#Se define el largo en funciòn a la cantidad de letras
			for x in range(0, (len(self.fontArray[" "][1])+self.caracterSpace) * len(self.textString) ):
				self.bitMap[y].append(0)		
				
	def addCaracterToBitMap( self, caracter, i ):
		for y in range(0, len( caracter) ):
			for x in range(0, len(caracter[y])):
				self.bitMap[y][x+i*len(caracter[0])] = caracter[y][x]

class ScreenEntity:
	px = 0
	py = 0
	color = 0
	pixelScreen = None
	bitMap = []
	scale = 1
	
	def setPx( self, x ):
		self.px = x
		
	def setPy( self, y ):
		self.py = y
		
	def getPx( self ):
		return self.px
		
	def getPy( self ):
		return self.py
		
	def setColor( self, color ):
		self.color = color
		
	def setBitmap( self, bitMap ):
		self.bitMap = bitMap
		
	def setPixelScreen( self, pS ):
		self.pixelScreen = pS
	
	def frameUpdate( self ):
		if (self.pixelScreen != None):		
			self.pixelScreen.setScreenMap( self.bitMap, self.px, self.py, self.color )
		else:
			print('Atención: No se definío objeto pixelScreen')
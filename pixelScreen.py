import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy

paleta = [ [0,0,0], [255,0,0], [0,255,0], [0,0,255], [255,255,0], [0,255,255], [255,255,255] ]

class PixelScreen:
	screenPixels = []
	brightness   = 0.25
	pixels       = []
	num_leds     = 144
	fps          = 30
	screenWidth  = 12
	screenHeight = 12
	
	def init( self ):
		self.pixels = neopixel.NeoPixel(board.D18, self.num_leds, brightness=self.brightness, auto_write=False)
		for i in range( 0, self.screenWidth ):
			self.screenPixels.append([])
			for j in range( 0, self.screenHeight):
				self.screenPixels[i].append([ 0,0,0 ])
	
	def setScreen( self, color ):
		for i in range(0, self.screenWidth ):
			for j in range(0, self.screenHeight):
				self.screenPixels[ i ][ j ] = color
			
	def setScreenMap( self, mapM, x, y, color ):
		for i in range(0, len( mapM) ):
			for j in range(0, len(mapM[i])):
				if (mapM[i][j] == 1):
					self.setPixel( i, j, paleta[ color ] )
	
	def setPixel( self, x, y, color ):
		if (x < self.screenWidth and x >= 0 and y >= 0 and y < self.screenHeight):
			self.screenPixels[ x ][ y ] = color
	
	def drawFrame( self ):
		k = self.num_leds - 1
		
		for fila in range(0, self.screenWidth ):
			#Para ahorrar cable, la cinta se invierte en filas pares
			if ( fila %2 == 0 ):
				for j in range(self.screenHeight-1, -1, -1):
					self.pixels[ k ] = self.screenPixels[ fila ][ j ]
					k-=1
			else:
				for j in range(0, self.screenHeight):
					self.pixels[ k ] = self.screenPixels[ fila ][ j ]
					k-=1
									
		self.pixels.show()
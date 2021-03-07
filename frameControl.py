import time
from pixelScreen import *

class FrameControl:
	fps = 30
	pixelScreen = None
	frameLoopCallback = None
	screenEntitys = []
	
	def setFrameLoopCallback( self, cbk ):
		self.frameLoopCallback = cbk

	def addScreenEntity( self, sE ):
		sE.setPixelScreen( self.pixelScreen )
		self.screenEntitys.append( sE )
		return len( self.screenEntitys )
		
	def getEntity( self, id ):
		return self.screenEntitys[ id - 1 ]
	
	def init( self ):
		self.pixelScreen.init()
		self.frameLoop()
		
	def frameLoop( self ):
		while True:
			#Se borra la pantalla previo a posicionar las entidades
			self.pixelScreen.setScreen( 0 )		
		
			#Se ejecuta el callback cada vez que se inicia el frame
			if (self.frameLoopCallback != None):
				self.frameLoopCallback( self )
			
			#Se actualiza la posiciòn de todas las entidades en pantalla
			for entity in self.screenEntitys:
				entity.frameUpdate()			
			
			#Se actualizan el estado de los LEDs
			self.pixelScreen.drawFrame()
			
			#Se aplica el delay necesario entre frame y frame
			time.sleep( 1/self.fps )
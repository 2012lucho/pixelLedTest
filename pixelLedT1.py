import random
from texto import *
from frameControl import *
from screenEntity import *
from pixelScreen import *
from colors import *

frameControl = FrameControl()
frameControl.fps = 10
frameControl.pixelScreen = PixelScreen()

point = ScreenEntity()
point.setColor( 1 )
point.setBitmap(letras["A"])
point.setPx(0)
point.setPy(0)

pointId = frameControl.addScreenEntity( point )

text = Text()
text.setFontArray( letras )
text.setColor( 2 )
text.setText( "HOLA MUNDO" )

textId = frameControl.addScreenEntity( text )

def newFrame( frameControl ):
	entity = frameControl.getEntity( textId )
	entity.setPx( entity.getPx()-1 )

frameControl.setFrameLoopCallback( newFrame )
frameControl.init()



import random
from texto import *
from frameControl import *
from screenEntity import *
from pixelScreen import *
from colors import *
from letras12x12 import *
from letras6x6 import *

frameControl = FrameControl()
frameControl.fps = 10
frameControl.pixelScreen = PixelScreen()

text = Text()
text.setFontArray( digitos_calc_12x12 )
text.setColor( 2 )
text.setText( "0123456789" )

textId = frameControl.addScreenEntity( text )

def newFrame( frameControl ):
	entity = frameControl.getEntity( textId )
	entity.setPx( entity.getPx()-1 )

frameControl.setFrameLoopCallback( newFrame )
frameControl.init()



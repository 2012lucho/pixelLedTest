import random
from texto import *
from frameControl import *
from screenEntity import *
from pixelScreen import *
from colors import *

frameControl = FrameControl()
frameControl.pixelScreen = PixelScreen()

point = ScreenEntity()
point.setColor( 1 )
point.setBitmap([[1,1]])
point.setPx(0)
point.setPy(0)

pointId = frameControl.addScreenEntity( point )

def newFrame( frameControl ):
	entity = frameControl.getEntity( pointId )
	entity.setPx( entity.getPx()+1 )

frameControl.setFrameLoopCallback( newFrame )
frameControl.init()



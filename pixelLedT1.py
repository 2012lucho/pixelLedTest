import random
import time
from texto import *
from pixelScreen import *

sc = PixelScreen()
sc.init()
sc.setScreen( paleta[0] )
sc.setScreenMap( letras["Z"], 0, 0, 2 )

x=0
y=0
while True:
	sc.drawFrame()
	time.sleep( 1/5 )
from mcpi.minecraft import Minecraft
DD=Minecraft.create()
import random 

x,y,z=DD.player.getPos()

for i in range(20):
    r=random.randrange(1,7)
    if r==1:
        DD.setBlocks(x,y,z,x,y,z+4,46)
        z=z+4
    elif r==2:
        DD.setBlocks(x,y,z,x,y,z-4,1)
        z=z-4
    elif r==3:
        DD.setBlocks(x,y,z,x+4,y,z,2)
        x=x+4
    elif r==4:
        DD.setBlocks(x,y,z,x-4,y,z,7)
        x=x-4
    elif r==5:
        DD.setBlocks(x,y,z,x,y+4,z,7)
        y=y+4
    elif r==6:
        DD.setBlocks(x,y,z,x,y-4,z,7)
        y=y-4
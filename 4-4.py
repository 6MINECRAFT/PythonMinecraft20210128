from mcpi.minecraft import Minecraft
DD=Minecraft.create()

list2=[[7,46,1],[2,86,133]]

myID=DD.getPlayerEntityId("HappierBroom427")
x,y,z=DD.entity.getTilePos(myID)

startx=x

for i in list2:
    for j in i:
        
        DD.setBlock(x,y,z,j)
        x=x+1
    x=startx
    z=z-1





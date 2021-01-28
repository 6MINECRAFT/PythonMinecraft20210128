from mcpi.minecraft import Minecraft
DD=Minecraft.create()
from random import randrange


for i in range(15):
    x,y,z=DD.player.getTilePos()
    z=z+i
    for f in range(15):
        color=randrange(0,16)
        x=x+1
        DD.setBlock(x,y,z,35,color)
        
ans = randrange(0,16)
while True:
    hits=DD.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        block=DD.getBlockWithData(h.pos)
        data = block.data
        
        if data==ans:
            DD.setBlock(h.pos,133)
            DD.postToChat("恭喜")
            break
        if data>ans:
            DD.postToChat("找小點的")
        if data<ans:
            DD.postToChat("找大點的")




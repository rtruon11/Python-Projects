import random

tails = 0
heads = 0
nflips = 10

for k in range (nflips):
    dice = random.randint(0,1)
    
    if dice == 0:
        tails = tails + 1
        
    else:
        heads = heads + 1
        
print ('Number of tails = ', tails)
print ('Number of heads = ', heads)
print ('# of heads = ', 100*(heads/nflips))

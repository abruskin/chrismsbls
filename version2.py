#knitting pattern
#modified version of Balls Up by General Hogbuffer

yarnweight = 'unknown'
needles = 'US5'
filename = f'BallsUpyarnweight{yarnweight}needles{needles}.txt'
#f = open(filename, "x")
#f.close()
roundx = 1
stitches = 16
n = 1

# ball measurements are in inches
balldiameter = 2.8
ballcircumference = 8.79
desiredlength = (ballcircumference/2)-.5
rows_per_inch = 14/1.75
stitches_per_inch = 16/2.5

#print(10/1.5)
f = open(filename, "w")
f.write('PART 1: \n'
f'CO 8 stitches and join in round \n'
f'Round 1: kfb into each stitch \n'
f'Round 2 (and all even rounds: k all stitches)\n' )
f.close()
width = 0
length = 0


def increaseround():
    increase = 8
    global roundx
    roundx += 2
    global n
    n += 1
    m = n - 1
    global stitches
    stitches += increase
    global width
    global length
    width = stitches / stitches_per_inch
    length = roundx / rows_per_inch

    f = open(filename, "a")
    f.write(f'round {roundx}: k1 *m1 k{n}, repeat from * to last stitch, m1 k{m} ({stitches} stitches) \n')
    f.close()
   # print(f'round {roundx}: k1 *m1 k{n}, repeat from * to last stitch, m1 k{m} ({stitches} stitches) ')
    #print(f' width:{width} length: {length}')


widthincreaseininches = 8 / stitches_per_inch
while width + widthincreaseininches < ballcircumference:
    increaseround()

print(length)
middlelength = desiredlength - (length * 2)
print(middlelength)
middlerows = round(middlelength * stitches_per_inch + 1)
print(f' middlerows: {middlerows}')
f = open(filename, "a")
f.write('\nPART 2\n')
f.write(f'knit {middlerows} rounds plain \n')

f.write('\nPART 3\n')
f.write('Round 2 and all even rounds: k 1 round\n')
f.write('if using a styrofoam ball, pop it in now and work around it\n')
f.close()
o = round((stitches / 8)-1)
roundy = -1


def decreaseround():
    global stitches
    global roundy
    global o
    decrease = 8
    stitches -= decrease
    roundy += 2
    o -= 1
    f = open(filename, "a")
    f.write(f'Round {roundy}: k{o} ssk repeat to end ({stitches} stitches)\n')
    f.close()


# rewrite the loop so that it runs until 8 sts remain
# for x in range(9):
#    decreaseround()
while stitches > 16:
    decreaseround()


def finaldecrease():
    global roundy
    global stitches
    decrease = 8
    roundy += 2
    stitches -= 8

finaldecrease()
f=open(filename, "a")
f.write(f'Round {roundy}: k2tog repeat to end ({stitches} stitches)\n')
f.write(
    'next round: k2tog 4 times. \nthen icord until long enough to make a nice loop. \nWeave in top ends; use CO end to close up gap on bottom and weave in end.')
f.close()
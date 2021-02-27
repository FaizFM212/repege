import color as c
import random
import sys

print("ANSI Escape Code graphic test\n")

#Text Style
print("Aa {1}Aa{0} {2}Aa{0} {3}Aa{0} {4}Aa{0}".format(c.reset, c.style(1), c.style(2), c.style(3), c.style(4)))

print("")

#8 or 16 Color
c.mode = "16color"
print("{1}  {2}  {3}  {4}  {5}  {6}  {7}  {8}  {0}".format(c.reset, c.colorb(0,0,0), c.colorb(7,0,0), c.colorb(1,0,0), c.colorb(2,0,0), c.colorb(3,0,0), c.colorb(4,0,0), c.colorb(5,0,0), c.colorb(6,0,0),)) #Colors
print("{1}  {2}  {3}  {4}  {5}  {6}  {7}  {8}  {0}".format(c.reset, c.colorb(0,1,0), c.colorb(7,1,0), c.colorb(1,0,0), c.colorb(2,1,0), c.colorb(3,1,0), c.colorb(4,1,0), c.colorb(5,1,0), c.colorb(6,1,0),)) #Bright Colors

print("")

#256 Color
c.mode = "256color"

for i in range(0, 256) :
    sys.stdout.write(c.colorb(i,0,0) + " " + c.reset)
    if i == 15 or i == 51 or i == 87 or i == 123 or i == 159 or i == 195 or i == 231 or i == 231 or i == 255 :
        print("")

print("")

#Custom Color (True Color)
c.mode = "truecolor"
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

print(c.colorb(r, g, b) + "                " + c.reset)

print(c.reset) #Reset style

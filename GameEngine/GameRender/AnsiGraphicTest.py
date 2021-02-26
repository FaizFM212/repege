import random

print("ANSI Escape Code graphic test\n")

#Text Style
print("\033[0mAa \033[1mAa \033[2mAa \033[0m\033[3mAa \033[4mAa")
print("\033[5mAa \033[6mAa \033[7mAa\033[0m")

print("")

#Background Color
print("\u001b[40m \u001b[41m \u001b[42m \u001b[43m \u001b[44m \u001b[45m \u001b[46m \u001b[47 \u001b[0m") #Colors
print("\u001b[100m \u001b[101m \u001b[102m \u001b[103m \u001b[104m \u001b[105m \u001b[106m \u001b[107 \u001b[0m") #Bright Colors

print("")

#Custom Color (True Color)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

print("\u001b[48;2;{0};{1};{2}m       \u001b[0m".format(r, g, b))

print("\u001b[0m") #Reset style

#Set color mode to true color
mode = "truecolor"

#Reset text style
reset = "\033[0m"

#Change text front color
def colorf(r, g, b) :
    if mode == "256color" :
        return "\033[38;5;{0}m".format(r)
    elif mode == "16color" :
        if g == 0 :
            return "\033[3{0}m".format(r)
        else :
            return "\033[9{0}m".format(r)
    else :
        return "\033[38;2;{0};{1};{2}m".format(r, g, b)

#Change text back color
def colorb(r, g, b) :
    if mode == "256color" :
        return "\033[48;5;{0}m".format(r)
    elif mode == "16color" :
        if g == 0 :
            return "\033[4{0}m".format(r)
        else :
            return "\033[10{0}m".format(r)
    else :
        return "\033[48;2;{0};{1};{2}m".format(r, g, b)

#Change text style
def style(style) :
    if style == "bold" or style == 1 :
        return "\033[1m"
    elif style == "faint" or style == "dim" or style == 2 :
        return "\033[2m"
    elif style == "italic" or style == 3 :
        return "\033[3m"
    elif style == "underline" or style == 4 :
        return "\033[4m"

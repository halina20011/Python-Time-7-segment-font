import sys

# https://wiki.bash-hackers.org/scripting/terminalcodes
# https://en.m.wikipedia.org/wiki/ANSI_escape_code
# https://github.com/shawwn/ansi-escapes-python/blob/master/ansi_escapes/ansi_escapes.py

ESC = '\u001B['
OSC = '\u001B]'
BEL = '\u0007'
SEP = ';'

_eraseEndLine = ESC + 'K'
_eraseStartLine = ESC + '1K'
_eraseLine = ESC + '2K'
_eraseDown = ESC + 'J'
_eraseUp = ESC + '1J'
_eraseScreen = ESC + '2J'
_scrollUp = ESC + 'S'
_scrollDown = ESC + 'T'

_cursorLeft = ESC + 'G'
_cursorSavePosition = '\u001B7' + ESC + 's'
_cursorRestorePosition = '\u001B8' + ESC + 'u'
_cursorGetPosition = ESC + '6n'
_cursorNextLine = ESC + 'E'
_cursorPrevLine = ESC + 'F'
_cursorHide = ESC + '?25l'
_cursorShow = ESC + '?25h'

clearScreen = '\u001Bc'

def move(x, y):
    # move cursor to pos = tuple (x,y)
    # x,y = pos
    sys.stdout.write('\x1b[{};{}H'.format(str(x),str(y)))
    sys.stdout.flush()

def run(command):
    sys.stdout.write(command)

def print(output, end = '\n'):
    sys.stdout.write(str(output) + end)

# ##########################################################################
# ############################### Color Text ###############################
# ##########################################################################

class color():
    underline = "4"
    whiteBackground = "7"
    blackBackground = "8"
    crossedout = "9"
    black = "30"
    red = "31"
    green = "32"
    yellow = "33"
    blue = "34"
    purple = "35"
    greenblue = "36"
    redBackground = "41"
    greenBackground = "42"
    yellowBackground = "43"
    blueBackground = "44"
    purpleBackground = "45"
    greenblueBackground = "46"
    whiteBackground = "47"

    def colorText(text, textColor, backgroundColor = "0"):
        start = f"\x1b[{backgroundColor};{str(textColor)}m"
        end = "\033[m"
        return start + text + end

    def rgb(text, r, g, b):
        start = f"\x1b[38;2;{r};{g};{b}m{text}"
        end = "\033[m"
        return start + end

class cursor():
    def hideCursor(): sys.stdout.write('\033[?25l')

    def showCursor(): sys.stdout.write('\033[?25h')

    def cursorUp(count=1): return ESC + str(int(count)) + 'A'

    def cursorDown(count=1): return ESC + str(int(count)) + 'B'

    def cursorForward(count=1): return ESC + str(int(count)) + 'C'

    def cursorBackward(count=1): return ESC + str(int(count)) + 'D'

def clear(whatToClear):
    clear = {
        'screen': '\x1b[2J\x1b[H',
        'line': '\x1b[2K\x1b[G',
        'bos': '\x1b[1J',
        'eos': '\x1b[J',
        'bol': '\x1b[1K',
        'eol': '\x1b[K',
        }
    return clear[whatToClear]

def eraseLines(self, count):
    clear = ""

    for i in range(count):
        if (i < count - 1): 
            clear += _eraseLine + self.cursor.cursorUp() 
        else: clear += ''

    if count != 0:
        clear += _cursorLeft

    sys.stdout.write(clear)

def eraseLine():
    run(cursor.cursorUp())
    run(_eraseLine)
    run(_cursorLeft)
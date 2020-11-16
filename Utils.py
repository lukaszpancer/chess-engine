"""Some functions helping maintain the code bearable"""
EngineDoneThinking = -1
import math


def rank(pos):
    return int(pos) // 8


def col(pos):
    return int(pos) % 8


def posToCoords(pos):
    return (rank(pos), col(pos))


def crToPos(col, rank):
    return rank * 8 + col


def posToTileCenter(pos):
    s = 90
    r = rank(pos)
    c = col(pos)
    return (s / 2 + s * c, s / 2 + s * (7 - r))


def oppColor(color):
    if color == 'w':
        return 'b'
    elif color == 'b':
        return 'w'


def moveToNotation(board, move):
    r, c = posToCoords(move.pos)
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    p = board[move.pos].piecelower
    if p == 'p':
        p = cols[c]
    s = p
    if move.capture:
        s += 'x'
    r1, c1 = posToCoords(move.dest)
    s += cols[c1] + str(r1 + 1)
    return s


def sortFields(f):
    return f.z


def easeOutElastic(t, b, c, d):
    s, a = 1.70158, c

    if t == 0:
        return b
    t /= d
    if t >= 1:
        return b + c

    p = d * 0.3
    if a < abs(c):
        a, s = c, p / 4
    else:
        s = p / (2 * math.pi) * math.asin(c / a)

    return (a * pow(2, -10 * t) * math.sin((t * d - s) *
                                           (2 * math.pi) / p) + c + b)


def easeOutBounce(t, b, c, d):
    t /= d
    if t < (1 / 2.75):
        return c * (7.5625 * t * t) + b

    elif t < (2 / 2.75):
        t -= (1.5 / 2.75)
        return c * (7.5625 * t * t + 0.75) + b

    elif t < (2.5 / 2.75):
        t -= (2.25 / 2.75)
        return c * (7.5625 * t * t + 0.9375) + b

    else:
        t -= (2.625 / 2.75)
        return c * (7.5625 * t * t + 0.984375) + b


def easeOutBack(t, b, c, d, s=1.70158):
    t = t / d - 1
    return c * (t * t * ((s + 1) * t + s) + 1) + b


def easeInExpo(t, b, c, d):
    return c * math.pow(2, 10 * (t / d - 1)) + b


def easeOutExpo(t, b, c, d):
    return c * (-math.pow(2, -10 * t / d) + 1) + b

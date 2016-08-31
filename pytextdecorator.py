#color utils

ESCAPE = '\033[%sm'
ENDC = ESCAPE % '0'


_TEXT_STYLE = {
    'bold' : '1',
    'faint' : '2',
    'underlined' : '4',
    'reverse_color' : '7',
    'concealed': '8', #for passwords or something
    'strikethrough' : '9',
}

_COLORS = {
    'black': '30',
    'red': '31',
    'green': '32',
    'yellow': '33',
    'blue': '34',
    'magenta': '35',
    'cyan': '36',
    'white': '37',
}

_BACKGROUND_COLORS = {
    'black' : '40',
    "red" : '41',
    'green': '42',
    'yellow' : '43',
    'blue' : '44',
    'magenta' : '45',
    'cyan':'46',
    'white':'47',
}

def _ExpandStyle(style):
    s = ""
    for st in style:
        s += _TEXT_STYLE[st] + ";"
    return s[:-1]

def _MakeTwoColorText(color, bcolor, msg):
    t = _COLORS[color] + ";" + _BACKGROUND_COLORS[bcolor]
    return _Decorate(t, msg)

def _MakeColorStyleText(color, style, msg):
    t = _COLORS[color] + ";" + _ExpandStyle(style)
    return _Decorate(t, msg)

def _MakeBColorStyleText(bcolor, style, msg):
    t = _BACKGROUND_COLORS[bcolor] + ";" + _ExpandStyle(style)
    return _Decorate(t, msg)

def _MakeFancyText(color, bcolor, style, msg):
    s = _ExpandStyle(style) + ";" + _COLORS[color] + ";" + _BACKGROUND_COLORS[bcolor]
    return _Decorate(s, msg)

def _MakeStyleText(style, msg):
    s = _ExpandStyle(style)
    return _Decorate(s, msg)

def _MakeBackColorText(color, msg):
    c = _BACKGROUND_COLORS[color]
    return _Decorate(c, msg)

def _MakeColorText(color, msg):
    c = _COLORS[color]
    return _Decorate(c, msg)

def _Decorate(fmt, msg):
    format_sequence = ESCAPE % fmt
    return format_sequence + msg + ENDC

def DecorateText(msg="", **kwargs):
    if('color' in kwargs) and ('bcolor' in kwargs) and ('style' in kwargs):
        t = _MakeFancyText(kwargs['color'], kwargs['bcolor'], kwargs['style'], msg)
    elif('color' in kwargs) and ('bcolor' in kwargs):
        t = _MakeTwoColorText(kwargs['color'], kwargs['bcolor'], msg)
    elif('color' in kwargs) and ('style' in kwargs):
        t = _MakeColorStyleText(kwargs['color'], kwargs['style'], msg)
    elif('bcolor' in kwargs) and ('style' in kwargs):
        t = _MakeBColorStyleText(kwargs['bcolor'], kwargs['style'], msg)
    elif('color' in kwargs):
        t = _MakeColorText(kwargs['color'], msg)
    elif('bcolor' in kwargs):
        t = _MakeBackColorText(kwargs['bcolor'], msg)
    elif('style' in kwargs):
        t = _MakeStyleText(kwargs['style'], msg)
    else:
        t = msg
    return t



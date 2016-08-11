#color utils

class TextDecorator():

    def __init__(self):
        #terminal escape codes for colors
        self.ESCAPE = '\033[%sm'
        self.ENDC = self.ESCAPE % '0'


        self.TEXT_STYLE = {
            'bold' : '1',
            'faint' : '2',
            'underline' : '4',
            'reverse_color' : '7',
            'concealed': '8', #for passwords or something
            'strikethrough' : '9',
        }

        self.COLORS = {
                'black': '30',
                'red': '31',
                'green': '32',
                'yellow': '33',
                'blue': '34',
                'magenta': '35',
                'cyan': '36',
                'white': '37',
        }

        self.BACKGROUND_COLORS = {
                'black' : '40',
                "red" : '41',
                'green': '42',
                'yellow' : '43',
                'blue' : '44',
                'magenta' : '45',
                'cyan':'46',
                'white':'47',
                }

    def _ExpandStyle(self, style):
        s = ""
        for i in range(len(style)):
            s += self.TEXT_STYLE[style[i]] + ";"
        return s[:-1]

    def _MakeTwoColorText(self, color, bcolor, msg):
        t = self.COLORS[color] + ";" + self.BACKGROUND_COLORS[bcolor]
        return self._Decorate(t, msg)

    def _MakeColorStyleText(self, color, style, msg):
        t = self.COLORS[color] + ";" + self._ExpandStyle(style)
        return self._Decorate(t, msg)

    def _MakeBColorStyleText(self, bcolor, style, msg):
        t = self.BACKGROUND_COLORS[bcolor] + ";" + self._ExpandStyle(style)
        return self._Decorate(t, msg)

    def _MakeFancyText(self, color, bcolor, style, msg):
        s = self._ExpandStyle(style) + ";" + self.COLORS[color] + ";" + self.BACKGROUND_COLORS[bcolor]
        return self._Decorate(s, msg)

    def _MakeStyleText(self, style, msg):
        s = self._ExpandStyle(style)
        return self._Decorate(s, msg)

    def _MakeBackColorText(self, color, msg):
        c = self.BACKGROUND_COLORS[color]
        return self._Decorate(c, msg)

    def _MakeColorText(self, color, msg):
        c = self.COLORS[color]
        return self._Decorate(c, msg)

    def _Decorate(self, fmt, msg):
        format_sequence = self.ESCAPE % fmt
        return format_sequence + msg + self.ENDC

    def DecorateText(self, msg="", **kwargs):
        if('color' in kwargs) and ('bcolor' in kwargs) and ('style' in kwargs):
            t = self._MakeFancyText(kwargs['color'], kwargs['bcolor'], kwargs['style'], msg)

        elif('color' in kwargs) and ('bcolor' in kwargs):
            t = self._MakeTwoColorText(kwargs['color'], kwargs['bcolor'], msg)
        elif('color' in kwargs) and ('style' in kwargs):
            t = self._MakeColorStyleText(kwargs['color'], kwargs['style'], msg)
        elif('bcolor' in kwargs) and ('style' in kwargs):
            t = self._MakeBColorStyleText(kwargs['bcolor'], kwargs['style'], msg)
        elif('color' in kwargs):
            t = self._MakeColorText(kwargs['color'], msg)
        elif('bcolor' in kwargs):
            t = self._MakeBackColorText(kwargs['bcolor'], msg)
        elif('style' in kwargs):
            t = self._MakeStyleText(kwargs['style'], msg)
        else:
            t = msg
        return t



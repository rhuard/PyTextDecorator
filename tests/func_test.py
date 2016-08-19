from PyTextDecorator.pytextdecorator import *

def test_color_black():
    s = DecorateText("test", color='black')
    assert s == '\x1b[30mtest\x1b[0m'

def test_color_red():
    s = DecorateText("test", color='red')
    assert s == '\x1b[31mtest\x1b[0m'

def test_color_green():
    s = DecorateText("test", color='green')
    assert s == '\x1b[32mtest\x1b[0m'

def test_color_yellow():
    s = DecorateText("test", color='yellow')
    assert s == '\x1b[33mtest\x1b[0m'

def test_color_blue():
    s = DecorateText("test", color='blue')
    assert s == '\x1b[34mtest\x1b[0m'

def test_color_magenta():
    s = DecorateText("test", color='magenta')
    assert s == '\x1b[35mtest\x1b[0m'

def test_color_cyan():
    s = DecorateText("test", color='cyan')
    assert s == '\x1b[36mtest\x1b[0m'

def test_color_white():
    s = DecorateText("test", color='white')
    assert s == '\x1b[37mtest\x1b[0m'

def test_color_bblack():
    s = DecorateText("test", bcolor='black')
    assert s == '\x1b[40mtest\x1b[0m'

def test_color_bred():
    s = DecorateText("test", bcolor='red')
    assert s == '\x1b[41mtest\x1b[0m'

def test_color_bgreen():
    s = DecorateText("test", bcolor='green')
    assert s == '\x1b[42mtest\x1b[0m'

def test_color_byellow():
    s = DecorateText("test", bcolor='yellow')
    assert s == '\x1b[43mtest\x1b[0m'

def test_color_bblue():
    s = DecorateText("test", bcolor='blue')
    assert s == '\x1b[44mtest\x1b[0m'

def test_color_bmagenta():
    s = DecorateText("test", bcolor='magenta')
    assert s == '\x1b[45mtest\x1b[0m'

def test_color_bcyan():
    s = DecorateText("test", bcolor='cyan')
    assert s == '\x1b[46mtest\x1b[0m'

def test_color_bwhite():
    s = DecorateText("test", bcolor='white')
    assert s == '\x1b[47mtest\x1b[0m'

def test_bold():
    s = DecorateText("test", style=['bold'])
    assert s == '\x1b[1mtest\x1b[0m'

def test_faint():
    s = DecorateText("test", style=['faint'])
    assert s == '\x1b[2mtest\x1b[0m'

def test_underline():
    s = DecorateText("test", style=['underlined'])
    assert s == '\x1b[4mtest\x1b[0m'

def test_reverse_color():
    s = DecorateText("test", style=['reverse_color'])
    assert s == '\x1b[7mtest\x1b[0m'

def test_concealed():
    s = DecorateText("test", style=['concealed'])
    assert s == '\x1b[8mtest\x1b[0m'

def test_strikethrough():
    s = DecorateText("test", style=['strikethrough'])
    assert s == '\x1b[9mtest\x1b[0m'

def test_two_color():
    s = DecorateText("test", color='red', bcolor='blue')
    assert s == '\x1b[31;44mtest\x1b[0m'

def test_color_style():
    s = DecorateText('test', color='red',style=['bold'])
    assert s == '\x1b[31;1mtest\x1b[0m'

def test_bcolor_style():
    s = DecorateText('test', bcolor='red', style=['bold'])
    assert s == '\x1b[41;1mtest\x1b[0m'

def test_multiple_style():
    s = DecorateText('test', style=['bold', 'faint', 'underlined',
        'reverse_color', 'concealed', 'strikethrough'])
    assert s == '\x1b[1;2;4;7;8;9mtest\x1b[0m'

def test_options():
    s = DecorateText('test', color='green', bcolor='blue', style=['bold',
        'underlined', 'strikethrough', 'concealed'])
    assert s == '\x1b[1;4;9;8;32;44mtest\x1b[0m'

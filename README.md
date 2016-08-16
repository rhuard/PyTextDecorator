# PyTextDecorator (cautious-spork)


Python Text Decorator. Uses the ANSI escape characters to allow python code to
print different styles and colors to the console screen

build off ideas found here: http://cwoebker.com/posts/ansi-escape-codes

## import
```python
from PyTextDecorator import *
```

## usage:
```python
T=TextDecorator()

print(T.DecorateText("Hello World", color="green", bcolor="red", style=["bold", "underline"]))
```

This would print `Hello World` in green text on a red background bolded and underlined.

If you do not wish to change either the color, background color or the style of text
from your terminals current then just leave out that parameter:
```python
T=TextDecorator()

print(T.DecorateText("Hello World", color="green", style=["bold", "underline"]))
```
This would print out the text `Hello World` in green text while being bolded and underlined and

```python
T=TextDecorator()

print(T.DecorateText("Hello World", color="green", bcolor="red"))
```

would print out `Hello World` in green text on a red background with no additonal style changes

The style parameter must be passed in as a list, even if there is only one item
`style='strikethrough'` will not work but `style=['strikethrough']` will

## Options
colors (both background and foreground) supported:
* black
* red
* green
* yellow
* blue
* magenta
* cyan
* white

Styles supported:
* bold
* faint
* underline
* reverse_color
* concealed
* strikethrough

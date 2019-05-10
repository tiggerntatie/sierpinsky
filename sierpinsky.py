# Sierpinsky demo
from ggame import CircleAsset, Sprite, App, Color, LineStyle

GASKET_SIZE = 256
black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)
asset = CircleAsset(0.5, thinline, black)

# Draw a Sierpinsky Gasket of width and height d,
# with upper left at (x, y).
def draw_sierpinsky(x, y, d):
    if d <= 1:
        Sprite(asset, (x, y))                 # base case
    else:
        # recurse on upper left quadrant
        draw_sierpinsky(x, y, d/2)
        # recurse on upper right quadrant
        draw_sierpinsky(x + d/2, y, d/2)
        # recurse on lower right quadrant
        draw_sierpinsky(x + d/2, y + d/2, d/2)

draw_sierpinsky(0, 0, GASKET_SIZE)

App().run()

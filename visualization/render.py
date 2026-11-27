"""Render rotating 3D cross-sections of the matched-means Laplace density ratio."""

import argparse
from math import cos, cosh, exp, sin, tau
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BG = "#101c30"
PANEL = "#1b2e4b"
LIGHT = "#f5f8fd"
MUTED = "#cfdef2"
TEAL = "#78dcd1"
TAIL = "#8a9fc5"


def ratio(x, t):
    if abs(x) >= 1:
        return cosh(t)
    return exp(-t * (1 - abs(x))) * cosh(t * x)


def project(x, height, z, angle):
    x, z = x * cos(angle) + z * sin(angle), z * cos(angle) - x * sin(angle)
    tilt = .41 + .13 * cos(angle)
    y, z = height * cos(tilt) - z * sin(tilt), height * sin(tilt) + z * cos(tilt)
    scale = 455 / (5.3 - z)
    return 214 + scale * x, 265 - scale * y, z


def frame(angle, title, label, value, body):
    image = Image.new("RGB", (880, 560), BG)
    draw = ImageDraw.Draw(image)
    draw.text((26, 20), "Rare reports carry the shape signal", font=title, fill=LIGHT)
    draw.line((28, 80, 852, 80), fill="#395375", width=2)
    draw.rounded_rectangle((27, 105, 413, 425), radius=16, fill=PANEL)
    draw.text((50, 121), "Scaled density ratio", font=label, fill=LIGHT)
    segments = []
    for row, t in enumerate((1/8, 1/4, 1/2, 1)):
        z = .53 * (row - 1.5)
        xs = [i / 12 for i in range(-24, 25)]
        points = [project(.78*x, (ratio(x,t)-1)/t, z, angle) for x in xs]
        for x, p, q in zip(xs, points, points[1:]):
            color = TEAL if -1 <= x < 1 else TAIL
            segments.append(((p[2] + q[2]) / 2, p[:2], q[:2], color))
        p, q = (project(.78*x, 0, z, angle) for x in (-2, 2))
        segments.append(((p[2]+q[2])/2, p[:2], q[:2], "#495e7d"))
    for _, p, q, color in sorted(segments):
        draw.line((p,q), fill=color, width=2 if color=="#495e7d" else 4)

    draw.rounded_rectangle((433,105,852,425), radius=16, fill=PANEL)
    draw.text((456,121), "As inverse scale t falls", font=label, fill=LIGHT)
    for y, name, order in ((180,"Interior mass","t"), (250,"Relative difference","t"),
                           (320,"Information","t³")):
        draw.text((457,y+7), name, font=body, fill=MUTED)
        draw.text((826,y), order, font=value, fill=TEAL, anchor="ra")
    for x,color,name in ((35,TEAL,"Interior"),(208,TAIL,"Tails")):
        draw.ellipse((x,455,x+18,473),fill=color)
        draw.text((x+28,445),name,font=body,fill=MUTED)
    draw.text((35,505),"Four inverse scales from 1/8 to 1",font=body,fill=MUTED)
    return image


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regular-font",default="DejaVuSans.ttf")
    parser.add_argument("--bold-font",default="DejaVuSans-Bold.ttf")
    parser.add_argument("--output",type=Path,default=Path("visualization/laplace-shapes.gif"))
    args=parser.parse_args()
    fonts=tuple(ImageFont.truetype(font,size) for font,size in (
        (args.bold_font,42),(args.bold_font,32),(args.bold_font,48),(args.regular_font,30)
    ))
    frames=[frame(.49+i*tau/64,*fonts).quantize(colors=120,method=2) for i in range(64)]
    frames[0].save(args.output,save_all=True,append_images=frames[1:],duration=92,loop=0,disposal=2,optimize=True)


if __name__=="__main__":
    main()

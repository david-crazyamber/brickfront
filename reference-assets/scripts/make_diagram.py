#!/usr/bin/env python3
"""AntCity 战场示意图 720x1280"""
from PIL import Image, ImageDraw, ImageFont

W, H = 720, 1280
CS = 36                 # cell size
GX, GY = 36, 92         # grid origin
COLS, ROWS = 18, 30
FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"

RED = (229, 72, 77)
BLU = (62, 99, 221)
NEU = (232, 230, 225)
WAT = (124, 199, 232)
TRE = (70, 168, 88)
FRU = (60, 200, 80)
INK = (40, 40, 46)
PAPER = (245, 243, 238)

f_t = ImageFont.truetype(FONT, 30)
f_s = ImageFont.truetype(FONT, 19)
f_x = ImageFont.truetype(FONT, 15)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

d.text((W // 2, 20), "AntCity 战场示意 · 18×30", font=f_t, fill=INK, anchor="ma")
d.text((W // 2, 52), "红上蓝下 · 中线为对峙国界 · 水洼不可铺设", font=f_x, fill=(120, 120, 128), anchor="ma")

# ---- territory 归属表 ----
# rows 0-1 红, 28-29 蓝; blob 边缘手工造锯齿战线
terr = {}
for r in range(ROWS):
    for c in range(COLS):
        terr[(c, r)] = "N"
# 红区: r0-9 全红, r10 偶数列红, r11 特定
for r in range(0, 10):
    for c in range(COLS):
        terr[(c, r)] = "R"
for c in range(0, 18, 2):
    terr[(c, 10)] = "R"
for c in (3, 7, 11, 15):
    terr[(c, 11)] = "R"
# 蓝区镜像但错开锯齿(体现非对称)
for r in range(20, 30):
    for c in range(COLS):
        terr[(c, r)] = "B"
for c in range(1, 18, 2):
    terr[(c, 19)] = "B"
for c in (2, 8, 12, 16):
    terr[(c, 18)] = "B"
# 水洼(非对称, 中线附近)
for c, r in [(5, 14), (6, 14), (6, 15), (12, 13), (13, 13)]:
    terr[(c, r)] = "W"

def cell(c, r):
    return (GX + c * CS, GY + r * CS, GX + (c + 1) * CS, GY + (r + 1) * CS)

for r in range(ROWS):
    for c in range(COLS):
        t = terr[(c, r)]
        col = NEU
        if t == "R": col = (249, 210, 212)
        elif t == "B": col = (210, 219, 249)
        elif t == "W": col = WAT
        d.rectangle(cell(c, r), fill=col, outline=(200, 198, 193))

# ---- 国界高亮: R/B 相邻的边界线 ----
for r in range(ROWS):
    for c in range(COLS):
        t = terr[(c, r)]
        if t in ("R", "B"):
            for dc, dr in ((1, 0), (0, 1)):
                n = terr.get((c + dc, r + dr))
                if n and n != t and n != "W":
                    x1, y1, x2, y2 = cell(c, r)
                    if dc == 1:
                        d.line([(x2, y1), (x2, y2)], fill=(255, 140, 60), width=3)
                    else:
                        d.line([(x1, y2), (x2, y2)], fill=(255, 140, 60), width=3)

# ---- 工厂 ----
def factory(c, r, color, name):
    x1, y1, x2, y2 = cell(c, r)
    d.rectangle([x1 + 3, y1 + 10, x2 - 3, y2 - 3], fill=(90, 90, 100), outline=color, width=3)
    d.rectangle([x1 + 8, y1 - 6, x1 + 16, y1 + 12], fill=(90, 90, 100))
    d.text(((x1 + x2) // 2, y1 + (y2 - y1) // 2 + 4), name, font=f_x, fill="white", anchor="mm")

factory(8, 0, RED, "红工厂")
factory(8, 29, BLU, "蓝工厂")

# ---- 树(红: rows4-7 散布; 蓝: rows22-25) ----
trees = [(3, 4), (9, 5), (14, 4), (6, 7), (12, 7), (4, 22), (10, 23), (15, 24), (7, 25), (13, 22)]
for c, r in trees:
    x1, y1, x2, y2 = cell(c, r)
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=TRE, outline=(40, 120, 60), width=2)
    d.rectangle([cx - 2, cy + 8, cx + 2, cy + 14], fill=(120, 80, 50))

# ---- 车辆 ----
def worker(c, r, color):
    x1, y1, x2, y2 = cell(c, r)
    d.rounded_rectangle([x1 + 6, y1 + 10, x2 - 6, y2 - 12], 6, fill="white", outline=color, width=3)
    d.rectangle([x1 + 10, y1 + 2, x2 - 14, y1 + 11], fill=color)  # 货斗砖

def planter(c, r, color):
    x1, y1, x2, y2 = cell(c, r)
    d.rounded_rectangle([x1 + 6, y1 + 12, x2 - 6, y2 - 10], 6, fill=(255, 244, 214), outline=color, width=3)
    d.ellipse([x2 - 16, y1 + 2, x2 - 6, y1 + 12], fill=TRE)

def fighter(c, r, color, dy):
    x1, y1, x2, y2 = cell(c, r)
    d.rectangle([x1 + 5, y1 + 9, x2 - 5, y2 - 9], fill=(70, 70, 78), outline=color, width=3)
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
    d.line([(cx, cy), (cx, cy + dy)], fill=(40, 40, 46), width=5)  # 炮管
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=color)

worker(8, 9, RED); worker(4, 10, RED); worker(12, 11, RED)
worker(8, 20, BLU); worker(13, 19, BLU); worker(5, 18, BLU)
planter(9, 6, RED); planter(11, 23, BLU)
fighter(8, 10, RED, 14); fighter(9, 11, RED, 14)
fighter(9, 18, BLU, -14); fighter(8, 19, BLU, -14)

# ---- 果实直飞虚线 ----
def dashed(p1, p2, color, width=3, dash=8, gap=6):
    x1, y1 = p1; x2, y2 = p2
    total = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    n = max(1, int(total // (dash + gap)))
    for i in range(n + 1):
        s = i * (dash + gap) / total
        e = min(1, (i * (dash + gap) + dash) / total)
        if s >= 1: break
        d.line([(x1 + (x2 - x1) * s, y1 + (y2 - y1) * s),
                (x1 + (x2 - x1) * e, y1 + (y2 - y1) * e)], fill=color, width=width)

for c, r in trees[:5]:  # 红树 -> 红工厂
    x1, y1, x2, y2 = cell(c, r)
    dashed(((x1 + x2) // 2, y1), (GX + 9 * CS, GY + 2 * CS), (90, 190, 100), 2)
for c, r in trees[5:]:  # 蓝树 -> 蓝工厂
    x1, y1, x2, y2 = cell(c, r)
    dashed(((x1 + x2) // 2, y2), (GX + 9 * CS, GY + 29 * CS), (90, 190, 100), 2)

# 果实图标
d.ellipse([GX + 9 * CS - 7, GY + 2 * CS - 7, GX + 9 * CS + 7, GY + 2 * CS + 7], fill=FRU, outline=(30, 140, 60), width=2)
d.ellipse([GX + 9 * CS - 7, GY + 29 * CS - 7, GX + 9 * CS + 7, GY + 29 * CS + 7], fill=FRU, outline=(30, 140, 60), width=2)

# ---- 图例 ----
ly = GY + 30 * CS + 8
lh = 92
d.rounded_rectangle([GX, ly, GX + 648, ly + lh], 8, fill="white", outline=(200, 198, 193))
row1 = [(RED, "红方领土"), (BLU, "蓝方领土"), (NEU, "中立"), (WAT, "水洼·不可铺")]
row2 = [((255, 140, 60), "国界·对峙线"), (TRE, "树"), ((90, 190, 100), "果实直飞线")]
row3 = [((70, 70, 78), "战斗车=黑身+炮管"), ((255, 244, 214), "种树车=黄身"), ("white", "铺地车=白身+货斗")]
x = GX + 12
for col, name in row1:
    d.rectangle([x, ly + 10, x + 16, ly + 26], fill=col, outline=(160, 160, 160))
    d.text((x + 22, ly + 18), name, font=f_x, fill=INK, anchor="lm")
    x += 22 + d.textlength(name, font=f_x) + 16
x = GX + 12
for col, name in row2:
    d.rectangle([x, ly + 40, x + 16, ly + 56], fill=col, outline=(160, 160, 160))
    d.text((x + 22, ly + 48), name, font=f_x, fill=INK, anchor="lm")
    x += 22 + d.textlength(name, font=f_x) + 16
x = GX + 12
for col, name in row3:
    d.rectangle([x, ly + 66, x + 16, ly + 82], fill=col, outline=(160, 160, 160))
    d.text((x + 22, ly + 74), name, font=f_x, fill=INK, anchor="lm")
    x += 22 + d.textlength(name, font=f_x) + 16

img.save("/tmp/ant-arena-assets/diagram-battlefield.png")
print("OK", img.size)

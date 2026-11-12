#!/usr/bin/env python3
"""Ant Arena 城市版 · 素材联系表生成器 v2（真实文件名）"""
from PIL import Image, ImageDraw, ImageFont
import os

FONT = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
SCALE = 3
CELL_IMG = 192
CELL_H = 250
COLS = 3
BG = (245, 243, 238)
CARD = (255, 255, 255)
INK = (40, 40, 46)
SUB = (125, 125, 132)

def font(sz):
    return ImageFont.truetype(FONT, sz)

def sheet(title, subtitle, items, out):
    rows = (len(items) + COLS - 1) // COLS
    W = COLS * (CELL_IMG + 16) + 16
    H = 100 + rows * (CELL_H + 12) + 16
    canvas = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(canvas)
    d.text((20, 16), title, font=font(30), fill=INK)
    d.text((20, 58), subtitle, font=font(16), fill=SUB)
    for i, (path, label, sub) in enumerate(items):
        r, c = divmod(i, COLS)
        x = 16 + c * (CELL_IMG + 16)
        y = 100 + r * (CELL_H + 12)
        d.rounded_rectangle([x, y, x + CELL_IMG, y + CELL_H - 8], 10, fill=CARD)
        im = Image.open(path).convert("RGBA").resize((CELL_IMG, CELL_IMG), Image.NEAREST)
        canvas.paste(im, (x, y), im)
        d.text((x + 8, y + CELL_IMG + 8), label, font=font(19), fill=INK)
        d.text((x + 8, y + CELL_IMG + 34), sub, font=font(13), fill=SUB)
    canvas.save(out)
    print("OK", out, canvas.size, len(items))

def p(pack, name):
    path = f"/tmp/ant-arena-assets/{pack}/Previews/{name}.png"
    assert os.path.exists(path), path
    return path

# 表1 · 车辆
sheet("表1 · 兵种车辆映射 — Kenney Car Kit (CC0)",
      "一张卡=一个独立模型+xN · 蓝红阵营运行时换色 · 预览64px放大3x",
      [
        (p("kenney_car-kit", "delivery"),        "Worker 铺设",   "厢货背5砖·delivery"),
        (p("kenney_car-kit", "police"),           "Soldier 近战",  "巡逻警车·police"),
        (p("kenney_car-kit", "firetruck"),        "Scorpion 减速", "水炮消防车·firetruck"),
        (p("kenney_car-kit", "tractor-shovel"),   "Dung 拆砖",     "装载推土机·tractor-shovel"),
        (p("kenney_car-kit", "kart-oozi"),        "Larva 群攻",    "卡丁车海·kart×N"),
        (p("kenney_car-kit", "truck"),            "Rhino 攻城",    "重卡冲锋·truck"),
        (p("kenney_car-kit", "truck-flat"),       "Queen 产兵",    "平板放兵·truck-flat"),
        (p("kenney_car-kit", "ambulance"),        "Shield 支援",   "维修力场·ambulance"),
        (p("kenney_car-kit", "sedan-sports"),     "Tiger 突袭",    "跑车·sedan-sports"),
        (p("kenney_car-kit", "garbage-truck"),    "Termite 拆砖",  "吃砖垃圾车·garbage"),
        (p("kenney_car-kit", "race-future"),      "Bombardier",    "火箭车·race-future"),
        (p("kenney_car-kit", "tractor"),          "Roly 架炮?",    "变形炮台·缺模型"),
      ],
      "/tmp/ant-arena-assets/sheet1-vehicles.png")

# 表2 · 城市建筑（商业+住宅）
sheet("表2 · 城市建筑 — City Kit Commercial + Suburban (CC0)",
      "地块可视化候选：铺下的领土上'长'建筑 · 或地图边缘装饰",
      [
        (p("city-kit-commercial", "building-a"),          "商业楼A", "commercial"),
        (p("city-kit-commercial", "building-c"),          "商业楼C", "commercial"),
        (p("city-kit-commercial", "building-e"),          "商业楼E", "commercial"),
        (p("city-kit-commercial", "building-h"),          "商业楼H", "commercial"),
        (p("city-kit-commercial", "building-skyscraper-a"),"摩天楼A", "commercial"),
        (p("city-kit-commercial", "building-skyscraper-c"),"摩天楼C", "commercial"),
        (p("city-kit-commercial", "low-detail-building-a"),"远景楼A", "批量远景"),
        (p("city-kit-suburban", "building-type-a"),       "住宅A",  "suburban"),
        (p("city-kit-suburban", "building-type-c"),       "住宅C",  "suburban"),
        (p("city-kit-suburban", "building-type-h"),       "公共建筑","suburban"),
        (p("city-kit-suburban", "building-type-m"),       "市政风", "suburban"),
        (p("city-kit-suburban", "building-type-q"),       "商铺风", "suburban"),
      ],
      "/tmp/ant-arena-assets/sheet2-buildings.png")

# 表3 · 地块+工业（铺地材料/障碍/砖块外观）
sheet("表3 · 地块与工业 — City Kit Roads + Industrial (CC0)",
      "地板块材料：道路件=铺地格 · 工业件=永久障碍与'砖块'外观候选",
      [
        (p("city-kit-roads", "road-straight"),        "直路格",    "roads·铺地基本件"),
        (p("city-kit-roads", "road-bend"),            "弯路格",    "roads"),
        (p("city-kit-roads", "road-crossroad"),       "十字路格",  "roads"),
        (p("city-kit-roads", "road-end"),             "断头路格",  "roads"),
        (p("city-kit-roads", "road-curve"),           "转角路格",  "roads"),
        (p("city-kit-roads", "construction-barrier"), "施工路障",  "roads·临时障碍"),
        (p("city-kit-industrial", "shipping-container-a"), "集装箱A", "砖块外观候选"),
        (p("city-kit-industrial", "shipping-container-b"), "集装箱B", "砖块外观候选"),
        (p("city-kit-industrial", "building-a"),      "厂房A",    "永久障碍"),
        (p("city-kit-industrial", "water-tower"),     "水塔",     "地图装饰"),
        (p("city-kit-industrial", "windmill"),        "风车",     "地图装饰"),
        (p("city-kit-industrial", "chimney-large"),   "大烟囱",   "地图装饰"),
      ],
      "/tmp/ant-arena-assets/sheet3-roads-industrial.png")

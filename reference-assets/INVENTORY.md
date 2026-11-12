# INVENTORY.md — Ant Arena 城市版素材暂存清单

日期：2026-11-12
状态：审查中，未复制进项目仓库。来源优先级：用户地址 > 本清单。

## 来源与许可

| 包 | 来源 | 许可 | 获取方式 |
|---|---|---|---|
| Kenney Car Kit 3.1 | https://kenney.nl/assets/car-kit | CC0（License.txt 随包） | 官网签名直链，无需登录 |

复现下载命令：
```bash
UA="Mozilla/5.0 Chrome/130.0.0.0 Safari/537.36"
curl -c cookies.txt -A "$UA" "https://kenney.nl/assets/car-kit" -o /dev/null
curl -b cookies.txt -A "$UA" -H "Referer: https://kenney.nl/assets/car-kit" \
  "https://kenney.nl/download-link/6173736574732f6361722d6b6974"
# 返回JSON中的url即签名直链，curl下载即可
```

## 目录结构

- `kenney_car-kit/Models/GLB format/` — **50个GLB**（glTF二进制，Cocos Creator 3.x原生支持）✅主用
- `kenney_car-kit/Models/FBX format/` — 50个FBX（备选）
- `kenney_car-kit/Models/OBJ format/` — 50个OBJ（备选）
- `kenney_car-kit/Previews/` — 每模型预览图
- `kenney_car-kit/License.txt` — CC0全文

## 兵种映射（城市版 · 草案）

| 兵种 | 角色 | 拟用模型 | 匹配度 |
|---|---|---|---|
| Worker（铺设） | 搬5块循环 | `delivery`（货斗 visibly 载货） | ★★★★★ |
| Soldier（近战基准） | 巡逻 | `police` | ★★★★ |
| Scorpion（远程减速） | 水炮减速 | `firetruck` | ★★★★ |
| Dung→改冲撞拆砖 | 推土 | `tractor-shovel` | ★★★★★ |
| Larva→改啃食群 | 小车海 | `kart-*` ×N（oobi/oodi/ooli/oopi/oozi） | ★★★★ |
| Rhino（攻城锤） | 重型冲锋 | `truck`（重卡冲撞） | ★★★ |
| Queen（产工蚁） | 平板车放兵 | `truck-flat`（单位从车斗驶出） | ★★★★★ |
| Shield Bugs（护盾支援） | 维修力场 | `ambulance` | ★★★★ |
| Tiger（快速突袭） | 跑车猎后排 | `sedan-sports` / `hatchback-sports` | ★★★★★ |
| Termite（拆砖工具） | 压碎方块 | `garbage-truck`（吃垃圾=吃砖，完美） | ★★★★★ |
| Bombardier（范围远程） | 火箭车 | `race-future` + 程序化发射器 | ★★★ |
| Roly（滚动→架炮） | 变形炮台 | **缺** — 见缺口 | — |

未指派可用模型：sedan、suv、suv-luxury、taxi、van、box、tractor、tractor-police、delivery-flat、race、5种wheel、debris×13（命中碎块可用！）

## 备选与缺口

- **缺口1：Rhino 真坦克造型**。Car Kit无军用模型。备选：Quaternius军事包 / poly.pizza搜"tank"（需API key）/ 程序化拼（盒体+履带轮+炮管）。
- **缺口2：Roly 展开炮台**。无现成。程序化拼（球罐+液压支架+炮管）最贴合低模风。
- **备选来源**：poly.pizza（City Pack含36个车/楼/路模型，CC0；站有Cloudflare，API需免费key）；Quaternius（CC0，部分带骨骼动画）。
- debris系列13件 → 直接做命中碎裂特效，白捡。

## 已入库包（全部CC0，License.txt随包）

| 包 | GLB数 | 用途 |
|---|---|---|
| Kenney Car Kit 3.1 | 50 | 兵种车辆 |
| City Kit Roads | 95 | 铺地格材料（道路件） |
| City Kit Industrial | 37 | 永久障碍/砖块外观/装饰 |
| City Kit Suburban | 40 | 建筑与围栏树木装饰 |
| City Kit Commercial | 41 | 领土建筑可视化候选 |

共263个GLB。tiny-city为2D瓦片包，不适用3D。
联系表：sheet1-vehicles / sheet2-buildings / sheet3-roads-industrial（已发用户微信）

## 待用户确认

1. Kenney低模卡通风格是否接受（联系表已发）
2. 仅CC0 or 接受CC-BY署名
3. 是否有自有的模型链接优先
4. 全军车化 or 保留部分虫形单位

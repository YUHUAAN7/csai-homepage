# -*- coding: utf-8 -*-
"""메인 비주얼 배경(assets/hero.svg)을 그린다. 사진이 아니라 직접 그린 야경 일러스트.
실제 사진을 쓰게 되면 assets/hero.svg 대신 사진 파일로 바꾸고 site.css의 .hero-art만 고치면 된다."""
import random

W, H, HORIZON = 1920, 640, 468


def windows(x, y, w, h, rnd, warm=0.18):
    """건물 창문 불빛."""
    out = []
    cw, ch = 7, 9
    cols, rows = max(1, int((w - 6) // cw)), max(1, int((h - 8) // ch))
    ox = x + (w - cols * cw) / 2 + 1.5
    for r in range(rows):
        for c in range(cols):
            p = rnd.random()
            if p < 0.46:
                continue
            col = "#FFD79A" if rnd.random() < warm else ("#BFE0FF" if rnd.random() < 0.6 else "#7FB6FF")
            op = round(0.35 + rnd.random() * 0.6, 2)
            out.append(f'<rect x="{ox + c * cw:.1f}" y="{y + 6 + r * ch:.1f}" width="4" height="5" fill="{col}" opacity="{op}"/>')
    return "".join(out)


def build():
    rnd = random.Random(72)
    city = []

    # 먼 배경 건물(흐릿한 층)
    x = 380
    while x < W + 40:
        w = rnd.randint(30, 80)
        h = rnd.randint(24, 96) + (48 if 1000 < x < 1700 else 0)
        city.append(f'<rect x="{x}" y="{HORIZON - h}" width="{w}" height="{h}" fill="#16346F" opacity=".55"/>')
        x += w + rnd.randint(0, 10)

    # 앞쪽 건물
    x = 560
    while x < W + 20:
        centre = 1.0 - min(abs(x - 1380) / 760.0, 1.0)
        w = rnd.randint(34, 78)
        h = int(56 + rnd.random() * 96 + centre * rnd.randint(50, 190))
        if 1010 < x < 1150:      # 타워 자리 비우기
            h = int(h * 0.45)
        y = HORIZON - h
        shade = rnd.choice(["#0B2150", "#0D2658", "#102C63", "#0A1D47"])
        city.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{shade}"/>')
        city.append(f'<rect x="{x}" y="{y}" width="2" height="{h}" fill="#5FA0F0" opacity=".35"/>')
        city.append(windows(x, y, w, h, rnd))
        if rnd.random() < 0.3:
            city.append(f'<rect x="{x + w / 2 - 1}" y="{y - 26}" width="2" height="26" fill="#89B8F5" opacity=".7"/>')
            city.append(f'<circle cx="{x + w / 2}" cy="{y - 27}" r="2.2" fill="#FF9A7A"/>')
        x += w + rnd.randint(2, 12)

    # 높은 유리 타워 두 채 (지평선 기준 상대좌표)
    g = []
    g.append('<path d="M1492 0 L1500 -360 Q1524 -396 1548 -360 L1556 0Z" fill="#0F2D68"/>')
    g.append('<path d="M1500 -360 Q1524 -396 1548 -360 L1546 -310 Q1524 -340 1502 -310Z" fill="#6FA8F5" opacity=".5"/>')
    g.append(windows(1500, -310, 48, 300, rnd, warm=0.1))
    g.append('<path d="M1612 0 L1616 -310 L1680 -324 L1686 0Z" fill="#0C2456"/>')
    g.append('<path d="M1630 -292 L1668 -300 L1670 -258 L1630 -254Z" fill="#081638"/>')
    g.append(windows(1618, -244, 64, 236, rnd, warm=0.25))
    city.append(f'<g transform="translate(330 {HORIZON}) scale(.8)">{"".join(g)}</g>')

    # 방송탑 모양의 타워
    t = []
    t.append('<path d="M-46 0 L-6 -180 L6 -180 L46 0 L34 0 L0 -140 L-34 0Z" fill="#B45BC8" opacity=".9"/>')
    t.append('<rect x="-7" y="-360" width="14" height="360" fill="#C56AD6"/>')
    t.append('<rect x="-2.5" y="-360" width="5" height="360" fill="#F3B9FF" opacity=".7"/>')
    t.append('<circle cx="0" cy="-158" r="34" fill="url(#orb)"/>')
    t.append('<circle cx="0" cy="-158" r="34" fill="none" stroke="#FFD0FF" stroke-opacity=".5"/>')
    t.append('<circle cx="0" cy="-310" r="23" fill="url(#orb)"/>')
    t.append('<circle cx="0" cy="-374" r="9" fill="url(#orb)"/>')
    t.append('<path d="M-2 -382 L0 -514 L2 -382Z" fill="#F0C4FF"/>')
    t.append('<circle cx="0" cy="-514" r="3" fill="#FFB199"/>')
    for yy in (-270, -230, -90, -50):
        t.append(f'<rect x="-12" y="{yy}" width="24" height="5" rx="2" fill="#F3B9FF" opacity=".8"/>')
    city.append(f'<g transform="translate(1080 {HORIZON}) scale(.78)">{"".join(t)}</g>')

    # 물가의 따뜻한 불빛 띠
    lights = []
    for i in range(210):
        lx = 470 + i * 7 + rnd.random() * 4
        lights.append(f'<circle cx="{lx:.0f}" cy="{HORIZON - 3 - rnd.random() * 10:.0f}" r="{1.2 + rnd.random() * 1.5:.1f}" fill="{rnd.choice(["#FFC978", "#FFE2A8", "#FF9F6B"])}" opacity="{0.55 + rnd.random() * 0.45:.2f}"/>')

    # 지구본 격자
    gx, gy, gr = 1600, 250, 380
    globe = [f'<circle cx="{gx}" cy="{gy}" r="{gr}" fill="url(#globeFill)"/>',
             f'<circle cx="{gx}" cy="{gy}" r="{gr}" fill="none" stroke="#9CC6FF" stroke-opacity=".5" stroke-width="1.4"/>']
    for k in (0.18, 0.4, 0.62, 0.82, 0.96):
        globe.append(f'<ellipse cx="{gx}" cy="{gy}" rx="{gr * k:.0f}" ry="{gr}" fill="none" stroke="#BFDcFF" stroke-opacity=".62" stroke-width="2.2" stroke-dasharray="1 10" stroke-linecap="round"/>')
    for k in (-0.75, -0.45, -0.15, 0.15, 0.45, 0.75):
        ry = gr * k
        rx = (gr ** 2 - ry ** 2) ** 0.5
        globe.append(f'<ellipse cx="{gx}" cy="{gy + ry:.0f}" rx="{rx:.0f}" ry="{rx * 0.16:.0f}" fill="none" stroke="#BFDCFF" stroke-opacity=".5" stroke-width="2.2" stroke-dasharray="1 10" stroke-linecap="round"/>')
    nodes = [(1320, 150), (1460, 70), (1650, 96), (1810, 180), (1530, 230), (1730, 300), (1390, 280)]
    for (a, b) in ((0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (4, 2), (6, 4), (5, 3)):
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        globe.append(f'<path d="M{x1} {y1} Q{(x1 + x2) / 2:.0f} {min(y1, y2) - 70} {x2} {y2}" fill="none" stroke="#CFE5FF" stroke-opacity=".5" stroke-width="1.2"/>')
    for (nx, ny) in nodes:
        globe.append(f'<circle cx="{nx}" cy="{ny}" r="3.4" fill="#EAF4FF"/><circle cx="{nx}" cy="{ny}" r="9" fill="#9CC6FF" opacity=".25"/>')

    ripples = "".join(
        f'<rect x="{rnd.randint(380, 1800)}" y="{HORIZON + 14 + i * 9}" width="{rnd.randint(60, 320)}" height="1.4" fill="#BFD9FF" opacity="{0.05 + rnd.random() * 0.12:.2f}"/>'
        for i in range(26))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" preserveAspectRatio="xMaxYMax slice">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#040D24"/><stop offset=".45" stop-color="#0A2152"/><stop offset=".72" stop-color="#21468F"/><stop offset=".74" stop-color="#0A1E4A"/><stop offset="1" stop-color="#050F28"/></linearGradient>
<radialGradient id="dusk" cx="1250" cy="{HORIZON}" r="820" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFBE78" stop-opacity=".95"/><stop offset=".22" stop-color="#F08A7E" stop-opacity=".62"/><stop offset=".55" stop-color="#8B62C8" stop-opacity=".34"/><stop offset="1" stop-color="#1B3E86" stop-opacity="0"/></radialGradient>
<radialGradient id="globeFill" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#3C7BE0" stop-opacity=".34"/><stop offset="1" stop-color="#0A2152" stop-opacity=".04"/></radialGradient>
<radialGradient id="orb" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#FFE3FF"/><stop offset=".5" stop-color="#D67BE6"/><stop offset="1" stop-color="#6E3AA8"/></radialGradient>
<linearGradient id="water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#143673"/><stop offset="1" stop-color="#050F28"/></linearGradient>
<linearGradient id="fadeL" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#050F28"/><stop offset=".32" stop-color="#061331" stop-opacity=".9"/><stop offset=".62" stop-color="#061331" stop-opacity="0"/></linearGradient>
<filter id="soft" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="cloud" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="26"/></filter>
<clipPath id="skyClip"><rect width="{W}" height="{HORIZON}"/></clipPath>
<clipPath id="waterClip"><rect y="{HORIZON}" width="{W}" height="{H - HORIZON}"/></clipPath>
<g id="city">{"".join(city)}</g>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<g clip-path="url(#skyClip)">
<rect width="{W}" height="{HORIZON}" fill="url(#dusk)"/>
<g filter="url(#cloud)" opacity=".62"><ellipse cx="780" cy="200" rx="300" ry="30" fill="#F29A8C"/><ellipse cx="1200" cy="120" rx="380" ry="28" fill="#C98BD8"/><ellipse cx="1660" cy="330" rx="340" ry="26" fill="#FFC08A"/><ellipse cx="560" cy="320" rx="260" ry="24" fill="#8E79D6"/><ellipse cx="1000" cy="380" rx="420" ry="26" fill="#FFB07A"/></g>
<g>{"".join(globe)}</g>
<use xlink:href="#city" href="#city"/>
<g>{"".join(lights)}</g>
</g>
<g clip-path="url(#waterClip)">
<rect y="{HORIZON}" width="{W}" height="{H - HORIZON}" fill="url(#water)"/>
<g transform="translate(0 {2 * HORIZON}) scale(1 -1)" opacity=".34" filter="url(#soft)"><use xlink:href="#city" href="#city"/></g>
<ellipse cx="1250" cy="{HORIZON + 6}" rx="760" ry="70" fill="#FFB56B" opacity=".2" filter="url(#cloud)"/>
{ripples}
</g>
<rect y="{HORIZON - 1}" width="{W}" height="2" fill="#FFD79A" opacity=".35"/>
<rect width="{W}" height="{H}" fill="url(#fadeL)"/>
</svg>'''


if __name__ == "__main__":
    import sys
    open(sys.argv[1], "w", encoding="utf-8").write(build())

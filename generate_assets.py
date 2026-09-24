import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

def create_svg_favicon():
    font = TTFont('C:\\Windows\\Fonts\\segoeuib.ttf')
    glyphset = font.getGlyphSet()
    cmap = font.getBestCmap()
    g7 = cmap[ord('7')]
    g2 = cmap[ord('2')]

    adv7 = font['hmtx'][g7][0]
    adv2 = font['hmtx'][g2][0]

    # Target size: 512x512
    # Segoe UI Bold: cap height is ~1458
    scale = 300.0 / 1458.0
    total_visual_width = (adv7 + 1039 - 96) * scale
    target_x = (512 - total_visual_width) / 2
    dx = target_x - 96 * scale

    baseline_y = 406

    pen7 = SVGPathPen(glyphset)
    tpen7 = TransformPen(pen7, (scale, 0, 0, -scale, dx, baseline_y))
    glyphset[g7].draw(tpen7)
    path7 = pen7.getCommands()

    pen2 = SVGPathPen(glyphset)
    tpen2 = TransformPen(pen2, (scale, 0, 0, -scale, dx + adv7 * scale, baseline_y))
    glyphset[g2].draw(tpen2)
    path2 = pen2.getCommands()

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="112" fill="#0f766e"/>
  <path d="{path7} {path2}" fill="#ffffff"/>
</svg>
'''
    with open('favicon.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print('Created favicon.svg')

def create_raster_favicons():
    size = 512
    img512 = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img512)
    radius = 112
    draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill='#0f766e')
    font = ImageFont.truetype('C:\\Windows\\Fonts\\segoeuib.ttf', 300)
    text = '72'
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (size - text_w) / 2 - bbox[0]
    y = (size - text_h) / 2 - bbox[1] - 6
    draw.text((x, y), text, font=font, fill='#ffffff')

    # Apple Touch Icon 180x180
    img180 = img512.resize((180, 180), Image.Resampling.LANCZOS)
    img180.save('apple-touch-icon.png', optimize=True)

    # 32x32 PNG
    img32 = img512.resize((32, 32), Image.Resampling.LANCZOS)
    img32.save('favicon-32x32.png', optimize=True)

    # 16x16 PNG
    img16 = img512.resize((16, 16), Image.Resampling.LANCZOS)
    img16.save('favicon-16x16.png', optimize=True)

    # Multi-resolution ICO (16, 32, 48)
    img48 = img512.resize((48, 48), Image.Resampling.LANCZOS)
    img512.save('favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    print('Created raster favicons: apple-touch-icon.png, favicon-32x32.png, favicon-16x16.png, favicon.ico')

def create_social_thumbnail():
    src_path = r'C:\Users\petrh\.gemini\antigravity\brain\87d3da08-14c1-4aed-8a8d-85f4714bae73\readiness_art_1790292839083.jpg'
    im = Image.open(src_path)

    # Aspect ratio 1200x630 (1.90476:1)
    target_w, target_h = 1200, 630
    target_ratio = target_w / target_h

    crop_h = int(im.width / target_ratio)
    crop_top = 10
    crop_box = (0, crop_top, im.width, crop_top + crop_h)
    cropped = im.crop(crop_box)
    base = cropped.resize((1200, 630), Image.Resampling.LANCZOS).convert('RGBA')

    overlay = Image.new('RGBA', base.size, (0, 0, 0, 0))

    # Top-left card
    bx, by = 48, 36
    bw, bh = 426, 82

    # Card subtle drop shadow
    s_layer = Image.new('RGBA', base.size, (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(s_layer)
    s_draw.rounded_rectangle([bx, by + 2, bx + bw, by + bh + 2], radius=16, fill=(0, 0, 0, 40))
    s_layer = s_layer.filter(ImageFilter.GaussianBlur(8))
    overlay = Image.alpha_composite(s_layer, overlay)
    draw = ImageDraw.Draw(overlay)

    # Card background (clean translucent white)
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=16, fill=(255, 255, 255, 245), outline=(203, 213, 225, 220), width=1)

    # Brand badge inside card: [ 72 HODIN ]
    logo_x, logo_y = bx + 14, by + 13
    logo_w, logo_h = 138, 56
    draw.rounded_rectangle([logo_x, logo_y, logo_x + logo_w, logo_y + logo_h], radius=10, fill='#0f766e')

    font_badge_num = ImageFont.truetype('C:\\Windows\\Fonts\\segoeuib.ttf', 32)
    font_badge_word = ImageFont.truetype('C:\\Windows\\Fonts\\segoeuib.ttf', 21)
    draw.text((logo_x + 12, logo_y + 10), '72', font=font_badge_num, fill='#ffffff')
    draw.text((logo_x + 56, logo_y + 18), 'HODIN', font=font_badge_word, fill='#ffffff')

    # Text next to logo badge
    font_title = ImageFont.truetype('C:\\Windows\\Fonts\\segoeuib.ttf', 21)
    font_sub = ImageFont.truetype('C:\\Windows\\Fonts\\segoeui.ttf', 17)
    draw.text((bx + 166, by + 16), 'Občanský manuál', font=font_title, fill='#0f172a')
    draw.text((bx + 166, by + 44), 'krizové připravenosti', font=font_sub, fill='#0f766e')

    # Top-right domain pill
    rx, ry = 1200 - 48 - 164, 36
    rw, rh = 164, 44
    s_layer2 = Image.new('RGBA', base.size, (0, 0, 0, 0))
    s_draw2 = ImageDraw.Draw(s_layer2)
    s_draw2.rounded_rectangle([rx, ry + 2, rx + rw, ry + rh + 2], radius=22, fill=(0, 0, 0, 35))
    s_layer2 = s_layer2.filter(ImageFilter.GaussianBlur(6))
    overlay = Image.alpha_composite(s_layer2, overlay)
    draw = ImageDraw.Draw(overlay)

    draw.rounded_rectangle([rx, ry, rx + rw, ry + rh], radius=22, fill=(255, 255, 255, 245), outline=(203, 213, 225, 220), width=1)
    font_domain = ImageFont.truetype('C:\\Windows\\Fonts\\segoeuib.ttf', 18)
    draw.text((rx + 28, ry + 10), '72hodin.info', font=font_domain, fill='#0f766e')

    final_thumb = Image.alpha_composite(base, overlay).convert('RGB')
    final_thumb.save('72hodin-thumbnail.png', optimize=True)
    # Also save jpg version as backup
    final_thumb.save('72hodin-thumbnail.jpg', quality=94, optimize=True)
    print('Created 72hodin-thumbnail.png and 72hodin-thumbnail.jpg (1200x630)')

if __name__ == '__main__':
    create_svg_favicon()
    create_raster_favicons()
    create_social_thumbnail()

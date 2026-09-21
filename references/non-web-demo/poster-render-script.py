from PIL import Image, ImageDraw, ImageFont
import random

FONT_DIR = "/Users/jacobhurvitz/.claude/skills/canvas-design/canvas-fonts"
W, H = 1600, 2000

bg = (238, 229, 212)
img = Image.new("RGB", (W, H), bg)

random.seed(7)
grain = Image.new("L", (W, H), 0)
gdraw = ImageDraw.Draw(grain)
for _ in range(30000):
    x, y = random.randint(0, W-1), random.randint(0, H-1)
    gdraw.point((x, y), fill=random.randint(0, 18))
img = Image.composite(Image.new("RGB",(W,H),(210,196,170)), img, grain)
draw = ImageDraw.Draw(img)

serif_display = ImageFont.truetype(f"{FONT_DIR}/InstrumentSerif-Regular.ttf", 340)
serif_italic = ImageFont.truetype(f"{FONT_DIR}/InstrumentSerif-Italic.ttf", 340)
italic_small = ImageFont.truetype(f"{FONT_DIR}/CrimsonPro-Italic.ttf", 34)
mono_label = ImageFont.truetype(f"{FONT_DIR}/JetBrainsMono-Regular.ttf", 22)

ink = (26, 22, 18)
accent = (163, 46, 33)
quiet = (120, 108, 90)

# vertically centered around the golden third, not the geometric middle
y0 = 740
draw.text((110, y0), "Design", font=serif_display, fill=ink)
draw.text((110, y0+340), "Mastery", font=serif_italic, fill=ink)
draw.ellipse((1160, y0+295, 1200, y0+335), fill=accent)
draw.text((116, y0+700), "is knowing precisely what to leave out.", font=italic_small, fill=(70, 60, 50))

# balancing element in the lower field: a single thin rule, off-center, echoing the
# frame rather than decorating the emptiness
draw.line((110, H-260, 780, H-260), fill=quiet, width=1)
draw.text((110, H-235), "SPECIMEN 5,000 / HOURS OBSERVED 300,000", font=mono_label, fill=quiet)

m = 60
draw.rectangle((m, m, W-m, H-m), outline=quiet, width=1)

out = "/private/tmp/claude-501/-Users-jacobhurvitz/2bc573b0-a030-4d8f-9f6e-6e08335b83b5/scratchpad/patient-ink-poster.png"
img.save(out, "PNG")
print("saved")

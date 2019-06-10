from PIL import Image
from PIL.ImageChops import difference

inter = Image.open('intercepted.png')
orig = Image.open('original.png')

assert inter.size == orig.size, "sizes do not match"
x, y = orig.size

diff = difference(inter, orig)

if diff.getbbox():
    diff.save('diff.png')

bbox = diff.getbbox()
print sum(x != (0, 0, 0) for x in diff.crop(bbox).getdata()) if bbox else 0

box = (0, 0, 1, y)
region = diff.crop(box)

region.save('rescaled.png','png')


import os
from book import Book


out = r'C:\Users\chaor\Downloads\out'
if not os.path.isdir(out):
    os.mkdir(out)


imgs = set(
    [
        str(n).zfill(3)
        for n in [14, 15, 21, 57, 65, 113, 135, 217, 265, 287, 292, 293, 294, 295, 296, 297, 298 ]
    ]
    + 
    [
        str(n).zfill(3)
        for n in range(6)
    ]
    # + [
    #     str(n).zfill(3)
    #     for n in range(346, 351)
    # ]
    # + [
    #     'tanetuske_{}'.format(str(n).zfill(3))
    #     for n in [1, 2, 3, 29, 43, 93, 129, 147, 190, 209, 231, 257, 269, 272, 283, 284]
    # ]
)
#
# is_img = lambda p: p.name.endswith('_img')

# imgs = set(['001', '002', '003', '006', '008'],)


book = (
    Book(r'C:\Users\chaor\Downloads\in')
    # .remove_border(0, 0, 75, 85, should_skip=lambda page: page.name not in imgs)
    # .remove_border(65, 350, 90, 62, skips=imgs) # モンスターのご主人様
    # .remove_border(66, 74, 50, 42, skips=imgs) # 英雄王、武を極めるため転生す ～そして
    # .remove_border(98, 100, 150, 180, should_skip=lambda page: page.name not in imgs) # 裏切られたSランク冒険者の俺は 
    # .remove_border(65, 65, 97, 112, skips=imgs) # 裏切られたSランク冒険者の俺は 
    .remove_border(79, 65, 35, 35, skips=imgs) # 歴史に残る悪女になるぞ
    # .remove_border(43, 43, 75, 75, skips=imgs)
    # .split(3, -30, skips=imgs)
    # .reverse_background(60, skips=imgs) #(should_skip=is_img)
    # .resize(0.6, skips={'P000A.jpg', 'P001.jpg'})
    # .blur((3, 3))
    .save(r'C:\Users\chaor\Downloads\out')
)


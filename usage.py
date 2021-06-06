import os
from book import Book


out = r'C:\Users\chaor\Downloads\out'
if not os.path.isdir(out):
    os.mkdir(out)


# imgs = set(
#     [
#         str(n).zfill(3)
#         for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#     ]
#     + [
#         'a08_{}'.format(str(n).zfill(3))
#         for n in (
#             list(range(1, 8))
#             + [43, 89, 157, 189, 227, 261, 263]
#             + list(range(275, 289))
#         )
#     ]
# )
#
# is_img = lambda p: p.name.endswith('_img')

# imgs = set(['001'])
#
# book = (
#     Book(r'C:\Users\chaor\Downloads\huifu\2')
#     .remove_border(98, 100, 95, 100, skips=imgs)
#     # .split(2, 110, skips=imgs)
#     # .reverse_background(60) #(should_skip=is_img)
#     .save(r'C:\Users\chaor\Downloads\out')
# )

folder = r'C:\漫画\2016虎之穴日本成人畅销漫画TOP20榜单'
for comic in os.listdir(folder):
    try:
        print(f'Processing {comic}')
        book = Book(os.path.join(folder, comic)).to_pdf(out)
    except Exception as e:
        import ipdb; ipdb.set_trace()

# comic = r'[[momi] ふらっぴー]'
# Book(os.path.join(folder, comic)).to_pdf(out)

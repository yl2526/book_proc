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
book = (
    Book(r'C:\Users\chaor\Downloads\in')
    # .remove_border(350, 350, 350, 350, skips={'001.jpg'})
    # .split(2, 110, skips=imgs)
    # .reverse_background(60) #(should_skip=is_img)
    # .resize(0.6, skips={'P000A.jpg', 'P001.jpg'})
    # .blur((9, 9), skips={'P000A.jpg', 'P001.jpg'})
    .save(r'C:\Users\chaor\Downloads\out')
)

folder = r'C:\BaiduYunDownload\漫画\temp'
for comic in os.listdir(folder):
    try:
        print(f'Processing {comic}')
        book = Book(os.path.join(folder, comic))
        book.to_pdf(out)
    except Exception as e:
        import ipdb; ipdb.set_trace()

# comic = r'[[momi] ふらっぴー]'
# Book(os.path.join(folder, comic)).to_pdf(out)

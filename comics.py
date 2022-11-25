import os
from book import Book


out = r'C:\Users\chaor\Downloads\out'
if not os.path.isdir(out):
    os.mkdir(out)


folder = r'C:\BaiduYunDownload\漫画\temp'


for comic in os.listdir(folder):
    try:
        print(f'Processing {comic}')
        book = Book(os.path.join(folder, comic))
        book.to_pdf(out)
    except Exception as e:
        print(f'Processing {comic} failed')
        print(e)
        # import ipdb; ipdb.set_trace()



# current_dir = os.getcwd()
# os.chdir(folder)
# for comic in os.listdir(folder):
#     try:
#         print(f'Processing {comic}')
        
#         with open('name_backup.txt', 'w+', encoding='utf-8') as f:
#             f.write(comic)
#         os.rename(comic, 'processing')
#         book = (
#             Book('processing')
#             .blur((3, 3))
#             # .remove_border(0, 0, 180, 180)
#             # .split(2, 90)
#         )
#         book.to_pdf(out, comic)
#     except Exception as e:
#         os.rename('processing', comic)
#         print(f'Processing {comic} failed')
#         print(e)
#         # import ipdb; ipdb.set_trace()
#     finally:
#         os.rename('processing', comic)
# os.remove('name_backup.txt')
# os.chdir(current_dir)


# comic = r'[[momi] ふらっぴー]'
# Book(os.path.join(folder, comic)).to_pdf(out)

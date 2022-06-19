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
        import ipdb; ipdb.set_trace()



# comic = r'[[momi] ふらっぴー]'
# Book(os.path.join(folder, comic)).to_pdf(out)

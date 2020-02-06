from book import Book

book = (
    Book(r'input/foler')
    .remove_border(50, 10, 10, 70)
    .split(2, 100, skips={'000', '004'})
    .save(r'export/foler')

)

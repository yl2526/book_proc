import cv2
import numpy as np


processors = []


def make_book_processor(process, is_multiple):
    def book_processor(book, *args, skips={}, should_skip=None, **options):
        pages = []
        for page in book.pages:
            is_skipping = (
                page.name in skips 
                or page.file_name in skips
                or (should_skip and should_skip(page))
            )

            if is_skipping:
                 processed = page
            else:
                processed = process(page, *args, **options)

            if is_multiple and not is_skipping:
                pages.extend(processed)
            else:
                pages.append(processed)
        
        book.pages = pages
        return book
    return book_processor


def registor_processor(process=None, is_multiple=False):
    if process:
        processors.append((process.__name__, process, make_book_processor(process, is_multiple)))
        return process

    def wrapper(process):
        processors.append((process.__name__, process, make_book_processor(process, is_multiple)))
        return process
    return wrapper


@registor_processor
def remove_border(page, top, down, left, right):
    height, width, *_ = page.image.shape
    down = height - down
    right = width - right
    page.image = page.image[top:down, left:right]
    return page


@registor_processor(is_multiple=True)
def split(page, n, edge_width=0):
    from book import Page

    _, width, *_ = page.image.shape

    try:
        edge_left_width, edge_right_width = edge_width
    except:
        edge_left_width, edge_right_width = edge_width, edge_width


    left_borders = [
        int(slice / n * width + (slice != 0) * edge_right_width / 2)
        for slice in range(n)
    ]
    right_borders = [
        int(slice / n * width - (slice != n) * edge_left_width / 2)
        for slice in range(1, n + 1)
    ]
    return [
        Page(
            page.image[:, left_border:right_border],
            '{}-split-{}'.format(page.name, n - slice),
            page.ext
        )
        for slice, (left_border, right_border)
        in enumerate(zip(left_borders, right_borders))
    ]


@registor_processor
def reverse_background(page, threshold=100):

    page.image = cv2.inRange(
        page.image,
        np.array([0, 0, 0], dtype="uint8"),
        np.array([threshold, threshold, threshold], dtype="uint8")
    )
    return page


@registor_processor
def resize(page, factor=0.75):

    height = int(factor * page.image.shape[0])
    width = int(factor * page.image.shape[1])

    page.image = cv2.resize(page.image, (width, height), interpolation=cv2.INTER_LANCZOS4)
    return page


@registor_processor
def blur(page, ksize=(9, 9), sigma=(1, 1)):

    page.image = cv2.GaussianBlur(page.image, ksize, *sigma)
    return page
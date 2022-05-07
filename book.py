import os
import shutil
import cv2
import numpy as np
from fpdf import FPDF
from PIL import Image

from processor import processors


class Page:
    def __init__(self, input=None, name=None, ext=None):
        try:
            name, ext =  os.path.split(input)[-1].rsplit('.', 1)
            self.image = cv2.imread(input)
        except:
            self.image = input

        self.name = name
        self.ext = ext

    @property
    def file_name(self):
        return '{}.{}'.format(self.name, self.ext)

    def save(self, output):
        cv2.imwrite(
            os.path.join(output, self.file_name),
            self.image
        )


class Book:

    def __init__(self, inputs=None, title=None):
        if isinstance(inputs, str) and os.path.isdir(inputs):
            _, title = os.path.split(inputs)
            inputs = [os.path.join(inputs, fn) for fn in os.listdir(inputs)]
        self.title = title
        self.inputs = inputs
        self._pages = None

    @property
    def pages(self):
        if self._pages is None:
            self._pages = [Page(fn) for fn in self.inputs]
        return self._pages

    @pages.setter
    def pages(self, pages):
        self._pages = pages

    @property
    def images(self):
        if self._pages is not None:
            return [
                Image.fromarray(page.image)
                for page in self._pages
            ]

        images = []
        for fn in self.inputs:
            try:
                image = Image.open(fn)
            except OSError as err:
                if err.args[0].startswith('cannot identify image file'):
                    print('The file below is not supported image type:')
                    print(fn)
                else:
                    raise err
            else:
                if image.mode == "RGBA":
                    rgb = Image.new('RGB', image.size, (255, 255, 255))
                    rgb.paste(image, mask=image.split()[3])
                    images.append(rgb)
                else:
                    images.append(image)

        return images

    def save(self, output, clear_output=True):
        if clear_output:
            shutil.rmtree(output, ignore_errors=True)
            os.makedirs(output)

        for page in self.pages:
            page.save(output)

    def to_pdf(self, output, title=None):
        title = title or self.title

        images = self.images
        images[0].save(
            os.path.join(output, f"{title}.pdf"),
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=images
        )
        return self


for name, process, book_process in processors:
    setattr(Page, name, process)
    setattr(Book, name, book_process)

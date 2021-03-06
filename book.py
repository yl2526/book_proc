import os
import shutil
import cv2
import numpy as np


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

    def remove_border(self, top, down, left, right, skip=False):
        if skip:
            return self

        height, width, *_ = self.image.shape
        down = height - down
        right = width - right
        self.image = self.image[top:down, left:right]
        return self

    def split(self, n, edge_width=0, skip=False):
        if skip:
            return [self]

        _, width, *_ = self.image.shape

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
                self.image[:, left_border:right_border],
                '{}-split-{}'.format(self.name, n - slice),
                self.ext
            )
            for slice, (left_border, right_border)
            in enumerate(zip(left_borders, right_borders))
        ]

    def reverse_background(self, threshold=100, skip=False):
        if skip:
            return self

        self.image = cv2.inRange(
            self.image,
            np.array([0, 0, 0], dtype="uint8"),
            np.array([threshold, threshold, threshold], dtype="uint8")
        )
        return self



class Book:

    def __init__(self, inputs=None):
        if isinstance(inputs, str) and os.path.isdir(inputs):
            inputs = [os.path.join(inputs, fn) for fn in os.listdir(inputs)]
        self.pages = [Page(fn) for fn in inputs]

    def save(self, output, clear_output=True):
        if clear_output:
            shutil.rmtree(output, ignore_errors=True)
            os.makedirs(output)

        for page in self.pages:
            page.save(output)

    @staticmethod
    def make_should_skip(skips):
        return lambda page: page.name in skips or page.file_name in skips

    def remove_border(self, top, down, left, right, skips={}, should_skip=None):
        should_skip = should_skip or self.make_should_skip(skips)

        self.pages = [
            page.remove_border(
                top, down, left, right,
                skip=should_skip(page)
            )
            for page in self.pages
        ]
        return self

    def split(self, n, edge_width=0, skips={}, should_skip=None):
        should_skip = should_skip or self.make_should_skip(skips)

        self.pages = np.hstack([
            page.split(n, edge_width, skip=should_skip(page))
            for page in self.pages
        ])
        return self

    def reverse_background(self, threshold=100, skips={}, should_skip=None):
        should_skip = should_skip or self.make_should_skip(skips)

        self.pages = [
            page.reverse_background(threshold=threshold, skip=should_skip(page))
            for page in self.pages
        ]
        return self

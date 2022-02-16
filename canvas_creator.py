import numpy as np
from PIL import Image
from filestack import Client


class Canvas:
    """
    This class creates canvas where we will draw
    our rectangles/squares
    """
    def __init__(self, height, width,  color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class FileSharer:

    def __init__(self, filepath, api_key="AexgcyGzxRBqrepeLcieQz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url

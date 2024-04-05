class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension
    def __str__(self) -> str:
        return f"{self.title}{self.extension}"    
    def resize(self, size = '50x50'):
        self.resolution = size

image1 = Image('100x100', 'image1', '.png')
print (image1.resolution, image1.title, image1.extension)
image1.resize()
print (image1.resolution)
print (image1)

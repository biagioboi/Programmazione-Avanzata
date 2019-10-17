class ImageProxy:
    def __init__(self, ImageClass, width=None, height=None, filename=None):
        assert (width is not None and height is not None) or \
        filename is not None
        self.Image = ImageClass
        self.commands = []
        if filename is not None:
            self.load(filename)
        else:
            self.commands = [(self.Image, width, height)]
            
    def load(self, filename):
        self.commands = [(self.Image, None, None, filename)]

    def save(self, filename=None):
        command = self.commands.pop(0)
        function, *args = command
        image = function(*args)

        for command in self.commands:
            function, *args = command
            function(image, *args)
        image.save(filename)
        return image
from media import *

class MediaGeométrica:
    def __init__(self, números):
        self.números = números

    def calcula(self):
        from math import prod
        mediaGeo = prod(self.números)**(1/len(self.números))
        return mediaGeo

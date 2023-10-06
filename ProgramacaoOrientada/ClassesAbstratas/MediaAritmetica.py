from media import *

class MediaAritmética(Media):
    def __init__(self,números):
        self.números = números

    def calcula(self):
        média = sum(self.números)/len(self.números)
        return média

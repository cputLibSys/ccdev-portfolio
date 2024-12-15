import os 
from django.templatetags.static import static

class FileSystem():

    def __init__(self, dirname='projects'):
        self.rootdir=dirname

    def getRoot(self):
        return  self.getFiles(self.rootdir)
    
    def getFiles(self, dirname):

        files=[[_file,(1 if os.path.isdir( os.path.join(os.path.dirname(os.path.realpath(__file__)),'static',dirname,_file)) else 0)] for _file in os.listdir( os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static', dirname))]
        return files




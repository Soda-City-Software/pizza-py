import glob
from importlib import import_module
from os.path import dirname, basename, isfile, join

class ModuleLoader:
    def __init__(self, file, namespaceGlobals):
        self.file = file
        self.globals = namespaceGlobals
        self.namespace = None
        self.all = []
        self.__loadDirectory()

    ##
    # returns array of module names 
    # found within the current module directory.
    def Modules(self):
        if len(self.all) <= 0:
            self.__loadModules()
        return self.all
    
    ##
    # loads classes from all of the current directory modules
    # set global variabes for the passed in file for the loaded classes
    # and returns an array of class names.
    # this only loads and sets classes where the class name is the same as the module name.
    def Classes(self):
        if len(self.all) <= 0:
            self.__loadClasses()
        return self.all

    ##
    # returns the app namespace for the current module directory.
    def getAppModuleNamespace(self):
        if self.namespace is None:
            index = self.directory.find('/app/')
            if index >= 0:
                self.namespace = self.directory[index+1::].replace('/','.')
        return self.namespace

    ##
    # set the member variables:
    #  directory, files, modules 
    def __loadDirectory(self):
        self.directory = dirname(self.file)
        self.files = glob.glob(join(self.directory, "*.py"))
        self.modules = [ basename(f)[:-3] for f in self.files if isfile(f) and not f.endswith('__init__.py')]

    ##
    # sets the values intended for the __all__ container 
    # with all module names found  within the current directory 
    def __loadModules(self):
        self.all = [ m for m in self.modules ]

    ##
    # sets the values intended for the __all__ container 
    # with all module-class names found  within the current directory 
    def __loadClasses(self):
        namespace = self.getAppModuleNamespace()
        for className in self.modules:
            namespaceModule = f"{namespace}.{className}"
            module = import_module(namespaceModule)
            
            middleware = getattr(module,className)

            self.globals[className] = middleware
            self.all.extend([className])

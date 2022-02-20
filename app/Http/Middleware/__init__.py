from foundation.ModuleLoader import ModuleLoader

loader = ModuleLoader(__file__, globals())

__all__ = loader.Classes()

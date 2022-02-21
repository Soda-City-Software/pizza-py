
config = {
    "env": 'dev'
}

def get(key,default=None):
    global config
    return config.get(key,default)

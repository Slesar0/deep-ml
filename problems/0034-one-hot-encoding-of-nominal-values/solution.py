import numpy as np

def to_categorical(x, n_col=None):
    if n_col==None:
        n_col = int(np.max(x))+1
    zer=np.zeros((len(x),n_col))
    ed=np.arange(len(x))
    zer[ed,x]=1
    return zer
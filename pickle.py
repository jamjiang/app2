__author__ = 'jamjiang'
import cPickle as P
# import pickle as P
shoplistfile = 'shoplist.data'
shoplist = ['apple' , 'mango' , 'carrot']
f = file(shoplistfile , 'w') # f is file handler
P.dump (shoplist , f)
f.close()
del shoplist
f = file ( shoplistfile)
storedlist = P.load(f)
print storedlist


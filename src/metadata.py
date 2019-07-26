# coding: utf-8
# In[1]:
# prepare search metadata class to employ during processing
import os
# In[2]:
import numpy as np
import pandas as pd

class MetaData:
	def __init__(self, path):
		self.meta=pd.read_csv(path, sep=',')
		self.meta.set_index('image', inplace=True)
	def search(self, image):
		return np.array(self.meta.loc[image].values)

# In[3]:
path = '/home/isic2019'
path = os.path.join(path,'ISIC_2019_Training_Metadata.csv')
meta = MetaData(path)

# In[11]:
# testing search metadata of a image
im = meta.search('ISIC_0025948')
print(im)

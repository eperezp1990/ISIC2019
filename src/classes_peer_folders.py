
# coding: utf-8
# In[33]:
# classify images and relocated in folders to process with keras later
import os
# In[34]:
path = '/home/isic2019'
labels = 'ISIC_2019_Training_GroundTruth.csv'
# where put the folder with the classes and images
folder = 'classes'
data = 'ISIC_2019_Training_Input'

# In[38]:
images = [(f,f[:f.rfind('.')]) for f in os.listdir(os.path.join(path,data)) if f.endswith('.jpg')]

# In[39]:
import pandas as pd
df = pd.read_csv(os.path.join(path,labels))
df.set_index('image',inplace=True)

# In[40]:
import numpy as np
import shutil
# unknow is empty, then you have to create the folder manually
# it is also necessary to put the index in front so that then keras when you read put them in order
for or_im,im in images:
	clas = df.columns[np.argmax(df.loc[im].values)]
	parent_path = os.path.join(path,folder,clas)
	if not os.path.exists(parent_path):
		os.makedirs(parent_path)
	shutil.move(os.path.join(path,data,or_im),os.path.join(path,folder,clas,or_im))

# In[14]:

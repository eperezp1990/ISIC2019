
# coding: utf-8

# In[3]:


! pip install imagehash
import os
import numpy as np
import imagehash
from PIL import Image

# In[4]:

# dir with others folders representing the labels and images
path = '/home/isic2019/ISIC2019_train'

# In[9]:
# (path, ID, label)
images = [(os.path.join(path, clas, im), im, clas) for clas in os.listdir(path)\
	 for im in os.listdir(os.path.join(path, clas))]
len(images)

# In[10]:
def getImageMetaData(file_path):
	with Image.open(file_path) as img:
		return imagehash.phash(img)
# In[17]:
duplicate = {}
for i in images:
	key = str(getImageMetaData(i[0]))
	if key not in duplicate:
		duplicate[key] = []
	duplicate[key].append((i[1],i[2]))
	if len(duplicate[key]) > 1:
		print(duplicate[key])

# In[20]:
count = 0 
for i in duplicate:
	if len(duplicate[i]) > 1:
		count+=1

# In[21]:
count
# In[22]:
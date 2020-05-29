#!/usr/bin/env python
# coding: utf-8

# In[ ]:


cf = open("change.txt","r")
n_epochs = cf.read()

n_epochs

type(n_epochs)

n_epochs = int(n_epochs)

n_epochs

n_epochs = n_epochs +2

n_epochs

with open("change.txt","w") as f:
    f.write("%d"%n_epochs)


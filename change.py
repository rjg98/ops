#!/usr/bin/env python
# coding: utf-8

# In[40]:


k=open("/prog/MlOp.py",'r')
a=k.readlines()
k.close()
count=open("/data/data/COUNT.txt",'r')
c=count.readlines()
count.close()
c


# In[41]:


if(c[0]=='1'):
    with open ("/prog/MlOp.py",'w') as k:
            for l in a:
                if l.strip("\n")!="l(32,count,size)":
                    k.write(l)
                if l.strip("\n")=="l(32,count,size)":
                    k.write(l.replace('l(32,count,size)','l(32,count,size)\nl(16,count,size)'))
elif(c[0]=='2'):
    with open ("/prog/MlOp.py",'w') as k:
            for l in a:
                if l.strip("\n")!="l(16,count,size)":
                    k.write(l)
                if l.strip("\n")=="l(16,count,size)":
                    k.write(l.replace('l(16,count,3)','l(16,count,3)\nl(8,count,3)'))
        


# In[42]:


print("model updated")


# In[ ]:





# In[ ]:





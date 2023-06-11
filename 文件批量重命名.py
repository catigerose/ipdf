#!/usr/bin/env python
# coding: utf-8

# In[103]:


from feed_funcs import get_soup
from bs4 import BeautifulSoup
import re
import os


# In[104]:


with open("1.html",encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')


# In[105]:


li_list = [x["title"] for x in soup.find_all("a")]
len(li_list)


# In[106]:


dict2 = {int(i.split("_")[0] ):i for i in li_list}


# In[108]:


dict2[1]


# In[125]:


path="./sgg"    

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)


# In[116]:


dict1 = {int(i.split("-")[0]):i for i in fileList }


# In[117]:


for i in range(1,142):
    print(dict1[i])
    #设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + dict1[i]# os.sep添加系统分隔符
    
    #设置新文件名
    newname=path + os.sep +dict2[i]+".mp4"
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    print(oldname,'======>',newname)



# In[114]:


for i in fileList:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + i # os.sep添加系统分隔符
    
    #设置新文件名
    newname=path + os.sep +i[1:]
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    #print(oldname,'======>',newname)


# In[126]:


for i in fileList:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+ os.sep + i # os.sep添加系统分隔符
    
    #设置新文件名
    newname=path + os.sep +i.replace("尚硅谷_","")
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    #print(oldname,'======>',newname)


# In[ ]:





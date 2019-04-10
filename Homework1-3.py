#!/usr/bin/env python
# coding: utf-8

# In[ ]:


分析資料:六都首長數位足跡
目標:韓國瑜近來為網路聲量相當高的政治人物，運用現有資料分析其高聲量是否得益於親中媒體的大量報導


# In[6]:


#讀取資料
import pandas as pd
list=['201808_data.csv','201809_data.csv','201810_data.csv','201811_data.csv','201812_data.csv','201901_data.csv']
notblue=[]
blue=[]
for i in list:
    df = pd.read_csv(i)
    df.fillna('零', inplace = True)
    df=df.drop(['Link','Type','created_time','Page_ID','WOW_COUNT','LOVE_COUNT','HAHA_COUNT','SAD_COUNT','Message','LIKE_COUNT','ANGRY_COUNT','Link Description'],axis=1)
    df_han=df[ df['Link_Title'].str.contains('韓國瑜') ]          #選取標題含有韓國瑜之新聞
    df_hanBL1=df_han[ df_han['Page_Name'].str.contains('中天') ]  #選取親藍媒體
    df_hanBL2=df_han[ df_han['Page_Name'].str.contains('中時') |df_han['Page_Name'].str.contains('China')]
    df_hanBL3=df_han[ df_han['Page_Name'].str.contains('中視') ]
    df_hanBL4=df_han[ df_han['Page_Name'].str.contains('TVBS') ]
    df_hanBL5=df_han[ df_han['Page_Name'].str.contains('聯合') ]
    df_hanBL6=df_han[ df_han['Page_Name'].str.contains('東森') ]
    df_hanGR1=df_han[ df_han['Page_Name'].str.contains('自由時報') ] #選取親綠媒體
    df_hanGR2=df_han[ df_han['Page_Name'].str.contains('民視') ]
    df_hanGR3=df_han[ df_han['Page_Name'].str.contains('三立') ]
    df_hanNO1=df_han[ df_han['Page_Name'].str.contains('公視新聞') ] #選取較為客觀中立之媒體
    df_hanNO2=df_han[ df_han['Page_Name'].str.contains('蘋果日報') ]
    
    
    bluestats=df_hanBL1.shape[0]+df_hanBL2.shape[0]+df_hanBL3.shape[0]+df_hanBL4.shape[0]+df_hanBL5.shape[0]+df_hanBL6.shape[0]
    nonbluestats=df_hanGR1.shape[0]+df_hanGR2.shape[0]+df_hanGR3.shape[0]+df_hanNO1.shape[0]+df_hanNO2.shape[0]
    blue.append(bluestats)
    notblue.append(nonbluestats)
    
    
    from matplotlib.font_manager import FontProperties
    import matplotlib.pyplot as plt

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(6,10))
    labels = '中天','中時','中視','TVBS','聯合','東森','自由時報','民視','三立','公視新聞','蘋果日報'
    size = [df_hanBL1.shape[0],df_hanBL2.shape[0],df_hanBL3.shape[0],df_hanBL4.shape[0],df_hanBL5.shape[0],df_hanBL6.shape[0],df_hanGR1.shape[0],df_hanGR2.shape[0],df_hanGR3.shape[0],df_hanNO1.shape[0],df_hanNO2.shape[0],]
    plt.pie(size , labels = labels,autopct='%1.1f%%',textprops = {'fontsize':10, 'color':'k'},
            colors = ['red','yellowgreen','lightskyblue','b','r','c','m','g','y','k','w'])
    plt.axis('equal')
    plt.title(i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+'媒體報導韓國瑜之比例')
    plt.show()

    


# In[ ]:


由各月份統計表可看出親藍媒體比起親綠以及中立媒體，報導韓國瑜新聞的量高出許多。


# In[5]:


ratio=[]
for i in range (0,6):
    a=blue[i]/ ( blue[i]+notblue[i]  )
    ratio.append( a )
ratio
x=['201808','201809','201810','201811','201812','201901']
y=[ratio[0],ratio[1],ratio[2],ratio[3],ratio[4],ratio[5]]
plt.plot(x,y)
plt.title("親中媒體報導韓國瑜數量佔韓國瑜總報導量之比例")
plt.xlabel('月份')
plt.ylabel('比例')


# In[ ]:


根據折線圖可看出，親中媒體報導韓國瑜的比例最高達到近八成，最低也有六成，可知韓國瑜的高網路聲量至少有一定程度來自於親中媒體的支持所獲得。


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[55]:


pip install arabic-reshaper python-bidi


# In[56]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display


# In[57]:


data = pd.read_csv(r"C:\Users\Najla\Downloads\Riyadh_RealEstate.csv")


# In[58]:


data.head


# In[60]:


print(data.columns)


# In[61]:


# حساب تكرار كل قيمة في العمود
value_counts = data['الحي'].value_counts()

# عرض القيم الأكثر تكرارًا
print(value_counts.head())  # هذا سيظهر أعلى 5 قيم متكررة


# In[62]:


print(data.head())


# In[64]:


# حساب تكرار كل قيمة في العمود 'الحي'
value_counts = data['الحي'].value_counts()

# عرض القيم الأكثر تكرارًا
top_values = value_counts.head()  # هذا سيظهر أعلى 5 قيم متكررة
print(top_values)


# In[89]:


import matplotlib.pyplot as plt

# تحليل توزيع نوع العقار
property_type_counts = data['نوع العقار'].value_counts()
plt.figure(figsize=(8, 6))
property_type_counts.plot(kind='bar')
plt.title('توزيع نوع العقار')
plt.xlabel('نوع العقار')
plt.ylabel('العدد')
plt.show()


# In[90]:


# تحليل توزيع الغرض
purpose_counts = data['الغرض'].value_counts()
plt.figure(figsize=(8, 6))
purpose_counts.plot(kind='bar')
plt.title('توزيع الغرض')
plt.xlabel('الغرض')
plt.ylabel('العدد')
plt.show()


# In[91]:


# تحليل توزيع المدينة
city_counts = data['المدينة'].value_counts()
plt.figure(figsize=(8, 6))
city_counts.plot(kind='bar')
plt.title('توزيع المدينة')
plt.xlabel('المدينة')
plt.ylabel('العدد')
plt.show()

# تحليل توزيع الحي
neighborhood_counts = data['الحي'].value_counts()
plt.figure(figsize=(8, 6))
neighborhood_counts.head(10).plot(kind='bar')  # عرض أكثر 10 أحياء شيوعًا
plt.title('توزيع الأحياء')
plt.xlabel('الحي')
plt.ylabel('العدد')
plt.show()


# In[71]:


import matplotlib.pyplot as plt
import seaborn as sns
import arabic_reshaper
from bidi.algorithm import get_display

# تمثيل القيم الأكثر تكرارًا بصريًا
sns.barplot(x=top_values.index, y=top_values.values)
plt.xlabel('الحي')
plt.ylabel('عدد التكرارات')
plt.title('أكثر الأحياء تكرارًا في العمود "الحي"')
plt.xticks(rotation=45)  # تدوير الأسماء لتكون أكثر وضوحًا
plt.show()


# In[92]:


# تحليل توزيع المدينة
city_counts = data['المدينة'].value_counts()
plt.figure(figsize=(8, 6))
city_counts.plot(kind='bar')
plt.title('توزيع المدينة')
plt.xlabel('المدينة')
plt.ylabel('العدد')
plt.show()

# تحليل توزيع الحي
neighborhood_counts = data['الحي'].value_counts()
plt.figure(figsize=(8, 6))
neighborhood_counts.head(10).plot(kind='bar')  # عرض أكثر 10 أحياء شيوعًا
plt.title('توزيع الأحياء')
plt.xlabel('الحي')
plt.ylabel('العدد')
plt.show()


# In[72]:


# تحديد الأحياء الخمسة الأكثر تكرارًا
top_neighborhoods = data['الحي'].value_counts().head(5).index


# In[93]:


# تحليل توزيع الواجهة
front_counts = data['الواجهة'].value_counts()
plt.figure(figsize=(8, 6))
front_counts.plot(kind='bar')
plt.title('توزيع الواجهات')
plt.xlabel('الواجهة')
plt.ylabel('العدد')
plt.show()


# In[75]:


import matplotlib.pyplot as plt
import seaborn as sns

# رسم مخطط شريطي لمقارنة متوسط سعر المتر بين الأحياء الخمسة
sns.barplot(x=average_price_per_neighborhood.index, y=average_price_per_neighborhood.values)
plt.xlabel('الحي')
plt.ylabel('متوسط السعر الاجمالي')
plt.title('مقارنة متوسط سعر المتر بين الأحياء الأكثر تكرارًا')
plt.xticks(rotation=45)
plt.show()



# In[81]:


# تحليل توزيع أنواع العقارات
print(data['نوع العقار'].value_counts())

# تحليل توزيع الأحياء
print(data['الحي'].value_counts())

# تحليل توزيع الأسعار
print(data['السعر الاجمالي'].describe())


# In[82]:


# مثال: تحليل العلاقة بين المساحة والسعر
# تحويل المساحة من نص إلى رقم
data['المساحة'] = pd.to_numeric(data['المساحة'], errors='coerce')

# حساب معامل الارتباط
print(data[['المساحة', 'السعر الاجمالي']].corr())


# In[84]:


# تحليل القيم المفقودة
print(data.isnull().sum())


# In[85]:


import matplotlib.pyplot as plt
import seaborn as sns

# مثال: رسم بياني لتوزيع الأسعار
plt.figure(figsize=(10, 6))
sns.histplot(data['السعر الاجمالي'], bins=50)
plt.title('توزيع الأسعار')
plt.xlabel('السعر الاجمالي')
plt.ylabel('العدد')
plt.show()


# In[86]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# تحويل بعض الأعمدة إلى عددية إذا كانت نصية
data['المساحة'] = pd.to_numeric(data['المساحة'], errors='coerce')
data['سعر المتر'] = pd.to_numeric(data['سعر المتر'], errors='coerce')

# تحليل توزيع المساحة
plt.figure(figsize=(10, 6))
sns.histplot(data['المساحة'].dropna(), bins=50, kde=True)
plt.title('توزيع المساحة')
plt.xlabel('المساحة')
plt.ylabel('العدد')
plt.show()

# تحليل توزيع سعر المتر
plt.figure(figsize=(10, 6))
sns.histplot(data['سعر المتر'].dropna(), bins=50, kde=True)
plt.title('توزيع سعر المتر')
plt.xlabel('سعر المتر')
plt.ylabel('العدد')
plt.show()


# In[87]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='المساحة', y='السعر الاجمالي', data=data)
plt.title('العلاقة بين المساحة والسعر الإجمالي')
plt.xlabel('المساحة')
plt.ylabel('السعر الإجمالي')
plt.show()


# In[88]:


# تحليل القيم المفقودة
missing_values = data.isnull().sum()
missing_values_percentage = (missing_values / len(data)) * 100
print(missing_values_percentage)


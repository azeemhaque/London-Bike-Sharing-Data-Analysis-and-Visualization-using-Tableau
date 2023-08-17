#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install kaggle')


# In[54]:


import pandas as pd


# In[55]:


bikes = pd.read_csv("D:\London Bike Sharing Project\LondonBikeRides-main\LondonBikeRides-main\london-bike-sharing-dataset\london_merged.csv")


# In[56]:


#explore the data
bikes.info()


# In[57]:


#displaying only the first 4 rows of dataframe
bikes.head()


# In[58]:


bikes.shape


# In[59]:


bikes


# In[60]:


#count the unique values in the weather_codes column
bikes.weather_code.value_counts()


# In[61]:


#count the unique values in the season column
bikes.season.value_counts()


# In[62]:


#specifying the column names I want to use
new_col_dic={'timestamp':'time',
            'cnt':'count',
            't1':'temp_real_C',
            't2':'temp_feels_like_C',
            'hum':'humidity_percent',
            'wind_speed':'wind_speed_kph',
            'weather_code':'weather',
            'is_holiday':'is_holiday',
            'is_weekend':'is_weekend',
            'season':'season'
}
#Renaming the columns to the specified column names
bikes.rename(new_col_dic,axis=1,inplace='true')


# In[63]:


#changing the humidity values to percentage
bikes.humidity_percent = bikes.humidity_percent/100


# In[64]:


#creating a season dictionary so that we can map the integer values 0-3 to the actual written values
season_dic={
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}

#creating a weather dictionary so that we can map the integer values to the actual written values
weather_dic={
    '1.0':'Clear',
    '2.0':'Scattered Clouds',
    '3.0':'Broken Clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
    
}

#changing season column datatype to string(str)
bikes.season = bikes.season.astype('str')
#mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dic)

#changing weather column datatype to string(str)
bikes.weather = bikes.weather.astype('str')
#mapping the values to the actual written weathers
bikes.weather = bikes.weather.map(weather_dic)


# In[65]:


bikes.head()


# In[ ]:


#bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')


#!/usr/bin/env python
# coding: utf-8

# # Project: Pima Indians Diabetes Medical Records - Using Data Analysis and Visual Tools to Predict Diabetes
# 
# ## BIOF 309
# 
# ## Anuj Kashyap
# 
# 
# 
# #### What is our project question? 
# Are we able to determine which factors affect diabetes in Pima Indians population?
# 
# #### Context
# Where did the data come from? 
# National Institute of Diabetes and Digestive and Kidney Diseases. 
# 
# #### Diabetes information:
# 
# What is diabetes?: If body does not produce or properly use insulin, it is released out through urination. This is called diabetes.
# 
# #### How many Americans have diabetes?
# 20.8 million children and adults (7% of population)
# (American Diabetes Association, 2007)
# 
# #### Pima Indian Diabetes (PID) dataset contains what?
# 768 records describing female patients of Pima Indian heritage which are 21 years old living in Phoenix, Arizona, USA (UCI-Machine-Learning Repository, 2007)
# 
# #### What do we want to do with this dataset?
# To diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements  
# 
# #### What are some contraints with working with this dataset? 
# Several constraints were placed on the selection of these instances from a larger database. 
# All patients here are females at least 21 years old of Pima Indian heritage.
# 
# #### What medical predictors are included in this dataset? 
# Several medical predictor variables such as the number of pregnancies the patient has had, their BMI, insulin level, age, etc.
# 
# #### Is there a target variable?
# Yes, one target variable, Outcome. 
# 
# #### Reference:
# kaggle datasets download -d uciml/pima-indians-diabetes-database
# https://www.kaggle.com/uciml/pima-indians-diabetes-database/downloads/pima-indians-diabetes-database.zip/1
# 
# Acknowledgements
# Smith, J.W., Everhart, J.E., Dickson, W.C., Knowler, W.C., & Johannes, R.S. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus. In Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261--265). IEEE Computer Society Press.
# 
# #### Inspiration:
# Can you build a machine learning model to accurately predict whether or not the patients in the dataset have diabetes or not?

# In[1]:


import pandas as pd


# ## Read input data
# Read the input CSV file as a pandas dataframe

# In[9]:


filename = "Desktop\diabetes.csv"

df = pd.read_csv(filename, sep=',', encoding='utf-8', header=0)


# In[72]:


# Assigning column names and mapping the meta information for each attribute
cols = df.columns = ['n_pregnant', 'glu_conc', 'bp', 'tst', 'insulin', 'bmi', 'dpf', 'age', 'diabetes?']
metainfo = {'n_pregnant': 'Number of times pregnant',
                     'glu_conc': 'Plasma glucose concentration a 2 hours in an oral glucose tolerance test',
                     'bp': 'Diastolic blood pressure (mm Hg)',
                     'tst': 'Triceps skin fold thickness (mm)',
                     'insulin': '2-Hour serum insulin (mu U/ml)',
                     'bmi': 'Body mass index (weight in kg/(height in m)^2)',
                     'dpf': 'Diabetes pedigree function',
                     'age': 'Age (years)',
                     'diabetes?': 'Class variable (0 or 1)'}

df.head()


# In[71]:


# Describe the dataset
df_temp = df.drop(labels = 'diabetes?', axis=1)
df_temp.describe()


# In[62]:


import numpy as np
import matplotlib.pyplot as plt
def bar_plot(df):
    plt.rcParams['figure.figsize'] = 12, 6
    df_0 = df[df['diabetes?'] == 0]
    df_1 = df[df['diabetes?'] == 1]
    mean_0 = df_0.mean()
    mean_1 = df_1.mean()
    list_0 = []
    list_1 = []
    for col in df.columns:
        list_0.append(mean_0[col])
        list_1.append(mean_1[col])

    index = np.arange(len(df.columns))
    bar_width = 0.35
    opacity = 0.8

    plt.bar(index, list_0, bar_width,
            alpha=opacity,
            color='b',
            label='Diabetes (-ve)')

    plt.bar(index + bar_width, list_1, bar_width,
            alpha=opacity,
            color='g',
            label='Diabebtes (+ve)')

    plt.title('Pima Indians Diabetes Dataset')
    plt.xticks(index + bar_width, tuple(df.columns))
    plt.legend()

    plt.tight_layout()
    plt.show()


# In[63]:


bar_plot(df)


# In[ ]:


#What did we find from the bar plot analysis? We can analyze that insulin and glucose concentrations (glu_conc) are significantly higher in women whose diabetes test is diagnosed positive. 
#One should consider that other attributes might be impacting the diabetes significantly 
#From our bar graph plot, we didn't find any significant difference in the other attributes.


# In[64]:


def box_plot(df, cols):
    plt.rcParams['figure.figsize'] = 12, 6
    data = np.array(df.values.tolist())
    plt.boxplot(data, labels=cols, showmeans=True)
    plt.show()


# In[65]:


box_plot(df, df.columns)


# #Normalize our data using pandas in a very simple and intuitive way i.e.  (x-mean)/(max-min)

# In[83]:


def normalize(df):
    df_norm = (df - df.mean()) / (df.max() - df.min())
    return df_norm
from pandas.plotting import scatter_matrix as pplotsm
def scatter_matrix(df):
    plt.rcParams["figure.figsize"] = (14, 14)
    colors = list('r' if i >= 0.5 else 'b' for i in df['diabetes?'])
    pplotsm(df, color=colors)
    plt.show()


# In[84]:


normalized_df.head()


# In[85]:


normalized_df = normalize(df)
scatter_matrix(normalized_df)


# In[ ]:


#visualize the bivariate relationship between each variable using a scatter plot. 
#normalized data for plotting the scattered matrix was used
#Both are overlapping with each other


# In[66]:


box_plot(normalized_df, df.columns)


# In[67]:


def stacked_histogram(df, cols):
    fig, axes = plt.subplots(3, 3, sharey=True) # Because I have 9 variables in the dataset
    plt.rcParams['figure.figsize'] = 14, 14
    df_1 = df[df['diabetes?'] == 1]
    df_2 = df[df['diabetes?'] == 0]
    col_index = 0
    for row in axes:
        for col in row:
            col.hist([df_2[cols[col_index]], df_1[cols[col_index]]], bins=10, stacked=True, color=['b', 'g'])
            col.set_ylabel(cols[col_index])
            col_index += 1
    plt.show()


# In[68]:


stacked_histogram(df, df.columns)


# In[ ]:


#Green bars shows the women with positive diabetes test and blue bars shows the women with negative diabetes test.
#In glu_conc we see that diabetes are diagnosed to those women having high glucose concentration levels. 
#Similarly, bp (blood pressure diastolic) histogram shows that positive diabetes was found in women with high bp. 
#Although there were samples where high bp women had a negative test but positive diabetes was found only with high bp. 
#Insulin histogram shows that women with lower insulin levels have a positive diabetes test.


# In[ ]:


####Future Directions
#Try other data analysis and visual tools to look at data in a different way


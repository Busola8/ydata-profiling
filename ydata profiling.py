# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:08:41 2023

@author: busola
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from ydata_profiling import ProfileReport

dataset = pd.read_csv("EDUCATION_ATTAINMENT.csv")
# dataset.info()
# dataset.head()
# dataset.tail()
# dataset.isnull().sum()
dataset.describe()
profile = ProfileReport(dataset,title = 'education attainment')
profile.to_notebook_iframe()
# profile.to_file("Education Attainment.html")

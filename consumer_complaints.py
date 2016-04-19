#Matthew O'Neill
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
%matplotlib inline


c_c = pd.read_csv('complaints_dec_2014.csv')

c_c.Product.value_counts().plot(title='Product Types', kind = 'barh')

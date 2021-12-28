import pandas as pd
import numpy as np
import random
import requests

file_path = "Canadasalesdata.csv"

original_data = pd.read_csv(file_path)

df = original_data.copy()

#
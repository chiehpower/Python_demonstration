"""
Reference from : https://towardsdatascience.com/learning-to-use-progress-bars-in-python-2dc436de81e5
"""

import time, numpy as np
from tqdm import tqdm
test_list = np.arange(100)
for i in tqdm(test_list):
    time.sleep(0.1)
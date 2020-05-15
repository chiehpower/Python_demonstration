"""
Reference from : https://towardsdatascience.com/learning-to-use-progress-bars-in-python-2dc436de81e5
"""

from alive_progress import alive_bar
import time, numpy as np
from alive_progress import config_handler, show_bars, show_spinners

config_handler.set_global(spinner='fish2')

test_list = np.arange(100)
with alive_bar(len(test_list),bar='filling') as bar:
    for i in test_list:
        bar()
        time.sleep(0.1)
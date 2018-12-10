#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7/17:12
# @Author  : SnrsGu
# @Email   : SnrsGu@qq.com & SnrsGu@gmail.com
# @File    : test.py
# @Software: PyCharm

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(10,90,(4,4)))
print(df.drop(1))
# 准备数据 , code from detailed_workflow.ipynb  


import sys
import os

# 添加qlib模块的路径到sys.path
# qlib_path = os.path.join(os.path.dirname(__file__), '..', 'qlib/qlib')
# sys.path.insert(0, os.path.abspath(qlib_path))

import qlib
# region in [REG_CN, REG_US]
from qlib.constant import REG_CN
from qlib.data import D
from qlib.data.dataset.handler import DataHandler

from qlib.contrib.data.handler import Alpha158

provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir
qlib.init(provider_uri=provider_uri, region=REG_CN)


market = D.instruments(market='csi300')


data_handler_config = {
  "start_time": "2022-01-01",
  "end_time": "2025-12-31",
  "fit_start_time": "2022-01-01",
  "fit_end_time": "2025-01-01",
  "instruments":market,
}

h = Alpha158(**data_handler_config)

# print(h.get_cols())
f_l = h.fetch(data_key=DataHandler.DK_L)
f_l.to_csv("alpha158.csv")

# print(h.fetch(col_set = "feature", data_key=DataHandler.DK_L))
# print(h.fetch(col_set = "feature", data_key=DataHandler.DK_L))

# print(h.fetch(col_set = "label", data_key=DataHandler.DK_L))
# print(h.fetch(col_set = "label", data_key=DataHandler.DK_I))






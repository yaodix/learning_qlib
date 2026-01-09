
import sys
import os

# 添加qlib模块的路径到sys.path
# qlib_path = os.path.join(os.path.dirname(__file__), '..', 'qlib/qlib')
# sys.path.insert(0, os.path.abspath(qlib_path))

import qlib
# region in [REG_CN, REG_US]
from qlib.constant import REG_CN
from qlib.data import D

provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir
qlib.init(provider_uri=provider_uri, region=REG_CN)

res = D.calendar(start_time='2010-01-01', end_time='2017-12-31', freq='day')
print(res)

market = D.instruments(market='all')

print(market)

mlist = D.list_instruments(instruments=market,as_list='list')

# 打印fields

# exit(0)

from qlib.contrib.data.handler import Alpha158

data_handler_config = {
  "start_time": "2010-01-01",
  "end_time": "2017-12-31",
  "fit_start_time": "2010-01-01",
  "fit_end_time": "2017-12-31",
  "instruments":mlist,
}

h = Alpha158(**data_handler_config)

print(h.get_cols())




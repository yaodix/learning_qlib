
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

print(len(mlist))
print(mlist[:10])

instruments = ['sz000001']
fields = ['$close', '$volume', 'Ref($close, 1)', 'Mean($close, 3)', '$high-$low']
re = D.features(instruments, fields, start_time='2020-01-01', end_time='2025-12-31', freq='day')
# D.features(instruments, fields, start_time='2010-01-01', end_time='2017-12-31', freq='day')
print(re)
print(re.head().to_string())

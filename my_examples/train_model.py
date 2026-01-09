### from huatai ai 40

import time
import qlib
from qlib.constant import REG_CN
from qlib.contrib.model.gbdt import LGBModel

from qlib.contrib.data.handler import Alpha158
from qlib.utils import init_instance_by_config, flatten_dict
from qlib.workflow import R
from qlib.workflow.record_temp import SignalRecord, PortAnaRecord


provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir
qlib.init(provider_uri=provider_uri, region=REG_CN)

market = "csi300"
BENCHMARK = "SH000300"

data_handler_config = {
    "start_time": "2008-01-01",  # all time
    "end_time": "2025-11-01",
    "fit_start_time": "2008-01-01", # train timegap 
    "fit_end_time": "2020-12-31",
    "instruments": market,
}

task = {
    "model": {
        "class": "LGBModel",
        "module_path": "qlib.contrib.model.gbdt",
        "kwargs": {
            "loss": "mse",
            "colsample_bytree": 0.8879,
            "learning_rate": 0.0421,
            "subsample": 0.8789,
            "lambda_l1": 205.6999,
            "lambda_l2": 580.9768,
            "max_depth": 8,
            "num_leaves": 210,
            "num_threads": 20,
        },
    },
    "dataset": {
        "class": "DatasetH",
        "module_path": "qlib.data.dataset",
        "kwargs": {
            "handler": {
                "class": "Alpha158",
                "module_path": "qlib.contrib.data.handler",
                "kwargs": data_handler_config,
            },
            "segments": {
                "train": ("2008-01-01", "2020-12-31"),
                "valid": ("2021-01-01", "2023-12-31"),
                "test": ("2024-01-01", "2025-11-01"),
            },
        },
    },
}
import pprint
# model initialization
model = init_instance_by_config(task["model"])
dataset = init_instance_by_config(task["dataset"])
###################################
# prediction, backtest & analysis
###################################
port_analysis_config = {
    "executor": {
        "class": "SimulatorExecutor",
        "module_path": "qlib.backtest.executor",
        "kwargs": {
            "time_per_step": "day",
            "generate_portfolio_metrics": True,
        },
    },
    "strategy": {
        "class": "TopkDropoutStrategy",
        "module_path": "qlib.contrib.strategy.signal_strategy",
        "kwargs": {
            "signal": "<PRED>",
            "topk": 50,
            "n_drop": 5,
        },
    },
    "backtest": {
        "start_time": "2024-01-01",
        "end_time": "2025-11-01",
        "account": 100000000,
        "benchmark": BENCHMARK,
        "exchange_kwargs": {
            "freq": "day",
            "limit_threshold": 0.095,
            "deal_price": "close",
            "open_cost": 0.0005,
            "close_cost": 0.0015,
            "min_cost": 5,
        },
    },
}
# start exp
with R.start(experiment_name="lgbm_train2008"):
    # train
    R.log_params(**flatten_dict(task))
    model.fit(dataset)
    R.save_objects(trained_model = model)
    recorder_id = R.get_recorder().id
    print(f"recorder_id {recorder_id}")
    
    # print(f"R.list_recorders() {R.list_recorders()}")
    # print(f"R.list_experiments() {R.list_experiments()}")    

    # prediction
    recorder = R.get_recorder()
    sr = SignalRecord(model, dataset, recorder)
    sr.generate()
    
    #  portfolio-based analysis: backtest
    par = PortAnaRecord(recorder, port_analysis_config, "day")
    par.generate()
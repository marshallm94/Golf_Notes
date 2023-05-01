import os

import pandas as pd
import numpy as np
import tidypolars as tp

yardages = pd.read_csv('../data/yardages.csv')
yardages = tp.from_pandas(yardages)

os.environ['POLARS_FMT_MAX_ROWS'] = '-1'

(
    yardages
    .summarize(Avg_Yardage = tp.mean("Yardage"),
               Std_Yardage = tp.sd("Yardage"),
               by=["Club","Wrist_Hinge","Swing_Degree"])
    .select('Avg_Yardage','Club','Wrist_Hinge','Swing_Degree')
    .arrange("Avg_Yardage")
)

# NOTE( 2023-04-23 ): lets wait to incorporate these stats
    # .mutate(
    #     Lower_Bound = tp.col('Avg_Yardage') - tp.col('Std_Yardage'),
    #     Upper_Bound = tp.col('Avg_Yardage') + tp.col('Std_Yardage'),
    # )



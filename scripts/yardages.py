import pandas as pd
import numpy as np
import tidypolars as tp

yardages = pd.read_csv('../data/yardages.csv')
yardages = tp.from_pandas(yardages)

(
    yardages
    .summarize(Avg_Yardage = tp.mean("Yardage"),
               Std_Yardage = tp.sd("Yardage"),
               by=["Club","Swing_Type"])
    .select('Avg_Yardage','Club','Swing_Type')
    .arrange("Avg_Yardage")
)

# NOTE( 2023-04-23 ): lets wait to incorporate these stats
    # .mutate(
    #     Lower_Bound = tp.col('Avg_Yardage') - tp.col('Std_Yardage'),
    #     Upper_Bound = tp.col('Avg_Yardage') + tp.col('Std_Yardage'),
    # )



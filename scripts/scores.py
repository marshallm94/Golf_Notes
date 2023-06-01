import os

import pandas as pd
import numpy as np
import tidypolars as tp
from plotnine import *

scores = pd.read_csv('../data/scores.csv')
# scores = tp.from_pandas(scores)

np.quantile(scores['Score'], np.arange(0, 1.1,0.1))
pd.DataFrame({
    'Quantile': np.arange(0, 1.1,0.1),
    'Score': np.quantile(scores.loc[scores['Yards'] == 3100, 'Score'], np.arange(0, 1.1,0.1))
    })
pd.DataFrame({
    'Quantile': np.arange(0, 1.1,0.1),
    'Score': np.quantile(scores.loc[scores['Yards'] == 3300, 'Score'], np.arange(0, 1.1,0.1))
    })

(
    ggplot(scores, aes(x='Date', y='Score', color='Yards')) +
    geom_point()
)


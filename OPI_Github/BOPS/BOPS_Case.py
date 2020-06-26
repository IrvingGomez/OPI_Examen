import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

# To manage databases with SQL and Python
import sqlite3

# We read the data of the B&M Sales
dat_bm = pd.read_csv (r'bops_bm_bis.csv')

# I want to select just those of USA and before the BOPS inciative
dat_usa_before = dat_bm.loc[(dat_bm['usa'] == 1) &
    (dat_bm['after'] == 0) & (dat_bm['week'] > 17)]

avg_sales_usa_before = dat_usa_before.groupby('week', as_index=False)[' sales '].mean()
avg_sales_usa_before['year'] = [2011]*25
avg_sales_usa_before['week_yr'] = pd.to_datetime(avg_sales_usa_before['year'].astype(str) + ' ' +
                                avg_sales_usa_before['week'].astype(str) + ' 1',
                                format='%Y %U %w')

AVG_BM_before = avg_sales_usa_before.plot(x='week_yr', y=' sales ')
fig_BM_before = AVG_BM_before.get_figure()
fig_BM_before.savefig("AVG_BM_before.png")

# Datos de USA despues de la introducción de BOPS
dat_usa_after = dat_bm.loc[(dat_bm['usa'] == 1) & (dat_bm['after'] == 1) &
    (dat_bm['week'] != 16) & (dat_bm['week'] != 15)]

avg_sales_usa_after = dat_usa_after.groupby('week', as_index=False)[' sales '].mean()
avg_sales_usa_after['year'] = [2012]*14+[2011]*11
avg_sales_usa_after['week_yr'] = pd.to_datetime(avg_sales_usa_after['year'].astype(str) + ' ' +
                                avg_sales_usa_after['week'].astype(str) + ' 1',
                                format='%Y %U %w')

AVG_BM_after = avg_sales_usa_after.plot(x='week_yr', y=' sales ')
fig_BM_after = AVG_BM_after.get_figure()
fig_BM_after.savefig("AVG_BM_after.png")

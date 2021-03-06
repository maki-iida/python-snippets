import pandas as pd

df = pd.DataFrame({'value': range(1, 32, 2)},
                  index=pd.date_range('2018-08-01', '2018-08-31', freq='2D'))

print(df)
#             value
# 2018-08-01      1
# 2018-08-03      3
# 2018-08-05      5
# 2018-08-07      7
# 2018-08-09      9
# 2018-08-11     11
# 2018-08-13     13
# 2018-08-15     15
# 2018-08-17     17
# 2018-08-19     19
# 2018-08-21     21
# 2018-08-23     23
# 2018-08-25     25
# 2018-08-27     27
# 2018-08-29     29
# 2018-08-31     31

print(df.asfreq('10D'))
#             value
# 2018-08-01      1
# 2018-08-11     11
# 2018-08-21     21
# 2018-08-31     31

print(df.asfreq('5D'))
#             value
# 2018-08-01    1.0
# 2018-08-06    NaN
# 2018-08-11   11.0
# 2018-08-16    NaN
# 2018-08-21   21.0
# 2018-08-26    NaN
# 2018-08-31   31.0

print(df.asfreq('W'))
#             value
# 2018-08-05    5.0
# 2018-08-12    NaN
# 2018-08-19   19.0
# 2018-08-26    NaN

print(df.asfreq('W-WED'))
#             value
# 2018-08-01    1.0
# 2018-08-08    NaN
# 2018-08-15   15.0
# 2018-08-22    NaN
# 2018-08-29   29.0

print(df.asfreq('W', fill_value=0))
#             value
# 2018-08-05      5
# 2018-08-12      0
# 2018-08-19     19
# 2018-08-26      0

print(df.asfreq('W', method='pad'))
#             value
# 2018-08-05      5
# 2018-08-12     11
# 2018-08-19     19
# 2018-08-26     25

print(df.asfreq('W', method='ffill'))
#             value
# 2018-08-05      5
# 2018-08-12     11
# 2018-08-19     19
# 2018-08-26     25

print(df.asfreq('W', method='backfill'))
#             value
# 2018-08-05      5
# 2018-08-12     13
# 2018-08-19     19
# 2018-08-26     27

print(df.asfreq('W', method='bfill'))
#             value
# 2018-08-05      5
# 2018-08-12     13
# 2018-08-19     19
# 2018-08-26     27

df_3D = pd.DataFrame({'value': range(1, 32, 3)},
                     index=pd.date_range('2018-08-01', '2018-08-31', freq='3D'))

print(df_3D.asfreq('D', method='bfill'))
#             value
# 2018-08-01      1
# 2018-08-02      4
# 2018-08-03      4
# 2018-08-04      4
# 2018-08-05      7
# 2018-08-06      7
# 2018-08-07      7
# 2018-08-08     10
# 2018-08-09     10
# 2018-08-10     10
# 2018-08-11     13
# 2018-08-12     13
# 2018-08-13     13
# 2018-08-14     16
# 2018-08-15     16
# 2018-08-16     16
# 2018-08-17     19
# 2018-08-18     19
# 2018-08-19     19
# 2018-08-20     22
# 2018-08-21     22
# 2018-08-22     22
# 2018-08-23     25
# 2018-08-24     25
# 2018-08-25     25
# 2018-08-26     28
# 2018-08-27     28
# 2018-08-28     28
# 2018-08-29     31
# 2018-08-30     31
# 2018-08-31     31

df_h = pd.DataFrame({'value': range(9)},
                    index=pd.date_range('2018-08-01', '2018-08-05', freq='12H'))
print(df_h)
#                      value
# 2018-08-01 00:00:00      0
# 2018-08-01 12:00:00      1
# 2018-08-02 00:00:00      2
# 2018-08-02 12:00:00      3
# 2018-08-03 00:00:00      4
# 2018-08-03 12:00:00      5
# 2018-08-04 00:00:00      6
# 2018-08-04 12:00:00      7
# 2018-08-05 00:00:00      8

print(df_h.asfreq('D'))
#             value
# 2018-08-01      0
# 2018-08-02      2
# 2018-08-03      4
# 2018-08-04      6
# 2018-08-05      8

print(df_h.resample('D').mean())
#             value
# 2018-08-01    0.5
# 2018-08-02    2.5
# 2018-08-03    4.5
# 2018-08-04    6.5
# 2018-08-05    8.0

import pandas as pd

df = pd.read_csv('http://www.post.japanpost.jp/zipcode/dl/oogaki/zip/13tokyo.zip',
                 header=None, encoding='shift_jis')

print(df.shape)
# (3851, 15)

print(df.head())
#       0    1        2       3      4                5    6     7           8   \
# 0  13101  100  1000000  ﾄｳｷﾖｳﾄ  ﾁﾖﾀﾞｸ  ｲｶﾆｹｲｻｲｶﾞﾅｲﾊﾞｱｲ  東京都  千代田区  以下に掲載がない場合   
# 1  13101  102  1020072  ﾄｳｷﾖｳﾄ  ﾁﾖﾀﾞｸ          ｲｲﾀﾞﾊﾞｼ  東京都  千代田区         飯田橋   
# 2  13101  102  1020082  ﾄｳｷﾖｳﾄ  ﾁﾖﾀﾞｸ         ｲﾁﾊﾞﾝﾁﾖｳ  東京都  千代田区         一番町   
# 3  13101  101  1010032  ﾄｳｷﾖｳﾄ  ﾁﾖﾀﾞｸ          ｲﾜﾓﾄﾁﾖｳ  東京都  千代田区         岩本町   
# 4  13101  101  1010047  ﾄｳｷﾖｳﾄ  ﾁﾖﾀﾞｸ           ｳﾁｶﾝﾀﾞ  東京都  千代田区         内神田   
#    9   10  11  12  13  14  
# 0   0   0   0   0   0   0  
# 1   0   0   1   0   0   0  
# 2   0   0   0   0   0   0  
# 3   0   0   1   0   0   0  
# 4   0   0   1   0   0   0  

print(df.tail())
#          0      1        2       3                  4                5    6   \
# 3846  13401  10015  1001511  ﾄｳｷﾖｳﾄ  ﾊﾁｼﾞﾖｳｼﾞﾏﾊﾁｼﾞﾖｳﾏﾁ              ﾐﾂﾈ  東京都   
# 3847  13402  10017  1001701  ﾄｳｷﾖｳﾄ           ｱｵｶﾞｼﾏﾑﾗ     ｱｵｶﾞｼﾏﾑﾗｲﾁｴﾝ  東京都   
# 3848  13421  10021  1002100  ﾄｳｷﾖｳﾄ           ｵｶﾞｻﾜﾗﾑﾗ  ｲｶﾆｹｲｻｲｶﾞﾅｲﾊﾞｱｲ  東京都   
# 3849  13421  10021  1002101  ﾄｳｷﾖｳﾄ           ｵｶﾞｻﾜﾗﾑﾗ            ﾁﾁｼﾞﾏ  東京都   
# 3850  13421  10022  1002211  ﾄｳｷﾖｳﾄ           ｵｶﾞｻﾜﾗﾑﾗ            ﾊﾊｼﾞﾏ  東京都   
#           7           8   9   10  11  12  13  14  
# 3846  八丈島八丈町          三根   0   0   0   0   0   0  
# 3847    青ヶ島村      青ヶ島村一円   0   0   0   0   0   0  
# 3848    小笠原村  以下に掲載がない場合   0   0   0   0   0   0  
# 3849    小笠原村          父島   0   0   0   0   0   0  
# 3850    小笠原村          母島   0   0   0   0   0   0  

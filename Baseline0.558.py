import pandas as pd

sales_sum = pd.read_csv('t_sales_sum.csv')  # t_sales_sum.csv文件路径
final = sales_sum.groupby(['shop_id'])[['sale_amt_3m']].mean()
final.to_csv('submission.csv', header=False)

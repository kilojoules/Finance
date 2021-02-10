from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si
import matplotlib.pyplot as plt

plt.subplots(figsize=(10, 10))
cash_flow_statement = si.get_cash_flow("MARA")

balance = si.get_balance_sheet("MARA")

assets = balance.loc['totalCurrentAssets']
debt = balance.loc['totalCurrentLiabilities']
cash = balance.loc['cash']

plt.plot(assets.index, assets / 10 ** 9, label='Assets (billions)', marker='x')
plt.plot(debt.index, debt / 10 ** 9, label='Total Debt (billions)', marker='x')
#plt.plot(cash.index, cash / 10 ** 9, label='Cash (billions)', marker='x')
plt.legend()
plt.savefig('ey')
plt.clf()

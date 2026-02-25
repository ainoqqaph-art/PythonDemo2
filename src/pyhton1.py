import yfinance as yf

def get_tsmc_price_yahoo():
	ticker = yf.Ticker('2330.TW')  # 台積電台股代碼
	data = ticker.history(period='1d')
	if not data.empty:
		price = data['Close'].iloc[-1]
		print(f"台積電 (2330.TW) Yahoo 股市最新收盤價: {price}")
	else:
		print("無法取得台積電股價資料。")


print ('hello world')
11+22


if __name__ == "__main__":
	get_tsmc_price_yahoo()
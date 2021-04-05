from datetime import datetime
from pandas import read_html
import csv
import schedule
import time

STOCK_ENDPOINT = "https://uk.finance.yahoo.com/cryptocurrencies"


def job():
    data = read_html(STOCK_ENDPOINT, header=None)
    df = data[0]

    current_time = datetime.now().time()

    data_list = []
    today_date = datetime.now().date()
    counter = 0
    for x in range(20):
        if str(df.iloc[x][1]) != "nan" and counter < 10:
            df_list = df.iloc[x].to_list()
            data_list.append(df_list)
            counter += 1

    file = open(f"Daily Data/crypto_data-{today_date}.csv", 'w+', newline='')

    with file:
        write = csv.writer(file)
        write.writerows(data_list)

    print(f"Job completed at {current_time},{today_date}")


schedule.every().day.at("19:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)

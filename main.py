from datetime import datetime
import pandas
import csv
import schedule
import time
import lxml

STOCK_ENDPOINT = "https://uk.finance.yahoo.com/cryptocurrencies"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/88.0.4324.190 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,el;q=0.8",
    "Accept-Encoding": "gzip, deflate",
}


def job():
    data = pandas.read_html(STOCK_ENDPOINT, header=None)
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
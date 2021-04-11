from datetime import datetime
from pandas import read_html
import pandas
import csv
import schedule
import time

STOCK_ENDPOINT = "https://uk.finance.yahoo.com/cryptocurrencies"


def clean_up(today_date):
    df = pandas.read_csv(f"Daily Data/crypto_data-{today_date}.csv")

    df.columns = ["Symbol", "Name", "Price", "(intraday)", "Change", "% change", "Market cap",
                  "Volume in currency (since 0:00 UTC)", "Volume in currency (24 hrs)",
                  "Total volume all currencies (24 hrs)", "Circulating supply", "Blank"]

    df.drop(['Circulating supply', 'Blank'], axis=1, inplace=True)

    df.to_csv(f"Daily Data/crypto_data-{today_date}.csv", index=False)


def extract_data():
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
        file.close()

    print(f"Job completed at {current_time},{today_date}")

    clean_up(today_date)


schedule.every().day.at("19:30").do(extract_data)

while True:
    schedule.run_pending()
    time.sleep(60)

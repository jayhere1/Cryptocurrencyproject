import pandas
from pathlib import Path


dir = 'Daily Data'
csv_files = [f for f in Path(dir).glob('*.csv')]

for csv in csv_files:
    try:
        df = pandas.read_csv(csv)

        df.columns = ["Symbol", "Name", "Price", "(intraday)", "Change", "% change", "Market cap",
                      "Volume in currency (since 0:00 UTC)", "Volume in currency (24 hrs)",
                      "Total volume all currencies (24 hrs)", "Circulating supply", "Blank"]

        df.drop(['Circulating supply', 'Blank'], axis=1, inplace=True)

        df.to_csv(csv, index=False)

    except ValueError:
        pass

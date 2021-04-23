import pandas
from pathlib import Path


dir = 'Daily Data'
csv_files = [f for f in Path(dir).glob('*.csv')]

for csv in csv_files:
    try:
        df = pandas.read_csv(csv)


        df.to_csv("Modified Files/", index=False)

    except ValueError:
        pass
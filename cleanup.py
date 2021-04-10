import pandas

df = pandas.read_csv("Daily Data/crypto_data-2021-03-12.csv")

df.columns = ["Symbol","Name","Price", "(intraday)","Change", "% change","Market cap",
           "Volume in currency (since 0:00 UTC)", "Volume in currency (24 hrs)","Total volume all currencies (24 hrs)",	"Circulating supply", "Blank"]

df.drop(['Circulating supply', 'Blank'], axis=1, inplace=True)

df.to_csv("Daily Data/crypto_data-2021-03-12.csv", index=False)

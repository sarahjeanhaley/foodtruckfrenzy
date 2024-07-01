import pandas as pd
from sqlalchemy import create_engine


csvSalesData = 'datafiles/foodtrucksalesdata.csv'
dfSalesData = pd.read_csv(csvSalesData)
csvItemPrices = 'datafiles/itemprices.csv'
dfPriceData = pd.read_csv(csvItemPrices)

db_url = 'sqlite:///database.db'
engine = create_engine(db_url)

tableNameSales = 'FoodTruckSales'
dfSalesData.to_sql(tableNameSales, engine, if_exists='replace', index=False)

tableNamePrices = 'ItemPrices'
dfPriceData.to_sql(tableNamePrices, engine, if_exists='replace', index=False)

engine.dispose()


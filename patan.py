# import mysql.connector as MySQL
# import pandas as pd
# dbconn = MySQL.connect(
#     host = "localhost",
#     user = "root",
#     password = "password",
#     db = "excel_db"
# )
# cursor = dbconn.cursor()
# free = pd.read_excel("Fins.xlsx", index_col=0)
# farmishes = pd.DataFrame(free).head().all()
# print(farmishes)
# for farmish in range(len(farmishes)):
#     famich = farmish + 1
#     print(farmishes.iloc[0])
# print(free)
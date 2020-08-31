import pandas as pd

excel = r"C:\Users\ff\Documents\AllInstalledApplications.xlsx"

dataframe = pd.read_excel(excel, sheet_name="AppsNoCorporativas")

#values = dataframe[["ProductName", "ComputerName", "Usuario"]]

#ataframe = [values]
#print(dataframe)

print(dataframe.groupby(['Usuario']).size().reset_index(name='l1'))

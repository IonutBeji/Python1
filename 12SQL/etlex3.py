import pandas as pd
df_financial = pd.read_excel('date_financiare.xlsx')
print(df_financial.head())

valori_lipsa = df_financial.isnull().sum()
print(valori_lipsa)

df_cu_valori_sterse = df_financial.dropna()

exchange_rate = {'USD': 4.2, 'EUR': 4.9, 'RON': 1.0}
df_financial['Suma_RON'] = df_financial.apply(lambda row: row['Suma_Tranzactie'] * exchange_rate[row['Valuta']], axis=1)
print(df_financial['Suma_RON'])
suma_clienti = df_financial.groupby('Client')['Suma_Transactie'].sum()
print(suma_clienti)

comision_mediu = df_financial.groupby('Tip_Transactie')['Comision'].mean()
print(comision_mediu)

tranzactii_problematice = df_financial[df_financial['Status_Transactie'] != 'Finalizata']
print(tranzactii_problematice)

tranzactii_mari = df_financial[df_financial['Suma_Transactie'] > 5000]
print(tranzactii_mari)

df_financial['Luna'] = df_financial['Data_Transactie'].dt.to_period('M')
suma_lunara = df_financial.groupby('Luna')['Suma_Transactie'].sum()
print(suma_lunara)


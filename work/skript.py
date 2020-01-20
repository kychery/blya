#Импортируем необходимые библиотеки

import pandas as pd
import numpy as np
import glob
import os

df_topfroders = pd.DataFrame()
df_froders = pd.DataFrame()

path_name = str(input('Введите название директории:'))
path = r'C:/Users/kychrey/Downloads/' + path_name

#Создаем папки для наших файлов
os.mkdir(r'C:/Users/kychrey/Downloads/' + path_name +'/results_nocommissions_froders')
os.mkdir(r'C:/Users/kychrey/Downloads/' + path_name +'/results_refund_froders')

all_files = glob.glob(path + "/*.csv")

#Безкомиссионные фродеры
for filename in all_files:
    df_input = pd.read_csv(filename)
    df = df_input[['driver_id', 'city', 'country', 'in_refund_status', 'success_commissions',
                   'refund_sum', 'success_commission_sum', 'accept_sum',
                   'driver_accepts', 'driver_cancel', 'client_cancel']].copy()
    df['commissions'] = df['in_refund_status'] + df['success_commissions']
    df['frod'] = df['driver_accepts'] - df['commissions']
    df['frod%'] = df['frod'] / df['driver_accepts']
    df['real_money'] = df['refund_sum'] + df['success_commission_sum']
    df = df.loc[df['driver_accepts'] >= 10]
    df = df.loc[df['frod%'] >= 0.4]
    df['drivers'] = 1
    df1 = df.loc[df['frod%'] >= 0.6] 
    df = df.loc[df['frod%'] < 0.6]
    df_froders = df_froders.append(df)
    df_topfroders = df_topfroders.append(df1)

g1_nc = df_froders.groupby(['city', 'country'])['frod', 'real_money', 'accept_sum', 'drivers'].sum().reset_index()
g2_nc = df_topfroders.groupby(['city', 'country'])['frod', 'real_money', 'accept_sum', 'drivers'].sum().reset_index()


g1_nc.to_csv(r'C:/Users/kychrey/Downloads/' + path_name + '/results_nocommissions_froders/results_froders.csv', index = None, header=True)
g2_nc.to_csv(r'C:/Users/kychrey/Downloads/' + path_name + '/results_nocommissions_froders/results_topfroders.csv', index = None, header=True)

df_froders.to_csv(r'C:/Users/kychrey/Downloads/' + path_name + '/results_nocommissions_froders/froders.csv', index = None, header=True) 
df_topfroders.to_csv(r'C:/Users/kychrey/Downloads/' + path_name + '/results_nocommissions_froders/topfroders.csv', index = None, header=True)


#Фродеры по возвратам
df_topfroders = pd.DataFrame()
df_froders = pd.DataFrame()

for filename in all_files:
    df_input = pd.read_csv(filename)
    df = df_input[['driver_id', 'city', 'country', 'in_refund_status', 'refund_sum', 'success_commissions', 
                   'driver_accepts', 'driver_cancel', 'client_cancel']].copy()
    df['frod%'] = df['in_refund_status'] / df['driver_accepts']
    df = df.loc[df['driver_accepts'] >= 10]
    df = df.loc[df['frod%'] >= 0.4]
    df['drivers'] = 1
    df1 = df.loc[df['frod%'] >= 0.6] 
    df = df.loc[df['frod%'] < 0.6]
    df_froders = df_froders.append(df)
    df_topfroders = df_topfroders.append(df1)

g1_re = df_froders.groupby(['city', 'country'])['in_refund_status', 'refund_sum', 'drivers'].sum().reset_index()
g2_re = df_topfroders.groupby(['city', 'country'])['in_refund_status', 'refund_sum', 'drivers'].sum().reset_index()

g1_re.to_csv(r'C:/Users/kychrey/Downloads/' + path_name + '/results_refund_froders/results_froders.csv', index = None, header=True)
g2_re.to_csv(r'C:/Users/kychrey/Downloads/' + path_name + '/results_refund_froders/results_topfroders.csv',  index = None, header=True)

df_froders.to_csv(r'C:/Users/kychrey/Downloads/' + path_name + '/results_refund_froders/froders.csv', index = None, header=True) 
df_topfroders.to_csv(r'C:/Users/kychrey/Downloads/' + path_name + '/results_refund_froders/topfroders.csv', index = None, header=True) 

print('Программа завершена.')

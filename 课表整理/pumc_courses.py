import pandas as pd
import numpy as np
import os

def df_clean(path,name):
    df = pd.read_excel(path)
    df = df.iloc[8:,0:9]
    df.drop(columns=['Unnamed: 7'],inplace=True)
    col_name = ['周次','月份','日期','星期','节次','内容','学时','教师']
    df.columns = col_name
    df = df.dropna(subset=['内容'])
    df['课程'] = [name for i in range(len(df))]
    return df

def get_name_list(path):
    namelist = []
    for dir in os.listdir(path):
        if os.path.isfile(path + dir):
            namelist.append(dir.split('.')[0])
    namelist.remove('')
    return namelist

def main():
    path = '/Users/apple/Desktop/PUMC/课程进度/'
    namelist = get_name_list(path)
    dfs = []
    for name in namelist:
        name_path = os.join(path, name+'.xls')
        print(name_path)
        df = df_clean(name_path, name)
        dfs.append(df)
    all_df = pd.concat(dfs)
    all_df['周次'] = all_df['周次'].astype(int)
    all_df.sort_values(by=['周次','月份','日期','节次'],inplace=True)
    all_df.to_excel(path + '总日程.xlsx', index=False)

if __name__ == '__main__':
    main()
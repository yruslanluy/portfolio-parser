from bs4 import BeautifulSoup as BS
import re
import numpy as np
import datetime as dt
from datetime import timedelta
# By Ruslan Apps & Crypto Chyvak 2022
# Telegram: @cryptochy


path = r"source.txt" # path to file
decimals = 8 # decimals after point: 0.1234...


with open(path, 'r') as file:
    soup = BS(file, "html.parser")
    data = [[], []]
    soup = soup.find('div', class_='sc-16r8icm-0 kjciSH')
    for line in soup.find_all('p', class_='sc-1eb5slv-0 hJMpdk')[4:]: # parsing dates
        data[0].append(line.text.rsplit(',', 1)[0])

    for amount in soup.find_all('p', class_=re.compile(r'sc-1eb5slv-0 (iRvyUh|hUkJcr)')): # parsing transactions amount
        data[1].append(amount.text.split(' ')[0])

    arr = np.array(data)
    arr = np.column_stack(arr)
    i = 0
    while True: # adding amounts in same days
        try:
            if arr[i][0] == arr[i+1][0]:
                arr[i] = [arr[i][0], float(arr[i][1]) + float(arr[i+1][1])]
                arr = np.delete(arr, i+1, 0)
                i -= 1
            i += 1
        except:
            break

    last_day = dt.datetime.strptime(arr[0][0], '%b %d, %Y').date()
    first_day = dt.datetime.strptime(arr[-1][0], '%b %d, %Y').date()

    dates = np.array([[(last_day).strftime('%b %#d, %Y'), 0], ]) # calculate dates array
    for i in range((last_day - first_day).days):
        dates = np.append(dates, [np.array([(last_day - timedelta(days=i+1)).strftime('%b %#d, %Y'), 0])], axis=0)

    for date in dates:
        for a in arr:
            if date[0] == a[0]:
                date[1] = a[1]

    sum = np.flip(np.reshape(np.cumsum(np.flip(dates[:, 1]), dtype='float'), (-1, 1))) # calculate sum of amounts
    dates = np.hstack((dates, np.around(sum, decimals)))

    np.set_printoptions(suppress=True)

    for line in dates:
        print(line[0] + " ; " + line[1] + " ; " + line[2])

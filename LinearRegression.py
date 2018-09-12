from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd

# def inputTahun():
#     inp = ''
#     while (inp != '1'):
#         inp = input('mauskan : ')
#         if (inp != '1'):
#             tahun.append(inp)
#         else:
#             break

data = pd.read_csv('ml.csv')

reg = linear_model.LinearRegression()
reg.fit(data[['tahun']], data.jumlah)

m = reg.coef_
b = reg.intercept_

# tahun = []

tahun = [2012, 2013]
jumlah = []

for i in tahun:
    y = m * int(i) + b
    jumlah.append(y)

for i in range(len(tahun)):
    print(str(tahun[i]) + ' jumlah Penduduk: ' + str(jumlah[i][0]))

plt.scatter(data.tahun, data.jumlah, color='red', marker='+')
predicted_values = [m * i + b for i in data.tahun]
plt.plot(data.tahun, predicted_values, 'b')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (Juta)')
plt.show()

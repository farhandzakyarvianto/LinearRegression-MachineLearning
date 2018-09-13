# from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd

def inputTahun():
    inp = ''
    while (inp != 'x'):
        inp = input('Masukan Tahun (klik `x` bila selesai) : ')
        if (inp != 'x'):
            tahun.append(inp)
        else:
            break

def decFormat(x):
    return ('%.8f' % x).rstrip('0').rstrip('.')

temp = []
err = []

def CalculateError():
    for i in data.tahun:
        o = v * i + w
        temp.append(o)

    for i in range(len(data.tahun)):
        s = (data.jumlah[i] - temp[i])**2
        err.append(s)

    _temp = sum(err)
    _temp = (_temp/len(data.tahun))**0.5
    print('Error : ' + str(_temp))


data = pd.read_csv('ml.csv')

# reg = linear_model.LinearRegression()
# reg.fit(data[['tahun']], data.jumlah)

# a = reg.coef_
# b = reg.intercept_
# tahun = [2012, 2013]

# print('-----------Data Diberikan-------------')
# for i in range(len(data.tahun)):
#     print('Tahun ' + str(data.tahun[i])+ ' jumlah Penduduk(juta): ' + str(data.jumlah[i]))

tahun = []
inputTahun()

jumlah = []


m = data.tahun
n = data.jumlah
_m = sum(m)
_n = sum(n)
_m2 = sum(m*m)
_n2 = sum(n*n)
mn = sum(m*n)
c = len(m)

print('-------------------------------------')
print('jumlah data = ' + str(c))
print('Jumlah x = ' + str(_m))
print('jumlah y = ' + str(_n))
print('jumlah x2= ' + str(_m2))
print('jumlah y2= ' + str(_n2))
print('jumlah xy= ' + str(mn))
print('-------------------------------------')

v = ((c*mn - _m*_n)/(c*_m2 - (_m)**2))
w = ((_m2*_n - _m*mn)/(c*_m2 - (_m)**2))

for i in tahun:
    y = v * int(i) + w
    jumlah.append(y)

print('a = ' + str(decFormat(w)) + ' dan b = ' + str(decFormat(v)))
print('-------------Prediksi----------------')

for i in range(len(tahun)):
    print('Tahun ' + str(tahun[i]) + ' jumlah Penduduk(juta): ' + str(decFormat(jumlah[i])))

# CalculateError()
plt.scatter(data.tahun, data.jumlah, color='red', marker='+')
predicted_values = [v * i + w for i in data.tahun]
plt.plot(data.tahun, predicted_values, 'b')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk (Juta)')
plt.show()

from tabulate import tabulate
import pandas as pd


data = [
  ['pr01', 'Oreo', 10000],
  ['pr02', 'Soft Cookies', 12000],
  ['pr03', 'Mie Goreng', 4000],
]

data2 = {
  'Kode Produk': ['pr01', 'pr02', 'pr03'],
  'Nama Produk': ['Oreo', 'Soft Cookies', 'Mie Goreng'],
  'Harga': [10000, 12000, 4000]
}

print('')
print('-' * 12, 'List Produk', '-' * 12)
print('')
print(tabulate(data, headers=['Kode Produk', 'Nama Produk', 'Harga']))
print('')
print('* Belanja lebih dari Rp.50000 dan dapatkan potongan 10% *')
print('')

result = []
total = 0
loop = True
dataExisting = True
isInt = True

def discountFunc(price):
  return price - (price * 0.1)

while loop:
  productId = input('Masukkan kode produk : ')
  while isInt:
    productQty = input('Masukkan jumlah produk : ')
    try:
      if type(eval(productQty)) is int:
        productQty = int(productQty)
        isInt = False
    except:
      print('Yang anda masukkan bukan angka')
    if isInt == False: break

  print('')

  for i in range(len(data)):
    if productId == data[i][0]:
      result.append([data[i][1], data[i][2], productQty, data[i][2] * productQty])
      total += data[i][2] * productQty
      dataExisting = True
      break
    if i == len(data) - 1:
      print('Kode Produk tidak sesuai')
      dataExisting = False

  while dataExisting:
    isAddProduct = input('Apakah ingin menambah produk? [y/t] : ')
    if isAddProduct == 't':
      loop = False
      break
    if isAddProduct != 'y':
      print('Jawaban tidak sesuai')

  if loop == False: break

print('')
print('-' * 14, 'Bukti Transaksi', '-' * 14)
print(tabulate(result, headers=['Nama Produk', 'Harga', 'Jumlah', 'Subtotal'], tablefmt='grid'))
print('')
if total > 50000:
  total = discountFunc(total)
  print('* Anda mendapat potongan 10%')
print('Total yang harus dibayar : Rp.%d' % (total))
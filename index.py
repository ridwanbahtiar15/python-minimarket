from tabulate import tabulate

data = [
  ['pr01', 'Oreo', 10000],
  ['pr02', 'Soft Cookies', 12000],
  ['pr03', 'Mie Goreng', 4000],
]

print('')
print('-' * 12, 'List Produk', '-' * 12)
print('')
print(tabulate(data, headers=['Kode Produk', 'Nama Produk', 'Harga', 'Stok']))
print('')
print('* Belanja lebih dari Rp.50000 dan dapatkan potongan 10% *')
print('')

result = []
total = 0
loop = True
dataExisting = False

def addProduct(productId, productQty):
  for i in range(len(data)):
    if productId == data[i][0]:
      result.append([data[i][1], data[i][2], productQty, data[i][2] * productQty])
      return data[i][2] * productQty

def discountFunc(price):
  return int(price * 0.1)

while loop:
  while not dataExisting:
    productId = input('Masukkan kode produk : ')

    for i in range(len(data)):
      if productId == data[i][0]:
        dataExisting = True
        break
      if i == len(data) - 1:
        print('Kode Produk tidak ditemukan. Coba lagi')

  while True:
    productQty = input('Masukkan jumlah produk : ')
    try:
        productQty = int(productQty)
        if productQty > 0:
          data[i]
          break
        else:
          print('Masukkan jumlah lebih dari 0')
    except:
      print('Masukkan angka yang valid. Coba lagi')

  if dataExisting == True:
    total += addProduct(productId, productQty)

  while dataExisting:
    isAddProduct = input('Apakah ingin menambah produk? [y/t] : ')
    if isAddProduct == 't':
      loop = False
      dataExisting = False
    elif isAddProduct == 'y':
      dataExisting = False
    else:
      print('Jawaban tidak valid. Coba lagi')

print('')
print('+' + '-' * 16, 'Bukti Transaksi', '-' * 16 + '+')
print(tabulate(result, headers=['Nama Produk', 'Harga', 'Jumlah', 'Subtotal'], tablefmt='grid'))
print('')

if total > 50000:
  print(f'* Anda mendapat potongan 10%. diskon Rp. {discountFunc(total)}')
  total = total - discountFunc(total)
print(f'Total yang harus dibayar : Rp. {total}')

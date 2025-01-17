from tabulate import tabulate
import mysql.connector

cnx = mysql.connector.connect(user='root', password='', host='localhost', database='minimarket')
cursor = cnx.cursor()

sql = ('SELECT * FROM product')
cursor.execute(sql)
data = cursor.fetchall()

print('')
print('-' * 16, 'List Produk', '-' * 16)
print('')
print(tabulate(data, headers=['Kode Produk', 'Nama Produk', 'Harga', 'Stok']))
print('')
print('* Belanja lebih dari Rp.50000 dan dapatkan potongan 10% *')
print('')

result = []
total = 0
loop = True
dataExisting = False

def searchProduct(productId):
  sqlFetch = "SELECT * FROM product WHERE product_id = %s"
  cursor.execute(sqlFetch, [productId])
  return cursor.fetchone()

def addProduct(productId, productQty):
  data = searchProduct(productId)
  if data:
    if data[3] == 0 or data[3] < productQty:
      return 0
    newStock =  data[3] - productQty
    result.append([data[0], data[1], productQty, data[2] * productQty])
    sqlUpdate = "UPDATE product SET stock = %s WHERE product_id = %s"
    val = (newStock, productId)
    try:
      cursor.execute(sqlUpdate, val)
      cnx.commit()
      return data[2] * productQty
    except:
      cursor.rollback()

def discountFunc(price):
  return int(price * 0.1)

while loop:
  while not dataExisting:
    productId = input('Masukkan kode produk : ')
    check = searchProduct(productId)
    if check != None:
      dataExisting = True
    else:
      print('Kode Produk tidak ditemukan. Coba lagi')

  while True:
    try:
      productQty = int(input('Masukkan jumlah produk : '))
      if productQty > 0:
        break
      print('Masukkan jumlah lebih dari 0')
    except:
      print('Masukkan angka yang valid. Coba lagi')

  if dataExisting:
    subtotal = addProduct(productId, productQty)
    if subtotal != 0:
      total += subtotal
    else:
      dataExisting = False
      print('Stok tidak tersedia')

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

cnx.close()

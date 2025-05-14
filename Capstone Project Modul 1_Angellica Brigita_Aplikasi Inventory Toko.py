# CAPSTONE PROJECT MODUL 1

# APLIKASI INVENTORY STOK GUDANG TOKO 'Clothin'
# Tujuan dari aplikasi ini adalah agar user bisa mengetahui dan mengupdate stok barang di toko 'Clothin'

# Function menu di aplikasi:
# Function Daftar Stok Inventory, Menambah Barang, Menghapus Barang, Update Stok, Update Harga, dan Kalkulator Harga

# Function Daftar Stok Inventory
dictStok = {
    'Kode Barang' : ['BW1', 'BW2', 'BW3', 'DW1', 'CW1/M', 'A1', 'A2', 'BP1', 'CP1/L', 'SA38'],
    'Nama Barang' : ['Blouse A', 'Top A', 'Cardigan A', 'Dress A', 'Celana Jeans A/M', 'Belt', 'Scarf', 'Kemeja Pria A', 'Celana Jeans Pria A/L', 'Flat Shoes A/38'],
    'Kategori'    : ['Pakaian Wanita', 'Pakaian Wanita', 'Pakaian Wanita', 'Pakaian Wanita', 'Pakaian Wanita', 'Aksesoris', 'Aksesoris', 'Pakaian Pria', 'Pakaian Pria', 'Sepatu'],
    'Warna'       : ['Hitam', 'Putih', 'Navy', 'Putih', 'Denim', 'Hitam', 'Multicolor', 'Putih', 'Denim', 'Cream'],
    'Ukuran'      : ['One Size', 'One Size', 'One Size', 'One Size', 'M', 'One Size', 'One Size', 'One Size', 'L', '38'],
    'Jumlah Stok' : [150, 200, 150, 125, 100, 75, 100, 200, 100, 50],
    'Harga Beli'  : [100000, 70000, 120000, 120000, 150000, 60000, 50000, 100000, 180000, 100000],
    'Harga Jual'  : [149990, 104990, 179990, 179990, 224990, 89990, 74990, 149990, 269990, 149990]}

from tabulate import tabulate 

def stokInventory():
    print(tabulate(dictStok, headers = ['Kode Barang', 'Nama Barang', 'Kategori', 'Warna', 'Ukuran', 'Jumlah Stok', 'Harga Beli', 'Harga Jual']))

# Function Menambah Barang
def tambahBarang():
    while True:
        kodePlus = input('Masukkan kode barang (ketik NO jika ingin berhenti): ').upper()
        if kodePlus == 'NO':
            break
        elif kodePlus in dictStok['Kode Barang']:
            print('Kode sudah ada, silahkan masukkan kode baru')
        else:
            namaPlus = input('Masukkan nama barang: ').title()
            kategoriPlus = input('Masukkan kategori barang (Pakaian Wanita/Pakaian Pria/Aksesoris/Sepatu): ').title()
            warnaPlus = input('Masukkan warna barang: ').title()
            ukuranPlus = input('Masukkan ukuran: ').title()
            jumlahPlus = int(input('Masukkan jumlah stok: '))
            hargaBeliPlus = int(input('Masukkan harga beli: '))
            hargaJualPlus = int(input('Masukkan harga jual: '))
            dictStok['Kode Barang'].append(kodePlus)
            dictStok['Nama Barang'].append(namaPlus)
            dictStok['Kategori'].append(kategoriPlus)
            dictStok['Warna'].append(warnaPlus)
            dictStok['Ukuran'].append(ukuranPlus)
            dictStok['Jumlah Stok'].append(jumlahPlus)
            dictStok['Harga Beli'].append(hargaBeliPlus)
            dictStok['Harga Jual'].append(hargaJualPlus)
            stokInventory()
            print(f'{namaPlus} berhasil ditambahkan')
            


# Function Menghapus Barang
def hapusBarang():
    stokInventory()
    while True:
        barangHapus = input('Masukkan kode barang yang ingin dihapus (ketik NO jika ingin berhenti): ').upper()
        if barangHapus in dictStok['Kode Barang']:
            i = dictStok['Kode Barang'].index(barangHapus)
            namaBarangHapus = dictStok['Nama Barang'][i]
            del dictStok['Kode Barang'][i]
            del dictStok['Nama Barang'][i]
            del dictStok['Kategori'][i]
            del dictStok['Warna'][i]
            del dictStok['Ukuran'][i]
            del dictStok['Jumlah Stok'][i]
            del dictStok['Harga Beli'][i]
            del dictStok['Harga Jual'][i]
            stokInventory()
            print(f'Kode {barangHapus} = {namaBarangHapus} berhasil dihapus')
        elif barangHapus == 'NO':
            break
        else:
            print('Kode barang tidak ditemukan')



# Function update stok
def updateStok():
    stokInventory()
    while True:
        updateBarang = input('Masukkan kode barang yang ingin di update (ketik NO jika ingin berhenti): ').upper()
        if updateBarang in dictStok['Kode Barang']:
            i = dictStok['Kode Barang'].index(updateBarang)
            stok = dictStok['Jumlah Stok'][i]
            print(f'Jumlah stok {updateBarang} saat ini adalah {stok}')
            while True:
                ubahStok = (input('Masukkan jumlah stok yang ingin di update (beri tanda + untuk menambah dan tanda - untuk mengurangi, ex.: +10 atau -15): '))
                ubahStok = ubahStok.replace(' ', '')
                if ubahStok.lstrip('+-').isdigit():
                    ubahStok = int(ubahStok)
                    stokBaru = stok + ubahStok
                    if stokBaru < 0:
                        print('Jumlah stok tidak boleh kurang dari 0')
                    else:
                        dictStok['Jumlah Stok'][i] = stokBaru
                        stokInventory()
                        print(f'Stok {updateBarang} berhasil diupdate menjadi {stokBaru}')
                        break
                else:
                    print('Stok tidak terbaca')
        elif updateBarang == 'NO':
            break
        else:
            print('Kode barang tidak ditemukan')



# Function update harga beli dan harga jual
def updateHarga ():
    stokInventory()
    while True:
        kodeHarga = input('Masukkan kode barang yang ingin diubah harganya (ketik NO jika ingin berhenti): ').upper()
        if kodeHarga in dictStok['Kode Barang']:
            i = dictStok['Kode Barang'].index(kodeHarga)
            hargaBeliNow = dictStok['Harga Beli'][i]
            hargaJualNow = dictStok['Harga Jual'][i]
            namaBarang = dictStok['Nama Barang'][i]
            print(f'''Harga beli {namaBarang} : {hargaBeliNow}
                  Harga jual {namaBarang} : {hargaJualNow}''')
            while True:
                hargaBeliBaru = (input('Masukkan harga beli baru: '))
                hargaJualBaru = (input('Masukkan harga jual baru: '))
                if hargaBeliBaru.isdigit() and hargaJualBaru.isdigit():
                    dictStok['Harga Beli'][i] = hargaBeliBaru
                    dictStok['Harga Jual'][i] = hargaJualBaru
                    print('Harga berhasil di update')
                    break
                else:
                    print('Masukkan ulang harga dalam bentuk angka')
            
            stokInventory()
        elif kodeHarga == 'NO':
            break
        else:
            print('Kode barang tidak ditemukan')


# Function Kalkulator Harga Jual
def kalkulatorHarga():
    while True:
        hargaBeli = (input('Masukkan harga beli (ketik NO jika ingin berhenti): ')).upper()
        if hargaBeli == 'NO':
            break
        elif hargaBeli.isdigit():
            intHargaBeli = int(hargaBeli)
            packaging = (intHargaBeli * 0.10)
            admin = (intHargaBeli * 0.05)
            markup = ((intHargaBeli * 0.35) + intHargaBeli)
            hargaJual = packaging + admin + markup
            pembulatan = (hargaJual//1000)*1000 - 10
            print(f'Harga jual: {pembulatan}')
        else:
            print('Harga beli tidak terbaca')
            


# ALUR FLOW PROGRAM

while True:
    inputMenu = input(f'''Selamat datang di Aplikasi Inventory Toko 'Clothin'.
Pilih menu yang diinginkan:
1. Daftar Stok Inventory
2. Menambah Barang
3. Menghapus Barang
4. Update Stok
5. Update Harga Jual dan Harga Beli
6. Kalkulator Harga Jual
7. Exit Program
          
Masukkan nomor menu yang ingin dijalankan: ''')
    if inputMenu == '1':
        stokInventory()
        
    elif inputMenu == '2':
        tambahBarang()
        
    elif inputMenu == '3':
        hapusBarang()
        
    elif inputMenu == '4':
        updateStok()
        
    elif inputMenu == '5':
        updateHarga()

    elif inputMenu == '6':
        kalkulatorHarga()

    elif inputMenu == '7':
        print('Terima kasih sudah menggunakan aplikasi ini')
        break

    else:
        print('Menu tidak tersedia, silahkan pilih angka 1 - 7')

        


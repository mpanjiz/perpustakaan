import model
import data
import uuid;
import bcrypt;
from tabulate import tabulate
import auth

roles = data.initRole();
users = data.initUser();
categories = data.initCategory();
catalogue = data.initCatalogue();
trx = data.initTrx();
isLogin = False;
toPosition = '0';
listCatalogue = [];
keranjang = [];

def main () :
    global isLogin;
    optionDash = dashboard('0', '')
    if (optionDash == 'L') :
        isLogin = auth.authLogin(users, roles)
        if (isLogin == False) :
            print('Login Gagal, silahkan coba beberapa saat lagi')
        
        optionDash = dashboard('0', '')
    elif (optionDash == '1') :
        while optionDash == '1' :
            keySearch = input("Cari judul buku : ")
            # search(keySearch);
            optionDash = dashboard('1', keySearch)
    elif (optionDash == '4') :
        if (isLogin == False) :
            print('Anda harus Login pada App terlebih dahulu untuk melanjutkan proses peminjaman buku\n')
            toLogin = input("Login (y/n) : ").lower()
            if  (toLogin == 'y') :
                isLogin = auth.authLogin(users, roles)
                if (isLogin == False) :
                    print('Login Gagal, silahkan coba beberapa saat lagi')
                optionDash = dashboard('0', '')
                if (optionDash == '4') :
                    loanOption = '1'
                    while loanOption == '1' :
                        print('1 : tambah buku')
                        print('2 : lihat keranjang')
                        loanOption = input("(1/2) : ").lower()
                        if  (loanOption == '1') :
                            addBookToLoan()
                    showData(keranjang);
        else :
            loanOption = '1'
            while loanOption == '1' :
                print('1 : tambah buku')
                print('2 : lihat keranjang')
                loanOption = input("(1/2) : ").lower()
                if  (loanOption == '1') :
                    addBookToLoan()
            showData(keranjang);

def addBookToLoan() :
    global keranjang;
    isAvail = False;
    isOnRange = False;
    chart = {};
    while isAvail == False :
        noBook = input("Pilih nomor produk : ")
        for i in range(len(listCatalogue)):
            if (listCatalogue[i]['No'] == noBook) :
                if (listCatalogue[i]['unit'] == '0') :
                    print('buku sedang tidak tersedia')
                else :
                    isAvail = True;
                    chart = listCatalogue[i]
                    break;
    
    while isOnRange == False :
        try :
            days = int(input("Jumlah Hari peminjaman buku? : "))
            if (chart['maks_hari_peminjaman'] < days) :
                print('jumlah hari peminjaman melebihi batas maksimal peminjaman')
            else :
                isOnRange = True
                
        except :
            print('Input hanya dapat berupa digit angka')
    
    keranjang.append(chart)

def mainMenu () :
    print('Menu')
    print('1 : Cari buku')
    print('2 : Filter')
    print('3 : reset')
    print('4 : Pinjam Buku')
    print('5 : Riwayat Peminjaman Buku\n')

def dashboard (type:any, search:any) :
    global listCatalogue;
    listCatalogue = []
    print('============== Selamat Datang di Perpustakaan Bandung ==============\n')
    print('Berikut katalog buku di perpustakaan Bandung')
    if (type == '0') :
        for i in range(len(catalogue)):
            displayCat = {}
            displayCat['No'] = str(i+1)
            displayCat['judul'] = catalogue[i]['title']
            for category in categories:
                if catalogue[i]['id_category'] == category['id']:
                    displayCat['genre'] = category['name']
                    break;
            displayCat['penulis'] = catalogue[i]['writer']
            displayCat['tanggal_terbit'] = catalogue[i]['published_date']
            displayCat['unit'] = catalogue[i]['capacity']
            displayCat['maks_hari_peminjaman'] = catalogue[i]['max_day_loans']
            displayCat['id'] = catalogue[i]['id']
            listCatalogue.append(displayCat)
    elif (type == '1') :
        for i in range(len(catalogue)):
            if search.lower() in catalogue[i]['title'].lower() :
                displayCat = {}
                displayCat['No'] = str(i+1)
                displayCat['judul'] = catalogue[i]['title']
                for category in categories:
                    if catalogue[i]['id_category'] == category['id']:
                        displayCat['genre'] = category['name']
                        break;
                displayCat['penulis'] = catalogue[i]['writer']
                displayCat['tanggal_terbit'] = catalogue[i]['published_date']
                displayCat['unit'] = catalogue[i]['capacity']
                displayCat['maks_hari_peminjaman'] = catalogue[i]['max_day_loans']
                displayCat['id'] = catalogue[i]['id']
                listCatalogue.append(displayCat)

    showData(listCatalogue);
    mainMenu();
    if (isLogin == False) :
        print('Saat ini anda belum Login, anda dapat login dengan cara ketik L\n')

    init = True
    while init :
        wOption = input("Pilih menu (1/2/3/4/L) : ")
        if (wOption == '1' or 
            wOption == '2' or 
            wOption == '3' or
            wOption == '4' or
            wOption == 'L') :
            init = False
        else :
            print('Pilihan anda tidak tersedia di daftar menu, silahkan pilih kembali')
    return wOption;

def loanBook () :
    print('pinjam buku')

def resetData () :
    return dashboard('0', '')

def showData (data:any) :
    print(tabulate(data, headers="keys", tablefmt="grid"))
    

main()
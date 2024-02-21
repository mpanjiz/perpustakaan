import getpass;
import uuid;
import bcrypt;
import model

def menuAkses (initRole:any) :
    print('Akses Aplikasi sebagai,')
    print('1 : Pengunjung Perpustakaan')
    print('2 : Admin Perpustakaan\n')

    while True :
        opsi = input("akses (1/2) : ")
        rl = '';
        role = '';
        if (opsi == '1' or 
            opsi == '2') :
            if (opsi  == '2'):
                rl = "admin"
            else :
                rl = "customer"
            break;
        else :
            print('Pilihan anda tidak tersedia dalam daftar, silahkan pilih kembali')
    
    for role in initRole :
        if(rl == role['name']): 
            role = role['id']
            break;
    
    return role;

def authLogin(usersData:any, initRole:any) :
    roleId = menuAkses(initRole)

    isValid = False;
    retry = 0
    while isValid == False and retry < 3 :
        retry += 1
        print('\n---login---')
        username = input("username : ")
        password = getpass.getpass("password:")

        for user in usersData:
            if (user['username'] == username and user['id_role'] == roleId) :
                passCode = password.encode('utf-8')
                checked = bcrypt.checkpw(passCode, user['password'])

                if (checked == True):
                    isValid = True;
                    break;
                else :
                    print('username atau password salah')

    return isValid;
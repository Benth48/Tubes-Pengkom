# No. Kelompok      : 4
# NIM/Nama Kelompok : 1. 16022061/Beni Lesmana
#                     2. 16022066/Arsyenala Mutiara Nadin Wowor
#                     3. 16022071/Jonathan Biliguna
#                     4. 16022076/Thio Novriery
# Deskripsi         : Program yang ditujukan untuk membuat salinan dari mesin ATM
#                     fitur yang diberikan pada program ini hanyalah fitur yang sering digunakan
#                     seperti Setor tunai, Tarik tunai, Transfer, Mutasi rekening, dan cek saldo

# Kamus :
# list_Kartu : string, menunjukkan list no kartu yang telah terdaftar
# list_password : string, menunjukkan list password yang terdaftar sesuai dengan no kartu
# list_profile : string, menunjukkan list nama profile yang terdaftar sesuai dengan no kartu
# list_balance : integer, menunjukkan list saldo yang dimiliki saat ini sesuai dengan no kartu
# list_history : string, menunjukkan list riwayat transaksi sesuai dengan no kartu
# no_profile : integer, digunakan untuk pengecekan apakah no kartu yang dimasukkan saat login telah terdaftar atau tidak
# profile_tujuan : integer, digunakan untuk pengecekan apakah no kartu yang dimasukkan untuk tujuan saat transfer telah terdaftar atau tidak
# now : string, menunjukkan waktu saat ini dan digunakan untuk mengetahui waktu saat dilakukannya transaksi
# waktu : string, digunakan untuk merapikan susunan waktu yang akan ditampilkan
# NoKartu : string, digunakan untuk input no kartu user
# Password : string, digunakan untuk input password user
# retry : string, digunakan untuk input pilihan antara mengulang input password atau tidak
# Pilihan : string, digunakan untuk input pilihan transaksi sesuai dengan no jenis transaksi yang ditampilkan
# Setor : integer, digunakan untuk input nominal uang yang akan disetor ke saldo no kartu yang digunakan 
# history : string, menunjukkan riwayat transaksi yang akan dimasukkan ke riwayat transaksi no kartu yang digunakan
# Tarik : integer, digunakan untuk input nominal uang yang akan ditarik dari saldo no kartu yang digunakan
# Tujuan : string, digunakan untuk input no kartu yang akan dijadikan tujuan dari transfer
# konfirmasi : string, digunakan untuk input pilihan antara 
# Dari : string, menunjukkan riwayat transaksi yang akan dimasukkan ke riwayat transaksi no kartu yang digunakan
# Kepada : string, menunjukkan riwayat transaksi yang akan dimasukkan ke riwayat transaksi no kartu tujuan
# Pilihan2 : string, digunakan untuk input pilihan transaksi sesuai dengan no jenis transaksi yang ditampilkan
# again : string, digunakan untuk input pilihan antara melanjutkan transaksi atau menyelesaikannya

import datetime
# Inisiasi
list_Kartu=['20042004','170845']
list_password=['123456','654321']
list_profile=['Benth', 'Hero']
list_balance=[1000000,1000000]
list_history=[[],[]]
no_profile=0
profile_tujuan=0
# Algoritma
print('Welcome To ATM Bank Ganesha')
NoKartu=input('No. Kartu   : ') 
# Perulangan untuk pengecekan no kartu
while (NoKartu!=list_Kartu[no_profile] and no_profile<len(list_Kartu)) :
    no_profile+=1
    if no_profile==len(list_Kartu) :
        print('Kartu belum terdaftar di bank \nSilahkan ulang program')
        exit()
# Perulangan untuk pengecekan password
while True :
    Password=input('Password    : ')
    # Percabangan untuk menentukan apakah password yang diinput benar
    if Password==list_password[no_profile] :
        print(f'\nwelcome {list_profile[no_profile]}')
        break
    else :
        print('Password Salah \nCoba Lagi? \nY/N')
        retry=input()
        # Percabangan untuk menentukan pengulangan password
        if retry=='Y' or retry=='y' :
            continue
        elif retry=='N' or retry=='n' :
            print('~~~Terima Kasih~~~')
            exit()
        else :
            print('============================== ERROR ==============================')
            exit()
# Perulangan untuk setiap melakukan transaksi
while True :
    now=datetime.datetime.now()
    waktu=now.strftime("%H:%M:%S %d/%m/%Y")
    print()
    print('1.Setor Tunai    3.Transfer')
    print('2.Tarik tunai    4.Cek')
    print()
    Pilihan=input()
    print()
    # Percabangan untuk jenis transaksi yang telah dipilih di menu transaksi
    if Pilihan=='1' :
        Setor=int(input('Masukkan Nominal :\nRp'))
        # Percabangan untuk koreksi nominal setor agar pasti lebih dari 0
        if Setor>0 :
            list_balance[no_profile]+=Setor
            history=f'{waktu} Rp{Setor} ditambahkan ke rekening {list_profile[no_profile]}'
            list_history[no_profile].append(history)
            print(f'\n{waktu} \n\nNo. Kartu : {list_Kartu[no_profile]} \nNama : {list_profile[no_profile]} \n\nSetor : Rp{Setor} \nSisa Saldo : Rp{list_balance[no_profile]}')
        else : 
            print()
            print('============================== ERROR ==============================')
    elif Pilihan=='2' :
        Tarik=int(input('Masukkan Nominal :\nRp'))   
        # Percabangan untuk koreksi nominal setor agar pasti lebih dari 0
        if Tarik>0 :
            if Tarik>list_balance[no_profile] :
                print()
                print('Saldo tidak cukup')
            else :
                list_balance[no_profile]-=Tarik
                history=f'{waktu} Rp{Tarik} ditarik dari rekening {list_profile[no_profile]}'
                list_history[no_profile].append(history)
                print(f'\n{waktu} \n\nNo. Kartu : {list_Kartu[no_profile]} \nNama : {list_profile[no_profile]} \n\nTarik : Rp{Tarik}\nSisa Saldo : Rp{list_balance[no_profile]}')
        else :
            print()
            print('============================== ERROR ==============================')
    elif Pilihan=='3' :
        profile_tujuan=0
        Tujuan=input('Masukkan No.Kartu yang dituju : ')
        # Perulangan untuk cek apakah no kartu yang dimasukkan telah terdaftar dan bukan kartu yang digunakan saat ini
        while (profile_tujuan<len(list_Kartu) and Tujuan!=list_Kartu[profile_tujuan] and Tujuan!=NoKartu ) :
            profile_tujuan+=1
            # Percabangan untuk pengecualian saat no kartu saat ini yang dimasukkan
            if profile_tujuan==no_profile :
                profile_tujuan+=1
        # Percabangan untuk menentukan apakah no kartu yang dimasukkan sesuai        
        if profile_tujuan!=len(list_Kartu) and Tujuan!=NoKartu :
            print(f'\nNo. Kartu : {list_Kartu[profile_tujuan]} \nNama : {list_profile[profile_tujuan]}')
            print()
            print('Apakah profile tujuan benar? \nY/N')
            print()
            konfirmasi=input()
            print()
            # Percabangan untuk konfirmasi profile tujuan
            if konfirmasi=='Y' or konfirmasi=='y' :
                Transfer=int(input('Masukkan Nominal :\nRp'))
                # Percabangan untuk koreksi nominal transfer agar pasti lebih dari 0
                if Transfer>0 :
                    if Transfer>list_balance[no_profile] :
                        print()
                        print('Saldo tidak cukup')
                    else :
                        list_balance[no_profile]-=Transfer
                        list_balance[profile_tujuan]+=Transfer
                        Dari=f'{waktu} Rp{Transfer} dikirim dari rekenening {list_profile[no_profile]} ke rekening {list_profile[profile_tujuan]}'
                        Kepada=f'{waktu} Rp{Transfer} diterima ke rekening {list_profile[profile_tujuan]} dari rekening {list_profile[no_profile]}'
                        list_history[no_profile].append(Dari)
                        list_history[profile_tujuan].append(Kepada)
                        print(f'\n{waktu} \n\nDari \nNo. Kartu : {list_Kartu[no_profile]} \nNama : {list_profile[no_profile]} \n\nKepada \nNo. Kartu : {list_Kartu[profile_tujuan]} \nNama : {list_profile[profile_tujuan]} \n\nTransfer : Rp{Transfer} \nSisa Saldo : Rp{list_balance[no_profile]}')
                else :
                    print()
                    print('============================== ERROR ==============================')  
        else :
            print('No.Kartu tidak dapat ditemukan')
    elif Pilihan=='4' :
        print('1.Riwayat        2.Cek Saldo')
        print()
        Pilihan2=input()
        print()
        # Percabangan untuk menyesuaikan transaksi yang telah dipilih dari menu transaksi yang ada
        if Pilihan2=='1' :
            # Perulangan untuk print semua riwayat dari no kartu saat ini yang telah dilakukan selama program berlangsung
            for check in range(len(list_history[no_profile])) :
                print(list_history[no_profile][check])
        elif Pilihan2=='2' :
            print(f'Saldo anda saat ini adalah Rp{list_balance[no_profile]}')
        else :
            print('============================== ERROR ==============================')
    else : 
        print()
        print('============================== ERROR ==============================')
    print()
    print('Apakah mau melanjutkan transaksi? \nY/N')
    print()
    again=input()
    # Percabangan untuk menentukan pengulangan transaksi
    if again=='Y' or again=='y' :
        continue
    elif again=='N' or again=='n' :
        print()
        print('~~~Terima Kasih~~~')
        exit()
    else :
        print()
        print('============================== ERROR ==============================')
        exit()
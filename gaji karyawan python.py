input_data_lagi='y'
while input_data_lagi=='y':



    print ("\t \t Program Menghitung Gaji Karyawan")

    print ("===============================================================================")
    nik=input("Masukan No Induk Karyawan \t: ")
    nama=input("Masukan Nama Karyawan \t: ")
    print ("1. Direksi \n2. DIrektur Utama \n3. Direktur \n4. Manajer \n5. Divisi \n6. Staff Lain")
    jabatan=input("Masukan Jabatan \t\t: ")
    alamat=input("Masukan Alamat \t\t\t: ")
    jml_anak=input("Masukan Jumlah Anak \t\t: ")
    if (jabatan=='1'):
        gaji_pokok=20000000
        jab="Direksi"
    elif(jabatan=='2'):
        gaji_pokok=18500000
        jab="DIrektur Utama"
    elif(jabatan=='3'):
        gaji_pokok=16000000
        jab="Direktur"
    elif(jabatan=='4'):
        gaji_pokok=10000000
        jab="Manajer"
    elif(jabatan=='5'):
        gaji_pokok=8000000
        jab="Divisi"
    else:
        gaji_pokok=3000000
        jab="Staff Lain"



    if(jml_anak>='5'):

        tunjangan=1000000
    elif(jml_anak <='3'):
        tunjangan=750000
    else:
        tunjangan=500000



    pajak= gaji_pokok *0.15

    gaji_bersih= gaji_pokok-pajak+tunjangan



    print ("")

    print ("\n")
    print ("===============================================================================")
    print ("")
    print ("NIK \t\t: ",nik)
    print ("Nama \t\t: ",nama)
    print ("Jabatan \t: ",jab)
    print ("Alamat \t\t: ",alamat)
    print ("Gaji bersih \t: ",gaji_bersih)
    print ("")
    print ("===============================================================================")
    print ("")
    input_data_lagi=input("Entry Data Lagi [y/n]? : ")
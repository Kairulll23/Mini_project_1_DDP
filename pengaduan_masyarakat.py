# Nama : Khairul Ikhsan
# Kelas: Sistem Informasi C
# Mini Project : Sistem Pengaduan Masyarakat

data = []
id = 1

while True:
    print("\n === Menu Pengaduan Masyarakat: ===")
    print("1. Tambah Pengaduan")
    print("2. Lihat Pengaduan")
    print("3. Update Status")
    print("4. Hapus Pengaduan")
    print("5. Keluar")

    pilih = input("Pilih menu: ")

    # untuk create
    if pilih == "1":
        nama = input("Nama pelapor: ")
        isi = input("Isi pengaduan: ")
        status = "Baru"
        laporan = (id, nama, isi, status)
        data = data + [laporan]
        id += 1
        print("Data pengaduan ditambahkan.")

    # untuk read
    elif pilih == "2":
        if len(data) == 0:
            print("Belum ada data.")
        else:
            for d in data:
                print("ID:", d[0], "| Nama:", d[1], "| Isi:", d[2], "| Status:", d[3])

    # untuk updet
    elif pilih == "3":
        ubah = int(input("Masukkan ID: "))
        ketemu = False
        for i in range(len(data)):
            if data[i][0] == ubah:
                status_baru = input("Status baru: ")
                data[i] = (data[i][0], data[i][1], data[i][2], status_baru)
                ketemu = True
        if ketemu:
            print("Status berhasil diubah.")
        else:
            print("ID tidak ditemukan.")

    # untuk delete
    elif pilih == "4":
        hapus = int(input("Masukkan ID yang dihapus: "))
        baru = []
        ketemu = False
        for d in data:
            if d[0] != hapus:
                baru = baru + [d]
            else:
                ketemu = True
        data = baru
        if ketemu:
            print("Data berhasil dihapus.")
        else:
            print("ID tidak ditemukan.")

    # untuk out
    elif pilih == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan salah.")




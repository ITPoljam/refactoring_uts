def pinjam_alat(nama, alat, jumlah, stok, status):
    if jumlah <= 0:
        print("Jumlah tidak valid")
    elif stok < jumlah:
        print("Stok tidak tersedia")
    elif status != "tersedia":
        print("Alat sedang dipinjam")
    else:
        stok = stok - jumlah
        status = "dipinjam"

        print("Nama mahasiswa:", nama)
        print("Nama alat:", alat)
        print("Jumlah pinjam:", jumlah)
        print("Peminjaman berhasil")

        print("Transaksi peminjaman dicatat")
        print("Status alat diperbarui")

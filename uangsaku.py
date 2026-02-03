"""Aplikasi sederhana untuk mengelola saldo uang saku.

Berisi fungsi `tambah_pemasukan()` yang meminta input jumlah, menambah ke `saldo`, dan
menampilkan pesan berhasil.
"""

saldo = 0.0


def tambah_pemasukan():
    """Meminta input jumlah pemasukan, menambahkannya ke `saldo`, dan menampilkan pesan."""
    global saldo
    try:
        teks = input("Masukkan jumlah pemasukan: ")
        jumlah = float(teks)
        if jumlah <= 0:
            print("Jumlah harus lebih besar dari 0.")
            return
        saldo += jumlah
        print(f"Pemasukan sebesar Rp{jumlah:.2f} berhasil ditambahkan. Saldo sekarang: Rp{saldo:.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka, contohnya: 10000")


def tambah_pengeluaran():
    """Meminta input jumlah pengeluaran, mengurangi `saldo` jika cukup, dan menampilkan pesan/peringatan."""
    global saldo
    try:
        teks = input("Masukkan jumlah pengeluaran: ")
        jumlah = float(teks)
        if jumlah <= 0:
            print("Jumlah harus lebih besar dari 0.")
            return
        if jumlah > saldo:
            print(f"Saldo tidak cukup. Saldo saat ini: Rp{saldo:.2f}")
            return
        saldo -= jumlah
        print(f"Pengeluaran sebesar Rp{jumlah:.2f} berhasil dikurangkan. Saldo sekarang: Rp{saldo:.2f}")
    except ValueError:
        print("Input tidak valid. Masukkan angka, contohnya: 5000")


def lihat_saldo():
    """Menampilkan saldo saat ini dengan format rapi."""
    global saldo
    # Menampilkan dengan pemisah ribuan dan dua desimal
    print(f"Saldo saat ini: Rp{saldo:,.2f}")


def main_menu():
    """Tampilkan menu utama untuk memilih aksi: lihat saldo, tambah pemasukan, tambah pengeluaran."""
    while True:
        print("\n=== Menu Utama ===")
        print("1. Lihat saldo")
        print("2. Tambah pemasukan")
        print("3. Tambah pengeluaran")
        print("4. Keluar")
        pilihan = input("Pilih (1-4): ").strip()
        if pilihan == "1":
            lihat_saldo()
        elif pilihan == "2":
            tambah_pemasukan()
        elif pilihan == "3":
            tambah_pengeluaran()
        elif pilihan == "4":
            print("Keluar. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1 sampai 4.")


if __name__ == "__main__":
    main_menu()

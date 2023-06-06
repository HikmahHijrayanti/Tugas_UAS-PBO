
# Tugas UAS Mata Kuliah Pemrograman Berorientasi Objek(PBO)


Pemrograman berorientasi objek merupakan paradigma pemrograman berdasarkan konsep "objek", yang dapat berisi data, dalam bentuk field atau dikenal juga sebagai atribut; serta kode, dalam bentuk fungsi/prosedur atau dikenal juga sebagai method.


## Anggota Kelompok

- G1A022026 | Hikmah Hijrayanti
- G1A022070 | Shalaudin Muhammad Sah
- G1A022072 | Yuda Reyvandra

## Penjelasan Source Code

```bash
import tkinter as tk # mengimpor modul tkinter sebagai tk untuk membuat GUI
import time #mengimpor modul time untuk mengatur waktu dalam aplikasi

# Mendefinisikan daftar_menu yang berisi beberapa menu makanan beserta harganya
daftar_menu = {     
    1: {"nama": "Nasi Goreng", "harga": 15000},
    2: {"nama":  "Pecel Lele", "harga": 10000},
    3: {"nama": "Ayam Bakar", "harga": 12000},
    4: {"nama": "Ayam Geprek", "harga": 10000},
    5: {"nama": "Ayam Goreng", "harga": 10000},
    6: {"nama": "Nilla Goreng", "harga": 10000},
    7: {"nama": "Mie Goreng", "harga": 8000},
    8: {"nama": "Mie Rebus", "harga": 8000},
}
```

Pada gambar diatas merupakan kode program penggunaan modul tkinter 
pada Bahasa pemrograman python. Pada baris pertama kode, merupakan 
kode untuk mengimpor modul tkinter. Tkinter adalah modul bawaan Python 
yang digunakan untuk membuat antarmuka grafis (GUI). Modul ini 
berfungsi sebagai penghubung antara program Python dengan toolkit Tk, 
yang merupakan toolkit GUI yang populer dan kuat. Dan pada gambar 
diatas telah tersedia beberapa menu makanan yang bisa dipesan oleh user, 
dan pada daftar menu makanan tersebut juga telah tersedia harga pada 
masing-masing makanan.

```bash
# Mendefinisikan keranjang sebagai list kosong untuk menyimpan pesanan
keranjang = []

# Mendefinisikan fungsi tampilan_menu untuk menampilkan menu pada tampilan window
def tampilkan_menu():
    print("Daftar Menu:")
    print("============")
    for key, menu in daftar_menu.items():   #Memulai loop yang akan mengiterasi setiap elemen dalam dictionary daftar_menu
        print(f"{key}. {menu['nama']} - Rp{menu['harga']}") #Mencetak baris daftar menu.

#mendefinisikan fungsi tambah_pesanan(pilihan) untuk menambahkan pesanan ke keranjang
def tambah_pesanan(pilihan):
    menu = daftar_menu.get(pilihan)
    if menu:
        keranjang.append(menu) #menambahkan menu kedalam keranjang
        print(f"{menu['nama']} telah ditambahkan ke keranjang.")
    else:
        print("Menu tidak valid.")

#Mendefinisikan fungsi hapus_pesanan(pilihan) untuk menghapus pesanan dari keranjang
def hapus_pesanan(pilihan):
    if pilihan > 0 and pilihan <= len(keranjang):
        menu = keranjang.pop(pilihan - 1)
        print(f"{menu['nama']} telah dihapus dari keranjang.")
    else:
        print("Pesanan tidak valid.")

#Mendefinisikan fungsi tampilkan_keranjang() untuk menampilkan isi keranjang pesanan pada window
def tampilkan_keranjang():
    print("Keranjang Pesanan:")
    print("==================")
    total_harga = 0
    if len(keranjang) > 0:
        for index, menu in enumerate(keranjang):
            print(f"{index+1}. {menu['nama']} - Rp{menu['harga']}")
            total_harga += menu['harga']
        print("Total Harga: Rp", total_harga)
    else:
        print("Keranjang kosong.")

```

Pada gambar diatas terdapat fungsi tampilkan_menu(): Fungsi ini 
digunakan untuk menampilkan daftar menu beserta harga. Fungsi ini akan 
mencetak nama menu dan harga yang disimpan dalam daftar_menu
menggunakan perulangan for. Lalu terdapat fungsi 
tambah_pesanan(pilihan): Fungsi ini digunakan untuk menambahkan 
pesanan ke dalam keranjang. Fungsi ini akan mengambil menu yang dipilih 
berdasarkan pilihan pengguna dari daftar_menu menggunakan metode 
.get(). Jika menu valid, maka menu tersebut akan ditambahkan ke dalam 
keranjang. Jika tidak valid, pesan "Menu tidak valid" akan dicetak. Lalu ada 
fungsi hapus_pesanan(pilihan): Fungsi ini digunakan untuk menghapus 
pesanan dari keranjang berdasarkan pilihan pengguna. Fungsi ini akan 
memeriksa apakah pilihan valid dengan membandingkannya dengan 
panjang keranjang. Jika pilihan valid, menu akan dihapus dari keranjang 
menggunakan metode .pop(). Jika pilihan tidak valid, pesan "Pesanan tidak 
valid" akan dicetak. Dan terakhir terdapat fungsi tampilkan_keranjang():
Fungsi ini digunakan untuk menampilkan isi keranjang pesanan beserta total 
harga. Fungsi ini akan mencetak menu-menu dalam keranjang 
menggunakan perulangan for dengan menggunakan fungsi enumerate()
untuk mengakses indeks dan elemen menu secara bersamaan. Selain itu, 
total harga akan dihitung dengan menjumlahkan harga dari setiap menu 
yang ada dalam keranjang. Jika keranjang kosong, pesan "Keranjang 
kosong" akan dicetak.

```bash
 # Membuat tampilan GUI
    main_frame = tk.Frame(root, bg="blue")
    main_frame.pack(padx=20, pady=20)

    # Label Daftar Menu
    menu_label = tk.Label(main_frame, text="Daftar Menu:", font=("Arial", 12), bg="blue", fg="white")
    menu_label.pack()

    # Button Tampilkan Menu
    tampilkan_menu_button = tk.Button(main_frame, text="Tampilkan Menu", command=tampilkan_menu_gui)
    tampilkan_menu_button.pack(pady=5)

    # Entry Nomor Menu
    nomor_menu_label = tk.Label(main_frame, text="Masukkan nomor menu:", font=("Arial", 12), bg="blue", fg="white")
    nomor_menu_label.pack()
    nomor_menu_entry = tk.Entry(main_frame)
    nomor_menu_entry.pack()

    # Button Tambah Pesanan
    tambah_pesanan_button = tk.Button(main_frame, text="Tambah Pesanan", command=tambah_pesanan_gui)
    tambah_pesanan_button.pack(pady=5)

    # Label Keranjang Pesanan
    keranjang_label = tk.Label(main_frame, text="Keranjang Pesanan:", font=("Arial", 12), bg="blue", fg="white")
    keranjang_label.pack()

    # Button Tampilkan Keranjang
    tampilkan_keranjang_button = tk.Button(main_frame, text="Tampilkan Keranjang", command=tampilkan_keranjang_gui)
    tampilkan_keranjang_button.pack(pady=5)

    # Entry Nomor Pesanan
    nomor_pesanan_label = tk.Label(main_frame, text="Masukkan nomor pesanan yang akan dihapus:", font=("Arial", 12), bg="blue", fg="white")
    nomor_pesanan_label.pack()
    nomor_pesanan_entry = tk.Entry(main_frame)
    nomor_pesanan_entry.pack()

    # Button Hapus Pesanan
    hapus_pesanan_button = tk.Button(main_frame, text="Hapus Pesanan", command=hapus_pesanan_gui)
    hapus_pesanan_button.pack(pady=5)

    # Menjalankan aplikasi
    root.mainloop()

#Menjalankan fungsi main() jika file ini dijalankan sebagai program utama
if __name__ == "__main__":
    main()

```

Pada gambar diatas terdapat kode main_frame = tk.Frame(root, 
bg="blue") main_frame.pack(padx=20, pady=20) pemrograman diatas 
untuk Frame utama dibuat dengan warna latar belakang biru dan diberi jarak 
padding pada setiap sisi menggunakan argumen Frame ini kemudian dipack ke dalam window utama. Lalu terdapat kode menu_label = 
tk.Label(main_frame, text="Daftar Menu:", font=("Arial", 12), bg="blue", 
fg="white") menu_label.pack() kode ini Label ini digunakan untuk 
menampilkan teks "Daftar Menu". Diberi warna latar belakang biru dan 
warna teks putih. Label ini juga diberi font Arial dengan ukuran 12. 
Kemudian terdapat tampilkan_menu_button = tk.Button(main_frame, 
text="TampilkanMenu",command=tampilkan_menu_gui)tampilkan_menu
_button.pack(pady=5) yang berfungsi sebagai Button yang digunakan untuk 
memanggil fungsi tampilkan_menu_gui ketika tombol ditekan. Label 
tombol ini adalah "Tampilkan Menu". Selanjutnya, nomor_menu_label = 
tk.Label(main_frame, text="Masukkan nomor menu:", font=("Arial", 12), 
bg="blue", fg="white"), nomor_menu_label.pack(), nomor_menu_entry = 
tk.Entry(main_frame), nomor_menu_entry.pack(). Label ini digunakan 
untuk memberikan petunjuk kepada pengguna untuk memasukkan nomor 
menu. Entry ini digunakan untuk pengguna memasukkan nomor menu 
secara interaktif. Lalu terdapat tambah_pesanan_button = 
tk.Button(main_frame,text="TambahPesanan",command=tambah_pesanan
_gui)tambah_pesanan_button.pack(pady=5) Button ini digunakan untuk 
memanggil fungsi tambah_pesanan_gui ketika tombol ditekan. Label 
tombol ini adalah "Tambah Pesanan". Kemudian, 
tampilkan_keranjang_button = tk.Button(main_frame, text="Tampilkan 
Keranjang",command=tampilkan_keranjang_gui)tampilkan_keranjang_bu
tton.pack(pady=5) Button ini digunakan untuk memanggil fungsi 
tampilkan_keranjang_gui ketika tombol ditekan. Label tombol ini adalah 
"Tampilkan Keranjang". Lalu terdapat, nomor_pesanan_label = 
tk.Label(main_frame, text="Masukkan nomor pesanan yang akan 
dihapus:",font=("Arial",12),bg="blue",fg="white"),nomor_pesanan_label.
pack(),nomor_pesanan_entry=tk.Entry(main_frame),nomor_pesanan_entr
12
y.pack(). Label ini digunakan untuk nomor pesanan yang akan dihapus. 
Entry ini digunakan untuk pengguna memasukkan nomor pesanan secara 
interaktif.

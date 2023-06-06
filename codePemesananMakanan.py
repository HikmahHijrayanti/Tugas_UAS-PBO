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

#Mendefinisikan fungsi main() sebagai entry point program:
def main():
    #Menampilkan pesan selamat datang dan judul aplikasi pada konsol
    print("Selamat datang di Aplikasi Pemesanan Makanan!")
    print("===========================================")

    #Membuat instance root sebagai objek Tkinter dan mengatur judul aplikasi dan latar belakang
    root = tk.Tk()
    root.title("Aplikasi Pemesanan Makanan")
    root.configure(background="blue")

    #Mendefinisikan fungsi tampilkan_menu_gui() untuk menampilkan daftar menu pada window
    def tampilkan_menu_gui():
        menu_text = "Daftar Menu:\n============\n"
        for key, menu in daftar_menu.items():
            menu_text += f"{key}. {menu['nama']} - Rp{menu['harga']}\n"
        menu_label.configure(text=menu_text)

    # Mendefinisikan fungsi tambah_pesanan_gui() untuk menambahkan pesanan ke keranjang pada window
    def tambah_pesanan_gui():
        nomor_menu = int(nomor_menu_entry.get())
        tambah_pesanan(nomor_menu)
        tampilkan_keranjang_gui()

    #Mendefinisikan fungsi hapus_pesanan_gui() untuk menghapus pesanan dari keranjang pada window
    def hapus_pesanan_gui():
        nomor_pesanan = int(nomor_pesanan_entry.get())
        hapus_pesanan(nomor_pesanan)
        tampilkan_keranjang_gui()

    #Mendefinisikan fungsi tampilkan_keranjang_gui() untuk menampilkan isi keranjang pesanan pada window
    def tampilkan_keranjang_gui():
        keranjang_text = "Keranjang Pesanan:\n==================\n"
        total_harga = 0
        if len(keranjang) > 0:
            for index, menu in enumerate(keranjang):
                keranjang_text += f"{index+1}. {menu['nama']} - Rp{menu['harga']}\n"
                total_harga += menu['harga']
            keranjang_text += "Total Harga: Rp" + str(total_harga)
        else:
            keranjang_text = "Keranjang kosong."
        
        keranjang_label.configure(text=keranjang_text)

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

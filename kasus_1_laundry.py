
class TagihanLaundry:
    # Konstruktor
    def __init__(self, nama_pelanggan, jenis_layanan, berat_cucian):
        # Validasi jenis layanan
        if jenis_layanan.lower() not in ["reguler", "kilat"]:
            raise ValueError("Jenis layanan harus Reguler atau Kilat!")

        # Validasi berat cucian
        if berat_cucian <= 0:
            raise ValueError("Berat cucian harus lebih dari 0 kg!")

        self.nama_pelanggan = nama_pelanggan
        self.jenis_layanan = jenis_layanan.capitalize()
        self.berat_cucian = berat_cucian

    # Menentukan tarif per kg
    def get_tarif(self):
        if self.jenis_layanan == "Reguler":
            return 8000
        else:
            return 12000

    # Menghitung subtotal
    def hitung_subtotal(self):
        return self.berat_cucian * self.get_tarif()

    # Menentukan persentase diskon
    def hitung_diskon(self):
        if self.berat_cucian >= 10:
            return 0.15
        elif self.berat_cucian >= 5:
            return 0.10
        else:
            return 0

    # Menghitung nominal potongan
    def hitung_potongan(self):
        return self.hitung_subtotal() * self.hitung_diskon()

    # Menghitung total pembayaran
    def hitung_total(self):
        return self.hitung_subtotal() - self.hitung_potongan()

    # Mencetak nota pembayaran
    def cetak_nota(self):
        print("\n=== NOTA PEMBAYARAN LAUNDRY ===")
        print(f"Pelanggan    : {self.nama_pelanggan}")
        print(
            f"Layanan      : {self.jenis_layanan} "
            f"(Rp{self.get_tarif():,.0f}/kg)"
        )
        print(f"Berat        : {self.berat_cucian:g} kg")
        print(f"Subtotal     : Rp{self.hitung_subtotal():,.0f}")
        print(f"Diskon       : {self.hitung_diskon():.0%}")
        print(f"Potongan     : Rp{self.hitung_potongan():,.0f}")
        print(f"Total Bayar  : Rp{self.hitung_total():,.0f}")


# Program utama
print("=== LAUNDRY CLEAN & FRESH ===")

nama = input("Nama pelanggan : ")
layanan = input("Jenis layanan  : ")

try:
    berat = float(input("Berat cucian   : "))

    laundry = TagihanLaundry(nama, layanan, berat)
    laundry.cetak_nota()

except ValueError as e:
    print("Input tidak valid:", e)

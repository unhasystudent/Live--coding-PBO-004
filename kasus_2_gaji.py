class Gajikaryawan:
    def __init__(self, id_karyawan, nama, jam_kerja):

        if not 1 <= jam_kerja <= 80:
            raise ValueError(
                "jam kerja harus antara 1 sampai 80 jam!"
            )

        self.id_karyawan = id_karyawan
        self.nama = nama
        self.jam_kerja = jam_kerja

        self.tarif_dasar = 30000
        self.tarif_lembur = 45000

    def hitung_gaji_pokok(self):
        jam_reguler = min(self.jam_kerja, 40)
        return jam_reguler * self.tarif_dasar

    def hitung_gaji_lembur(self) :
        jam_lembur = max(self.jam_kerja - 40, 0)
        return jam_lembur * self.tarif_lembur

    def hitung_gaji_kotor(self):
        return(
            self.hitung_gaji_pokok()
            + self.hitung_gaji_lembur()
        )
    def hitung_pajak(self):
        gaji_kotor = self.hitung_gaji_kotor()

        if gaji_kotor >= 1500000:
            return gaji_kotor * 0.05
        else:
            return 0

    def hitung_gaji_bersih(self):
        return (
            self.hitung_gaji_kotor()
            - self.hitung_pajak()
        )

    def cetakk_slip_gaji(self):
        jam_reguler = min(self.jam_kerja, 40)
        jam_lembur = max(self.jam_kerja - 40, 0)

        print("\n========== SLIP GAJI KARYAWAN ==========")
        print(f"ID karyawan : {self.id_karyawan}")
        print(f"Nama        : {self.nama}")
        print(f"total jam   : {self.jam_kerja} jam")
        print(f"__________________________________")

        print(
            f"jam reguler : {jam_reguler} jam "
            f"(Rp{self.hitung_gaji_pokok():,.0f})"
        )
        print(
            f"jam lembur : {jam_lembur} jam "
            f"(Rp{self.hitung_gaji_lembur():,.0f})"
        )
        print("__________________________________")
        print(f"gaji kotor : Rp{self.hitung_gaji_kotor():,.0f}")
        print(f"pajak      : Rp{self.hitung_pajak():,.0f}")
        print(f"gaji bersih : Rp{self.hitung_gaji_bersih():,.0f}")
        print("=====================================")

print("=== SISTEM PENGGAJIAN KARYAWAN ===")

id_karyawan = input("ID karyawan : ")
nama = input("nama        : ")

try:
    jam_kerja = int(input("jam kerja : "))

    karyawan = Gajikaryawan(
        id_karyawan,
        nama,
        jam_kerja
    )
    karyawan.cetakk_slip_gaji()

except ValueError as e:
    print("input tidak valid:", e)

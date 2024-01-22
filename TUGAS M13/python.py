import heapq

class Graf:
    def __init__(self):
        self.graf = {}

    def tambah_sisi(self, u, v, berat):
        if u not in self.graf:
            self.graf[u] = []
        if v not in self.graf:
            self.graf[v] = []
        self.graf[u].append((v, berat))
        self.graf[v].append((u, berat))  # Mengasumsikan graf tidak berarah

    def dijkstra(self, awal, akhir):
        antrian_prioritas = [(0, awal)]
        dikunjungi = set()

        while antrian_prioritas:
            (jarak_saat_ini, simpul_saat_ini) = heapq.heappop(antrian_prioritas)

            if simpul_saat_ini in dikunjungi:
                continue

            dikunjungi.add(simpul_saat_ini)

            if simpul_saat_ini == akhir:
                return jarak_saat_ini

            for (tetangga, berat) in self.graf[simpul_saat_ini]:
                if tetangga not in dikunjungi:
                    heapq.heappush(antrian_prioritas, (jarak_saat_ini + berat, tetangga))

        return float('inf')  # Tidak ada jalur yang ditemukan

# Contoh Penggunaan:
graf = Graf()
graf.tambah_sisi('A', 'B', 1)
graf.tambah_sisi('A', 'C', 4)
graf.tambah_sisi('B', 'C', 2)
graf.tambah_sisi('B', 'D', 5)
graf.tambah_sisi('C', 'D', 1)
graf.tambah_sisi('D', 'E', 7)

simpul_awal = 'A'
simpul_akhir = 'E'

jarak_terpendek = graf.dijkstra(simpul_awal, simpul_akhir)

if jarak_terpendek != float('inf'):
    print(f"Jarak terpendek dari {simpul_awal} ke {simpul_akhir} adalah: {jarak_terpendek}")
else:
    print(f"Tidak ada jalur dari {simpul_awal} ke {simpul_akhir}")

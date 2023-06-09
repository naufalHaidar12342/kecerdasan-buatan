from PIL import Image
import sys

peta_jateng_dfs = {
    "Pekalongan": ["Kendal"],
    "Kendal": ["Pekalongan", "Semarang"],
    "Semarang": ["Kendal", "Salatiga", "Purwodadi", "Kudus"],
    "Kudus": ["Semarang", "Purwodadi", "Jepara", "Rembang"],
    "Jepara": ["Rembang"],
    "Rembang": ["Blora", "Purwodadi", "Kudus"],
    "Blora": ["Purwodadi", "Kudus", "Rembang"],
    "Purwodadi": ["Kudus", "Blora", "Surakarta", "Semarang"],
    "Salatiga": ["Semarang", "Boyolali", "Magelang"],
    "Magelang": ["Salatiga"],
    "Boyolali": ["Surakarta", "Salatiga"],
    "Surakarta": ["Boyolali", "Purwodadi"],
}


def readable_city(peta):
    return ", ".join(peta.keys())


def dfs(peta, kota_asal, kota_tujuan, visited=None):
    if visited is None:
        visited = set()
    visited.add(kota_asal)
    if kota_asal == kota_tujuan:
        print("kota asal=", [kota_asal])
        return [kota_asal]
    for tetangga in peta[kota_asal]:
        if tetangga not in visited:
            jalur = dfs(peta, tetangga, kota_tujuan, visited)
            if jalur:
                print("jalur=", [kota_asal] + jalur)
                return [kota_asal] + jalur


def shows_peta_jateng():
    try:
        img = Image.open("pertemuan-4\peta_jateng.jpeg")
        img.show()
    except FileNotFoundError:
        print("File tidak ditemukan. Silahkan cek kembali file path.")
        sys.exit(1)


def program_introduction():
    print("=====================================")
    print("DFS dengan Peta Jawa Tengah")
    print("Daftar kota: ", readable_city(peta_jateng_dfs))


def dfs_dynamic():
    print("\n")
    print("DFS dengan Peta Jawa Tengah secara dinamis")
    kota_asal = input("Masukkan kota asal: ")
    kota_tujuan = input("Masukkan kota tujuan: ")

    if kota_asal and kota_tujuan in peta_jateng_dfs.keys():
        rute_perjalanan = dfs(peta_jateng_dfs, kota_asal, kota_tujuan)
        if rute_perjalanan is not None:
            print("Jalur ditempuh dari {} ke {}: {}".format(
                kota_asal, kota_tujuan, " -> ".join(rute_perjalanan)))
        else:
            print("Tidak ada jalur dari {} ke {}".format(
                kota_asal, kota_tujuan), ". Silahkan coba dengan kota lain.")
    elif kota_asal not in peta_jateng_dfs.keys():
        print("Kota {} tidak ditemukan. Silahkan cek kembali daftar kota yang ada.".format(
            kota_asal))
    elif kota_tujuan not in peta_jateng_dfs.keys():
        print("Kota {} tidak ditemukan. Silahkan cek kembali daftar kota yang ada.".format(
            kota_tujuan))


def main_function():
    program_introduction()
    print(
        "Jalur ditempuh dari Semarang ke Surakarta:", " -> ".join(
            dfs(peta_jateng_dfs, "Semarang", "Surakarta"))
    )
    shows_peta_jateng()
    # dfs_dynamic()


if __name__ == "__main__":
    main_function()

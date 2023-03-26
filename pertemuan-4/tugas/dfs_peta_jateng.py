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
    dictionary_key = []
    for key in peta.keys():
        dictionary_key.append(key)
    return ", ".join(dictionary_key)


def dfs(peta, kota_asal, kota_tujuan, visited=None):
    if visited is None:
        visited = set()
    visited.add(kota_asal)
    if kota_asal == kota_tujuan:
        return [kota_asal]
    for tetangga in peta[kota_asal]:
        if tetangga not in visited:
            jalur = dfs(peta, tetangga, kota_tujuan, visited)
            if jalur:
                return [kota_asal] + jalur


def human_readable_dfs_path(dfs_function):
    if dfs_function is not None:
        return " -> ".join(dfs_function)


def main_function():
    print("=====================================")
    print("DFS dengan Peta Jawa Tengah")
    print("Daftar kota: ", readable_city(peta_jateng_dfs))
    print(
        "jalur ditempuh dari Semarang ke Surakarta: ",
        dfs(peta_jateng_dfs, "Semarang", "Surakarta")
    )


if __name__ == "__main__":
    main_function()

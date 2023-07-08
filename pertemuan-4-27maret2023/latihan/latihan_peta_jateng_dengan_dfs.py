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

# fungsi depth first search dengan jalur yang ditempuh

# main function


def dfs(peta, kota_asal, kota_tujuan):
    antrian = [kota_asal]
    resultNode = []
    jalurNode = {}
    processNode = kota_tujuan


def dfs_wiki(peta, kota_asal, kota_tujuan, jalan_dicoba=set(), jalur_sejauh_ini=""):
    jalan_dicoba.add(kota_asal)
    if kota_asal == kota_tujuan:
        return jalur_sejauh_ini + kota_asal
    for kota in peta[kota_asal]:
        if kota not in jalan_dicoba:
            jalur = dfs_wiki(
                peta,
                kota,
                kota_tujuan,
                jalan_dicoba,
                jalur_sejauh_ini + kota_asal
            )
            if jalur:
                return jalur
    return ""


def dfs_custom(peta, kota_asal, kota_tujuan):
    jalur_ditempuh = set()
    jalur_sejauh_ini = ""
    jalur_ditempuh.add(kota_asal)
    if kota_asal == kota_tujuan:
        return jalur_sejauh_ini + " -> "+kota_asal
    for kota in peta[kota_asal]:
        if kota not in jalur_ditempuh:
            jalur = dfs_wiki(
                peta,
                kota,
                kota_tujuan,
                jalur_ditempuh,
                jalur_sejauh_ini + kota_asal
            )
            if jalur:
                return jalur
    return ""


def dfs_custom2(peta, kota_asal, kota_tujuan):
    jalur_ditempuh = set()
    jalur_sejauh_ini = ""
    jalur_ditempuh.add(kota_asal)
    if kota_asal == kota_tujuan:
        return jalur_sejauh_ini+kota_asal
    for kota in peta[kota_asal]:
        if kota not in jalur_ditempuh:
            jalur = dfs_wiki(
                peta,
                kota,
                kota_tujuan,
                jalur_ditempuh,
                jalur_sejauh_ini+kota_asal
            )
            if jalur:
                return jalur
    return ""


def dfs_custom3(peta, kota_asal, kota_tujuan, visited=None, path=""):
    if visited is None:
        visited = set()
    visited.add(kota_asal)
    path += kota_asal+""
    if kota_asal == kota_tujuan:
        return path.strip()
    for kota in peta[kota_asal]:
        if kota not in visited:
            jalur = dfs_custom3(peta, kota, kota_tujuan, visited, path)
            if jalur:
                return jalur
    return ""


def dfs_non_recursive(peta, kota_asal, kota_tujuan):
    visited = set()  # set to keep track of visited nodes
    # stack to keep track of nodes to visit and their path
    stack = [(kota_asal, [kota_asal])]

    while stack:
        (node, path) = stack.pop()  # pop the last element from stack
        if node not in visited:
            visited.add(node)  # add node to visited set
            if node == kota_tujuan:
                return path  # return path if goal node is reached

            # iterate over adjacent nodes and add them to stack
            for neighbor in peta[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None  # return None if goal node is not reachable from start node


def main():
    print("DFS dengan Peta Jawa Tengah")
    print("Kota asal: Semarang")
    print("Kota tujuan: Surakarta")
    print("Jalur yang ditempuh: ", dfs_wiki(
        peta_jateng_dfs, "Semarang", "Surakarta"))
    print("Jalur yang ditempuh: ", dfs_wiki(
        peta_jateng_dfs, "Semarang", "Surakarta", jalan_dicoba=set(), jalur_sejauh_ini=""))
    print("Jalur yang ditempuh: ", dfs_custom(
        peta_jateng_dfs, "Semarang", "Surakarta"))
    print("Jalur yang ditempuh: ", dfs_custom2(
        peta_jateng_dfs, "Semarang", "Surakarta"))
    print("Jalur yang ditempuh dfscustom3: ", dfs_custom3(
        peta_jateng_dfs, "Semarang", "Surakarta"))
    print("Jalur yang ditempuh: ", dfs_custom2(
        peta_jateng_dfs, "Semarang", "Surakarta"))
    print("Jalur yang ditempuh: ", dfs_non_recursive(
        peta_jateng_dfs, "Semarang", "Surakarta"))
    print("Jalur yang ditempuh: ", dfs_non_recursive(
        peta_jateng_dfs, "Semarang", "Surakarta"))


if __name__ == "__main__":
    main()

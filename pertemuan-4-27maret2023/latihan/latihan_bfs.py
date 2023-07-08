peta_jateng = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B", "I", "H", "D"],
    "D": ["C", "H", "E", "F"],
    "E": ["F"],
    "F": ["G", "H", "D"],
    "G": ["H", "D", "F"],
    "H": ["D", "G", "L", "C"],
    "I": ["C", "K", "J"],
    "J": ["I"],
    "K": ["L", "I"],
    "L": ["K", "H"],
}

# breadth first search function


def bfs(peta, mulai):
    antrian = [mulai]
    resultNode = []

    while antrian:
        prosesNode = antrian.pop(0)
        resultNode.append(prosesNode)
        for anak in peta[prosesNode]:
            if anak not in resultNode and anak not in antrian:
                antrian.append(anak)
    return resultNode


# sebelum ada goal/target  yang dituju
bfs(peta_jateng, "C")

# breadth first search function with target


def bfs_parsing(jalurNode, mulai, tujuan):
    jalur = [tujuan]
    processNode = tujuan
    while processNode != mulai:
        processNode = jalurNode[processNode]
        jalur.append(processNode)
    # jalur.reverse()
    return jalur


def bfs_goal(peta, mulai, tujuan):
    antrian = [mulai]
    resultNode = []
    jalurNode = {}

    while antrian:
        prosesNode = antrian.pop(0)
        resultNode.append(prosesNode)
        for anak in peta[prosesNode]:
            if anak not in resultNode:
                antrian.append(anak)
                jalurNode[anak] = prosesNode
    print("jalur pencarian ala komputer = ", jalurNode)
    solusi = bfs_parsing(jalurNode, mulai, tujuan)
    print("solusi ala komputer = ", solusi)
    print("solusi ala manusia = ", solusi[::-1])


bfs_goal(peta_jateng, "C", "L")

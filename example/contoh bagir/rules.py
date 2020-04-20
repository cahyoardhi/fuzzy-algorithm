Ifuzzy_set = {
    'CPU': ['Lambat', 'Sedang', 'Cepat'],
    'Core': ['Kurang Optimal', 'Optimal', 'Sangat Optimal'],
    'RAM': ['Kecil', 'Standar', 'Besar']
}

Ofuzzy_set = {
    'Kelayakan': ['Biasa', 'Standar', 'Bagus']
}

DataMaxEntry = {
    'CPU': 4,
    'Core': 16,
    'RAM': 32
}

fuzzy_1_1, fuzzy_1_2, fuzzy_1_3 = 0, 0, 0
fuzzy_2_1, fuzzy_2_2, fuzzy_2_3 = 0, 0, 0
fuzzy_3_1, fuzzy_3_2, fuzzy_3_3 = 0, 0, 0


def cari_nilai_fuzzifikasi(key, category, value):

    if key == 'CPU':
        if category == 'Lambat':
            if value >= 0 and value <= 2:
                fuzzy_1_1 = 1
            elif 2 < value < 2.4:
                fuzzy_1_1 = (2.4 - value) / (2.4 - 2)
            else:
                fuzzy_1_1 = 0
            return ["Lambat", round(fuzzy_1_1, 1)]

        elif category == "Sedang":
            if value <= 2 or value >= 3:
                fuzzy_1_2 = 0
            elif 2 < value < 2.4:
                fuzzy_1_2 = (value - 2) / (2.4 - 2)
            elif 2.6 < value < 3:
                fuzzy_1_2 = (3 - value) / (3 - 2.6)
            elif 2.4 <= value <= 2.6:
                fuzzy_1_2 = 1
            return ["Sedang", round(fuzzy_1_2, 1)]

        elif category == "Cepat":
            if 2.6 < value < 3:
                fuzzy_1_3 = (value - 2.6) / (3 - 2.6)
            elif 3 <= value:
                fuzzy_1_3 = 1
            else:
                fuzzy_1_3 = 0
            return ["Cepat", round(fuzzy_1_3, 1)]

    elif key == "Core":
        if category == 'Kurang Optimal':
            if 0 <= value <= 1:
                fuzzy_2_1 = 1
            elif 1 < value < 2:
                fuzzy_2_1 = (2 - value) / (2-1)
            else:
                fuzzy_2_1 = 0
            return ["Kurang Optimal", fuzzy_2_1]

        elif category == "Optimal":
            if 1 < value < 2:
                fuzzy_2_2 = (value - 1) / (2 - 1)
            elif 2 <= value <= 4:
                fuzzy_2_2 = 1
            elif 4 < value < 5:
                fuzzy_2_2 = (5 - value) / (5 - 4)
            else:
                fuzzy_2_2 = 0
            return ["Optimal", fuzzy_2_2]

        if category == "Sangat Optimal":
            if 4 < value < 5:
                fuzzy_2_3 = (value - 4) / (5 - 4)
            elif value >= 5:
                fuzzy_2_3 = 1
            else:
                fuzzy_2_3 = 0
            return ["Sangat Optimal", fuzzy_2_3]

    elif key == "RAM":
        if category == 'Kecil':
            if 0 <= value <= 2:
                fuzzy_3_1 = 1
            elif 2 < value < 4:
                fuzzy_3_1 = (4 - value) / (4 - 2)
            else:
                fuzzy_3_1 = 0
            return ["Kecil", fuzzy_3_1]

        if category == "Standar":
            if 2 < value < 4:
                fuzzy_3_2 = (value - 2) / (4 - 2)
            elif 4 <= value <= 8:
                fuzzy_3_2 = 1
            elif 8 < value < 16:
                fuzzy_3_2 = (16 - value) / (16 - 8)
            else:
                fuzzy_3_2 = 0
            return ["Standar", fuzzy_3_2]

        if category == "Besar":
            if 8 < value < 16:
                fuzzy_3_3 = (value - 8) / (16 - 8)
            elif value >= 16:
                fuzzy_3_3 = 1
            else:
                fuzzy_3_3 = 0
            return ["Besar", fuzzy_3_3]


def fuzzy_rules(cpuType, cpuValue, coreType, coreValue, ramType, ramValue):

    # Kondisi CPU Lambat
    if cpuType == "Lambat" and coreType == "Kurang Optimal" and ramType == "Kecil":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Kurang Optimal" and ramType == "Standar":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Kurang Optimal" and ramType == "Besar":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Lambat" and coreType == "Optimal" and ramType == "Kecil":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Optimal" and ramType == "Standar":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Optimal" and ramType == "Besar":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Lambat" and coreType == "Sangat Optimal" and ramType == "Kecil":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Sangat Optimal" and ramType == "Standar":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Lambat" and coreType == "Sangat Optimal" and ramType == "Besar":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]

    # Kondisi CPU Sedang
    if cpuType == "Sedang" and coreType == "Kurang Optimal" and ramType == "Kecil":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Kurang Optimal" and ramType == "Standar":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Kurang Optimal" and ramType == "Besar":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Sedang" and coreType == "Optimal" and ramType == "Kecil":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Optimal" and ramType == "Standar":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Optimal" and ramType == "Besar":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Sedang" and coreType == "Sangat Optimal" and ramType == "Kecil":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Sangat Optimal" and ramType == "Standar":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Sedang" and coreType == "Sangat Optimal" and ramType == "Besar":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]

    # Kondisi CPU Cepat
    if cpuType == "Cepat" and coreType == "Kurang Optimal" and ramType == "Kecil":
        return ["Biasa", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Kurang Optimal" and ramType == "Standar":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Kurang Optimal" and ramType == "Besar":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Cepat" and coreType == "Optimal" and ramType == "Kecil":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Optimal" and ramType == "Standar":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Optimal" and ramType == "Besar":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
        #
    if cpuType == "Cepat" and coreType == "Sangat Optimal" and ramType == "Kecil":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Sangat Optimal" and ramType == "Standar":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]
    if cpuType == "Cepat" and coreType == "Sangat Optimal" and ramType == "Besar":
        return ["Bagus", min(cpuValue, coreValue, ramValue)]

#     # rules:
#     # IF CPU = Lambat AND Core = Kurang Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Kurang Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Kurang Optimal AND RAM = Besar THEN Kelayakan = Biasa

#     # IF CPU = Lambat AND Core = Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Optimal AND RAM = Besar THEN Kelayakan = Biasa

#     # IF CPU = Lambat AND Core = Sangat Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Sangat Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Lambat AND Core = Sangat Optimal AND RAM = Besar THEN Kelayakan = Biasa

#     # 2

#     # IF CPU = Sedang AND Core = Kurang Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Kurang Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Kurang Optimal AND RAM = Besar THEN Kelayakan = Biasa

#     # IF CPU = Sedang AND Core = Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Optimal AND RAM = Standar THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Optimal AND RAM = Besar THEN Kelayakan = Bagus

#     # IF CPU = Sedang AND Core = Sangat Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Sedang AND Core = Sangat Optimal AND RAM = Standar THEN Kelayakan = Bagus
#     # IF CPU = Sedang AND Core = Sangat Optimal AND RAM = Besar THEN Kelayakan = Bagus

#     # 3

#     # IF CPU = Cepat AND Core = Kurang Optimal AND RAM = Kecil THEN Kelayakan = Biasa
#     # IF CPU = Cepat AND Core = Kurang Optimal AND RAM = Standar THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Kurang Optimal AND RAM = Besar THEN Kelayakan = Bagus

#     # IF CPU = Cepat AND Core = Optimal AND RAM = Kecil THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Optimal AND RAM = Standar THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Optimal AND RAM = Besar THEN Kelayakan = Bagus

#     # IF CPU = Cepat AND Core = Sangat Optimal AND RAM = Kecil THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Sangat Optimal AND RAM = Standar THEN Kelayakan = Bagus
#     # IF CPU = Cepat AND Core = Sangat Optimal AND RAM = Besar THEN Kelayakan = Bagus

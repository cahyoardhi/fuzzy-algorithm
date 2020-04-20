# Input =
# CPU = [Lambat, sedang, cepat]
# Core = [Kurang Optimal, Optimal, sangat optimal]
# RAM = [Kecil, standar, besar]

# Output=
# Kelayakan = [biasa, standar, bagus]
# Input =
# CPU = [Lambat, sedang, cepat]
# Core = [Kurang Optimal, Optimal, sangat optimal]
# RAM = [Kecil, standar, besar]

# Output=
# Kelayakan = [biasa, standar, bagus]


import rules
import numpy as np
import matplotlib.pyplot as plt


def check(key, data):
    if(rules.DataMaxEntry[key] < data) or (data < 0):
        return False
    return True


def data_input():
    dataUser = []
    for key in rules.Ifuzzy_set:
        if key == 'CPU':
            entry = float(input(f'Masukkan {key}: '))
        else:
            entry = int(input(f'Masukkan {key}: '))
        if check(key, entry):
            dataUser.append(entry)
        else:
            print("Maaf inputan anda salah!")
            entry = float(input(f'Masukkan {key}: '))
    return dataUser


def fuzzifikasi(data, i):
    fuzzy = []
    for keys, values in rules.Ifuzzy_set.items():
        for value in values:
            x = rules.cari_nilai_fuzzifikasi(keys, value, data[i])
            fuzzy.append(x)
        i += 1
    return fuzzy


def inferensi(cpu, core, ram):
    inferens = []
    for cpuType, cpuValue in cpu:
        for coreType, coreValue in core:
            for ramType, ramValue in ram:
                inferens.append(rules.fuzzy_rules(
                    cpuType, cpuValue, coreType, coreValue, ramType, ramValue))
    return inferens


def defuzzifikasi(biasa, bagus, sample):
    tempBiasa, tempBagus, x, y = (0 for i in range(4))
    for i in range(0, 101, sample):
        if i <= 60:
            tempBiasa += i
            x += 1
        else:
            tempBagus += i
            y += 1

    x -= 1
    return ((tempBiasa * biasa) + (tempBagus * bagus)) / ((biasa * x) + (bagus * y))


if __name__ == "__main__":

    # fig = plt.figure(figsize=(6, 4))

    # # Inputan CPU
    # ax1 = fig.add_subplot(221)
    # t1 = [0, 1, 2, 2.4]
    # t2 = [1, 1, 1, 0]
    # x1 = [2, 2.4, 2.6, 3]
    # x2 = [0, 1, 1, 0]
    # z1 = [2.6, 3, 4]
    # z2 = [0, 1, 1]
    # plt.plot(t1, t2, label="Lambat")
    # plt.plot(x1, x2, label="Sedang")
    # plt.plot(z1, z2, label="Cepat")
    # plt.xlabel('GHz')
    # plt.ylabel('\u03BC')
    # plt.title("CPU", fontsize="12", color="red")
    # plt.legend()

    # # Inputan Core
    # ax2 = fig.add_subplot(222)
    # t1 = [*range(1, 6)]
    # t2 = [0, 1, 1, 1, 0]
    # x1 = [*range(0, 3)]
    # x2 = [1, 1, 0]
    # z1 = [*range(4, 7)]
    # z2 = [0, 1, 1]
    # plt.plot(x1, x2, label="Kurang Optimal")
    # plt.plot(t1, t2, label="Optimal")
    # plt.plot(z1, z2, label="Sangat Optimal")
    # plt.xlabel('Hz (Speed)')
    # plt.ylabel('\u03BC')
    # plt.title("Core", fontsize="12", color="red")
    # plt.legend()

    # # Inputan RAM
    # ax3 = fig.add_subplot(223)
    # t1 = [0, 1, 2, 4]
    # t2 = [1, 1, 1, 0]
    # x1 = [2, 4, 8, 16]
    # x2 = [0, 1, 1, 0]
    # z1 = [8, 16, 20]
    # z2 = [0, 1, 1]
    # plt.plot(t1, t2, label="Kecil")
    # plt.plot(x1, x2, label="Standard")
    # plt.plot(z1, z2, label="Besar")
    # plt.title("RAM", fontsize="12", color="red")
    # plt.xlabel('Gigabyte')
    # plt.ylabel('\u03BC')
    # plt.legend()

    # # Outputan Nilai Kelayakan
    # ax3 = fig.add_subplot(224)
    # t1 = [0, 50, 70]
    # t2 = [1, 1, 0]
    # x1 = [50, 70, 80]
    # x2 = [0, 1, 1]
    # plt.plot(t1, t2, label="Biasa")
    # plt.plot(x1, x2, label="Bagus")
    # plt.title("Nilai Kelayakan", fontsize="12", color="green")
    # plt.xlabel('Kualitas')
    # plt.ylabel('\u03BC')
    # plt.legend()

    # fig.tight_layout()
    # plt.show()

    i = 0
    data = data_input()
    nilai = fuzzifikasi(data, i)
    cpu, core, ram = ([] for i in range(3))
    for jenis, nilaiJenis in nilai:
        if jenis == "Lambat" or jenis == "Sedang" or jenis == "Cepat":
            cpu.append([jenis, nilaiJenis])
        if jenis == "Kurang Optimal" or jenis == "Optimal" or jenis == "Sangat Optimal":
            core.append([jenis, nilaiJenis])
        if jenis == "Kecil" or jenis == "Standar" or jenis == "Besar":
            ram.append([jenis, nilaiJenis])

    # Fuzzifikasi
    j = 0
    print(f'\nNilai Fuzzifikasi:')
    for keys, values in rules.Ifuzzy_set.items():
        print(f'{keys}: ')
        for value in values:
            if nilai[j] != 0:
                print(f'{value}: {nilai[j]}')
            j += 1

    # Inferensi
    temp, temp2, hasilAkhirInferensi = ([] for i in range(3))
    nilaiInferensi = inferensi(cpu, core, ram)

    for NK, nilai in nilaiInferensi:
        if NK == "Biasa":
            temp.append(nilai)
        else:
            temp2.append(nilai)

    inferensiBiasa = max(temp)
    inferensiBagus = max(temp2)

    hasilAkhirInferensi = [
        ["Biasa", inferensiBiasa],
        ["Bagus", inferensiBagus]
    ]
    print(f'\nHasil Inferensi: {hasilAkhirInferensi}\n')

    while True:
        sampleTitik = int(
            input("Masukkan Sample Titik dengan Syarat dapat dibagi 10: "))
        if sampleTitik % 10 != 0:
            print("Maaf inputan Anda Salah!")
        else:
            break

    # Defuzzifikasi
    nilaiDefuzzifikasi = defuzzifikasi(
        inferensiBiasa, inferensiBagus, sampleTitik)
    print(
        f'\nSample Titik: {sampleTitik}\nNilai Kelayakan: {nilaiDefuzzifikasi}')

import inferensi
# import defuzzyfikasi
import fuzzyfikasi


def main():

    print('\n\nPROGRAM PEGADAIAN EMAS BERBASIS FUZZY\n\n')
    print('KETENTUAN INPUTAN\n')
    print('berat\t\t: 0.5 gram - 2000 gram')
    print('Lama Pinjam\t: 1 bulan - 24 bulan')
    print('Harga\t\t: Rp 495.000 - Rp 1.783.200.000\n')
    print('Silakan memasukan input pada parameter-parameter berikut:\n')
    # berat   = float(input('berat (gram)\t\t: '))
    # lpinjam = int(input('lama pinjam (bulan)\t: '))
    # harga   = int(input('harga (rupiah)\t\t: '))

    berat = 900
    lpinjam = 13
    harga = 700000000

    fberat = fuzzyfikasi.ffuzzyfikasi(berat, 'berat')
    fpinjam = fuzzyfikasi.ffuzzyfikasi(lpinjam, 'lpinjam')
    fharga = fuzzyfikasi.ffuzzyfikasi(harga, 'harga')

    # print('\n\nHASIL FUZZYFIKASI\n')
    # print(f'Berat:')
    # for keys, values in fberat.items():
    #     if values != 0:
    #         print(f'{keys}: {values}')

    # print(f'Pinjam: ')
    # for keys, values in fpinjam.items():
    #     if values != 0:
    #         print(f'{keys}: {values}')

    # print(f'Harga: ')
    # for keys, values in fharga.items():
    #     if values != 0:
    #         print(f'{keys}: {values}')

    print('\n\nHASIL FUZZYFIKASI\n')
    print(f'Berat\t\t: {fberat}')
    print(f'Lama Pinjam\t: {fpinjam}')
    print(f'Harga\t\t: {fharga}\n')

    hinferensi = inferensi.finferensi(fberat, fpinjam, fharga)

    # names, values = hinferensi
    # i = 0
    # for index, name in enumerate(names):
    #     if values[i] != 0:
    #         print(f'{index+1}. {name}: {values[i]}')
    #     i += 1

    # print(f'\n\nHASIL INFERENSI\t: {hinferensi}')
    # print("\n\nHASIL INFERENSI\t: (['kecil','besar','besar','besar','besar','besar','besar','besar'], [0.2,0.2,0.42,0.33,0.2,0.2,0.33,0.5])")
    # print("HASIL AKHIR INFERENSI\t: (['besar','kecil'],[0.5,0.2]")


if __name__ == '__main__':
    main()

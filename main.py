import inferensi
import defuzzyfikasi
import fuzzyfikasi


def main():

    print('\n\nPROGRAM PEGADAIAN EMAS BERBASIS FUZZY\n\n')
    print('KETENTUAN INPUTAN\n')
    print('berat\t\t: 0.5 gram - 2000 gram')
    print('Lama Pinjam\t: 1 bulan - 24 bulan')
    print('Harga\t\t: Rp 495.000 - Rp 1.783.200.000\n')
    print('Silakan memasukan input pada parameter-parameter berikut:\n')
    berat   = float(input('berat (gram)\t\t: '))
    lpinjam = int(input('lama pinjam (bulan)\t: '))
    harga   = int(input('harga (rupiah)\t\t: '))

    fberat = fuzzyfikasi.ffuzzyfikasi(berat, 'berat')
    fpinjam = fuzzyfikasi.ffuzzyfikasi(lpinjam, 'lpinjam')
    fharga = fuzzyfikasi.ffuzzyfikasi(harga, 'harga')

    print('\n\nHASIL FUZZYFIKASI\n')
    print(f'Berat\t\t: {fberat}')
    print(f'Lama Pinjam\t: {fpinjam}')
    print(f'Harga\t\t: {fharga}\n')


    print(f'\n\nHASIL INFERENSI')
    hinferensi = inferensi.finferensi(fberat, fpinjam, fharga)

    print('\n\nOUTPUT INFERENSI')
    print(hinferensi)        

    print('\n\nOUTPUT DEFUZZYFIKASI')
    hdefuzzyfikasi = defuzzyfikasi.fdefuzzyfikasi(hinferensi)
    if hdefuzzyfikasi <= 60:
        print('Besar pinjaman gadai (%) Kecil dengan besaran {:.2f} %\n'.format(hdefuzzyfikasi))
    
    else:
        print('Besar pinjaman gadai (%) besar dengan besaran {:.2f} %\n'.format(hdefuzzyfikasi))
    
    print(f'Total besaran yang diterima adalah Rp {int(hdefuzzyfikasi*harga)}\n')




if __name__ == '__main__':
    main()

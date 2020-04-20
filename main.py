import inferensi
import defuzzyfikasi
import fuzzyfikasi

def main():

    print('PROGRAM PEGADAIAN EMAS BERBASIS FUZZY\n\n')
    print('Silakan memasukan input pada parameter-parameter berikut:\n')
    berat   = float(input('berat (gram)\t\t: '))
    lpinjam = int(input('lama pinjam (bulan)\t: '))
    harga   = int(input('harga (rupiah)\t\t: '))

    fberat  = fuzzyfikasi.fberat(berat)    
    fpinjam = fuzzyfikasi.flpinjam(lpinjam)    
    fharga  = fuzzyfikasi.fharga(harga)
    
    print('\n\nBerikut ini status derajat keanggotaan tiap inputan:')
    print(f'{fberat}\n')
    print(f'{fpinjam}\n')
    print(f'{fharga}\n')
    
    hinferensi = inferensi(fberat,fpinjam,fharga)

if __name__ == '__main__':
    main()
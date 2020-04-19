import inferensi
import defuzzyfikasi
import fuzzyfikasi

def main():

    print('PROGRAM PEGADAIAN EMAS BERBASIS FUZZY\n\n')
    print('Silakan memasukan input pada parameter-parameter berikut:\n')
    berat   = float(input('berat (gram)\t\t: '))
    lpinjam = int(input('lama pinjam (bulan)\t: '))
    harga   = int(input('harga (rupiah)\t\t: '))

    fberat  = fuzzyfikasi.fdberat(berat)    
    fpinjam = fuzzyfikasi.fdlpinjam(lpinjam)    
    fharga  = fuzzyfikasi.fdharga(harga)
    
    print('\n\nBerikut ini status derajat keanggotaan tiap inputan:')
    print(f'Berat: {berat} gram,\tAnggota : {fberat.values()},\tDerajat : {fberat.keys()}')
    print(f'Lama Pinjam: {lpinjam} bulan,\tAnggota : {fpinjam.values()},\tDerajat : {fpinjam.keys()}')
    print(f'Harga: {harga} Rupiah,\tAnggota : {fharga.values()},\tDerajat : {fharga.keys()}')

if __name__ == '__main__':
    main()
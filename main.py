import inferensi
import defuzzyfikasi
import fuzzyfikasi

def main():

    print('PROGRAM PEGADAIAN EMAS BERBASIS FUZZY\n\n')
    print('Silakan memasukan input pada parameter-parameter berikut:\n')
    berat   = float(input('berat (gram)\t\t: '))
    lpinjam = int(input('lama pinjam (bulan)\t: '))
    harga   = int(input('harga (rupiah)\t\t: '))

    fberat      = fuzzyfikasi.ffuzzyfikasi(berat,'berat')
    fpinjam     = fuzzyfikasi.ffuzzyfikasi(lpinjam,'lpinjam')
    fharga      = fuzzyfikasi.ffuzzyfikasi(harga,'harga')
    hinferensi  = inferensi.finferensi(fberat,fpinjam,fharga)

    fuzzyfikasi.outputhasil(fberat,fpinjam,fharga)
    print(hinferensi)
    
    



if __name__ == '__main__':
    main()
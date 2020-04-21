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

    fuzzyfikasi.outputhasil(fberat,fpinjam,fharga)
    out = inferensi.finferensi(fberat,fpinjam,fharga)
    print(out)
    
    



if __name__ == '__main__':
    main()
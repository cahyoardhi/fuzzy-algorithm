import main
import inferensi
import defuzzyfikasi

#Fuzzy set
fuzzyset = {
    'berat'     : { 'ringan'    : {'a': None, 'b' : 0.5, 'c' : 100, 'd' : 200},
                    'sedang'    : {'a': 100, 'b' : 200, 'c' : 500, 'd' : 1000},
                    'berat'     : {'a': 500, 'b' : 1000, 'c': 2000, 'd': None}
                    },



    'lpinjaman' : { 'sebentar'  : {'a': None, 'b' : 1, 'c' : 6, 'd' : 10},
                    'menengah'  : {'a': 6, 'b' : 10, 'c' : 12, 'd' : 15},
                    'lama'      : {'a': 12, 'b' : 15, 'c': 24, 'd': None}
                    },



    'harga'     : { 'rendah'    : {'a': None, 'b' : 495000, 'c' : 89300000, 'd' : 178600000},
                    'menengah'  : {'a': 89300000, 'b' : 178600000, 'c' : 445800000, 'd' : 891600000},
                    'tinggi'    : {'a': 445800000, 'b' : 891600000, 'c': 1783200000, 'd': None}
                    },



    'bpg'       : { 'sedikit'   : {'a': None, 'b' : 25, 'c' : 50, 'd' : 60},
                    'menengah'  : {'a': 50, 'b' : 60, 'c' : 70, 'd' : 80},
                    'besar'     : {'a': 70, 'b' : 80, 'c': 90, 'd': None}
                    },
}





def fberat(masukan):
    output = {}

    #ringan
    if masukan >= fuzzyset['berat']['ringan']['b'] and masukan <= fuzzyset['berat']['ringan']['d']:
        if masukan >= fuzzyset['berat']['ringan']['b'] and masukan <= fuzzyset['berat']['ringan']['c']:
            output['ringan'] = 1
        
        else:
            output['ringan'] = (fuzzyset['berat']['ringan']['d'] - masukan) / (fuzzyset['berat']['ringan']['d'] - fuzzyset['berat']['ringan']['c'])
    
    #sedang
    if masukan >= fuzzyset['berat']['sedang']['a'] and masukan <= fuzzyset['berat']['sedang']['d']:
        if masukan >= fuzzyset['berat']['sedang']['b'] and masukan <= fuzzyset['berat']['sedang']['c']:
            output['sedang'] = 1
        
        if masukan >= fuzzyset['berat']['sedang']['a'] and masukan <= fuzzyset['berat']['sedang']['b']:
            output['sedang'] = (masukan - fuzzyset['berat']['sedang']['a']) / (fuzzyset['berat']['sedang']['b'] - fuzzyset['berat']['sedang']['a'])

        if masukan >= fuzzyset['berat']['sedang']['c'] and masukan <= fuzzyset['berat']['sedang']['d']:
            output['sedang'] = (fuzzyset['berat']['sedang']['d'] - masukan) / (fuzzyset['berat']['sedang']['d'] - fuzzyset['berat']['sedang']['c'])
    
    #berat
    if masukan >= fuzzyset['berat']['berat']['a'] and masukan <= fuzzyset['berat']['berat']['c']:
        if masukan >= fuzzyset['berat']['berat']['b'] and masukan <= fuzzyset['berat']['berat']['c']:
            output['berat'] = 1
        
        if masukan >= fuzzyset['berat']['berat']['a'] and masukan <= fuzzyset['berat']['berat']['b']:
            output['berat'] = (masukan - fuzzyset['berat']['berat']['a']) / (fuzzyset['berat']['berat']['b'] - fuzzyset['berat']['berat']['a'])
    
    return output





def flpinjam(masukan):
    output = {}

    #sebentar
    if masukan >= fuzzyset['lpinjaman']['sebentar']['b'] and masukan <= fuzzyset['lpinjaman']['sebentar']['d']:
        if masukan >= fuzzyset['lpinjaman']['sebentar']['b'] and masukan <= fuzzyset['lpinjaman']['sebentar']['c']:
            output['sebentar'] = 1
        
        else:
            output['sebentar'] = (fuzzyset['lpinjaman']['sebentar']['d'] - masukan) / (fuzzyset['lpinjaman']['sebentar']['d'] - fuzzyset['lpinjaman']['sebentar']['c'])
    
    #menengah
    if masukan >= fuzzyset['lpinjaman']['menengah']['a'] and masukan <= fuzzyset['lpinjaman']['menengah']['d']:
        if masukan >= fuzzyset['lpinjaman']['menengah']['b'] and masukan <= fuzzyset['lpinjaman']['menengah']['c']:
            output['menengah'] = 1
        
        if masukan >= fuzzyset['lpinjaman']['menengah']['a'] and masukan <= fuzzyset['lpinjaman']['menengah']['b']:
            output['menengah'] = (masukan - fuzzyset['lpinjaman']['menengah']['a']) / (fuzzyset['lpinjaman']['menengah']['b'] - fuzzyset['lpinjaman']['menengah']['a'])

        if masukan >= fuzzyset['lpinjaman']['menengah']['c'] and masukan <= fuzzyset['lpinjaman']['menengah']['d']:
            output['menengah'] = (fuzzyset['lpinjaman']['menengah']['d'] - masukan) / (fuzzyset['lpinjaman']['menengah']['d'] - fuzzyset['lpinjaman']['menengah']['c'])
    
    #lama
    if masukan >= fuzzyset['lpinjaman']['lama']['a'] and masukan <= fuzzyset['lpinjaman']['lama']['c']:
        if masukan >= fuzzyset['lpinjaman']['lama']['b'] and masukan <= fuzzyset['lpinjaman']['lama']['c']:
            output['lama'] = 1
        
        if masukan >= fuzzyset['lpinjaman']['lama']['a'] and masukan <= fuzzyset['lpinjaman']['lama']['b']:
            output['lama'] = (masukan - fuzzyset['lpinjaman']['lama']['a']) / (fuzzyset['lpinjaman']['lama']['b'] - fuzzyset['lpinjaman']['lama']['a'])
    
    return output





def fharga(masukan):
    output = {}

    #rendah
    if masukan >= fuzzyset['harga']['rendah']['b'] and masukan <= fuzzyset['harga']['rendah']['d']:
        if masukan >= fuzzyset['harga']['rendah']['b'] and masukan <= fuzzyset['harga']['rendah']['c']:
            output['rendah'] = 1
        
        else:
            output['rendah'] = (fuzzyset['harga']['rendah']['d'] - masukan) / (fuzzyset['harga']['rendah']['d'] - fuzzyset['harga']['rendah']['c'])
    
    #menengah
    if masukan >= fuzzyset['harga']['menengah']['a'] and masukan <= fuzzyset['harga']['menengah']['d']:
        if masukan >= fuzzyset['harga']['menengah']['b'] and masukan <= fuzzyset['harga']['menengah']['c']:
            output['menengah'] = 1
        
        if masukan >= fuzzyset['harga']['menengah']['a'] and masukan <= fuzzyset['harga']['menengah']['b']:
            output['menengah'] = (masukan - fuzzyset['harga']['menengah']['a']) / (fuzzyset['harga']['menengah']['b'] - fuzzyset['harga']['menengah']['a'])

        if masukan >= fuzzyset['harga']['menengah']['c'] and masukan <= fuzzyset['harga']['menengah']['d']:
            output['menengah'] = (fuzzyset['harga']['menengah']['d'] - masukan) / (fuzzyset['harga']['menengah']['d'] - fuzzyset['harga']['menengah']['c'])
    
    #tinggi
    if masukan >= fuzzyset['harga']['tinggi']['a'] and masukan <= fuzzyset['harga']['tinggi']['c']:
        if masukan >= fuzzyset['harga']['tinggi']['b'] and masukan <= fuzzyset['harga']['tinggi']['c']:
            output['tinggi'] = 1
        
        if masukan >= fuzzyset['harga']['tinggi']['a'] and masukan <= fuzzyset['harga']['tinggi']['b']:
            output['tinggi'] = (masukan - fuzzyset['harga']['tinggi']['a']) / (fuzzyset['harga']['tinggi']['b'] - fuzzyset['harga']['tinggi']['a'])
    
    return output





def outputhasil(berat,pinjam,harga):
    print('\n\nHASIL FUZZYFIKASI:')
    for i,((bk,bv), (pk,pv), (hk,hv)) in enumerate(zip(berat.items(), pinjam.items(), harga.items())):
        print(f'Berat\t{i+1}: {bk}\t {bv}')
        print(f'pinjam\t{i+1}: {pk}\t {pv}')
        print(f'harga\t{i+1}: {hk}\t {hv}\n')
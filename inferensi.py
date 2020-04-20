import main
import defuzzyfikasi
import fuzzyfikasi

def inferensi(berat,pinjaman,harga):
    '''
    IF IPK = BURUK AND G = KECIL THEN NK = RENDAH
    '''
    if berat.keys() == 'ringan' and pinjaman.keys()  == 'sebentar' and harga.keys() == 'rendah':
        bpg = 'sedikit'
    
    return bpg
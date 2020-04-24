import main
import fuzzyfikasi
import defuzzyfikasi



def finferensi(berat,pinjam,harga):
    output = {}
    for (bk,bv), (pk,pv), (hk,hv) in zip(berat.items(), pinjam.items(), harga.items()):
        #rule 1
        if bk == 'ringan' and pk == 'sebentar' and hk == 'rendah':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 2
        if bk == 'ringan' and pk == 'sebentar' and hk =='menengah':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 3
        if bk == 'ringan' and pk == 'sebentar' and hk =='tinggi':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 4
        if bk == 'ringan' and pk == 'menengah' and hk =='rendah':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 5
        if bk == 'ringan' and pk == 'menengah' and hk =='menengah':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 6
        if bk == 'ringan' and pk == 'menengah' and hk =='tinggi':            
            output['menengah'] = min(bv, pv, hv)

        #rule 7
        if bk == 'ringan' and pk == 'lama' and hk =='rendah':            
            output['menengah'] = min(bv, pv, hv)
        
        #rule 8
        if bk == 'ringan' and pk == 'lama' and hk =='menengah':            
            output['menengah'] = min(bv, pv, hv)
        
        #rule 9
        if bk == 'ringan' and pk == 'lama' and hk =='tinggi':            
            output['besar'] = min(bv, pv, hv)            
        
        #rule 10
        if bk == 'sedang' and pk == 'sebentar' and hk =='rendah':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 11
        if bk == 'sedang' and pk == 'sebentar' and hk =='menengah':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 12
        if bk == 'sedang' and pk == 'sebentar' and hk =='tinggi':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 13
        if bk == 'sedang' and pk == 'menengah' and hk =='rendah':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 14
        if bk == 'sedang' and pk == 'menengah' and hk =='menengah':            
            output['menengah'] = min(bv, pv, hv)
        
        #rule 15
        if bk == 'sedang' and pk == 'menengah' and hk =='tinggi':            
            output['menengah'] = min(bv, pv, hv)
        
        #rule 16
        if bk == 'sedang' and pk == 'lama' and hk =='rendah':            
            output['menengah'] = min(bv, pv, hv)
        
        #rule 17
        if bk == 'sedang' and pk == 'lama' and hk =='menengah':            
            output['menengah'] = min(bv, pv, hv)
        
        #rule 18
        if bk == 'sedang' and pk == 'lama' and hk =='tinggi':            
            output['besar'] = min(bv, pv, hv)
        
        #rule 19
        if bk == 'berat' and pk == 'sebentar' and hk =='rendah':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 20
        if bk == 'berat' and pk == 'sebentar' and hk =='menengah':            
            output['kecil'] = min(bv, pv, hv)
        
        #rule 21
        if bk == 'berat' and pk == 'sebentar' and hk =='tinggi':        
            output['kecil'] = min(bv, pv, hv)
        
        #rule 22
        if bk == 'berat' and pk == 'menengah' and hk =='rendah':            
            output['menengah'] = min(bv, pv, hv)
        
        #rule 23
        if bk == 'berat' and pk == 'menengah' and hk =='menengah':            
            output['menengah'] = min(bv, pv, hv)
        
        #rule 24
        if bk == 'berat' and pk == 'menengah' and hk =='tinggi':            
            output['besar'] = min(bv, pv, hv)
        
        #rule 25
        if bk == 'berat' and pk == 'lama' and hk =='rendah':            
            output['menengah'] = min(bv, pv, hv)
        
        #rule 26
        if bk == 'berat' and pk == 'lama' and hk =='menengah':            
            output['besar'] = min(bv, pv, hv)
        
        #rule 27
        if bk == 'berat' and pk == 'lama' and hk =='tinggi':
            output['besar'] = min(bv, pv, hv)
            

    return output




# def outputhasil(inputan):


            
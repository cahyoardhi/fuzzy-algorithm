def finferensi(berat, pinjam, harga):
    linguistik = []
    derajat = []

    
    for bk, bv in berat.items():
        for pk, pv in pinjam.items():
            for hk, hv in harga.items():

                # rule 1
                if bk == 'ringan' and pk == 'sebentar' and hk == 'rendah':
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 2
                if bk == 'ringan' and pk == 'sebentar' and hk == 'menengah':
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 3
                if bk == 'ringan' and pk == 'sebentar' and hk == 'tinggi':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 4
                if bk == 'ringan' and pk == 'menengah' and hk == 'rendah':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 5
                if bk == 'ringan' and pk == 'menengah' and hk == 'menengah':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 6
                if bk == 'ringan' and pk == 'menengah' and hk == 'tinggi':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 7
                if bk == 'ringan' and pk == 'lama' and hk == 'rendah':
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 8
                if bk == 'ringan' and pk == 'lama' and hk == 'menengah':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 9
                if bk == 'ringan' and pk == 'lama' and hk == 'tinggi':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 10
                if bk == 'sedang' and pk == 'sebentar' and hk == 'rendah':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 11
                if bk == 'sedang' and pk == 'sebentar' and hk == 'menengah':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 12
                if bk == 'sedang' and pk == 'sebentar' and hk == 'tinggi':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 13
                if bk == 'sedang' and pk == 'menengah' and hk == 'rendah':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))
                # rule 14
                if bk == 'sedang' and pk == 'menengah' and hk == 'menengah':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 15
                if bk == 'sedang' and pk == 'menengah' and hk == 'tinggi':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 16
                if bk == 'sedang' and pk == 'lama' and hk == 'rendah':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 17
                if bk == 'sedang' and pk == 'lama' and hk == 'menengah':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 18
                if bk == 'sedang' and pk == 'lama' and hk == 'tinggi':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 19
                if bk == 'berat' and pk == 'sebentar' and hk == 'rendah':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 20
                if bk == 'berat' and pk == 'sebentar' and hk == 'menengah':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 21
                if bk == 'berat' and pk == 'sebentar' and hk == 'tinggi':    
                    linguistik.append('kecil')                    
                    derajat.append(min(bv, pv, hv))

                # rule 22
                if bk == 'berat' and pk == 'menengah' and hk == 'rendah':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 23
                if bk == 'berat' and pk == 'menengah' and hk == 'menengah':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 24
                if bk == 'berat' and pk == 'menengah' and hk == 'tinggi':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 25
                if bk == 'berat' and pk == 'lama' and hk == 'rendah':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 26
                if bk == 'berat' and pk == 'lama' and hk == 'menengah':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))

                # rule 27
                if bk == 'berat' and pk == 'lama' and hk == 'tinggi':                    
                    linguistik.append('besar')                    
                    derajat.append(min(bv, pv, hv))                


    i = 0
    templinguistik = []
    tempderajat = []

    for index,nama in enumerate(linguistik):
        if derajat[i] != 0:
            templinguistik.append(nama)
            tempderajat.append(derajat[i])                        
            print(f'{index+1}. {nama}: {derajat[i]}')
        i += 1



    tkecil = []
    tbesar = []
    for li,de in zip (templinguistik,tempderajat):
        if li == 'kecil':
            tkecil.append(de)
        else:
            tbesar.append(de)    

    if tkecil == []:
        tkecil = [0,0]

    elif tbesar == []:
        tbesar = [0,0]
    
    kecil = max(tkecil)
    besar = max(tbesar)
    
    output = dict(kecil=kecil,besar=besar)

    return output

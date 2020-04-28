def ffuzzyfikasi(masukan,jenis):    

    #Menentukan jenis fuzzyfikasi
    if jenis == 'berat':
        fuzzyset = {
            'input'     : { 'keanggotaan1'  : {'a': 0.5, 'b' : 0.5, 'c' : 100, 'd' : 200},
                            'keanggotaan2'  : {'a': 100, 'b' : 200, 'c' : 500, 'd' : 1000},
                            'keanggotaan3'  : {'a': 500, 'b' : 1000, 'c': 2000, 'd': 2001}
                            },


            'keanggotaan':{ 'anggota1' : 'ringan',
                            'anggota2' : 'sedang',
                            'anggota3' : 'berat'
                            }
        }        


    elif jenis == 'lpinjam':
        fuzzyset = {
            'input'     : { 'keanggotaan1'  : {'a': 1, 'b' : 1, 'c' : 6, 'd' : 10},
                            'keanggotaan2'  : {'a': 6, 'b' : 10, 'c' : 12, 'd' : 15},
                            'keanggotaan3'  : {'a': 12, 'b' : 15, 'c': 24, 'd': 23}
                            },


            'keanggotaan':{ 'anggota1' : 'sebentar',
                            'anggota2' : 'menengah',
                            'anggota3' : 'lama'
                            }
        }        
    

    elif jenis == 'harga':
        fuzzyset = {
            'input'     : { 'keanggotaan1'  : {'a': 495000, 'b' : 495000, 'c' : 89300000, 'd' : 178600000},
                            'keanggotaan2'  : {'a': 89300000, 'b' : 178600000, 'c' : 445800000, 'd' : 891600000},
                            'keanggotaan3'  : {'a': 445800000, 'b' : 891600000, 'c': 1783200000, 'd': 1783200001}
                            },


            'keanggotaan':{ 'anggota1' : 'rendah',
                            'anggota2' : 'menengah',
                            'anggota3' : 'tinggi'
                            }
        }        


    output = {}

#keanggotaan1    
    if masukan >= fuzzyset['input']['keanggotaan1']['b'] and masukan <= fuzzyset['input']['keanggotaan1']['c']:            
        anggota = fuzzyset['keanggotaan']['anggota1']
        derajat = 1 
        output[anggota] = derajat

    if masukan <= fuzzyset['input']['keanggotaan1']['a'] or masukan >= fuzzyset['input']['keanggotaan1']['d']:
        anggota = fuzzyset['keanggotaan']['anggota1']
        derajat = 0
        output[anggota] = derajat
    
    if masukan >= fuzzyset['input']['keanggotaan1']['c'] and masukan <= fuzzyset['input']['keanggotaan2']['d']: 
        anggota = fuzzyset['keanggotaan']['anggota1']
        derajat = (fuzzyset['input']['keanggotaan1']['d'] - masukan) / (fuzzyset['input']['keanggotaan1']['d'] - fuzzyset['input']['keanggotaan1']['c'])
        if derajat < 0:
            derajat = 0

        output[anggota] = derajat



#keanggotaan2
    if masukan >= fuzzyset['input']['keanggotaan2']['b'] and masukan <= fuzzyset['input']['keanggotaan2']['c']:     
        anggota =  fuzzyset['keanggotaan']['anggota2']   
        derajat = 1    
        output[anggota] = derajat
    
    if masukan <= fuzzyset['input']['keanggotaan2']['a'] or masukan >= fuzzyset['input']['keanggotaan1']['d']:
        anggota = fuzzyset['keanggotaan']['anggota2']
        derajat = 0 
        output[anggota] = derajat

    if masukan >= fuzzyset['input']['keanggotaan2']['a'] and masukan <= fuzzyset['input']['keanggotaan2']['b']:      
        anggota = fuzzyset['keanggotaan']['anggota2']       
        derajat = (masukan - fuzzyset['input']['keanggotaan2']['a']) / (fuzzyset['input']['keanggotaan2']['b'] - fuzzyset['input']['keanggotaan2']['a'])
        if derajat < 0:
            derajat = 0        
        output[anggota] = derajat

    if masukan >= fuzzyset['input']['keanggotaan2']['c'] and masukan <= fuzzyset['input']['keanggotaan2']['d']: 
        anggota = fuzzyset['keanggotaan']['anggota2']
        derajat = (fuzzyset['input']['keanggotaan2']['d'] - masukan) / (fuzzyset['input']['keanggotaan2']['d'] - fuzzyset['input']['keanggotaan2']['c'])
        if derajat < 0:
            derajat = 0        

        output[anggota] = derajat                       



#keanggotaan3
    if masukan >= fuzzyset['input']['keanggotaan3']['b'] and masukan <= fuzzyset['input']['keanggotaan3']['c']:                                
        anggota = fuzzyset['keanggotaan']['anggota3']
        derajat = 1
        output[anggota] = derajat

    if masukan <= fuzzyset['input']['keanggotaan3']['a'] or masukan >= fuzzyset['input']['keanggotaan3']['d']:
        anggota = fuzzyset['keanggotaan']['anggota3']
        derajat = 0 
        output[anggota] = derajat
    
    if masukan >= fuzzyset['input']['keanggotaan3']['a'] and masukan <= fuzzyset['input']['keanggotaan3']['b']:                        
        anggota = fuzzyset['keanggotaan']['anggota3']
        derajat = (masukan - fuzzyset['input']['keanggotaan3']['a']) / (fuzzyset['input']['keanggotaan3']['b'] - fuzzyset['input']['keanggotaan3']['a'])
        if derajat < 0:
            derajat = 0        
        output[anggota] = derajat

    return output
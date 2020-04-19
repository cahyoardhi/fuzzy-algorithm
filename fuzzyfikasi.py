import main
import inferensi
import defuzzyfikasi

#Fuzzy set
fuzzy_set_berat     = ['ringan','sedang','berat']
fuzzy_set_lpinjam   = ['sebentar','menengah','lama']
fuzzy_set_harga     = ['murah','sedang','mahal']


#fungsi derajat keanggotaan berat
def fdberat(input):
    #ringan  
    if input >= 0.5 and input <=200:
        if input >= 0.5 and input <= 100:
            dberat = 1
            sberat = fuzzy_set_berat[0]            

        else:
            dberat = (200 - input) / (200-100)
            sberat = fuzzy_set_berat[0]

            #Jika derajat kurang dari 0.5, ganti keanggotaan
            if dberat < 0.5:
                dberat = (input - 100) / (200 - 100)
                sberat = fuzzy_set_berat[1]

    
    #sedang
    if input >= 100 and input <= 1000:
        if input >= 200 and input <= 500:
            dberat = 1
            sberat = fuzzy_set_berat[1]
        
        if input >= 100 and input <= 200:
            dberat = (input - 100) / (200 - 100)
            sberat = fuzzy_set_berat[1]

            #Jika derajat kurang dari 0.5, ganti keanggotaan
            if dberat < 0.5:
                dberat = (200 - input) / (200-100)
                sberat = fuzzy_set_berat[0]
        
        if input >= 500 and input <= 1000:
            dberat = (1000 - input) / (1000 - 500)
            sberat = fuzzy_set_berat[1]

            #Jika derajat kurang dari 0.5, ganti keanggotaan
            if dberat < 0.5:
                dberat = (input - 500) / (1000 - 500)
                sberat = fuzzy_set_berat[2]
    
    #berat
    if input >= 500 and input >= 1000:
        if input >= 1000:
            dberat = 1
            sberat = fuzzy_set_berat[2]
        
        if input >= input>=500 and input >= 1000:
            dberat = (input - 500) / (1000 - 500)
            sberat = fuzzy_set_berat[2]

            #Jika derajat kurang dari 0.5, ganti keanggotaan
            if dberat < 0.5:
                dberat = (1000 - input) / (1000 - 500)
                sberat = fuzzy_set_berat[1]


    output = {dberat:sberat}
    return  output





def fdlpinjam(input):
    #sebentar  
    if input >= 1 and input <= 9:
        if input >= 1 and input <= 8:
            dlpinjam = 1
            slpinjam = fuzzy_set_lpinjam[0]            

        else:
            dlpinjam = (9 - input) / (9-8)
            slpinjam = fuzzy_set_lpinjam[0]

            #Jika derajat kurang dari 0.5, ganti keanggotaan
            # if dlpinjam < 0.5:
            #     dlpinjam = (input - 8) / (9 - 8)
            #     slpinjam = fuzzy_set_lpinjam[1]

    
    #menengah
    if input >= 8 and input <= 17:
        if input >= 9 and input <= 16:
            dlpinjam = 1
            slpinjam = fuzzy_set_lpinjam[1]
        
        # if input >= 8 and input <= 9:
        #     dlpinjam = (input - 8) / (9 - 8)
        #     slpinjam = fuzzy_set_lpinjam[1]

            # #Jika derajat kurang dari 0.5, ganti keanggotaan
            # if dlpinjam < 0.5:
            #     slpinjam = (9 - input) / (9 - 8)
            #     slpinjam = fuzzy_set_lpinjam[0]
        
        # if input >= 16 and input <= 17:
        #     dlpinjam = (17 - input) / (17 - 16)
        #     slpinjam = fuzzy_set_lpinjam[1]

            # #Jika derajat kurang dari 0.5, ganti keanggotaan
            # if dlpinjam < 0.5:
            #     dlpinjam = (input - 16) / (17 - 16)
            #     slpinjam = fuzzy_set_lpinjam[2]
    
    #lama
    if input >= 16 and input <= 24:
        if input >= 17 and input <= 24:
            dlpinjam = 1
            slpinjam = fuzzy_set_lpinjam[2]
        
        # if input >= 16 and input <= 17:
        #     dlpinjam = (input - 16) / (17 - 16)
        #     slpinjam = fuzzy_set_lpinjam[2]

            # #Jika derajat kurang dari 0.5, ganti keanggotaan
            # if dlpinjam < 0.5:
            #     dlpinjam = (17 - input) / (17 - 16)
            #     slpinjam = fuzzy_set_lpinjam[1]


    output = {dlpinjam:slpinjam}
    return  output





def fdharga(input):
    #murah  
    if input >= 495000 and input <= 89300000:
        if input >= 495000 and input <= 89300000:
            dharga = 1
            sharga = fuzzy_set_harga[0]            

        else:
            dharga = (178600000 - input) / (178600000 - 89300000)
            sharga = fuzzy_set_lpinjam[0]

            #Jika derajat kurang dari 0.5, ganti keanggotaan
            if dharga < 0.5:
                dharga = (input - 89300000) / (178600000 - 89300000)
                sharga = fuzzy_set_harga[1]

    
    #sedang
    if input >= 889300000 and input <= 891600000:
        if input >= 178600000 and input <= 445800000:
            dharga = 1
            sharga = fuzzy_set_harga[1]
        
        if input >= 89300000 and input <= 178600000:
            dharga = (input - 89300000) / (178600000 - 89300000)
            sharga = fuzzy_set_harga[1]

            #Jika derajat kurang dari 0.5, ganti keanggotaan
            if dharga < 0.5:
                dharga = (178600000 - input) / (178600000 - 89300000)
                sharga = fuzzy_set_harga[0]
        
        if input >= 445800000 and input <= 891600000:
            dharga = (891600000 - input) / (891600000 - 445800000)
            sharga = fuzzy_set_harga[1]

            #Jika derajat kurang dari 0.5, ganti keanggotaan
            if dharga < 0.5:
                sharga = (input - 445800000) / (891600000 - 445800000)
                dharga = fuzzy_set_harga[2]
    
    #lama
    if input >= 445800000 and input >= 891600000:
        if input >= 891600000:
            dharga = 1
            sharga = fuzzy_set_harga[2]
        
        if input >= 445800000 and input <= 891600000:
            dharga = (input - 445800000) / (891600000 - 445800000)
            sharga = fuzzy_set_harga[2]

            #Jika derajat kurang dari 0.5, ganti keanggotaan
            if dharga < 0.5:
                dharga = (891600000 - input) / (891600000 - 445800000)
                sharga = fuzzy_set_harga[1]


    output = {dharga:sharga}
    return  output
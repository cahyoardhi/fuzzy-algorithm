import main
import inferensi
import defuzzyfikasi

#Fuzzy set
fuzzy_set_berat     = ['ringan','sedang','berat']
fuzzy_set_lpinjam   = ['sebentar','menengah','lama']
fuzzy_set_harga     = ['murah','sedang','mahal']


#fungsi derajat keanggotaan berat
def fdberat(masukan):
    dberat = []
    sberat = []

    #ringan  
    if masukan >= 0.5 and masukan <=200:
        if masukan >= 0.5 and masukan <= 100:
            dberat.append(1)
            sberat.append(fuzzy_set_berat[0])                    

        else:
            dberat.append((200 - masukan) / (200-100))            
            sberat.append(fuzzy_set_berat[0])

    #sedang
    if masukan >= 100 and masukan <= 1000:
        if masukan >= 200 and masukan <= 500:
            dberat.append(1)
            sberat.append(fuzzy_set_berat[1])                        
        
        if masukan >= 100 and masukan <= 200:
            dberat.append((masukan - 100) / (200 - 100))
            sberat.append(fuzzy_set_berat[1]))            

        if masukan >= 500 and masukan <= 1000:
            dberat.append((1000 - masukan))
            sberat.append(fuzzy_set_berat[1]))                                 

    #berat
    if masukan >= 500 and masukan >= 1000:
        if masukan >= 1000:
            dberat.append()
            temp.update(dict(dberat = 1,sberat = fuzzy_set_berat[2]))
                        
        
        if masukan >= masukan>=500 and masukan >= 1000:
            temp.update(dict(dberat = (masukan - 500) / (1000 - 500),sberat = fuzzy_set_berat[2]))
                        

    return  temp





# def fdlpinjam(masukan):
#     #sebentar  
#     if masukan >= 1 and masukan <= 9:
#         if masukan >= 1 and masukan <= 8:
#             dlpinjam = 1
#             slpinjam = fuzzy_set_lpinjam[0]            

#         else:
#             dlpinjam = (9 - masukan) / (9-8)
#             slpinjam = fuzzy_set_lpinjam[0]

#             #Jika derajat kurang dari 0.5, ganti keanggotaan
#             # if dlpinjam < 0.5:
#             #     dlpinjam = (masukan - 8) / (9 - 8)
#             #     slpinjam = fuzzy_set_lpinjam[1]

    
#     #menengah
#     if masukan >= 8 and masukan <= 17:
#         if masukan >= 9 and masukan <= 16:
#             dlpinjam = 1
#             slpinjam = fuzzy_set_lpinjam[1]
        
#         # if masukan >= 8 and masukan <= 9:
#         #     dlpinjam = (masukan - 8) / (9 - 8)
#         #     slpinjam = fuzzy_set_lpinjam[1]

#             # #Jika derajat kurang dari 0.5, ganti keanggotaan
#             # if dlpinjam < 0.5:
#             #     slpinjam = (9 - masukan) / (9 - 8)
#             #     slpinjam = fuzzy_set_lpinjam[0]
        
#         # if masukan >= 16 and masukan <= 17:
#         #     dlpinjam = (17 - masukan) / (17 - 16)
#         #     slpinjam = fuzzy_set_lpinjam[1]

#             # #Jika derajat kurang dari 0.5, ganti keanggotaan
#             # if dlpinjam < 0.5:
#             #     dlpinjam = (masukan - 16) / (17 - 16)
#             #     slpinjam = fuzzy_set_lpinjam[2]
    
#     #lama
#     if masukan >= 16 and masukan <= 24:
#         if masukan >= 17 and masukan <= 24:
#             dlpinjam = 1
#             slpinjam = fuzzy_set_lpinjam[2]
        
#         # if masukan >= 16 and masukan <= 17:
#         #     dlpinjam = (masukan - 16) / (17 - 16)
#         #     slpinjam = fuzzy_set_lpinjam[2]

#             # #Jika derajat kurang dari 0.5, ganti keanggotaan
#             # if dlpinjam < 0.5:
#             #     dlpinjam = (17 - masukan) / (17 - 16)
#             #     slpinjam = fuzzy_set_lpinjam[1]


#     output = {dlpinjam:slpinjam}
#     return  output





# def fdharga(masukan):
#     #murah  
#     if masukan >= 495000 and masukan <= 89300000:
#         if masukan >= 495000 and masukan <= 89300000:
#             dharga = 1
#             sharga = fuzzy_set_harga[0]            

#         else:
#             dharga = (178600000 - masukan) / (178600000 - 89300000)
#             sharga = fuzzy_set_lpinjam[0]

#             #Jika derajat kurang dari 0.5, ganti keanggotaan
#             if dharga < 0.5:
#                 dharga = (masukan - 89300000) / (178600000 - 89300000)
#                 sharga = fuzzy_set_harga[1]

    
#     #sedang
#     if masukan >= 889300000 and masukan <= 891600000:
#         if masukan >= 178600000 and masukan <= 445800000:
#             dharga = 1
#             sharga = fuzzy_set_harga[1]
        
#         if masukan >= 89300000 and masukan <= 178600000:
#             dharga = (masukan - 89300000) / (178600000 - 89300000)
#             sharga = fuzzy_set_harga[1]

#             #Jika derajat kurang dari 0.5, ganti keanggotaan
#             if dharga < 0.5:
#                 dharga = (178600000 - masukan) / (178600000 - 89300000)
#                 sharga = fuzzy_set_harga[0]
        
#         if masukan >= 445800000 and masukan <= 891600000:
#             dharga = (891600000 - masukan) / (891600000 - 445800000)
#             sharga = fuzzy_set_harga[1]

#             #Jika derajat kurang dari 0.5, ganti keanggotaan
#             if dharga < 0.5:
#                 sharga = (masukan - 445800000) / (891600000 - 445800000)
#                 dharga = fuzzy_set_harga[2]
    
#     #lama
#     if masukan >= 445800000 and masukan >= 891600000:
#         if masukan >= 891600000:
#             dharga = 1
#             sharga = fuzzy_set_harga[2]
        
#         if masukan >= 445800000 and masukan <= 891600000:
#             dharga = (masukan - 445800000) / (891600000 - 445800000)
#             sharga = fuzzy_set_harga[2]

#             #Jika derajat kurang dari 0.5, ganti keanggotaan
#             if dharga < 0.5:
#                 dharga = (891600000 - masukan) / (891600000 - 445800000)
#                 sharga = fuzzy_set_harga[1]


    # output = {dharga:sharga}
    # return  output
def fdefuzzyfikasi(inputan):
    for k,v in inputan.items(): 
        if k == 'kecil':
            kecil = v
        else:
            besar = v
    
    tempbesar   = 0
    tempkecil   = 0
    x           = 0
    y           = 0

    for i in range(20,90,7):
        if i <= 60:
            tempkecil += i
            x += 1
        else:
            tempbesar += i
            y += 1
    x -=1
    return ((tempkecil * kecil) + (tempbesar * besar)) / ((kecil * x) + (besar * y))
        #((27+34+41+48+55)*0.2 + (62+69+76+83+90)*0.5) / ((0.5)*5 + (0.2)*5)    kasus 1
        #((45 + 50 + 55) * 0.75 + (60+65+70+75+80+85+90) * 0.25 / ((0.75)*3) + (0.25)*7)) kasus 2
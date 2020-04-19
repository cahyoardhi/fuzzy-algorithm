#include <conio.h>
#include <iostream>
#include <string>

using namespace std;

string namaNutrisi[3] = {"BURUK","CUKUP","BAIK"};
string namaCahaya[3] = {"KURANG","NORMAL","BANYAK"};
string namaKualitasAir[3] = {"ASAM","IDEAL","BASA"};
float nilaiNutrisi[8], nilaiCahaya[8], nilaiKualitasAir[8], nilaiKualitas[27];
int i, j, k, z;
char *kualitas[8];
float besarX = 0;
float besarY = 0;

// NUTRISI BURUK
float nutrisiBuruk(float nutrisi) {
    float nilainutrisiburuk = 0;
    if(nutrisi <= 500) {
        nilainutrisiburuk = 1;
    }
    else if((nutrisi > 500) && (nutrisi < 1000)) {
        nilainutrisiburuk = (1000 - nutrisi)/500;
    }
    else {
        nilainutrisiburuk = 0;
    }
	return nilainutrisiburuk;
}
// NUTRISI CUKUP
float nutrisiCukup(float nutrisi) {

    float nilainutrisicukup = 0;

    if (nutrisi < 1000) {

        nilainutrisicukup = (nutrisi - 500)/500;
	}

	else if((nutrisi > 500) && (nutrisi < 2000)) {
		nilainutrisicukup= (2000 - nutrisi)/1000;
	}
	else if ((nutrisi <= 500) || (nutrisi >= 2000)){
        nilainutrisicukup = 0;
	}
	else {
        nilainutrisicukup = 1;
	}
    return nilainutrisicukup;
}
// NUTRISI BAIK
float nutrisiBaik(float nutrisi) {
	float nilainutrisibaik = 0;
    if(nutrisi >= 2000) {
        nilainutrisibaik = 1;
    }
    else if((nutrisi < 2000) && (nutrisi > 1000)) {
        nilainutrisibaik = (nutrisi - 1000)/1000;
    }
    else {
        nilainutrisibaik=0;
    }
	return nilainutrisibaik;
}

// CAHAYA KURANG
float cahayaKurang(float cahaya) {
    float nilaicahayakurang = 0;
    if(cahaya<= 25) {
        nilaicahayakurang = 1;
    }
    else if((cahaya > 25) && (cahaya < 50)) {
        nilaicahayakurang = (50 - cahaya)/25;
    }
    else {
        nilaicahayakurang = 0;
    }
	return nilaicahayakurang;
}
// CAHAYA NORMAL
float cahayanormal(float cahaya) {
    float nilaicahayanormal = 0;
    if (cahaya < 50) {

        nilaicahayanormal = (cahaya - 25)/25;
	}

	else if((cahaya > 25) && (cahaya < 100)) {
		nilaicahayanormal= (100 - cahaya)/50;
	}
	else if ((cahaya <= 25) || (cahaya >= 100)){
        nilaicahayanormal = 0;
	}
	else {
        nilaicahayanormal = 1;
	}
    return nilaicahayanormal;
}
// CAHAYA BANYAK
float cahayabanyak(float cahaya) {
	float nilaicahayabanyak = 0;
    if(cahaya >= 100) {
        nilaicahayabanyak = 1;
    }
    else if((cahaya < 100) && (cahaya > 50)) {
        nilaicahayabanyak = (cahaya - 50)/50;
    }
    else {
        nilaicahayabanyak=0;
    }
	return nilaicahayabanyak;
}

// KUALITAS AIR
float kualitasairAsam(float kualitasAir) {
    float nilaikualitasairasam = 0;
    if(kualitasAir <= 5) {
        nilaikualitasairasam = 1;
    }
    else if((kualitasAir < 5.5) && (kualitasAir > 5)) {
        nilaikualitasairasam = (5.5 - kualitasAir)/0.5;
    }
    else if(kualitasAir >= 60) {
        nilaikualitasairasam = 0;
    }
	return nilaikualitasairasam;
}
// KUALITAS AIR IDEAL
float kualitasairideal(float kualitasAir) {
    float nilaikualitasairideal = 0;
    if((kualitasAir >= 5.5) && (kualitasAir <= 6.5)) {
        nilaikualitasairideal = 1;
    }
    else if((kualitasAir > 5) && (kualitasAir < 5.5)) {
        nilaikualitasairideal = (kualitasAir - 5)/0.5;
    }
    else if((kualitasAir > 6.5) && (kualitasAir < 7.5)) {
        nilaikualitasairideal = (7.5 - kualitasAir)/1;
    }
    else if((kualitasAir <= 5) && (kualitasAir >= 7.5)) {
        nilaikualitasairideal = 0;
    }
    return nilaikualitasairideal;
}
// KUALITAS AIR BASA
float kualitasairbasa(float kualitasAir) {
	float nilaikualitasairbasa = 0;
    if(kualitasAir >= 7.5) {
        nilaikualitasairbasa = 1;
    }
    else if((kualitasAir < 7.5) && (kualitasAir > 6.5)) {
        nilaikualitasairbasa = (kualitasAir - 6.5)/1;
    }
    else if(kualitasAir <= 80) {
        nilaikualitasairbasa = 0;
    }
	return nilaikualitasairbasa;
}

void fuzzifikasi() {
	for(i=0; i<3; i++) {
		if(nilaiNutrisi[i] > 0) {
			cout << endl << "NUTRISI " << namaNutrisi[i] << " : " << nilaiNutrisi[i];
		}
	}
	for(i=0; i<3; i++) {
		if(nilaiCahaya[i] > 0) {
			cout << endl << " CAHAYA " << namaCahaya[i] << " : " << nilaiCahaya[i];
		}
	}
	for(i=0; i<3; i++) {
		if(nilaiKualitasAir[i] > 0) {
			cout << endl << "KUALITAS AIR " << namaKualitasAir[i] << " : " << nilaiKualitasAir[i];
		}
	}
}

void inferensi() {
    for(i=0; i<3; i++) {
        for(j=0; j<3; j++) {
            for(k=0; k<3; k++) {
                if((nilaiNutrisi[i] > 0) && (nilaiCahaya[j] > 0) && (nilaiKualitasAir[k] > 0)) {
                    if((nilaiNutrisi[i] < nilaiCahaya[j]) && (nilaiNutrisi[i] < nilaiKualitasAir[k])) {
                        nilaiKualitas[z] = nilaiNutrisi[i];
                    }
                    else if((nilaiKualitasAir[k] < nilaiCahaya[j]) && (nilaiKualitasAir[k] < nilaiNutrisi[i])) {
                        nilaiKualitas[z] = nilaiKualitasAir[k];
                    }
                    else if((nilaiCahaya[j] < nilaiNutrisi[i]) && (nilaiCahaya[j] < nilaiKualitasAir[k])) {
                        nilaiKualitas[z] = nilaiCahaya[j];
                    }
                    else if((nilaiNutrisi[i] == nilaiCahaya[j]) && (nilaiNutrisi[i] < nilaiKualitasAir[k])) {
                        nilaiKualitasAir[z] = nilaiNutrisi[i];
                    }
                    else if((nilaiNutrisi[i] == nilaiKualitasAir[k]) && (nilaiNutrisi[i] < nilaiCahaya[j])) {
                        nilaiKualitas[z] = nilaiNutrisi[i];
                    }
                    else if((nilaiCahaya[j] == nilaiKualitasAir[k]) && (nilaiNutrisi[i] > nilaiKualitasAir[k])) {
                        nilaiKualitas[z] = nilaiKualitasAir[k];
                    }
                    else if((nilaiNutrisi[i] == nilaiCahaya[j]) && (nilaiKualitasAir[k] < nilaiCahaya[j])) {
                        nilaiKualitas[z] = nilaiKualitasAir[k];
                    }
                    else if((nilaiNutrisi[i] == nilaiKualitasAir[k]) && (nilaiNutrisi[i] > nilaiCahaya[j])) {
                        nilaiKualitas[z] = nilaiCahaya[j];
                    }
                    else if((nilaiCahaya[j] == nilaiKualitasAir[k]) && (nilaiNutrisi[i] < nilaiCahaya[j])) {
                        nilaiKualitas[z] = nilaiNutrisi[i];
                    }
                    else {
                        nilaiKualitas[z] = nilaiKualitasAir[k];
                    }
                    // RULES
                    if((i==0) && (j==0) && (k==0)) { kualitas[z] = "JELEK"; }            // RULE 1
                    else if((i==0) && (j==0) && (k==2)) { kualitas[z] = "JELEK"; }       // RULE 2
                    else if((i==0) && (j==0) && (k==1)) { kualitas[z] = "JELEK"; }       // RULE 3
                    else if((i==0) && (j==1) && (k==0)) { kualitas[z] = "JELEK"; }       // RULE 4
                    else if((i==0) && (j==1) && (k==1)) { kualitas[z] = "UNGGUL"; }     // RULE 5
                    else if((i==0) && (j==1) && (k==2)) { kualitas[z] = "JELEK"; }       // RULE 6
                    else if((i==0) && (j==2) && (k==0)) { kualitas[z] = "JELEK"; }      // RULE 7
                    else if((i==0) && (j==2) && (k==1)) { kualitas[z] = "UNGGUL"; }    // RULE 8
                    else if((i==0) && (j==2) && (k==2)) { kualitas[z] = "JELEK"; }       // RULE 9
                    else if((i==1) && (j==0) && (k==0)) { kualitas[z] = "JELEK"; }       // RULE 10
                    else if((i==1) && (j==0) && (k==1)) { kualitas[z] = "UNGGUL"; }    // RULE 11
                    else if((i==1) && (j==0) && (k==2)) { kualitas[z] = "JELEK"; }       // RULE 12
                    else if((i==1) && (j==1) && (k==0)) { kualitas[z] = "UNGGUL"; }    // RULE 13
                    else if((i==1) && (j==1) && (k==1)) { kualitas[z] = "UNGGUL"; }    // RULE 14
                    else if((i==1) && (j==1) && (k==2)) { kualitas[z] = "UNGGUL"; }    // RULE 15
                    else if((i==1) && (j==2) && (k==0)) { kualitas[z] = "UNGGUL"; }    // RULE 16
                    else if((i==1) && (j==2) && (k==1)) { kualitas[z] = "UNGGUL"; }    // RULE 17
                    else if((i==1) && (j==2) && (k==2)) { kualitas[z] = "UNGGUL"; }    // RULE 18
                    else if((i==2) && (j==0) && (k==0)) { kualitas[z] = "JELEK"; }       // RULE 19
                    else if((i==2) && (j==0) && (k==1)) { kualitas[z] = "UNGGUL"; }       // RULE 20
                    else if((i==2) && (j==0) && (k==2)) { kualitas[z] = "JELEK"; }       // RULE 21
                    else if((i==2) && (j==1) && (k==0)) { kualitas[z] = "UNGGUL"; }       // RULE 22
                    else if((i==2) && (j==1) && (k==1)) { kualitas[z] = "UNGGUL"; }    // RULE 23
                    else if((i==2) && (j==1) && (k==2)) { kualitas[z] = "UNGGUL"; }       // RULE 24
                    else if((i==2) && (j==2) && (k==0)) { kualitas[z] = "UNGGUL"; }       // RULE 25
                    else if((i==2) && (j==2) && (k==1)) { kualitas[z] = "UNGGUL"; }    // RULE 26
                    else if((i==2) && (j==2) && (k==2)) { kualitas[z] = "UNGGUL"; }       // RULE 27
                    cout << "Nutrisi : " << namaNutrisi[i]
                        << " Cahaya : " << namaCahaya[j]
                         << " Kualitas Air : " << namaKualitasAir[k]
                         << " Kualitas : " << kualitas[z]
                         << " Dengan Nilai : " << nilaiKualitas[z] << endl;
                    z = z + 1;
                }
            }
        }
    }
    for(i=0; i<=z; i++) {
        if(kualitas[i]=="UNGGUL") {
            if(i==0) {
                besarX = nilaiKualitas[i];
            }
            else {
                if(nilaiKualitas[i] > besarX) {
                    besarX = nilaiKualitas[i];
                }
            }
        }
        else if(kualitas[i]=="JELEK") {
            if(i==0) {
                besarY = nilaiKualitas[i];
            }
            else {
                if(nilaiKualitas[i] > besarY) {
                    besarY = nilaiKualitas[i];
                }
            }
        }

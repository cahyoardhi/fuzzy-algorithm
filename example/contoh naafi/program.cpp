#include <stdio.h>
#include <iostream>

using namespace std;
class Fuzzy {

 float memberIPKBuruk = 0;
 float memberIPKCukup = 0;
 float memberIPKBagus = 0;
 float memberGajiKecil = 0;
 float memberGajiSedang = 0;
 float memberGajiBesar = 0;
 float memberGajiSgtBesar = 0;
 float terbesarX, terbesarY;

public:

 //keanggotaan IPK
 void anggotaIPK(float inputIPK) {
  if (inputIPK <= 2.0) {
   memberIPKBuruk = 1;
  }
  else {
   if (inputIPK < 2.75) {
    memberIPKBuruk = (float)((-inputIPK + 2.75) / 0.75);
   }
   else memberIPKBuruk = 0;
  }
  if ((inputIPK <= 2.0) || (inputIPK >= 3.25)) {
   memberIPKCukup = 0;
  }
  else {
   if (inputIPK > 2.0 && inputIPK < 2.75) {
    memberIPKCukup = (float)((inputIPK - 2) / 0.75);
   }
   else {
    if (inputIPK > 2.75 && inputIPK < 3.25) {
     memberIPKCukup = (float)((-inputIPK + 3.25) / 0.5);
    }
    else memberIPKCukup = 1;
   }
  }
  if (inputIPK <= 2.75) {
   memberIPKBagus = 0;
  }
  else {
   if (inputIPK > 2.75 && inputIPK < 3.25) {
    memberIPKBagus = (float)((inputIPK - 2.75) / 0.5);
   }
   else memberIPKBagus = 1;
  }
 }

 //Keanggotaan Gaji
 void anggotaGaji(float inputGaji) {
  if (inputGaji >= 3.0) {
   memberGajiKecil = 0;
  }
  else {
   if (inputGaji > 1.0 && inputGaji < 3.0) {
    memberGajiKecil = (float)((3.0 - inputGaji) / 2.0);
   }
   else memberGajiKecil = 1;
  }
  if ((inputGaji >= 6.0) || (inputGaji <= 1.0)) {
   memberGajiSedang = 0;
  }
  else {
   if (inputGaji > 1.0 && inputGaji < 3.0) {
    memberGajiSedang = (float)((inputGaji - 1) / 2.0);
   }
   else {
    if (inputGaji > 4.0 && inputGaji < 6.0) {
     memberGajiSedang = (float)((6.0 - inputGaji) / 2.0);
    }
    else memberGajiSedang = 1;
   }
  }
  if ((inputGaji >= 12.0) || (inputGaji <= 4.0)) {
   memberGajiBesar = 0;
  }
  else {
   if (inputGaji > 4.0 && inputGaji < 6.0) {
    memberGajiBesar = (float)((inputGaji - 4) / 2.0);
   }
   else {
    if (inputGaji > 7.0 && inputGaji < 12.0) {
     memberGajiBesar = (float)((12.0 - inputGaji) / 5.0);
    }
    else memberGajiBesar = 1;
   }
  }
  if (inputGaji <= 7.0) {
   memberGajiSgtBesar = 0;
  }
  else {
   if (inputGaji > 7.0 && inputGaji < 12.0) {
    memberGajiSgtBesar = (float)((inputGaji - 7.0) / 5.0);
   }
   else memberGajiSgtBesar = 1;
  }
 }

 void cetakMember() {
  cout << "\n\n----------PROSES FUZZIFIKASI----------\n" << endl;
  cout << "~Nilai Fuzzy IPK~" << endl;
  cout << "Buruk \n" << memberIPKBuruk << endl;
  cout << "Cukup \n" << memberIPKCukup << endl;
  cout << "Bagus \n" << memberIPKBagus << endl;
  cout << "\n\n~Nilai Fuzzy gaji~" << endl;
  cout << "Kecil \n" << memberGajiKecil << endl;
  cout << "Sedang \n" << memberGajiSedang << endl;
  cout << "Besar \n" << memberGajiBesar << endl;
  cout << "Sangat Besar \n" << memberGajiSgtBesar << endl;

 }
 void inferensi()
 {
  int k = 0;
  float nilaiKondisi[4];
  string kondisi[4];
  float nilaiIPK[3] = { memberIPKBuruk,memberIPKCukup,memberIPKBagus };
  float nilaiGaji[4] = { memberGajiKecil,memberGajiSedang,memberGajiBesar,memberGajiSgtBesar };

  //menentukan rules dan nilai minimum
  for (int i = 0; i < 3; i++)
  {
   for (int j = 0; j < 4; j++)
   {
    if ((nilaiIPK[i] > 0) && (nilaiGaji[j] > 0))
    {
     if (nilaiIPK[i] < nilaiGaji[j])
     {
      nilaiKondisi[k] = nilaiIPK[i];
     }
     else
     {
      nilaiKondisi[k] = nilaiGaji[j];
     }
     if ((i == 0) && (j >= 0))
     {
      kondisi[k] = "RENDAH";
     }
     else if ((i == 1) && (j >= 0))
     {
      kondisi[k] = "RENDAH";
     }
     else if ((i == 2) && (j > 2))
     {
      kondisi[k] = "RENDAH";
     }
     else
     {
      kondisi[k] = "TINGGI";
     }
     cout << "Ketika IPK " << nilaiIPK[i] << " dan GAJI " << nilaiGaji[j] << " maka Siswa " << kondisi[k] << " dengan nilai= " << nilaiKondisi[k] << endl;
     k = k + 1;
    }
   }
  }
  //menentukan nilai max
  for (int i = 0; i < k; i++)
  {
   if (kondisi[i] == "RENDAH")
   {
    if (i == 0)
    {
     terbesarX = nilaiKondisi[i];
    }
    else
    {
     if (nilaiKondisi[i] > terbesarX)
     {
      terbesarX = nilaiKondisi[i];
     }
    }
   }
   else
   {
    if (i == 0)
    {
     terbesarY = nilaiKondisi[i];
    }
    else
    {
     if (nilaiKondisi[i] > terbesarY)
     {
      terbesarY = nilaiKondisi[i];
     }
    }
   }
  }
  if (terbesarX > 0)
  {
   cout << endl << " Nilai siswa tidak BEASISWA \t= " << terbesarX << endl;
  }
  if (terbesarY > 0)
  {
   cout << endl << "Nilai dapat BEASISWA \t\t= " << terbesarY << endl;
  }
 }
float defuzzifikasi(int sampel){
            float pengaliX, pengaliY;
            float hasilPembilang = 0;
            float hasilPenyebut = 0;
            float hasilDefuzzifikasi;
            int titik_sampel = 0;
            float jumlah_sampelX = 0;
            float jumlah_sampelY = 0;
            float pengaliZ[100], titik_sampelZ[100];
            int delta = 0;
            int k = 0;
            pengaliX = terbesarX;
            pengaliY = terbesarY;
            delta = 100 / sampel;
            titik_sampel += delta;

            for(int i = 1;i <= sampel;i++){
                if(titik_sampel <= 50){
                    hasilPembilang += titik_sampel * pengaliX;
                    jumlah_sampelX += 1;
                }else if(titik_sampel >= 80){
                    hasilPembilang += titik_sampel * pengaliY;
                    jumlah_sampelY += 1;
                }else if((titik_sampel > 50) && (titik_sampel < 80)){
                    if (pengaliX > pengaliY){
                        titik_sampelZ[k] = titik_sampel;
                        pengaliZ[k] = (int) (((80
                                                - titik_sampelZ[k])/30)*1000);
                        pengaliZ[k] = (float)(pengaliZ[k]/1000);
                    hasilPembilang += titik_sampelZ[k] * pengaliZ[k];
                    }else{
                        titik_sampelZ[k] = titik_sampel;
                        pengaliZ[k] = (int)(((titik_sampelZ[k] - 50)/30)*1000);
                        pengaliZ[k] = (float)(pengaliZ[k]/1000);
                        hasilPembilang += titik_sampelZ[k] * pengaliZ[k];
                    }
                    k += 1;
                }
                    titik_sampel += delta;
            }
                hasilPenyebut = (jumlah_sampelX * pengaliX) + (jumlah_sampelY * pengaliY);
                for(int i = 0;i < k;i++){
                    hasilPenyebut += pengaliZ[i];
                }
                cout << "\nHasil Pembilang\t\t= " << hasilPembilang << endl;
                cout << "Hasil Penyebut\t\t= " << hasilPenyebut << endl;
                hasilDefuzzifikasi = hasilPembilang / hasilPenyebut;
                return hasilDefuzzifikasi;
}
};

int main() {
 float ipk, gaji;
 int sampel;
 float na;
 Fuzzy masuk;

 cout << "input data" << endl;
 cout << "IPK : "; cin >> ipk;
 cout << "GAJI : "; cin >> gaji;
 cout << "\n=====FUZZIFIKASI=====\n";
 masuk.anggotaIPK(ipk);
 masuk.anggotaGaji(gaji);
 masuk.cetakMember();
 cout << "\n=====INFERENSI=====\n";
 masuk.inferensi();
 cout << "\n=====DEFUZZIFIKASI=====\n";
cout<< "\nMasukkan jumlah sampel\t="; cin >> sampel;
cout << endl;
na = masuk.defuzzifikasi(sampel);
cout<< "Nilai Akhir \t\t= " << na;
 return 0;
}
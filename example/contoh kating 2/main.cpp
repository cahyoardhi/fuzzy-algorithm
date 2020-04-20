#include <iostream>
#include <conio.h>
#include <string>
#include <stdlib.h>

using namespace std;

string datakemiringan[4] = {"DATAR ", "LANDAI", "CURAM", "SANGAT CURAM"};
string datatinggiair[3] = {"NORMAL ", "SEDANG ", "TINGGI "};
string datavolume[3] = {"SEDIKIT", "CUKUP  ", "BANYAK "};

float nilaikemiringan[8], nilaitinggiair[6], nilaivolume[6], nilailevel[40];
int i, j, k, z, sampel;
char* datalevel[12];
float besarA = 0, besarB=0, besarC=0, besarD=0;

float datar(float kemiringan)
{
    float persentaseD = 0;

    if(kemiringan <= 8)
    {
        persentaseD = 1;
    }
    else if((kemiringan > 8) && (kemiringan < 11))
    {
        persentaseD = (11 - kemiringan)/(11 - 8);
    }
    else
    {
        persentaseD = 0;
    }
    return persentaseD;
}

float landai (float kemiringan)
{
    float persentaseL = 0;

    if((kemiringan >= 11) && (kemiringan <= 15))
    {
        persentaseL = 1;
    }
    else if((kemiringan > 8) && (kemiringan <11))
    {
        persentaseL = (kemiringan - 8)/(11 - 8);
    }
    else if((kemiringan > 15) && (kemiringan < 18))
    {
        persentaseL = (18 - kemiringan)/(18-11);
    }
    else
    {
        persentaseL = 0;
    }
    return persentaseL;
}

float curam(float kemiringan)
{
    float persentaseC = 0;

    if((kemiringan >= 18) && (kemiringan <= 32))
    {
        persentaseC = 1;
    }
    else if((kemiringan > 15) && (kemiringan < 18))
    {
        persentaseC = (kemiringan - 15)/(18 - 15);
    }
    else if((kemiringan > 32) && (kemiringan < 35))
    {
        persentaseC= (35 - kemiringan)/(35 - 32);
    }
    else
    {
        persentaseC = 0;
    }
    return persentaseC;
}

float sangatcuram(float kemiringan)
{
    float persentasiSC = 0;

    if(kemiringan >= 35)
    {
        persentasiSC = 1;
    }
    else if((kemiringan > 32) && (kemiringan < 35))
    {
        persentasiSC = (kemiringan - 32)/(35 - 32);
    }
    else
    {
        persentasiSC = 0;
    }
    return persentasiSC;
}

float normal(float tinggiair)
{
    float persentaseN = 0;

    if(tinggiair <= 10)
    {
        persentaseN = 1;
    }
    else if((tinggiair > 10) && (tinggiair < 20))
    {
        persentaseN = (20 - tinggiair)/(20 - 10);
    }
    else
    {
        persentaseN = 0;
    }
    return persentaseN;
}

float sedang(float tinggiair)
{
    float persentaseS = 0;

    if(tinggiair == 20)
    {
        persentaseS = 1;
    }
    else if((tinggiair > 10) && (tinggiair < 20))
    {
        persentaseS = (tinggiair - 10)/(20 - 10);
    }
    else if((tinggiair > 20) && (tinggiair < 30))
    {
        persentaseS = (30 - tinggiair)/(30 - 20);
    }
    else
    {
        persentaseS = 0;
    }
    return persentaseS;
}

float tinggi(float tinggiair)
{
    float persentaseT = 0;

    if(tinggiair >= 30)
    {
        persentaseT = 1;
    }
    else if((tinggiair > 20) && (tinggiair < 30))
    {
        persentaseT = (tinggiair - 20)/(30 - 20);
    }
    else
    {
        persentaseT = 0;
    }
    return persentaseT;
}

float sedikit(float volume)
{
    float persentaseSd = 0;

    if(volume <= 700000 )
    {
        persentaseSd = 1;
    }
    else if((volume > 700000) && (volume < 950000))
    {
        persentaseSd = (950000 - volume)/(950000 - 700000);
    }
    else
    {
        persentaseSd = 0;
    }
    return persentaseSd;
}

float cukup(float volume)
{
    float persentaseCkp = 0;

    if(volume == 950000)
    {
        persentaseCkp = 1;
    }
    else if((volume > 700000) && (volume < 950000))
    {
        persentaseCkp = ((volume - 700000)/(950000 - 700000));
    }
    else if((volume > 950000) && (volume < 1200000))
    {
        persentaseCkp = ((1200000 - volume)/(1200000 - 950000));
    }
    else
    {
        persentaseCkp = 0;
    }
    return persentaseCkp;
}

float banyak(float volume)
{
    float persentaseB = 0;

    if(volume >= 1200000)
    {
        persentaseB = 1;
    }
    else if((volume > 950000)  && (volume < 1200000))
    {
        persentaseB = ((volume - 950000)/(1200000 - 950000));
    }
    else
    {
        persentaseB = 0;
    }
    return persentaseB;
}

void fuzzifikasi()
{

    for(i=0; i < 4; i++)
    {
        if(nilaikemiringan[i] > 0)
        {
            cout << endl;
            cout << "Kemiringan yang  " << datakemiringan[i] << "  = " << nilaikemiringan[i];
        }
    }


    for(i=0; i < 3; i++)
    {
        if(nilaivolume[i] > 0)
        {
            cout << endl;
            cout << "Volume air yang  " << datavolume[i] << " = " << nilaivolume[i];
        }
    }


    for(i=0; i < 3; i++)
    {
        if(nilaitinggiair[i] > 0)
        {
            cout << endl;
            cout << "Tinggi air yang  " << datatinggiair[i] << " = " << nilaitinggiair[i];
        }
    }
}

void inferensi()
{
    for(i=0; i < 4; i++)
    {
        for(j=0; j < 3; j++)
        {
            for(k=0; k < 3; k++)
            {

                if((nilaikemiringan[i] > 0) && (nilaivolume[j] > 0) && (nilaitinggiair[k] > 0))
                {
                    if((nilaikemiringan[i] <= nilaivolume[j]) && (nilaikemiringan[i] <= nilaitinggiair[k]))
                    {
                        nilailevel[z] = nilaikemiringan[i];
                    }
                    else if((nilaivolume[j] <= nilaikemiringan[i]) && (nilaivolume[j] <= nilaitinggiair[k]))
                    {
                        nilailevel[z] = nilaivolume[j];
                    }
                    else if ((nilaitinggiair[k] <= nilaikemiringan[i]) && (nilaitinggiair[k] <= nilaivolume[j]))
                    {
                        nilailevel[z] = nilaitinggiair[k];
                    }


                    if((i==0) && (j==0) && (k==0))
                    {
                        datalevel[z] = "Siaga 4";
                    }
                    else if((i==0) && (j==0) && (k==1))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==0) && (j==0) && (k==2))
                    {
                        datalevel[z] = "Siaga 2";
                    }

                    else if((i==0) && (j==1) && (k==0))
                    {
                        datalevel[z] = "Siaga 4";
                    }
                    else if((i==0) && (j==1) && (k==1))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==0) && (j==1) && (k==2))
                    {
                        datalevel[z] = "Siaga 2";
                    }


                    else if((i==0) && (j==2) && (k==0))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==0) && (j==2) && (k==1))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==0) && (j==2) && (k==2))
                    {
                        datalevel[z] = "Siaga 2";
                    }


                    else if((i==1) && (j==0) && (k==0))
                    {
                        datalevel[z] = "Siaga 4";
                    }
                    else if((i==1) && (j==0) && (k==1))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==1) && (j==0) && (k==2))
                    {
                        datalevel[z] = "Siaga 2";
                    }


                    else if((i==1) && (j==1) && (k==0))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==1) && (j==1) && (k==1))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==1) && (j==1) && (k==2))
                    {
                        datalevel[z] = "Siaga 2";
                    }


                    else if((i==1) && (j==2) && (k==0))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==1) && (j==2) && (k==1))
                    {
                        datalevel[z] = "Siaga 2";
                    }
                    else if((i==1) && (j==2) && (k==2))
                    {
                        datalevel[z] = "Siaga 2";
                    }


                    else if((i==2) && (j==0) && (k==0))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==2) && (j==0) && (k==1))
                    {
                        datalevel[z] = "Siaga 2";
                    }
                    else if((i==2) && (j==0) && (k==2))
                    {
                        datalevel[z] = "Siaga 2";
                    }


                    else if((i==2) && (j==1) && (k==0))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==2) && (j==1) && (k==1))
                    {
                        datalevel[z] = "Siaga 2";
                    }
                    else if((i==2) && (j==1) && (k==2))
                    {
                        datalevel[z] = "Siaga 1";
                    }


                    else if((i==2) && (j==2) && (k==0))
                    {
                        datalevel[z] = "Siaga 3";
                    }
                    else if((i==2) && (j==2) && (k==1))
                    {
                        datalevel[z] = "Siaga 2";
                    }
                    else if((i==2) && (j==2) && (k==2))
                    {
                        datalevel[z] = "Siaga 1";
                    }


                    else if((i==3) && (j==0) && (k==0))
                    {
                        datalevel[z] = "Siaga 2";
                    }
                    else if((i==3) && (j==0) && (k==1))
                    {
                        datalevel[z] = "Siaga 1";
                    }
                    else if((i==3) && (j==0) && (k==2))
                    {
                        datalevel[z] = "Siaga 1";
                    }


                    else if((i==3) && (j==1) && (k==0))
                    {
                        datalevel[z] = "Siaga 2";
                    }
                    else if((i==3) && (j==1) && (k==1))
                    {
                        datalevel[z] = "Siaga 1";
                    }
                    else if((i==3) && (j==1) && (k==2))
                    {
                        datalevel[z] = "Siaga 1";
                    }


                    else if((i==3) && (j==2) && (k==0))
                    {
                        datalevel[z] = "Siaga 1";
                    }
                    else if((i==3) && (j==2) && (k==1))
                    {
                        datalevel[z] = "Siaga 1";
                    }
                    else if((i==3) && (j==2) && (k==2))
                    {
                        datalevel[z] = "Siaga 1";
                    }


                    cout << "Ketika Kemiringan " << datakemiringan[i]
                    << ", Dengan Volume Air " << datavolume[j]
                    << " Dan Tinggi Air " << datatinggiair[k]
                    << " Maka Tingkat Kesiagaaan adalah " << datalevel[z] << " Dengan Nilai = " << nilailevel[z] << endl;
                    z = z + 1;
                }
            }
        }
    }


    for(i=0; i <= z; i++)
    {
        if(datalevel[i]== "Siaga 4")
        {
            if(i==0)
            {
                besarA = nilailevel[i];
            }
            else
            {
                if(nilailevel[i] > besarA)
                {
                    besarA = nilailevel[i];
                }
            }
        }
        else if(datalevel[i]== "Siaga 3")
        {
            if(i==1)
            {
                besarB = nilailevel[i];
            }
            else
            {
                if(nilailevel[i] > besarB)
                {
                    besarB = nilailevel[i];
                }
            }
        }
        else if(datalevel[i]== "Siaga 2")
        {
            if(i==2)
            {
                besarC = nilailevel[i];
            }
            else
            {
                if(nilailevel[i] > besarC)
                {
                    besarC = nilailevel[i];
                }
            }
        }
        else if(datalevel[i]== "Siaga 1")
        {
            if(i==3)
            {
                besarD = nilailevel[i];
            }
            else
            {
                if(nilailevel[i] > besarD)
                {
                    besarD = nilailevel[i];
                }
            }
        }
    }
cout<<endl;

    if(besarA > 0)
    {
        cout << endl;
        cout << "Nilai Kelayakan dari Siaga 4 = " << besarA;
    }
    if(besarB > 0)
    {
        cout << endl;
        cout << "Nilai Kelayakan dari Siaga 3 = " << besarB;
    }
    if(besarC > 0)
    {
        cout << endl;
        cout << "Nilai Kelayakan dari Siaga 2 = " << besarC;
    }
    if(besarD > 0)
    {
        cout << endl;
        cout << "Nilai Kelayakan dari Siaga 1 = " << besarD;
    }
 /* cout<<"\n besar A = "<<besarA;
    cout<<"\n besar B = "<<besarB;
    cout<<"\n besar C = "<<besarC;
    cout<<"\n besar D = "<<besarD;
*/
}


float defuzzifikasi (int sampel)
{
 float hasilDefuzzifikasi, pengaliA, pengaliB, pengaliC, pengaliD;
 float jumlah_sampelD = 0, jumlah_sampelC = 0, jumlah_sampelB = 0, jumlah_sampelA = 0, hasilPembilang = 0, hasilPenyebut = 0;
 int titik_sampel = 0;
 float pengaliZ[200], titik_sampelZ[200];
 float delta = 0;

 z = 0;

 pengaliA = besarA;
 pengaliB = besarB;
 pengaliC = besarC;
 pengaliD = besarD;


 delta = 200 / sampel;
  titik_sampel += delta;

  for(i = 1;i <= sampel;i++)
    {
       if(titik_sampel <= 30)
       {
          hasilPembilang += titik_sampel * besarA;
          jumlah_sampelA += 1;
          //cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;
       }

       else if((titik_sampel > 30) && (titik_sampel < 50))
        {
            if(pengaliA > pengaliB)
                {
                   titik_sampelZ[z] = titik_sampel;
                    pengaliZ[z] = (int) (((50 - titik_sampelZ[z])/20)*200);
                    pengaliZ[z] = (float) (pengaliZ[z]/200);
                   hasilPembilang += titik_sampelZ[z] * pengaliZ[z];
                            // cout<<"\n pembilang"<<i<<" = "<<hasilPembilang<<"\n pengali = "<<pengaliZ[z];
                             z += 1;

                 }
                 else if((pengaliA==0)&&(pengaliB==0)){
                hasilPembilang += titik_sampelZ[z] * 0;
               // cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;
                 }
                else
                {
                  titik_sampelZ[z] = titik_sampel;
                  pengaliZ[z] = (int) (((titik_sampelZ[z] - 30)/20)*200);
                  pengaliZ[z] = (float) (pengaliZ[z]/200);
                  hasilPembilang += titik_sampelZ[z] * pengaliZ[z];
                         //   cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;
                            z += 1;

                }

        }
       else if((titik_sampel >= 50) && (titik_sampel <=100))
        {
          hasilPembilang += titik_sampel * pengaliB;
         // cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;
          jumlah_sampelB += 1;

        }

        else if((titik_sampel > 100) && (titik_sampel < 120))
        {
            if(pengaliB > pengaliC)
                {
                   titik_sampelZ[z] = titik_sampel;
                    pengaliZ[z] = (int) (((120 - titik_sampelZ[z])/20)*200);
                    pengaliZ[z] = (float) (pengaliZ[z]/200);
                   hasilPembilang += titik_sampelZ[z] * pengaliZ[z];
                            // cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;
                             z += 1;

                 }
                else
                {
                  titik_sampelZ[z] = titik_sampel;
                  pengaliZ[z] = (int) (((titik_sampelZ[z] - 100)/20)*200);
                  pengaliZ[z] = (float) (pengaliZ[z]/200);
                  hasilPembilang += titik_sampelZ[z] * pengaliZ[z];
                            //cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;

                            z += 1;
                }

        }

        else if((titik_sampel >= 120) && (titik_sampel <= 150))
        {
          hasilPembilang += titik_sampel * pengaliC;
          jumlah_sampelC += 1;
                    //cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;

        }

        else if((titik_sampel > 150) && (titik_sampel < 170))
        {
            if(pengaliC > pengaliD)
                {
                   titik_sampelZ[z] = titik_sampel;
                    pengaliZ[z] = (((170 - titik_sampelZ[z])/20)*200);
                    pengaliZ[z] = (pengaliZ[z]/200);

                   if(pengaliZ[z] > besarC)
                   {
                       pengaliZ[z]=besarC;
                   hasilPembilang += titik_sampelZ[z] * pengaliZ[z];

                   }
                             /*cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;
                             cout<<"\n pengali = "<<pengaliZ[z];
*/
                             z += 1;
                 }
                else
                {
                  titik_sampelZ[z] = titik_sampel;
                  pengaliZ[z] = (int) (((titik_sampelZ[z] - 150)/20)*200);
                  pengaliZ[z] = (float) (pengaliZ[z]/200);

                  if(pengaliZ[z] > besarC)
                   {
                       if (besarB>0)
                       {
                    pengaliZ[z] = besarC;
                   hasilPembilang += titik_sampelZ[z] * pengaliZ[z];

                       }

                   else if ( besarB==0)
                   {
                       hasilPembilang += titik_sampelZ[z] * pengaliZ[z];
                   }

                   }


                   /*   cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;
                    cout<<"\npengali = "<<pengaliZ[z];
*/
                            z += 1;
                }

        }

        else
        {
          hasilPembilang += titik_sampel * pengaliD;
          jumlah_sampelD += 1;
                    //cout<<"\n pembilang"<<i<<" = "<<hasilPembilang;

        }



    titik_sampel += delta;
  }
  hasilPenyebut = (jumlah_sampelA * pengaliA) + (jumlah_sampelB * pengaliB)+(jumlah_sampelC * pengaliC) + (jumlah_sampelD * pengaliD);

  for(i = 0;i < z;i++)
    {
      hasilPenyebut += pengaliZ[i];
    }
  cout << "\nHasil Pembilang\t\t= " << hasilPembilang << endl;
  cout << "Hasil Penyebut\t\t= " << hasilPenyebut << endl;

  hasilDefuzzifikasi = hasilPembilang / hasilPenyebut;
  return hasilDefuzzifikasi;
}

int main()
{
    float kemiringan, tinggiair, volume, na;
    char pilihsampel1, pilihsampel2;
    int sampel;
    menu0:
    cout << "\n\t\tPREDIKSI SISTEM BANJIR" << endl;
    cout << "=====================================================\n" << endl;
    cout << "Masukan Kemiringan (0 - 40)\t\t: ";
    cin >> kemiringan;
    cout << "Masukan Volume Air (0 - 1.500.000)\t: ";
    cin >> volume;
    cout << "Masukan Tinggi Air (0 - 40) \t\t: ";
    cin >> tinggiair;
    cout << endl << endl;


    nilaikemiringan[0] = datar(kemiringan);
    nilaikemiringan[1] = landai(kemiringan);
    nilaikemiringan[2] = curam(kemiringan);
    nilaikemiringan[3] = sangatcuram(kemiringan);

    nilaivolume[0] = sedikit(volume);
    nilaivolume[1] = cukup(volume);
    nilaivolume[2] = banyak(volume);

    nilaitinggiair[0] = normal(tinggiair);
    nilaitinggiair[1] = sedang(tinggiair);
    nilaitinggiair[2] = tinggi(tinggiair);


    cout << "\tFUZZIFIKASI" << endl;
    cout << "====================================================" << endl;
    fuzzifikasi();
    cout << endl << endl;
    system("pause");

    //Keterangan

    cout << "\tINFERENSI" << endl;
    cout << "====================================================" << endl;
    inferensi();
    cout << endl << endl;
    system("pause");

    cout << "\tDEFUZZIFIKASI" << endl;
    cout << "====================================================" << endl;
    menu1:
    cout<< "\n Masukkan jumlah sampel\t= ";
	cin >> sampel;
	cout << endl;
	na = defuzzifikasi(sampel);

	cout<< "Nilai Tinggi Air Banjir = " <<na<<" CM";
	cout<<"\n\n Ingin Input Ulang Sampel ? Pilih (y / n) : ";
	cin>>pilihsampel1;

	if(pilihsampel1=='y')
    {

        	goto menu1;

	}
	else
	{



            cout<<"\n====================================================\n";
            cout<<"\t\t TERIMA KASIH"<<endl;

	}

    cout<<endl;



}


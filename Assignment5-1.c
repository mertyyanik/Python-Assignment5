#include <stdio.h>

int main( int argc, char* argv[])
{
    int sayi = atoi(argv[1]);
    int sayac = 1;
    int azalis = sayi;
    int artis = sayi;
    int i,b,c;
    for(i=1;i<=sayi;i++){
        for(b=1;b<=sayi*2;b++){
            if(sayac == azalis){
                printf("/");
            }
            else{
                printf(" ");
            }
            if (sayac == artis){
                printf("\\");
            }
            
            sayac+=1;
        }
        printf("\n");
        if(azalis == 1){
            break;
        }
        sayac = 1;
        artis +=1;
        azalis -= 1;
    }
    int sayac2 = 1;
    int azalis2 = 1;
    int artis2 = sayi*2-1;
    for(i=1;i<=sayi;i++){
        for(b=1;b<=sayi*2;b++){
            if(sayac2 == azalis2){
                printf("\\");
            }
            else{
                printf(" ");
            }
            if (sayac2 == artis2){
                printf("/");
            }
            
            sayac2+=1;
        }
        printf("\n");
        if(azalis2 == sayi){
            break;
        }
        sayac2 = 1;
        artis2 -=1;
        azalis2 += 1;
    }
    return 0;
}

#include <stdio.h>
#include <conio.h>

int main() {
    int num1;
    printf("Enter your name : ");
    //scanf("%d",&num1);
    printf("%d",num1);
    for(int i=6;i>0;i--) {
        for(int j=0;j<i;j++) {  printf("*");    }
        printf("\n");
    }
    return 0;
}

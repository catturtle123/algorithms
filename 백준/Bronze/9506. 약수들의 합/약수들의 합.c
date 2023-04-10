#include <stdio.h>
#include <math.h>

int main() {
   int n, sum = 0,i;
   while (1) {
      scanf("%d", &n); //테스트케이스마다 한줄에 하나씩 출력
      if (n == -1)
         break;
      else {
         for (i = 1; i < n; i++) {
            if (n % i == 0)
               sum += i;
         }

         if (sum == n) {
            printf("%d = 1", n);
            for (i = 2; i < n; i++) {
               if (n % i == 0){
                  printf(" + %d", i);
              }
            }
            printf("\n");
         }
         else {
            printf("%d is NOT perfect.\n", n);
         }
      }
      sum = 0;
   }
   return 0;
}
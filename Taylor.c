#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    double x, f, fact[150], pwr[150], s[1];
    int i, term, k, j, t;
    double sum;

    printf("Exponential [PROMPT] Enter the value of x (between 0 to 100) (for calculating exp(x)):");
    scanf("%lf", &x);
    printf("X is : %lf",x);
    #pragma omp parallel num_threads(10)
    {
    #pragma omp for
    for (k = 0; k < 150; k++) {
        for (int h = 0; h <= k; h++) {
            if (h == 0)
               { x = 1;}
            else
               { pwr[k] = pow(x, k);}
        }
    }
    #pragma omp for
        for (term = 1; term < 150; term++) {
            f = 1.0;
            for (j = term; j > 0; j--)
                f = f * j;
            fact[term] = f;
        }
    }
    s[0]=0;
    // #pragma omp parallel for shared(s, t) reduction(+: s)
        for (t = 0; t < 150; t++)
            s[0] += (pwr[t] / fact[t]);

        printf("\neXPONENTIAL [INFO] Value of exp(%lf) is : %lf\n\n", x, s[0]);
        exit(1);
    }
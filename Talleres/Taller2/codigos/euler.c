//Emanuel ESquivel Lopez
//2016133597

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

float euler(int iterations)
{
  float euler = 0;
  float n = 1;

  for (int i = 1; i < iterations; ++i)
  {
    euler += 1 / n;
    n *= i;
  }

  return euler;
}

double euler_P(int iterations)
{
  omp_set_num_threads(4);
  int i;
  double n = 1;
  double e = 0;
  double error = 0;

#pragma omp parallel private(i) shared(iterations, e, n)
  {
#pragma omp for reduction(+ \
                          : e)
    for (i = 1; i < iterations; ++i)
    {
      e = e + (1 / n);
      n *= i;
    }
  }
  //CAlc e
  return e;
}

int main()

{

  const int N = 500000;
  const double eT = 2.7182818284590452353602875;

  double s_time = omp_get_wtime();
  double eS = euler(N);
  double eP = euler_P(N);
  double r_time = omp_get_wtime() - s_time;

  double errorS = ((eS- eT) / eS)*100;
  double errorP = ((eP - eT) / eP)*100;
  printf("Serie: EL valor de e es %f calculado en %f segundos, para %d iteraciones y %.25f porcentaje de error rate\n", eS, r_time, N, errorS);
  printf("PAralelo: EL valor de e es %f calculado en %f segundos, para %d iteraciones y %.25f porcentaje de error rate\n", eP, r_time, N, errorP);


  return 0;
}

//End
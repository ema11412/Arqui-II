//Emanuel ESquivel Lopez
//2016133597


#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <omp.h>


//Serial
void saxpy(int n, float v, float *restrict x, float *restrict y)
{
  for (int i = 0; i < n; ++i)
  
    y[i] = v * x[i] + y[i];
}


//PAralelo.
void saxpy_P(int n, float v, float *restrict x, float *restrict y)
{
  omp_set_num_threads(4); //# de proces
  int i;

#pragma omp parallel private(i) shared(v, n, x, y)

  {
#pragma omp for
    for (i = 0; i < n; ++i)
    {
      y[i] = v * x[i] + y[i];
    }
  }
}


int main()
{
  srand((unsigned int)time(NULL));

  const int n = 150000;
  float x[n];
  float y[n];

  for (int i = 0; i < n; ++i)
  {
    x[i] = (float)rand();
    y[i] = (float)rand();
  }

  // Serial 
  double start_time_S = omp_get_wtime();
  saxpy(n, 15, x, y);
  double run_time_S = omp_get_wtime() - start_time_S;

  // Paralelo 
  double start_time_P = omp_get_wtime();
  saxpy_P(n, 15, x, y);
  double run_time_P = omp_get_wtime() - start_time_P;




  printf("Serial SAXPY in %f segundos para %d Elementos\n", run_time_S, n);
  printf("Paralelo SAXPY in %f segundos para %d Elementos\n", run_time_P, n);

  return 0;
}


//end
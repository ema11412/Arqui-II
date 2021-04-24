
#include <stdio.h>
#include <omp.h>

int main ()
{
	  printf("Numero de procesadores disponibles: %d \n", omp_get_num_procs());

	  return 0;
}	  






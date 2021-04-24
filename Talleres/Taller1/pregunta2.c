//include ---------------------------------------
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
//include ---------------------------------------

int global = 0;
pthread_mutex_t lock;

void *threadF1(void *args)
{
    while (1)
    {
        pthread_mutex_lock(&lock);
        printf("Funcion 1\n");
        global += 1;
        printf("Variable: %i\n", global);
        printf("Saliendo de la funcion 1\n");
        printf("\n");
        pthread_mutex_unlock(&lock);
        sleep(1);
    }
}
void *threadF2(void *args)
{
    while (1)
    {
        pthread_mutex_lock(&lock);
        printf("Funcion 2\n");
        global += 1;
        printf("Variable: %i\n", global);
        printf("Saliendo fde la funcion 2\n");
        printf("\n");
        pthread_mutex_unlock(&lock);
        sleep(1);
    }
}

//------- Creacion de los threads
int main()
{
    /*creating threads id*/
    pthread_t id1, id2;
    int ret, ret2;

    /*creating threads*/
    ret = pthread_create(&id1, NULL, &threadF1, NULL);
    if (ret == 0)
    {
        printf("Creado.\n");
    }
    else
    {
        printf("Error.\n");
        return 0;
    }

    ret2 = pthread_create(&id2, NULL, &threadF2, NULL);
    if (ret2 == 0)
    {
        printf("Creado.\n");
    }
    else
    {
        printf("Error\n");
        return 0;
    }

    pthread_join(id1, NULL);
    pthread_join(id2, NULL);
    
    pthread_mutex_destroy(&lock);

    return 0;
}
//------- Creacion de los threads
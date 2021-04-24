//include ---------------------------------------
#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
//include ---------------------------------------

int a1[15], a2[15], XOR[15];

//Valores random 0,255
//10ms
void *threadF1(void *args)
{
    while (1)
    {
        for (int i = 0; i < 6; i++)
        {
            int ran1 = rand() % 256;
            a1[i] = ran1;
            usleep(10);//ms
        }
        printf("Arreglo 1 = [");
        for (int i = 0; i < 6; i++)
        {
            printf(" %d ", a1[i]);
        }
        printf("] \n");
    }
}

//Valores random 0,255
//5ms
void *threadF2(void *args)
{
    while (1)
    {
        for (int i = 0; i < 6; i++)
        {
            int ran2 = rand() % 256;
            a2[i] = ran2;
            usleep(5);//ms
        }
        printf("Arreglo 2 = [");
        for (int i = 0; i < 6; i++)
        {
            printf(" %d ", a2[i]);
        }
        printf("] \n");
    }
}

//XOR entre las funciones anteriores
void *threadF3(void *args)
{
    while (1)
    {
        for (int i = 0; i < 6; i++)
        {
            XOR[i] = a1[i] ^ a2[i]; 
            usleep(20);
        }
        printf("XOR = [");
        for (int i = 0; i < 6; i++)
        {
            printf(" %d ", XOR[i]);
        }
        printf("] \n");
    }
}

//------- Creacion de los threads
int main()
{
    // Creacion de las IDs
    pthread_t id1, id2, id3;
    int ret, ret2, ret3;

    // Crear threads
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
        printf("Creado\n");
    }
    else
    {
        printf("Error.\n");
        return 0;
    }
    ret3 = pthread_create(&id3, NULL, &threadF3, NULL);
    if (ret3 == 0)
    {
        printf("Creado.\n");
    }
    else
    {
        printf("Error.\n");
        return 0;
    }


    pthread_join(id1, NULL);
    pthread_join(id2, NULL);
    pthread_join(id3, NULL);

    return 0;
}
//------- Creacion de los threads
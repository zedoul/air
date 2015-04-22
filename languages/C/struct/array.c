/*****************************************
http://stackoverflow.com/questions/19613752/how-to-properly-malloc-for-array-of-struct-in-c
*****************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Vec2d {
    float x; 
    float y; 
} Vec2d;

typedef struct Food {
    int color;
    struct Vec2d* pos;
} Food;

int main() {
    int number_of_foods = 10;
    struct Food* foods = malloc(number_of_foods * sizeof(struct Food));

    for (int i=0;i<number_of_foods;i++) {
        foods[i].color = i;
        foods[i].pos = malloc(1 * sizeof(struct Vec2d));
        foods[i].pos->x = 10+i;
        foods[i].pos->y = 100+i;

    }
    for (int i=0;i<number_of_foods;i++) {
        printf ("color %d\n", foods[i].color);
        printf ("pos [%f, %f]\n", foods[i].pos->x, foods[i].pos->y);
    }

    for (int i=0;i<number_of_foods;i++) {
        free(foods[i].pos);
    }

    free(foods);

    return 0;
}

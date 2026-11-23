#include <stdlib.h>
#include <stdio.h>

#define MAX_CAPACITY 40001

typedef struct {
    int* prefix_product;
    int size;
    int capacity;
} ProductOfNumbers;


ProductOfNumbers* productOfNumbersCreate() {
    ProductOfNumbers* obj = (ProductOfNumbers*)malloc(sizeof(ProductOfNumbers));
    obj->capacity = MAX_CAPACITY;
    obj->prefix_product = (int*)malloc(sizeof (int)*obj->capacity);
    obj->size = 0;
    obj->prefix_product[0]=1;
    return obj;
}

void productOfNumbersAdd(ProductOfNumbers* obj, int num) {
    if (num==0){
        obj->size = 0;
        obj->prefix_product[0]=1;
        return ;
    }    

    if (obj->size+1 >=obj->capacity){
        obj->capacity *= 2;
        obj->prefix_product = (int*)realloc(obj->prefix_product,sizeof(int)*obj->capacity);
    }
    obj->prefix_product[obj->size+1] = obj->prefix_product[obj->size]*num;
    obj->size++;

}

int productOfNumbersGetProduct(ProductOfNumbers* obj, int k) {
    if (k>obj->size) return 0;
    return obj->prefix_product[obj->size]/obj->prefix_product[obj->size-k];
}

void productOfNumbersFree(ProductOfNumbers* obj) {
    free(obj->prefix_product);
    free(obj);
}








/**
 * Your ProductOfNumbers struct will be instantiated and called as such:
 * ProductOfNumbers* obj = productOfNumbersCreate();
 * productOfNumbersAdd(obj, num);
 
 * int param_2 = productOfNumbersGetProduct(obj, k);
 
 * productOfNumbersFree(obj);
*/
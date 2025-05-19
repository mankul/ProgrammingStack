using swap_fn = void (*) (void *, int const, int const);
using compare_fn = bool (*) (void *, int const, int const);


int partition( void * arr, const int low, const int high, compare_fn fcomp, swap_fn fswap){

    int i = low - 1;
    for(int j = low; j < high; j++){
        if(fcomp(arr, j, i)){
            i++;
            fswap(arr, i, j);
        }
    }
    fswap(arr, i+1, high);
    return i + 1;
}

void quick_sort(void * arr, swap_fn fswap, compare_fn fcomp, const int low, const int high){
    if (low < high){
        int const pi = partition(arr, low, high, fcomp, fswap);
        quick_sort(arr, fswap, fcomp, low, pi-1);
        quick_sort(arr, fswap, fcomp, pi+1, high);
    }
}


void swap_int(void * arr, int const i, int const j){
    int *iarr = (int *)arr;
    int t = iarr[i];
    iarr[i] = iarr[j];
    iarr[j] = t;
}

bool compare_int(void * arr, int const i, int const j){
    int * iarr = (int *) arr;
    return iarr[i] <= iarr[j];
}

int main(){
    int arr[] = {1,23,4,5,3,55,23,44554,33,245,54};
    int n = sizeof(arr);
    quick_sort(arr, swap_int, compare_int, 0, n-1);
}
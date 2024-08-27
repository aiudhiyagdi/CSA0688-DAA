#include <stdio.h>


int calculateTotal(int denominations[], int quantities[], int size) {
    int total = 0;
    for(int i = 0; i < size; i++) {
        total += denominations[i] * quantities[i];
    }
    return total;
}

int main() {
    int denominations[4] = {2000, 500, 200, 100};
    int quantities[4];
    int priority[4];

    printf("Enter the priority of denominations (0 for 2000, 1 for 500, 2 for 200, 3 for 100):\n");
    for(int i = 0; i < 4; i++) {
        printf("Priority %d: ", i+1);
        scanf("%d", &priority[i]);
    }

    for(int i = 0; i < 4; i++) {
        int denom_index = priority[i];
        printf("Enter the number of %d notes: ", denominations[denom_index]);
        scanf("%d", &quantities[denom_index]);
    }

    
    int totalAmount = calculateTotal(denominations, quantities, 4);
    printf("Total amount available in the ATM: %d\n", totalAmount);

    return 0;
}

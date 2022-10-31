#include <stdio.h>

int main() {
    // ****************************************************************************************************

    // Definindo conjunto A
    unsigned int tamA;                          // #A

    printf("#A: ");
    scanf("%u", &tamA);

    int setA[tamA];

    for (int i = 0; i < tamA; i++) {
	printf("Elemento #%d: ", i + 1);
	scanf("%d", &setA[i]);                  // Definindo elementos de A
    }

    printf("\n");

    // Definindo conjunto B
    unsigned int tamB;                          // #B

    printf("#B: ");
    scanf("%u", &tamB);

    int setB[tamB];

    for (int i = 0; i < tamB; i++) {
	printf("Elemento #%d: ", i + 1);
	scanf("%d", &setB[i]);                  // Definindo conjuntos de B
    }

    // ****************************************************************************************************

    int sizeCP = tamA * tamB;
    int AxB[sizeCP][2];                         // Produto cartesiano de A x B
    int BxA[sizeCP][2];                         // Produto cartesiano de B x A
    int c = 0;

    // A x B
    for (int i = 0; i < tamA; i++) {
	for (int j = 0; j < tamB; j++) {
	    AxB[c][0] = setA[i];                // Define a de (a, b)
	    AxB[c][1] = setB[j];                // Define b de (a, b)
	    c++;
	}
    }

    c = 0;                                      // Reinicia contador

    // B x A
    for (int i = 0; i < tamB; i++) {
	for (int j = 0; j < tamA; j++) {
	    BxA[c][0] = setB[i];                // Define b de (b, a)
	    BxA[c][1] = setA[j];                // Define a de (b, a)
	    c++;
	}
    }

    // ****************************************************************************************************

    // Imprima A x B
    printf("\nA x B = {");

    for (int i = 0; i < sizeCP; i++) {
	printf("(%d, %d)", AxB[i][0], AxB[i][1]);     // Imprime cada par ordenado
	
	if (i != sizeCP - 1) {
	    printf(", ");                             // Imprime ', ' se 'i' não é final
	}
    }

    printf("}\n");


    // Imprima B x A
    printf("B x A = {");

    for (int i = 0; i < sizeCP; i++) {
	printf("(%d, %d)", BxA[i][0], BxA[i][1]);     // Imprime cada par ordenado

	if (i != sizeCP - 1) {
	    printf(", ");                             // Imprime ', ' se 'i' não é final
	}
    }

    printf("}\n");

    return 0;
}

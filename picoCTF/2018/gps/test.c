#include <stdio.h>

typedef void (fn_t)(void);

int main(){

	fn_t *location;

	scanf("%p", &location);

	printf("%p", location);
}
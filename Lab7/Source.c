#define True 1
#define False 0
#define bool _Bool
#define and &&
#define or ||



#include <stdio.h>
#include <Windows.h>
#include <math.h>
#include <string.h>

void mario() {
	int height = 0;
	printf("Height: ");
	scanf("%d", &height);
	while (!(height <= 23 and height > 0)) {
		printf("Try again :");
		scanf("%d", &height);
	}
	printf("%d\n", height);
	for (int i = 0;i < height;i++) {
		for (int j = 0; j < height + 1;j++) {
			if (j < height-i-1)
				printf(" ");
			else
				printf("#");
		}
		printf("\n");
	}
}

void numbers() {
	int a, b;
	printf("Input a and b (a<b)");
	scanf("%d %d", &a, &b);
	for (int i = a;i <= b;i++) {
		switch (i) {
		case 1:
			printf("one\n");
			break;
		case 2:
			printf("two\n");
			break;
		case 3:
			printf("three\n");
			break;
		case 4:
			printf("four\n");
			break;
		case 5:
			printf("five\n");
			break;
		case 6:
			printf("six\n");
			break;
		case 7:
			printf("seven\n");
			break;
		case 8:
			printf("eight\n");
			break;
		case 9:
			printf("nine\n");
			break;
		default:
			if (i % 2)
				printf("odd\n");
			else
				printf("even\n");
		}
	}
}

void scifer() {
	char str[82];
	;
	scanf("%[A-Za-z ]", str);
	int rows = sqrt(strlen(str));
	int columns = rows + 1;
	int k = 0;
	for (int i = 0;i < rows;i++) {
		for (int o = 0;o < columns;o++,k++) {
			if (str[k] == '\0')
				goto endloop;
			printf("%c", str[k]);
		}
		printf("\n");
	}
	endloop:
	printf("\n");
}


void change() {
	float money;
	scanf("%f", &money);
	int coins=0;
	while (money>=0.01)
	{
		if (money >= 0.25)
			money -= 0.25;
		else if (money >= 0.1)
			money -= 0.1;
		else if (money >= 0.05)
			money -= 0.05;
		else
			money -= 0.01;
		coins++;
	}
	printf("\n%d", coins);
}

int main() {
	mario();
	numbers();
	scifer();
	change();
	return 0;
}

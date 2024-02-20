#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int capacity;
    int top;
    int* array;
} Stack;

Stack* createStack() {
	int capacity=0;
	printf("������ջ��С\n");
	scanf("%d",&capacity);
    Stack* stack = (Stack*) malloc(sizeof(Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*) malloc(stack->capacity * sizeof(int));
    return stack;
}

int isEmpty(Stack* stack) {
    return stack->top == -1;
}

int isFull(Stack* stack) {
    return stack->top == stack->capacity - 1;
}

void push(Stack* stack, int item) {
    if (isFull(stack)) {
        printf("Stack is full, cannot push element.\n");
        return;
    }
    stack->array[++stack->top] = item;
    printf("%d pushed to Stack.\n", item);
}

int pop(Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty, cannot pop element.\n");
        return -1;
    }
    return stack->array[stack->top--];
}

int peek(Stack* stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty.\n");
        return -1;
    }
    return stack->array[stack->top];
}

void choice(Stack *stack){
	printf("����0ѹ�룬1������2��ջ��\n");
	int y=-1;
	scanf("%d", &y);
	//ѹ�� 
	if (y == 0){
		int item=0;
		printf("����ѹ��ֵ\n");
		scanf("%d", &item);
		push(stack, item);
	}
	//����
	else if (y == 1){
		int top=pop(stack);
		if (top == -1) return;
		else printf("%d\n", top);
	} 
	//��ջ��
	else if (y == 2){
		int top = peek(stack);
		if (top == -1) return;
		else printf("%d\n", top);
	}
	else{
		printf("�������!\n");
	} 
}

void freestack(Stack* stack){
	stack->top=-1;
	free(stack);
}

int main() {
	int x=0;
	Stack* stack = createStack();
	while(1){
		choice(stack);
		int flag=0;
		printf("�������0����������˳�\n"); 
		scanf("%d",&flag); 
		if (flag == 0) continue;
		else{
			freestack(stack);
			break;
		}
	} 
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int front, rear;
    int *data;
} Queue;

void initializeQueue(Queue *q, int size) {
    q->data = (int *)malloc(sizeof(int) * size);
    q->front = -1;
    q->rear = -1;
}

int isFull(Queue *q, int size) {
    return (q->rear + 1) % size == q->front;
}

int isEmpty(Queue *q) {
    return q->front == -1;
}

void enqueue(Queue *q, int size) {
    int t = 0;
    printf("输入入队数字\n");
    scanf("%d", &t);
    
    if (isFull(q, size)) {
        printf("Queue is full.\n");
        return;
    }
    
    if (isEmpty(q)) {
        q->front = 0;
    }
    
    q->rear = (q->rear + 1) % size;
    q->data[q->rear] = t;
    printf("%d enqueued to the queue.\n", t);
}

int dequeue(Queue *q, int size) {
    int item;
    
    if (isEmpty(q)) {
        printf("Queue is empty.\n");
        return -1;
    }
    
    item = q->data[q->front];
    
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % size;
    }
    
    return item;
}

void displayQueue(Queue *q,int size) {
    int i;
    
    if (isEmpty(q)) {
        printf("Queue is empty.\n");
        return;
    }
    
    printf("Elements in the queue are: \n");
    
    for (i = q->front; i != q->rear; i = (i + 1) % size) {
        printf("%d ", q->data[i]);
    }
    
    printf("%d\n", q->data[i]); // Print the last element
}

void choice(Queue *q, int size) {
    int y = 0;
    printf("输入0入队，1出队，2展示\n");
    scanf("%d", &y);
    
    if (y == 0) {
        enqueue(q, size);
    } else if (y == 1) {
        dequeue(q, size);
    } else if (y == 2) {
        displayQueue(q, size);
    } else {
        printf("输入错误！\n");
        return;
    }
}

int main() {
    Queue q;
    int size = 0;
    
    printf("输入你要的队列大小\n");
    scanf("%d", &size);
    
    initializeQueue(&q, size);
    
    while (1) {
        int y = -1;
        choice(&q, size);
        printf("若退出请输入0，输入其他数字继续\n");
        scanf("%d", &y);
        
        if (y == 0) {
            break;
        } else {
            continue;
        }
    }
    
    free(q.data); // 释放内存
    
    return 0;
}

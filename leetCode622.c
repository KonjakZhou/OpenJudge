#include<stdio.h>
#include<stdlib.h>

typedef struct {
    int *queue;
    int len, h, t, state;
} MyCircularQueue;

/** Initialize your data structure here. Set the size of the queue to be k. */

MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue *instance = (MyCircularQueue *)malloc(sizeof(MyCircularQueue));
    instance -> len = k;
	instance -> h = 0;
    instance -> t = 0;
    instance -> state = -1;
    instance -> queue = (int *) malloc(sizeof(int) * k);
    return instance;
}

/** Insert an element into the circular queue. Return true if the operation is successful. */
int myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
  	if (myCircularQueueIsFull(obj))
  	{
  		return 0;
  	}
  	
  	obj -> queue[ obj->t ] = value;
  	obj -> t = ((obj->t) + 1) % (obj->len);
	if ((obj->h) == (obj->t))
  	{
  		obj -> state = 1;
  	}
  	else 
  	{
  		obj -> state = 0;
  	}
  	return 1;
}

/** Delete an element from the circular queue. Return true if the operation is successful. */
int myCircularQueueDeQueue(MyCircularQueue* obj) {
  	if (myCircularQueueIsEmpty(obj))
  	{
  		return 0;
  	}
  	obj -> h = ((obj->h) + 1) % (obj->len);
  	if ((obj->h) == (obj->t))
  	{
  		obj -> state = -1;
  	}
  	else 
  	{
  		obj -> state = 0;
  	}
  	return 1;
}

/** Get the front item from the queue. */
int myCircularQueueFront(MyCircularQueue* obj) {
	if (myCircularQueueIsEmpty(obj))
	{
		return -1;
	}
	return obj -> queue[ obj->h ];
}

/** Get the last item from the queue. */
int myCircularQueueRear(MyCircularQueue* obj) {
	if (myCircularQueueIsEmpty(obj))
	{
		return -1;
	}
	return obj -> queue[ ((obj->t) + (obj->len) - 1) % (obj->len) ];
}

/** Checks whether the circular queue is empty or not. */
int myCircularQueueIsEmpty(MyCircularQueue* obj) {
	if (obj -> state == -1)
	{
		return 1;
	} 
	return 0;
}

/** Checks whether the circular queue is full or not. */
int myCircularQueueIsFull(MyCircularQueue* obj) {
	if (obj -> state == 1)
  	{
  		return 1;
  	}
  	return 0;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj);
}


/* Your MyCircularQueue struct will be instantiated and called as such: */
int main(void)
{
	MyCircularQueue* obj = myCircularQueueCreate(3);
	int param_1 = myCircularQueueEnQueue(obj, 1);
 
	int param_2 = myCircularQueueDeQueue(obj);
 
	int param_3 = myCircularQueueFront(obj);
 
	int param_4 = myCircularQueueRear(obj);
 
	int param_5 = myCircularQueueIsEmpty(obj);
 
 	int param_6 = myCircularQueueIsFull(obj);
 
	myCircularQueueFree(obj);
	
	printf("%d, %d, %d, %d, %d, %d", param_1, param_2, param_3, param_4, param_5, param_6);
}
 

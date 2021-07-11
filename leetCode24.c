#include<stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* head){
	struct ListNode *virtualHead, *p ,*q, *t;
	virtualHead = (struct ListNode*)malloc(sizeof(struct ListNode));
	virtualHead->next = head;
	
	p = virtualHead;
	t = head;
	
	while (t)
	if (t->next)
	{
		q = t->next;
		p->next = q;
		t->next = q->next;
		q->next = t;
		
		p = t;
		t = t->next;
	}
	else 
	{
		head = virtualHead->next;
		return head;
	}
	
	head = virtualHead->next;
	return head;
}

int main(void)
{
	int num[10] = {1,2,3,4};
	int numSize = 4;
	int i;
	
	struct ListNode * head, *p;
	head = (struct ListNode*) malloc(sizeof(struct ListNode));
	head->next = NULL;
	p = head;
	for (i=0;i<numSize;i++)
	{
		p->next = (struct ListNode*) malloc(sizeof(struct ListNode));
		p = p->next;
		
		p->next = NULL;
		p->val = num[i];
	}
	head = head->next;
	
	head = swapPairs(head);
	while (head)
	{
		printf("%d ", head->val);
		head = head->next;
	}
}

#include<stdio.h>
#include<malloc.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseKGroup(struct ListNode* head, int k){
	
	if (k==1) return head;
	
	struct ListNode *virtualHead,*h,*t,*p,*q,*last;
	
	virtualHead = (struct ListNode *)malloc(sizeof(struct ListNode));
	virtualHead->val = -1;
	virtualHead->next = head;
	h = head;
	t = head;
	last = virtualHead;
	
	int i;
	for (i=1;i<k && t; i++)
		t = t->next;
	
	while (t)
	{
		p = h;
		h = h->next;
		q = h->next;
		p->next = t->next;
		
		while (h!=t)
		{
			h->next = p;
			p = h;
			h = q;
			q = q->next;
		}
		
		t = last->next;
		last->next = h;
		h->next = p;
		last = t;
		t = q;
		h = q;
		
		for (i=1;i<k && t; i++)
			t = t->next;
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
	
	head = reverseKGroup(head, 1);
	while (head)
	{
		printf("%d ", head->val);
		head = head->next;
	}
}


#include<stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
	struct ListNode *temp[10000];
	int k=0;
	struct ListNode *p = head;
	while (p)
	{
		temp[k++] = p;
		p = p->next;
	}
	temp[k] = NULL;
	
	if (k==n) 
		return temp[1];
	temp[k-n-1]->next = temp[k-n+1];
	return head;
}



 

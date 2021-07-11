#include<stdio.h>
#include<string.h>

struct ListNode {
	int val;
	struct ListNode *next;
};


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
	struct ListNode *p, *q, *head;
	
	int a[1000];
	int b[1000];
	int lena=0, lenb=0;
	int res=0;
		
	p = l1;
	q = l2;
	
	memset(a, 0, sizeof(a));
	memset(b, 0, sizeof(b));
	
	while (p)
	{
		a[lena++] = p->val;
		p = p->next;
	}
	while (q)
	{
		b[lenb++] = q->val;
		q = q->next;
	}
	
	int maxlen = lena>lenb? lena : lenb;
	int i;
	
	for (i=0;i<maxlen;i++)
	{
		a[i] = a[i] + b[i];
		a[i+1] = a[i+1] + a[i] / 10;
		a[i] = a[i]%10;
	}
	
	if (a[maxlen]) maxlen++;
	
	p = (struct ListNode*)malloc(sizeof(struct ListNode));
	p->next = NULL;
	p->val = a[0];
	head = p;
	
	for (i=1;i<maxlen;i++)
	{
		q = (struct ListNode*)malloc(sizeof(struct ListNode));
		q->next = NULL;
		q->val = a[i];
		
		p->next = q;
		p = q;
	}
	
	return head;
}

int main(void)
{
	return 0;
}

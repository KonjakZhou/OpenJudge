#include<stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
	struct ListNode * head, *p, *q, *t;
	
	head = (struct ListNode *) malloc(sizeof(struct ListNode));
	
	p = l1;
	q = l2;
	t = head;
	head -> next = NULL;
	while (l1 && l2)
	{
		t->next =  (struct ListNode*) malloc(sizeof(struct ListNode));
		t = t->next;
		t->next = NULL;
		if ((l1->val)<=(l2->val))
		{
			t->val = l1->val;
			l1 = l1->next;
		}
		else
		{
			t->val = l2->val;
			l2 = l2->next;
		}
	}
	if (l1) t->next = l1;
	if (l2) t->next = l2;
	head = head->next;
	return head;
}



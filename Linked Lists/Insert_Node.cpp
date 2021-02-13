#include <bits/stdc++.h>

using namespace std;

class SinglyLinkedListNode {
    public:
        int data;
        SinglyLinkedListNode *next;

        SinglyLinkedListNode(int node_data) {
            this->data = node_data;
            this->next = nullptr;
        }
};

class SinglyLinkedList {
    public:
        SinglyLinkedListNode *head;
        SinglyLinkedListNode *tail;

        SinglyLinkedList() {
            this->head = nullptr;
            this->tail = nullptr;
        }

        void insert_node(int node_data) {
            SinglyLinkedListNode* node = new SinglyLinkedListNode(node_data);

            if (!this->head) {
                this->head = node;
            } else {
                this->tail->next = node;
            }

            this->tail = node;
        }
};

void print_singly_linked_list(SinglyLinkedListNode* node, string sep) {
    while (node) {
        //fout << node->data;
        cout << node->data;

        node = node->next;

        if (node) {
            //fout << sep;
            cout << sep;
        }
    }
}

void free_singly_linked_list(SinglyLinkedListNode* node) {
    while (node) {
        SinglyLinkedListNode* temp = node;
        node = node->next;

        free(temp);
    }
}

// Complete the insertNodeAtPosition function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
SinglyLinkedListNode* insertNodeAtPosition(SinglyLinkedListNode* head, int data, int position) {

    //create the new node
    SinglyLinkedListNode* newNode = new SinglyLinkedListNode(data);

    if( position == 0 ){ //insert at the beginning
        newNode->next = head;
        return newNode;
    }else{ //insert at another position
        SinglyLinkedListNode* pointerAfter = head;
        SinglyLinkedListNode* pointerBefore;
        //cycle to go for the needed position
        for(int i=0; i<position; i++){
            pointerBefore = pointerAfter;
            pointerAfter = pointerAfter->next;
        }
        newNode->next = pointerAfter;
        pointerBefore->next = newNode;
        return head;
    }
}

int main()
{
    //ofstream fout(getenv("OUTPUT_PATH"));

    SinglyLinkedList* llist = new SinglyLinkedList();

    int llist_count;
    cin >> llist_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int i = 0; i < llist_count; i++) {
        int llist_item;
        cin >> llist_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        llist->insert_node(llist_item);
    }

    int data;
    cin >> data;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int position;
    cin >> position;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    SinglyLinkedListNode* llist_head = insertNodeAtPosition(llist->head, data, position);

    //print_singly_linked_list(llist_head, " ", fout);
    print_singly_linked_list(llist_head, " ");
    //fout << "\n";
    cout << "\n";

    free_singly_linked_list(llist_head);

    //fout.close();

    return 0;
}

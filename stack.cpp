#include <bits/stdc++.h>
using namespace std;


class Node {
public:
    int value;
    Node* parent;
    Node* child;

    Node(int value, Node* parent, Node* child) {
        this->value = value;
        this->parent = parent;
        this->child = child;
    }

    void print() {
        int p, c;
        if (this->parent != NULL) p = this->parent->value;
        else p = -1;

        if (this->child != NULL) c = this->child->value;
        else c = -1;
        printf(" ---Node---\n value:%d \n parent:%d \n child:%d\n -----------\n", this->value, p, c);
    }
};


class CustomStack {
public:
    Node* top;
    CustomStack() {
        this->top = NULL;
    }

    void push(Node* node) {
        node->parent = this->top;
        if (this->top != NULL)
            this->top->child = node;
        this->top = node;
    }

    Node* pop() {
        Node* popped_node = this->top;
        this->top = this->top->parent;
        if (this->top != NULL)
            this->top->child = NULL;
        return popped_node;
    }

    bool is_empty() {
        return this->top == NULL;
    }

};


class CustomQueue {
public:
    Node* front;
    Node* back;

    CustomQueue() {
        this->front = NULL;
        this->back = NULL;
    }

    void push(Node* node) {
        node->parent = this->back;
        if (this->back != NULL)
            this->back->child = node;
        this->back = node;
        if (this->front == NULL)
            this->front = node;
    }

    Node* pop() {
        Node* popped_node = this->front;
        this->front = this->front->child;
        if (this->front != NULL)
            this->front->parent = NULL;
        if (this->front == NULL)
            this->back = NULL;
        return popped_node;
    }

    bool is_empty() {
        return this->back == NULL or this->front == NULL;
    }
};


void stack_driver() {
    CustomStack stack;
    vector<int> x = { 4, 7, 9, 1, 3, 0, 12 };

    for (int a : x) {
        Node* node = new Node(a, NULL, NULL);
        stack.push(node);
        node->print();
    }

    while (!(stack.is_empty())) {
        stack.pop()->print();
    }
}

void queue_driver() {
    CustomQueue queue;
    vector<int> x = { 4, 7, 9, 1, 3, 0, 12 };

    for (int a : x) {
        Node* node = new Node(a, NULL, NULL);
        queue.push(node);
    }

    while (!(queue.is_empty())) {
        queue.pop()->print();
    }
}


int main() {
    cout << "===========Running Stack Test============\n";
    stack_driver();
    cout << "===========Running Queue Test==============\n";
    queue_driver();
    return 0;
}

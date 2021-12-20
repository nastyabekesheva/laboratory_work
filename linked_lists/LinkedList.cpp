//
//  LinkedList.cpp
//  linked_list
//
//  Created by Nastya Bekesheva on 09.12.2021.
//

#include "LinkedList.hpp"
#include <iostream>
#include <string>

void get_list(Link *head){
    bool stop = false;
    string buff;
    Link *current;
    
    cout << "Enter new elements" << endl << "If you want to stop enter \"stop\"";

    while (!stop){

        cin >> buff;

        if (buff == "stop"){
            stop = true;
        }
        else{
            current = new Link;
            current->str = buff;
            current->next = head->next;
            head -> next = current;

        }
    }
    return;
}

void print_list(Link *head)
{
  while(head != NULL)
  {
      cout << head->str << " ";
      head = head->next;
  }
    cout << endl;
}

void return_second(Link *head){
    Link *ptr = head;
    Link *ptr1 = ptr->next;
    cout << ptr1->next << "-" << ptr1->next->str <<endl;
    
}

void return_last(Link *head){
    Link *ptr = head;
    Link *ptr1 = ptr->next;
    while(ptr1){
        if(ptr1->next == NULL){
            cout << ptr1 << "-" << ptr1->str << endl;
            break;
        }
        ptr = ptr1;
        ptr1 = ptr1->next;
    }
}
    

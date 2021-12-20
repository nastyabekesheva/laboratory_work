//
//  main.cpp
//  linked_list
//
//  Created by Nastya Bekesheva on 09.12.2021.
//

#include <iostream>
#include <string>
#include "LinkedList.hpp"
int main(){
    bool stop = false;
    int choice;
    Link *head = new Link;
    head->next = NULL;

    while (!stop){
        cout << "1. get list from input" << endl
            << "2. print list" << endl
            << "3. print second pointer" << endl
            << "4. print last pointer" << endl
            << "5. stop" << endl;
        cin >> choice;
        switch(choice){
        case 1: get_list(head);
            break;
        case 2: print_list(head);
            break;
        case 3: return_second(head);
            break;
        case 4: return_last(head);
            break;
        case 5: stop = true;
            break;
        default:
            cout << "That is not a valid input, quitting program";
            stop = true;
        }
    }
    
}

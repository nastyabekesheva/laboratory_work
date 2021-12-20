//
//  LinkedList.hpp
//  linked_list
//
//  Created by Nastya Bekesheva on 09.12.2021.
//

#ifndef LinkedList_hpp
#define LinkedList_hpp

#include <stdio.h>

#endif /* LinkedList_hpp */
#include <string>
#include <vector>
using namespace std;

struct Link{
    string str;
    Link *next;
};

void get_list(Link *head);
void print_list(Link *head);
void return_second(Link *head);
void return_last(Link *head);
//Link* get_list();
//void Count(Link*);


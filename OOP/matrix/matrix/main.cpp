//
//  main.cpp
//  matrix
//
//  Created by Nastya Bekesheva on 18.02.2022.
//

#include <iostream>
#include <vector>
using namespace std;

class Matrix{
    protected:
        unsigned int _rows;
        unsigned int _cols;
        vector<vector<unsigned int> > _matrix;
    
    public:
    
        Matrix(int _rows, int _cols);
        Matrix(const Matrix &);
    
        void pushData();
        void getData();
        void getSize();
        void getElement(unsigned int value);
        int getItem(int i, int j);
        void setItem(int i, int j, unsigned int value);
    
};

Matrix::Matrix(int _rows, int _cols){
    this->_rows = _rows;
    this->_cols = _cols;
}


Matrix::Matrix(const Matrix& other){
    this->_rows = other._rows;
    this->_cols = other._cols;
    this->_matrix = other._matrix;
}

void Matrix::pushData(){
    cout << "Enter values: " << endl;
    for(int i = 0; i < _rows; i++){
        vector<unsigned int> row;
        for(int j = 0; j < _cols; j++){
            int temp;
            cin >> temp;
            row.push_back(temp);
        }
        _matrix.push_back(row);
    }
}


void Matrix::getData(){
    cout << "Your matrix" << endl;
    for(int i = 0; i < _rows; i++){
        for(int j = 0; j < _cols; j++){
            cout << _matrix[i][j] << " ";
        }
        cout << endl;
    }
}

void Matrix::getSize(){
    int size = _rows * _cols;
    cout << "Size of your matrix: " << size << endl;
}

void Matrix::getElement(unsigned int value){
    bool temp = false;
    for(int i = 0; i < _rows; i++){
        for(int j = 0; j < _cols; j++){
            if(_matrix[i][j] == value){
                cout << "Element " << value << " found at row: " << i << " col: " << j << endl;
                temp = true;
            }
        }
    }
    if(temp == false){
        cout << "No such element" << endl;
    }
}

int Matrix::getItem(int i, int j){
    return _matrix[i][j];
}

void Matrix::setItem(int i, int j, unsigned int value){
    _matrix[i][j] = value;
}

int main() {
    Matrix matrix(3, 3);
    matrix.pushData();
    cout << endl;
    matrix.getData();
    cout << endl;
    matrix.getSize();
    cout << endl;
    matrix.getElement(3);
    Matrix mat = matrix;
    return 0;
}

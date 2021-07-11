# include <iostream>

int fun(){
    int a[100];
    std::cout << a[18] << "\n" << std::endl;
    return 0;
}

int main(){
    int a = 1;
    float b = {a};

    fun();
    std::cout << "hello world\n" ;
    return 0;
}
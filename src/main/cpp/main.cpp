#include <iostream>

int main(){

    std::cout << "Hello, world of c++!" << std::endl;
    std::string myStr {"String one"};
    std::cout << myStr << std::endl;

    std::cout << "What is your name? ";
    std::string myName{};
    std::cin >> myName;
    std::cout << "Hello, " << myName << std::endl;
}
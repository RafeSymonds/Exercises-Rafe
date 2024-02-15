
#include <iostream>

using namespace std;

int main() {
    int num = 0;
    int pow = 0;
    cin >> num >> pow;

    int total = 1;

    for (; pow >= 1; --pow) {
        total *= num;
    }
    cout << total << "\n";
    return 0;
}

#include <iostream>

using namespace std;

int main() {
    int num = 0;
    cin >> num;

    if (num <= 1) {
        cout << "False\n";
        return 0;
    }
    for (int i = 2; i < num; ++i) {
        if (num % i == 0) {
            cout << "False\n";
            return 0;
        }
    }
    cout << "True\n";
    return 0;
}

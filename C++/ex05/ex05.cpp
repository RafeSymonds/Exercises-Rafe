
#include <cmath>
#include <cstddef>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int num;
    cin >> num;
    string s = to_string(num);
    for (size_t i = 0; i < s.size() / 2; ++i) {
        if (s[i] != s[s.size() - i - 1]) {
            cout << "False\n";
            return 0;
        }
    }
    cout << "True\n";

    return 0;
}

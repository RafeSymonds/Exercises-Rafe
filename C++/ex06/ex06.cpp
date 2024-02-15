#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    string s1;
    string s2;
    cin >> s1 >> s2;

    if (s1.size() != s2.size()) {
        cout << "False\n";
        return 0;
    }

    vector<int> charsCount(26, 0);

    for (size_t i = 0; i < s1.size(); ++i) {
        ++charsCount[s1[i] - 'a'];
        --charsCount[s2[i] - 'a'];
    }
    for (size_t i = 0; i < charsCount.size(); ++i) {
        if (charsCount[i] != 0) {
            cout << "False\n";
            return 0;
        }
    }
    cout << "True\n";
    return 0;
}

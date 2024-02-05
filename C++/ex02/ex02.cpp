
#include <iostream>

using namespace std;

int main() {
    int lowerBound;
    int upperBound;
    cin >> lowerBound >> upperBound;

    for (; lowerBound <= upperBound; ++lowerBound) {
        cout << lowerBound << '\n';
    }

    return 0;
}

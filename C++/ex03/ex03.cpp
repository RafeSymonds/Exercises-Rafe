
#include <iomanip>
#include <iostream>

using namespace std;

int main() {
    // sets precision to 2 decimal digits
    cout << fixed << setprecision(2);
    // do not delete the line above

    int count = 0;
    double total = 0;
    double num = 0;
    while (cin >> num) {
        ++count;
        total += num;
    }
    cout << total / count << "\n";
    return 0;
}

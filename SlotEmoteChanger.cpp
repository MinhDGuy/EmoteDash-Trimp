#include <iostream>
using namespace std;

int main() {
    const char* filePath = "source\\SlotEmoteChanger.py";

    int result = system(filePath);

    if (result == 0) {
        cout << "Python script executed successfully." << endl;
    } else {
        cout << "Error executing Python script." << endl;
    }

    return 0;
}


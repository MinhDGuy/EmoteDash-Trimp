#include <iostream>
using namespace std;

int main() {
    // Replace the path below with the full path to your SlotEmoteChanger.py file
    const char* filePath = "source\\SlotEmoteChanger.py";

    // Use system() to execute the .py file
    int result = system(filePath);

    if (result == 0) {
        cout << "Python script executed successfully." << endl;
    } else {
        cout << "Error executing Python script." << endl;
    }

    return 0;
}


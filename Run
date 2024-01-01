#include <iostream>
#include <Windows.h>
using namespace std;

int main() {
    const wchar_t* filePath = L"source\\EmoteTrimp.ahk";

    HINSTANCE result = ShellExecuteW(NULL, L"open", filePath, NULL, NULL, SW_SHOWNORMAL);

    if ((intptr_t)result > 32) {
        wcout << L"AutoHotkey script executed successfully." << endl;
    } else {
        wcout << L"Error executing AutoHotkey script." << endl;
    }

    return 0;
}

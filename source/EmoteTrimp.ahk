#If WinActive("ahk_exe RobloxPlayerBeta.exe")

$g::
	SendInput {f down} {f up}
	Sleep 25
	SendInput {g down} {g up}
  SendInput {1 down} {1 up}
	Sleep 100
	SendInput {c down}
Return

$h::SendInput {c up} {g down} {g up}

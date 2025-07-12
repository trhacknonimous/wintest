import tkinter as tk
from tkinter import messagebox
import subprocess
import shutil
import os
import urllib.request

# URLS officielles
GIT_URL = "https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe"
PYTHON_URL = "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
NODE_URL = "https://nodejs.org/dist/v20.11.1/node-v20.11.1-x64.msi"

INSTALL_FOLDER = "installers"

os.makedirs(INSTALL_FOLDER, exist_ok=True)

# Téléchargement avec progression
def download_file(name, url, filename):
    try:
        label_status.config(text=f"Téléchargement de {name}...", fg="yellow")
        urllib.request.urlretrieve(url, filename)
        label_status.config(text=f"{name} téléchargé.", fg="green")
    except Exception as e:
        label_status.config(text=f"Erreur téléchargement {name}: {e}", fg="red")

# Vérifie si l'outil est installé
def is_installed(cmd):
    return shutil.which(cmd) is not None

# Exécute le .exe ou .msi
def run_installer(path):
    subprocess.run([path], shell=True)

# Installe Git
def install_git():
    if is_installed("git"):
        label_status.config(text="Git est déjà installé.", fg="green")
    else:
        path = os.path.join(INSTALL_FOLDER, "git.exe")
        download_file("Git", GIT_URL, path)
        run_installer(path)

# Installe Python
def install_python():
    if is_installed("python"):
        label_status.config(text="Python est déjà installé.", fg="green")
    else:
        path = os.path.join(INSTALL_FOLDER, "python.exe")
        download_file("Python", PYTHON_URL, path)
        run_installer(path)

# Installe Node.js
def install_node():
    if is_installed("node"):
        label_status.config(text="Node.js est déjà installé.", fg="green")
    else:
        path = os.path.join(INSTALL_FOLDER, "node.msi")
        download_file("Node.js", NODE_URL, path)
        run_installer(path)

# Installe tout
def install_all():
    install_git()
    install_python()
    install_node()

# Interface graphique
root = tk.Tk()
root.title("TRHACKNON SETUP INSTALLER")
root.geometry("540x360")
root.config(bg="black")

font_title = ("Courier", 20, "bold")
font_btn = ("Courier", 12, "bold")

title = tk.Label(root, text="TRHACKNON INSTALLER", fg="lime", bg="black", font=font_title)
title.pack(pady=20)

tk.Button(root, text="Installer Git", command=install_git, bg="black", fg="cyan", font=font_btn).pack(pady=5)
tk.Button(root, text="Installer Python", command=install_python, bg="black", fg="yellow", font=font_btn).pack(pady=5)
tk.Button(root, text="Installer Node.js", command=install_node, bg="black", fg="magenta", font=font_btn).pack(pady=5)
tk.Button(root, text="Installer TOUS", command=install_all, bg="darkgreen", fg="white", font=font_btn).pack(pady=10)

label_status = tk.Label(root, text="Statut : En attente...", fg="gray", bg="black", font=("Courier", 10))
label_status.pack(pady=10)

root.mainloop()

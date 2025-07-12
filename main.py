import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTextEdit, QLabel, QComboBox
)
from PyQt5.QtCore import Qt

# 🔐 Fonction pour exécuter avec privilèges admin
def run_as_admin(cmd):
    return subprocess.run(
        ['powershell', '-Command',
         f'Start-Process cmd -ArgumentList "/c {cmd}" -Verb runAs'],
        shell=True
    )

class CommandCenter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧠 trhacknon's Cyberpunk CMD")
        self.setFixedSize(900, 600)

        self.layout = QVBoxLayout()

        self.label = QLabel("Commande personnalisée :")
        self.layout.addWidget(self.label)

        self.cmd_input = QLineEdit()
        self.layout.addWidget(self.cmd_input)

        buttons_layout = QHBoxLayout()
        self.run_btn = QPushButton("▶ Exécuter")
        self.run_btn.clicked.connect(self.run_command)

        self.admin_btn = QPushButton("🛡️ Admin")
        self.admin_btn.clicked.connect(self.run_command_admin)

        buttons_layout.addWidget(self.run_btn)
        buttons_layout.addWidget(self.admin_btn)

        self.layout.addLayout(buttons_layout)

        self.quick_label = QLabel("🔧 Commandes rapides :")
        self.layout.addWidget(self.quick_label)

        self.combo = QComboBox()
        self.combo.addItems([
            "ipconfig /all",
            "whoami",
            "systeminfo",
            "netstat -ano",
            "tasklist",
            "wmic os get caption",
            "bcdedit",
            "powershell Get-ExecutionPolicy"
        ])
        self.combo.currentIndexChanged.connect(self.set_quick_command)
        self.layout.addWidget(self.combo)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.layout.addWidget(self.output)

        self.setLayout(self.layout)

        # 🔥 Appliquer le thème
        self.apply_styles()

    def apply_styles(self):
        with open("assets/cyberpunk.qss", "r") as f:
            self.setStyleSheet(f.read())

    def set_quick_command(self):
        self.cmd_input.setText(self.combo.currentText())

    def run_command(self):
        cmd = self.cmd_input.text()
        if not cmd:
            return
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            self.output.setText(result)
        except subprocess.CalledProcessError as e:
            self.output.setText(f"[Erreur]\n{e.output}")

    def run_command_admin(self):
        cmd = self.cmd_input.text()
        if not cmd:
            return
        run_as_admin(cmd)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CommandCenter()
    window.show()
    sys.exit(app.exec_())

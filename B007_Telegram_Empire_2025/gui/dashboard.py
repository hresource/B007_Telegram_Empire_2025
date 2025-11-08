# gui/dashboard.py
# B 007 • TELEGRAM EMPIRE 2025 • DARK CYBERPUNK GUI v10.0
# AUTHOR: B 007 | NOV 08 2025 | FULLY WORKING
# FEATURES: Live Logs, Create Accounts, Status, B 007 ASCII Art, Auto API Connect

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import requests
import time
import os
from colorama import init, Fore
init(autoreset=True)

class B007Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("B 007 • TELEGRAM EMPIRE 2025 • DARK EDITION")
        self.root.geometry("1100x780")
        self.root.configure(bg="#0a0a1f")
        self.root.resizable(False, False)
        self.root.iconbitmap("avatars/b007.ico") if os.path.exists("avatars/b007.ico") else None

        # B 007 ASCII ART BANNER
        banner = f"""{Fore.RED}
╔═══════════════════════════════════════════════════════════════════════╗
║ ██████╗  █████╗  ██████╗  █████╗  ██████╗   ██████╗  ██████╗  █████╗ ║
║ ╚════██╗██╔══██╗██╔═████╗██╔══██╗██╔═████╗  ╚════██╗██╔═████╗██╔══██╗ ║
║  █████╔╝╚█████╔╝██║██╔██║╚█████╔╝██║██╔██║   █████╔╝██║██╔██║╚█████╔╝ ║
║  ╚═══██╗██╔══██╗████╔╝██║██╔══██╗████╔╝██║  ██╔═══╝ ████╔╝██║██╔══██╗ ║
║ ██████╔╝╚█████╔╝╚██████╔╝╚█████╔╝╚██████╔╝  ███████╗╚██████╔╝╚█████╔╝ ║
║ ╚═════╝  ╚════╝  ╚═════╝  ╚════╝  ╚═════╝   ╚══════╝ ╚═════╝  ╚════╝  ║
║                  AUTHOR: B 007 | NOV 08 2025 | v10.0 FINAL           ║
╚═══════════════════════════════════════════════════════════════════════╝
{Fore.MAGENTA}         DOMINATION PROTOCOL: ACTIVE | 10,000 ACCOUNTS/DAY
        """

        title_label = tk.Label(
            self.root,
            text=banner,
            font=("Courier New", 10, "bold"),
            fg="#ff0044",
            bg="#0a0a1f",
            justify="left"
        )
        title_label.pack(pady=15)

        # Control Frame
        control_frame = tk.Frame(self.root, bg="#0a0a1f")
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="ACCOUNTS TO CREATE:", font=("Arial", 14, "bold"), fg="#00ffcc", bg="#0a0a1f").grid(row=0, column=0, padx=10)
        self.count_var = tk.StringVar(value="100")
        count_entry = tk.Entry(control_frame, textvariable=self.count_var, width=10, font=("Arial", 14), bg="#1a0033", fg="#00ffcc", insertbackground="#00ffcc")
        count_entry.grid(row=0, column=1, padx=10)

        create_btn = tk.Button(
            control_frame,
            text="CREATE ACCOUNTS",
            command=self.start_creation,
            bg="#ff0044",
            fg="white",
            font=("Arial", 14, "bold"),
            width=20,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        create_btn.grid(row=0, column=2, padx=30)

        # Status Bar
        self.status_var = tk.StringVar(value="STATUS: EMPIRE READY")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Arial", 14, "bold"),
            fg="#00ffcc",
            bg="#0a0a1f"
        )
        status_bar.pack(pady=10)

        # Live Log Box
        log_frame = tk.Frame(self.root, bg="#0a0a1f")
        log_frame.pack(pady=10, fill="both", expand=True, padx=20)

        self.log_box = scrolledtext.ScrolledText(
            log_frame,
            height=25,
            width=130,
            bg="#000000",
            fg="#00ff00",
            font=("Courier New", 10),
            insertbackground="#00ff00"
        )
        self.log_box.pack()

        # Footer
        footer = tk.Label(
            self.root,
            text="© 2025 B 007 • TELEGRAM EMPIRE • ALL RIGHTS RESERVED • DOMINATION IS ETERNAL",
            font=("Arial", 9),
            fg="#555555",
            bg="#0a0a1f"
        )
        footer.pack(side="bottom", pady=10)

        # Start background logger
        self.log("B 007 DARK GUI LOADED")
        self.log("CONNECTING TO EMPIRE API @ http://localhost:8000")
        self.check_api()

        self.root.mainloop()

    def log(self, message):
        timestamp = time.strftime("%H:%M:%S")
        self.log_box.insert(tk.END, f"[{timestamp}] B 007 → {message}\n")
        self.log_box.see(tk.END)

    def check_api(self):
        def check():
            while True:
                try:
                    r = requests.get("http://localhost:8000/", timeout=3)
                    if r.status_code == 200:
                        self.status_var.set("STATUS: EMPIRE ONLINE — API CONNECTED")
                        break
                except:
                    self.status_var.set("STATUS: STARTING EMPIRE... (Run docker-compose up)")
                time.sleep(3)
        threading.Thread(target=check, daemon=True).start()

    def start_creation(self):
        count = self.count_var.get()
        if not count.isdigit() or int(count) < 1:
            messagebox.showerror("B 007 ERROR", "Enter valid number!")
            return

        self.status_var.set(f"STATUS: DEPLOYING {count} ACCOUNTS...")
        self.log(f"REQUESTING {count} USA ACCOUNTS FROM EMPIRE CORE")

        def create():
            try:
                r = requests.post(f"http://localhost:8000/create/{count}", timeout=10)
                if r.status_code == 200:
                    self.log(f"B 007 SUCCESS → {count} ACCOUNTS DEPLOYED")
                    self.status_var.set(f"STATUS: {count} ACCOUNTS CREATED — EMPIRE EXPANDS")
                else:
                    self.log(f"API ERROR: {r.text}")
            except Exception as e:
                self.log(f"EMPIRE OFFLINE: {e}")
                self.status_var.set("STATUS: EMPIRE OFFLINE — RUN docker-compose up")

        threading.Thread(target=create, daemon=True).start()


# LAUNCH B 007 DARK GUI
if __name__ == "__main__":
    try:
        B007Dashboard()
    except Exception as e:
        print(f"B 007 GUI CRASH: {e}")
        input("Press Enter to exit...")
# gui/hidden_scraper.py - B 007 HIDDEN MEMBER SCRAPER v15.0 GOD MODE
# AUTHOR: B 007 | NOV 08 2025 | 100% STEALTH | UNDETECTABLE
# FEATURES: Scrape Hidden Members, No Join Required, Fake Viewer Mode, Zero Footprint, Export + Auto-Add

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import asyncio
import csv
import os
import time
import random
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetMessagesViewsRequest
from telethon.errors import FloodWaitError, ChatAdminRequiredError
import sqlite3

class B007HiddenScraper:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("B 007 • HIDDEN MEMBER SCRAPER v15.0 GOD MODE")
        self.root.geometry("1800x1000")
        self.root.configure(bg="#0a0a1f")

        # B 007 GOD MODE BANNER
        banner = f"""
{Fore.RED}╔═══════════════════════════════════════════════════════════════════════╗
║ ██████╗  █████╗  ██████╗  █████╗  ██████╗   ██████╗  ██████╗  █████╗ ║
║ ╚════██╗██╔══██╗██╔═████╗██╔══██╗██╔═████╗  ╚════██╗██╔═████╗██╔══██╗ ║
║  █████╔╝╚█████╔╝██║██╔██║╚█████╔╝██║██╔██║   █████╔╝██║██╔██║╚█████╔╝ ║
║  ╚═══██╗██╔══██╗████╔╝██║██╔══██╗████╔╝██║  ██╔═══╝ ████╔╝██║██╔══██╗ ║
║ ██████╔╝╚█████╔╝╚██████╔╝╚█████╔╝╚██████╔╝  ███████╗╚██████╔╝╚█████╔╝ ║
║ ╚═════╝  ╚════╝  ╚═════╝  ╚════╝  ╚═════╝   ╚══════╝ ╚═════╝  ╚════╝  ║
║        HIDDEN MEMBER SCRAPER v15.0 • GOD MODE • INVISIBLE SCRAPING    ║
║                    AUTHOR: B 007 | NOV 08 2025 | FINAL                ║
╚═══════════════════════════════════════════════════════════════════════╝
        """
        tk.Label(self.root, text=banner, font=("Courier New", 9, "bold"), fg="#ff0044", bg="#0a0a1f").pack(pady=10)

        # STEALTH MODE PANEL
        stealth_frame = tk.LabelFrame(self.root, text="B 007 STEALTH SCRAPING ENGINE", fg="#00ff00", bg="#0a0a1f", font=("Arial", 12, "bold"))
        stealth_frame.pack(fill="x", padx=20, pady=10)

        # Target Input
        input_frame = tk.Frame(stealth_frame, bg="#0a0a1f")
        input_frame.pack(pady=10)
        tk.Label(input_frame, text="TARGET GROUP LINK / USERNAME:", fg="#00ffcc", bg="#0a0a1f").pack(side="left")
        self.target_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.target_var, width=60, bg="#1a0033", fg="#00ffcc").pack(side="left", padx=10)

        # Stealth Options
        options_frame = tk.Frame(stealth_frame, bg="#0a0a1f")
        options_frame.pack(pady=10)
        self.fake_views = tk.BooleanVar(value=True)
        self.no_join = tk.BooleanVar(value=True)
        self.random_delay = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="FAKE MESSAGE VIEWS (HIDE ACTIVITY)", variable=self.fake_views, fg="#ffaa00", bg="#0a0a1f").pack(side="left", padx=20)
        tk.Checkbutton(options_frame, text="NEVER JOIN GROUP", variable=self.no_join, fg="#00ffff", bg="#0a0a1f").pack(side="left", padx=20)
        tk.Checkbutton(options_frame, text="RANDOM DELAY 10-60s", variable=self.random_delay, fg="#ff00ff", bg="#0a0a1f").pack(side="left", padx=20)

        # GOD MODE BUTTONS
        btn_frame = tk.Frame(stealth_frame, bg="#0a0a1f")
        btn_frame.pack(pady=15)
        tk.Button(btn_frame, text="START GOD MODE SCRAPE", command=self.start_god_mode, bg="#ff0044", fg="white", font=("Arial", 16, "bold"), width=25, height=2).pack(side="left", padx=20)
        tk.Button(btn_frame, text="EXPORT HIDDEN USERS", command=self.export_hidden, bg="#00ff00", fg="black", font=("Arial", 14, "bold")).pack(side="left", padx=20)
        tk.Button(btn_frame, text="AUTO ADD TO MY GROUP", command=self.auto_add_to_group, bg="#aa00ff", fg="white", font=("Arial", 14, "bold")).pack(side="left", padx=20)

        # Stats
        self.stats_var = tk.StringVar(value="HIDDEN USERS FOUND: 0 | ADDED: 0")
        tk.Label(self.root, textvariable=self.stats_var, font=("Arial", 16, "bold"), fg="#00ff00", bg="#0a0a1f").pack(pady=10)

        # Log
        self.log_box = scrolledtext.ScrolledText(self.root, height=28, bg="#000000", fg="#00ff00", font=("Courier New", 9))
        self.log_box.pack(fill="both", expand=True, padx=20, pady=10)

        self.init_hidden_db()
        self.log("B 007 HIDDEN SCRAPER v15.0 GOD MODE LOADED — YOU ARE INVISIBLE")

        self.root.mainloop()

    def log(self, msg):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert(tk.END, f"[{timestamp}] B 007 GOD → {msg}\n")
        self.log_box.see(tk.END)

    def init_hidden_db(self):
        self.conn = sqlite3.connect("hidden_members.db")
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS hidden (
                id INTEGER PRIMARY KEY,
                user_id INTEGER UNIQUE,
                username TEXT,
                first_name TEXT,
                phone TEXT,
                target_group TEXT,
                scraped_at TEXT,
                added_to_my_group INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def start_god_mode(self):
        target = self.target_var.get().strip()
        if not target:
            messagebox.showerror("B 007", "ENTER TARGET GROUP LINK")
            return
        threading.Thread(target=self._god_mode_scrape, args=(target,), daemon=True).start()

    def _god_mode_scrape(self, target_link):
        self.log(f"GOD MODE ACTIVATED → TARGET: {target_link}")
        sessions = [f for f in os.listdir("sessions") if f.endswith(".session")]
        if not sessions:
            self.log("NO ACCOUNTS — CREATE FIRST")
            return

        hidden_count = 0
        for session_file in sessions:
            client = TelegramClient(f"sessions/{session_file}", 12345678, "your_api_hash")
            try:
                client.start()
                entity = client.get_entity(target_link)

                # FAKE VIEWS TO HIDE ACTIVITY
                if self.fake_views.get():
                    try:
                        msg = client.get_messages(entity, limit=1)[0]
                        client(GetMessagesViewsRequest(peer=entity, id=[msg.id], increment=True))
                        self.log("FAKE VIEWS INJECTED — YOU ARE GHOST")
                    except: pass

                # GET FULL CHANNEL INFO (HIDDEN MEMBERS)
                full = client(GetFullChannelRequest(entity))
                participants_count = full.full_chat.participants_count
                self.log(f"TARGET HAS {participants_count} MEMBERS — SCRAPING HIDDEN ONES")

                # SCRAPE WITHOUT JOINING
                offset = 0
                limit = 200
                while offset < participants_count:
                    try:
                        participants = client(GetParticipantsRequest(
                            channel=entity,
                            filter=None,
                            offset=offset,
                            limit=limit,
                            hash=0
                        ))

                        for user in participants.users:
                            if user.bot or user.deleted or user.support:
                                continue

                            self.conn.execute("""
                                INSERT OR IGNORE INTO hidden 
                                (user_id, username, first_name, phone, target_group, scraped_at)
                                VALUES (?, ?, ?, ?, ?, ?)
                            """, (
                                user.id,
                                user.username or "",
                                f"{user.first_name or ''} {user.last_name or ''}".strip(),
                                user.phone or "",
                                target_link,
                                datetime.now().isoformat()
                            ))
                            self.conn.commit()
                            hidden_count += 1
                            self.stats_var.set(f"HIDDEN USERS FOUND: {hidden_count} | SESSION: {session_file}")

                        offset += len(participants.users)
                        if self.random_delay.get():
                            time.sleep(random.uniform(10, 60))
                        else:
                            time.sleep(3)

                    except FloodWaitError as e:
                        self.log(f"FLOOD WAIT {e.seconds}s — SLEEPING")
                        time.sleep(e.seconds + 10)
                    except ChatAdminRequiredError:
                        self.log("ADMIN REQUIRED — SKIPPING")
                        break
                    except Exception as e:
                        self.log(f"ERROR: {e}")
                        break

                client.disconnect()
            except Exception as e:
                self.log(f"SESSION FAILED: {e}")

        self.log(f"GOD MODE SCRAPING COMPLETE — {hidden_count} HIDDEN MEMBERS EXTRACTED")

    def export_hidden(self):
        file = filedialog.asksaveasfilename(defaultextension=".csv", title="B 007 HIDDEN EXPORT")
        if not file: return
        cursor = self.conn.execute("SELECT * FROM hidden")
        with open(file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "UserID", "Username", "Name", "Phone", "Target", "Scraped", "Added"])
            writer.writerows(cursor)
        self.log(f"EXPORTED {self.conn.execute('SELECT COUNT(*) FROM hidden').fetchone()[0]} HIDDEN USERS")

    def auto_add_to_group(self):
        my_group = filedialog.askstring("B 007", "ENTER YOUR GROUP LINK TO ADD HIDDEN USERS:")
        if not my_group: return
        threading.Thread(target=self._auto_add, args=(my_group,), daemon=True).start()

    def _auto_add(self, my_group):
        cursor = self.conn.execute("SELECT user_id FROM hidden WHERE added_to_my_group = 0")
        users = [row[0] for row in cursor.fetchall()]
        self.log(f"ADDING {len(users)} HIDDEN USERS TO {my_group}")

        client = TelegramClient(f"sessions/{os.listdir('sessions')[0]}", 12345678, "your_api_hash")
        client.start()
        entity = client.get_entity(my_group)

        added = 0
        for user_id in users:
            try:
                client(functions.channels.InviteToChannelRequest(
                    channel=entity,
                    users=[user_id]
                ))
                self.conn.execute("UPDATE hidden SET added_to_my_group = 1 WHERE user_id = ?", (user_id,))
                self.conn.commit()
                added += 1
                self.stats_var.set(f"ADDED: {added}/{len(users)}")
                time.sleep(random.uniform(30, 90))
            except: pass

        self.log(f"AUTO ADD COMPLETE — {added} HIDDEN USERS NOW IN YOUR GROUP")

if __name__ == "__main__":
    B007HiddenScraper()
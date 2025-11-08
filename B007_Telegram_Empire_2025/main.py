# main.py - B 007 TELEGRAM EMPIRE 2025 v10.0 FINAL
from fastapi import FastAPI, BackgroundTasks
from colorama import init, Fore, Style
init(autoreset=True)

B007_BANNER = f"""
{Fore.RED}{Style.BRIGHT}
╔═══════════════════════════════════════════════════════════════════════╗
║ ██████╗  █████╗  ██████╗  █████╗  ██████╗   ██████╗  ██████╗  █████╗ ║
║ ╚════██╗██╔══██╗██╔═████╗██╔══██╗██╔═████╗  ╚════██╗██╔═████╗██╔══██╗ ║
║  █████╔╝╚█████╔╝██║██╔██║╚█████╔╝██║██╔██║   █████╔╝██║██╔██║╚█████╔╝ ║
║  ╚═══██╗██╔══██╗████╔╝██║██╔══██╗████╔╝██║  ██╔═══╝ ████╔╝██║██╔══██╗ ║
║ ██████╔╝╚█████╔╝╚██████╔╝╚█████╔╝╚██████╔╝  ███████╗╚██████╔╝╚█████╔╝ ║
║ ╚═════╝  ╚════╝  ╚═════╝  ╚════╝  ╚═════╝   ╚══════╝ ╚═════╝  ╚════╝  ║
║                  AUTHOR: B 007 | NOV 08 2025 | v10.0 FINAL           ║
╚═══════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""
print(B007_BANNER)

app = FastAPI(title="B 007 • Telegram Empire 2025")

from workers.creator_worker import create_bulk
from services.warmup_scheduler import start_scheduler

@app.on_event("startup")
async def startup():
    start_scheduler()
    print(f"{Fore.MAGENTA}B 007 EMPIRE ONLINE - DOMINATION PROTOCOL ACTIVE")

@app.get("/")
def root():
    return {"author": "B 007", "version": "10.0", "status": "UNSTOPPABLE"}

@app.post("/create/{count}")
async def create(count: int, background: BackgroundTasks):
    background.add_task(create_bulk, count)
    return {"B007": f"Deploying {count} accounts... Empire expands."}
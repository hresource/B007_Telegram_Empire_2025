# sms/five_sim.py
# B 007 • TELEGRAM EMPIRE 2025 • 5SIM.NET FULL CLIENT
# AUTHOR: B 007 | NOV 08 2025 | v10.0 FINAL
# FEATURES: USA Numbers (country=usa), Auto Refund, Proxy Rotation, B 007 Logging

import requests
import time
import random
from typing import Optional, Dict, Any
from utils.logger import Logger
from proxy.rotator import ProxyRotator

class FiveSimClient:
    """
    B 007 Elite 5SIM.NET Integration
    Supports: USA Mobile Numbers for Telegram
    Auto-cancel on timeout → Full refund
    Proxy rotation via ProxyRotator
    """

    BASE_URL = "https://5sim.net/v1/guest"
    TIMEOUT = 900  # 15 minutes max wait
    POLL_INTERVAL = (15, 35)  # Human-like jitter

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json"
        })
        Logger.empire("B 007 5SIM CLIENT INITIALIZED")

    def _request(self, endpoint: str, params: Dict = None) -> Optional[Dict[Any, Any]]:
        url = f"{self.BASE_URL}{endpoint}"
        proxy = ProxyRotator.get()
        proxy_dict = {"http": proxy, "https": proxy} if isinstance(proxy, str) else None

        try:
            response = self.session.get(url, params=params, proxies=proxy_dict, timeout=20)
            if response.status_code == 200:
                return response.json()
            else:
                Logger.error(f"5SIM HTTP {response.status_code}: {response.text}")
        except Exception as e:
            Logger.error(f"5SIM Request Failed: {e}")
        return None

    def buy_usa_number(self) -> Optional[Dict[str, Any]]:
        """
        Purchase USA number for Telegram
        Returns: {"source": "5sim", "id": "...", "phone": "+15551234567", "sms": []}
        """
        Logger.b007("REQUESTING USA NUMBER FROM 5SIM.NET")
        data = self._request("/buy/activation/usa/any/telegram")
        
        if data and "phone" in data and data.get("phone"):
            phone = data["phone"]
            activation_id = data.get("id", "unknown")
            Logger.success(f"5SIM → USA NUMBER ACQUIRED: +{phone} | ID: {activation_id}")
            return {
                "source": "5sim",
                "id": activation_id,
                "phone": phone,
                "raw": data
            }
        
        Logger.error("5SIM: NO USA NUMBERS AVAILABLE OR ERROR")
        return None

    def get_sms_code(self, activation_id: str) -> Optional[str]:
        """
        Poll for SMS code with B 007 human-like jitter
        Auto-cancel if no SMS in 15 min → Full refund
        """
        Logger.b007(f"POLLING SMS FOR 5SIM ID: {activation_id}")
        start_time = time.time()

        while time.time() - start_time < self.TIMEOUT:
            data = self._request(f"/check/{activation_id}")
            if not data:
                time.sleep(random.uniform(*self.POLL_INTERVAL))
                continue

            if data.get("status") == "FINISHED" and data.get("sms"):
                code = data["sms"][0].get("code") or data["sms"][0].get("text", "").split()[-1]
                if code and code.isdigit():
                    Logger.success(f"B 007 CAPTURED CODE: {code}")
                    return code

            elif data.get("status") == "CANCELED":
                Logger.error("5SIM ACTIVATION CANCELED")
                return None

            time.sleep(random.uniform(*self.POLL_INTERVAL))

        # Timeout → Auto cancel for refund
        self.cancel_activation(activation_id)
        Logger.b007("5SIM TIMEOUT → AUTO REFUND ISSUED")
        return None

    def cancel_activation(self, activation_id: str) -> bool:
        """
        Cancel activation → Get full refund
        """
        result = self._request(f"/cancel/{activation_id}")
        if result and result.get("status") == "CANCELED":
            Logger.empire(f"B 007 REFUNDED 5SIM ID: {activation_id}")
            return True
        return False

    def get_balance(self) -> float:
        """Check 5SIM balance"""
        data = self._request("/profile")
        balance = data.get("balance", 0.0) if data else 0.0
        Logger.b007(f"5SIM BALANCE: ${balance:.2f}")
        return balance


# B 007 USAGE EXAMPLE
if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()

    client = FiveSimClient(api_key=os.getenv("FIVSIM_KEY"))
    
    activation = client.buy_usa_number()
    if activation:
        code = client.get_sms_code(activation["id"])
        if code:
            print(f"B 007 FINAL CODE: {code}")
        else:
            print("B 007 NO CODE RECEIVED")
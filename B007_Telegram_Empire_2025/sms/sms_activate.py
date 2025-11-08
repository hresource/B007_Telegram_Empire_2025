# sms/sms_activate.py
import requests, time, random
from utils.logger import Logger
from proxy.rotator import ProxyRotator

class SMSActivateClient:
    BASE_URL = "https://api.sms-activate.ae/stubs/handler_api.php"

    def __init__(self, api_key):
        self.api_key = api_key
        self.session = requests.Session()

    def buy_usa_number(self):
        params = {"action": "getNumber", "service": "tg", "country": 6, "maxPrice": 1.20, "api_key": self.api_key}
        proxy = ProxyRotator.get()
        try:
            r = self.session.get(self.BASE_URL, params=params, proxies={"http": proxy, "https": proxy} if isinstance(proxy, str) else None, timeout=20)
            if "ACCESS_NUMBER" in r.text:
                _, aid, phone = r.text.split(":")
                Logger.success(f"SMS-Activate → +{phone}")
                return {"source": "smsactivate", "aid": aid, "phone": phone}
        except: pass
        return None

    def get_code(self, aid):
        for _ in range(40):
            resp = self.session.get(self.BASE_URL, params={"action": "getStatus", "id": aid, "api_key": self.api_key})
            if "STATUS_OK" in resp.text:
                code = resp.text.split(":")[1]
                self.session.get(self.BASE_URL, params={"action": "setStatus", "status": 6, "id": aid, "api_key": self.api_key})
                return code
            time.sleep(random.uniform(15, 32))
        self.session.get(self.BASE_URL, params={"action": "setStatus", "status": 8, "id": aid, "api_key": self.api_key})
        return None
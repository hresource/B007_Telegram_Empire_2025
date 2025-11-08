# proxy/rotator.py
import random, time
from utils.logger import Logger

class ProxyRotator:
    @staticmethod
    def get():
        techniques = [
            f"http://mobile-us-5g-rotate:pass@mobile.proxyempire.io:9000",
            f"http://customer-user-cc-US-session-{int(time.time())}{random.randint(10000,99999)}-sesstime-20:pass@p.iproyal.com:12321",
            ("proxy.mtproto.co", 443, f"dd{random.randint(1,9)}ad=1ttl={random.randint(64,128)}")
        ]
        proxy = random.choice(techniques)
        Logger.empire(f"PROXY ROTATION → {type(proxy).__name__}")
        return proxy
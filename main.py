from rich import print
from hashlib import sha256


def Hash(self, DATA):
    return sha256(DATA.encode("ascii")).hexdigest()

def Mine(self, MineData, turns, dif=1):
    zeroes = "0" * dif
    current = ""
    for nonce in range(0, turns):
        current = self.Hash(f"{MineData}{nonce}")
        if self.Show:
            print(f"[blue] HASH : {current} | ZEROES : {current[:dif]} [/blue]")
        if current.startswith(zeroes):
            print(f"[green] HASH : {current} | ZEROES : {current[:dif]} [/green]")
            break
    return current

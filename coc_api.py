import httpx
import json

class ClashOfClansAPI:
    def __init__(self):
        self.client = None

    async def start(self, token:str):
        self.client = httpx.AsyncClient(
            base_url="https://api.clashofclans.com/v1/",
            headers={"Authorization": f"Bearer {token}"} 
        )
        
    async def get_clan_war_log(self, tag: str):
        assert self.client is not None
        r = await self.client.get(f"clans/{tag}/currentwar")
        assert r.status_code==200, print(r)
        r = r.json()
        return r
        
    async def close(self):
        assert self.client is not None
        await self.client.aclose()


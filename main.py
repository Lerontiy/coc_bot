import asyncio
import traceback
from pprint import pprint

from coc_api.coc_api import ClashOfClansAPI
from coc_api.coc_token import COC_TOKEN

async def main():
    coc = ClashOfClansAPI()
    await coc.start(COC_TOKEN) 

    clan_tag = "%232CRCJP2GU"
    
    r:dict = await coc.get_clan_war_log(clan_tag)
    pprint(r)
    
    await coc.close() 
    
if __name__ == "__main__":
    asyncio.run(main())
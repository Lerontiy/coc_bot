import asyncio

from coc_api import ClashOfClansAPI
from coc_token import COC_TOKEN

async def main():
    coc = ClashOfClansAPI()
    await coc.start(COC_TOKEN) 

    clan_tag = "%232CRCJP2GU"
    
    try:
        print(await coc.get_clan_wag_log(clan_tag))
    except Exception as e:
        print("Error:", e)
    finally:
        await coc.close() 
    
if __name__ == "__main__":
    asyncio.run(main())
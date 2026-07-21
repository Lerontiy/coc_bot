import asyncio
# from pprint import pprint

from coc_api.coc_api import ClashOfClansAPI
from coc_api.coc_token import COC_TOKEN

from sheets_api.sheets_api import add_star

async def main():
    coc = ClashOfClansAPI()
    await coc.start(COC_TOKEN) 

    clan_tag = "%232CRCJP2GU"
    
    r:dict = await coc.get_current_war(clan_tag)
    # pprint(r)
    if r['state'] == "war":
        for m in r['clan']['members']:
            if 'attacks' in m:
                s = 0
                for a in m['attacks']:
                    s += a['starrs']
                if s >= 5:
                    await add_star(m['name'], r['opponent']['name'])
    
    await coc.close() 
    
if __name__ == "__main__":
    asyncio.run(main())
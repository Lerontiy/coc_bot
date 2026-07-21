import asyncio
import gspread_asyncio
from google.oauth2.service_account import Credentials
from gspread.utils import rowcol_to_a1

def get_creds():
    creds = Credentials.from_service_account_file('./coc-bot.json')
    scoped = creds.with_scopes([
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ])
    return scoped

async def add_new_info(player_name:str, clan_name:str):
    agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
    
    agc = await agcm.authorize()
    
    sh = await agc.open("Голі баби")
    worksheet = await sh.get_worksheet(0)
    
    player_cell = await worksheet.find(player_name, in_column=1)
    if player_cell is None:
        player_cell = await worksheet.append_row(
            [player_name],
            value_input_option="USER_ENTERED",  
            insert_data_option="INSERT_ROWS"    
        )
        player_cell = player_cell['updates']['updatedRange'].split('!')[1][1:]
    else:
        player_cell = player_cell.address[1:]

    clan_cell = await worksheet.find(clan_name, in_row=1)
    if clan_cell is None:
        first_row = await worksheet.row_values(1)
        next_col_index = len(first_row) + 1
        start_cell = rowcol_to_a1(1, next_col_index)    
        clan_cell = await worksheet.update(
            [[clan_name]], 
            range_name=start_cell,
            value_input_option="USER_ENTERED",
        )
        clan_cell = clan_cell['updatedRange'].split('!')[1][:1]
    else:
        clan_cell = clan_cell.address[:1]
    
    await worksheet.update(
        range_name=f"{clan_cell}{player_cell}", 
        values=[["*"]]
    )

    await worksheet.sort([(2, 'des')])
    # print(f"{clan_cell}{player_cell}")
    
asyncio.run(add_new_info("123", "123"))
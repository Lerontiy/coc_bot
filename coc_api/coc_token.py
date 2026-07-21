import os
import dotenv
dotenv.load_dotenv()

COC_TOKEN = os.environ.get("COC_TOKEN")
assert COC_TOKEN is not None
COC_TOKEN = str(COC_TOKEN)
    
import os
from datetime import datetime
import random

admin = 787080961

token = ''
parse_mode = 'Markdown'

coder_info = '\n\033[30m    ' \
             '\033[39m- \033[34mGithub \033[39m: @alexndrev\n' \
             '\033[30m    ' \
             '\033[39m- \033[34mTelegram \033[39m: @alexndrev'


async def on_startup(dp):
    os.system("cls")
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    print(f'\033[35mBot Started :\033[39m {current_time}')
    print('- - - - - - - - - - - - - -')
    print(f'\033[35mCreator contacts: {coder_info}\033[39m')
    print('- - - - - - - - - - - - - -')


async def on_shutdown(dp):
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    print(f'\033[35mBot Stopped :\033[39m {current_time}')

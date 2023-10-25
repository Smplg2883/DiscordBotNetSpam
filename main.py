import asyncio

from bot import MyBot

channel_id1 = 534252345



TOKEN1 = 'TOKEN HERE'
#TOKEN2 = 

file_path = "n.txt"
with open(file_path, 'r') as file:
    file_contents = file.read()
    print(f"{file_path} has {len(file_contents)} characters")

bot1 = MyBot(TOKEN1, channel_id1, file_contents)
#bot2 = 

loop = asyncio.get_event_loop()
tasks = [  
    asyncio.ensure_future(bot1.run_bot()),
    #asyncio.ensure_future(bot2.run_bot())
    
]
loop.run_until_complete(asyncio.wait(tasks))

# bot2.run_bot()

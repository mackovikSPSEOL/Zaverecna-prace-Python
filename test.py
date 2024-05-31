timer = 0
import asyncio
while True:
    async def pocitani_sekund():
        global timer
        await asyncio.sleep(1)
        timer += 1
    asyncio.run(pocitani_sekund())
    print(timer)
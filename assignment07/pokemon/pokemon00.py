import aiofiles
import asyncio
import json

pokemonapi_directory = "./assignment07/pokemon/pokemonapi"
pokemonmove_directory = "./assignment07/pokemon/pokemonmove"

async def main():
    #Read the content of the json file.
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode = 'r') as f:
        content = await f.read()
    print(content)

asyncio.run(main())
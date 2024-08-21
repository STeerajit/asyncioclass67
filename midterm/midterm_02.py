import asyncio
import httpx
import time
async def pokemon_names(ability_url):
    async with httpx.AsyncClient() as client:
        response = await client.get(ability_url)
        data = response.json()
        pokemon_names = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
        return pokemon_names

async def main():
    start_time = time.perf_counter()
    end_time = time.perf_counter()
    ability_urls = {
        "battle_armor": "https://pokeapi.co/api/v2/ability/battle-armor",
        "speed_boost": "https://pokeapi.co/api/v2/ability/speed-boost"
    }

    tasks = [pokemon_names(url) for url in ability_urls.values()]

    results = await asyncio.gather(*tasks)

    battle_armor_pokemon, speed_boost_pokemon = results
    
    print("battle armor:")
    print(f"{time.ctime()} - Asynchronous get {len(battle_armor_pokemon)} pokemons. Time taken: {end_time-start_time} seconds")
    print(", ".join(battle_armor_pokemon))

    print("speed boost:")
    print(f"{time.ctime()} - Asynchronous get {len(speed_boost_pokemon)} pokemons. Time taken: {end_time-start_time} seconds")
    print(", ".join(speed_boost_pokemon))

asyncio.run(main())

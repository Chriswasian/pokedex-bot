import discord
from discord.ext import commands
from pokedex import get_evolution
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def build_chain(chain, indent=0):
    name = chain['species']['name'].capitalize()
    details = chain.get('evolution_details', [])
    detail = details[0] if details else {}
    level = detail.get('min_level')
    item = detail.get('item')
    happiness = detail.get('min_happiness')
    trigger = (detail.get('trigger') or {}).get('name', '')
    condition = ""
    if level:
        condition = f" (level {level})"
    elif item:
        condition = f" ({item['name'].replace('-', ' ').title()})"
    elif happiness:
        condition = " (happiness)"
    elif trigger == 'trade':
        condition = " (trade)"
    result = " " * indent + "→ " + name + condition + "\n"
    for evo in chain.get('evolves_to', []):
        result += build_chain(evo, indent + 1)
    return result

@bot.command()
async def evolve(ctx, pokemon):
    chain = get_evolution(pokemon)
    if chain is None:
        await ctx.send(f"❌ Pokémon '{pokemon}' not found!")
    else:
        result = build_chain(chain)
    await ctx.send(f"**{pokemon.capitalize()} Evolution Chain:**\n{result}")
    
bot.run(os.getenv('DISCORD_TOKEN'))

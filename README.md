# Pokédex Discord Bot

A Discord bot that looks up Pokémon evolution chains using the PokéAPI.

## Commands
- `!evolve <pokemon>` — returns the full evolution chain for any Pokémon

## Examples
- `!evolve pikachu` → Pichu → Pikachu → Raichu
- `!evolve eevee` → all 8 Eeveelutions

## How to Run
bash
source venv/bin/activate
python3 bot.py
## Setup
1. Create a bot at https://discord.com/developers/applications
2. Enable Message Content Intent under Bot settings
3. Add your token to a `.env` file: `DISCORD_TOKEN=your_token_here`
4. Invite the bot to your server via OAuth2 URL Generator

## Built with
Python · discord.py · PokéAPI · dotenv 
import discord
from discord.ext import commands
from colorama import Fore, init
import os
import requests
import re
import json
import sys

init(convert=True)

with open("token.json", "r") as file:
    data = json.load(file)

def check():
    r = requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": data["token"]})
    if r.status_code == 200:
       pass
    else:
        print(f"{Fore.RED}Token invalide." + Fore.RESET)
        os.system('pause')
        sys.exit()

check()

client = commands.Bot("", self_bot=True)

codeRegex = re.compile("(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")
     
@client.event
async def on_connect():
    print(f"""{Fore.BLUE}
        
        
                                 _   _ _ _              _____ _       _                     
                                | \ | (_) |            / ____| |     (_)                    
                                |  \| |_| |_ _ __ ___ | |    | | __ _ _ _ __ ___   ___ _ __ 
                                | . ` | | __| '__/ _ \| |    | |/ _` | | '_ ` _ \ / _ \ '__|
                                | |\  | | |_| | | (_) | |____| | (_| | | | | | | |  __/ |   
                                |_| \_|_|\__|_|  \___/ \_____|_|\__,_|_|_| |_| |_|\___|_|    by Teobre


                                {Fore.WHITE}Connecté sur {Fore.GREEN}{client.user.name}#{client.user.discriminator}


        """ + Fore.RESET)

@client.event
async def on_message(message):
    if codeRegex.search(message.content):
        code = codeRegex.search(message.content).group(2)

        if len(code) < 16:
            try:
                print(f"\n{Fore.LIGHTRED_EX}[-] Code fake auto-détecté: {code}\n      {Fore.LIGHTYELLOW_EX}Utilisateur: {message.author.name}#{message.author.discriminator}\n      Serveur: {message.guild.name}\n      Channel: {message.channel.name}" + Fore.RESET)
            except:
                print(f"\n{Fore.LIGHTRED_EX}[-] Code fake auto-détecté: {code}\n      {Fore.LIGHTYELLOW_EX}Utilisateur: {message.author.name}#{message.author.discriminator}" + Fore.RESET)
        else:
            headers = {"authorization": data["token"]}
            payload = {"channel_id": str(message.channel.id)}
            r = requests.post(f"https://discord.com/api/v8/entitlements/gift-codes/{code}/redeem", headers=headers, json=payload).text
            if "This gift has been redeemed already." in r:
                try:
                    print(f"\n{Fore.LIGHTYELLOW_EX}[-] Code déjà utilisé: {code}\n        {Fore.LIGHTYELLOW_EX}Utilisateur: {message.author.name}#{message.author.discriminator}\n       Serveur: {message.guild.name}\n       Channel: {message.channel.name}" + Fore.RESET)
                except:
                    print(f"\n{Fore.LIGHTYELLOW_EX}[-] Code déjà utilisé: {code}\n{       Fore.LIGHTYELLOW_EX}Utilisateur: {message.author.name}#{message.author.discriminator}" + Fore.RESET)
            elif "subscription_plan" in r:
                try:
                    print(f"\n{Fore.LIGHTGREEN_EX}[+] Code valide: {code}\n        {Fore.LIGHTYELLOW_EX}Utilisateur: {message.author.name}#{message.author.discriminator}\n      Serveur: {message.guild.name}\n       Channel: {message.channel.name}" + Fore.RESET)
                except:
                    print(f"\n{Fore.LIGHTGREEN_EX}[+] Code valide: {code}\n       {Fore.LIGHTYELLOW_EX}Utilisateur: {message.author.name}#{message.author.discriminator}" + Fore.RESET)
            elif "Unknow" in r:
                try:
                    print(f"\n{Fore.RED}[-] Code invalide: {code}\n       {Fore.LIGHTYELLOW_EX}Utilisateur: {message.author.name}#{message.author.discriminator}\n       Serveur: {message.guild.name}\n       Channel: {message.channel.name}" + Fore.RESET)
                except:
                    print(f"\n{Fore.RED}[-] Code invalide: {code}\n       {Fore.LIGHTYELLOW_EX}Utilisateur: {message.author.name}#{message.author.discriminator}" + Fore.RESET)


client.run(data["token"], bot=False)

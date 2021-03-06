import discord
import asyncio
import random
from pickle import load
import requests
import requests.auth
from discord.ext import commands
import time
start_time = time.time()

import wikipedia
import praw
import os
import sys
import psutil

## Prompt / Response variables
prompt = requests.get('https://raw.githubusercontent.com/CocoisBuggy/Prompt-response567576/master/prompt.txt')
prompt_list_layer1 = prompt.text.replace('\n', '')
prompt_list_layer2 = (prompt_list_layer1).split(',')
odd_i = []
even_i = []
for i in range(0, len(prompt_list_layer2)):
    if i % 2:
        even_i.append(prompt_list_layer2[i])
    else :
        odd_i.append(prompt_list_layer2[i])



def command_count():
    message_count=open("disbot_data.txt", 'r+', encoding='utf8')
    message_count_vol=int(message_count.read())
    message_count.close()

    last_count=message_count_vol
    a_count = last_count+1
    gfg = open("disbot_data.txt", 'w', encoding='utf8')
    gfg.write(str(a_count))
    gfg.close()
    print('total commands called:',a_count)



emoji = '\N{MUSHROOM}'


###REDDIT log in
redd_cred = open('praw_cred.txt', 'r', encoding='utf8')
all_lines = redd_cred.readlines()

reddit = praw.Reddit(client_id=all_lines[0].replace('\n', ''),
                     client_secret=all_lines[1].replace('\n', ''),
                     password=all_lines[2].replace('\n', ''),
                     user_agent=all_lines[3].replace('\n', ''),
                     username=all_lines[4].replace('\n', ''))
currentuser=reddit.user.me()
print('REDDIT USER LOGGED IN AS:')
print(currentuser)


url='https://icanhazdadjoke.com/'
modelgen=open("smartgen.txt", "r", encoding='utf8')
thoughts=open("thoughts.JSON", "r", encoding='utf8')
split_thought=thoughts.readlines()
facts=open("facts.txt", "r", encoding='utf8')
readfacts=facts.readlines()
lms=modelgen.readlines()

link_log = open('link_log.txt', 'a+', encoding='utf8')
link_log.close()

class MyClient(discord.Client):

    async def on_ready(self):
        activity = discord.Game(name="Everything.")
        await client.change_presence(status=discord.Status.online, activity=activity)
        print('Logged on as {0}!'.format(self.user))
        print('We go now!')


    async def on_message(self, message):
        if message.author.id == self.user.id:
            command_count()
            return

        cont=message.content.lower()

        print(message.author.id, 'Message from {0.author}: {0.content}'.format(message))
        if cont.startswith('https:'):
            with open('link_log.txt', 'a+', encoding='utf8') as link_log:
                link_log.write(cont+'\n')
        if cont.startswith('-play https:'):
            hsj=cont[6:]
            with open('link_log.txt', 'a+', encoding='utf8') as link_log:
                link_log.write(hsj+'\n')


##RCON DEFINE   ###############################################################

        if message.content.startswith('!mushRcon:'):
            print('rcon access requested')
            if message.author.id == 387898904710217728:
                await message.channel.send('`>> rcon access granted`')
                print('rcon access granted')


                if message.content == ('!mushRcon: help'):
                    await message.channel.send('`>>  -c  prefix for execution in shell`')
                    await message.channel.send('`>>  -mush (netstat, netstat/clear, print-uptime)`')

                if message.content.startswith('!mushRcon: -c '):
                    command=message.content[14:]
                    exec(command)
                    print(command)

                if message.content == ('!mushRcon: -mush netstat'):
                    await message.channel.send(file=discord.File('datausage.png'))

                if message.content == ('!mushRcon: -mush netstat/clear'):
                    os.remove("datausage.png")
                    await message.channel.send('`>> Datausage log cleared`')

                if message.content == ('!mushRcon: -mush reload'):

                    await message.channel.send('`>> reloaded`')

                if message.content == ('!mushRcon: -mush print-uptime'):
                    elapsed_time = time.time() - start_time
                    round_time=round(elapsed_time, 2)
                    round_minutes=(round_time/60)
                    await message.channel.send('`>> {} minutes. Fuck you do the math. `'.format(round_minutes))

            else:
                await message.channel.send('`>> RCON Access denied. Fucker.`')
###############################################################################``

        if (message.author.id == 220156117983035392):
            billchance=random.randint(1,20)
            if billchance == 1:
                await message.channel.send("Bill? More like LOSER! **GOTEEEM**")


        if cont == ('!mush'):
            embed = (discord.Embed(description="HELP?!?!?!", colour=0x3DF270))
            await message.channel.send(embed=embed)
            await message.add_reaction(emoji) #Reaction

        if cont == ('!mushcount'):
            message_count=open("disbot_data.txt", 'r+', encoding='utf8')
            message_count_vol=int(message_count.read())
            message_count.close()
            await message.channel.send("You guys have called me **{}** times. Damn you.".format(message_count_vol))
            await message.add_reaction(emoji) #Reaction

        if cont == ('what are you looking at?'):

            random_submission = reddit.subreddit('all').random()
            if random_submission.over_18:
                await message.channel.send("uh... Nothing.")
            else:
                print(random_submission.url)
                await message.channel.send("This thing from **{}** \n{}".format(random_submission.subreddit_name_prefixed, random_submission.url))

            await message.add_reaction(emoji) #Reaction




        if cont == ('teach me something'):
            randw=wikipedia.random(pages=1)

            try:
                p = wikipedia.page(randw)
                sum = wikipedia.summary(randw)
            except wikipedia.DisambiguationError as e:
                s = random.choice(e.options)
                p = wikipedia.page(s)
                sum = wikipedia.summary(s)


            wiki = (discord.Embed(title=p.title,description=sum[:700]+'...', colour=0x3DF270, url=p.url))
            wiki.set_author(name='Here\'s something you can learn', icon_url='https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/103px-Wikipedia-logo-v2.svg.png')
            try:
                wiki.set_image(url=p.images[0])
            except IndexError:
                wiki.set_images(url='https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/103px-Wikipedia-logo-v2.svg.png')

            await message.channel.send(embed=wiki)
            await message.add_reaction(emoji) #Reaction


        if cont.startswith('!mushseek'):
            search=cont[9:]

            try:
                ps = wikipedia.page(search)
                sums = wikipedia.summary(search)
            except wikipedia.DisambiguationError as es:
                ss = random.choice(es.options)
                ps = wikipedia.page(ss)
                sums = wikipedia.summary(ss)


            wiki2 = (discord.Embed(title=ps.title,description=sums[:700]+'...', colour=0x3DF270, url=ps.url))
            wiki2.set_author(name='Here\'s something you can learn', icon_url='https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/103px-Wikipedia-logo-v2.svg.png')
            try:
                wiki2.set_image(url=ps.images[0])
            except IndexError:
                wiki2.set_image(url='https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/103px-Wikipedia-logo-v2.svg.png')
               ## pass
            await message.channel.send(embed=wiki2)
            await message.add_reaction(emoji) #Reaction


        if cont == ('i am coco'):
            if message.author.id == 387898904710217728:
                await message.channel.send('Daddy?')
            else:
                await message.channel.send('Fuck right off you dumb imposter.')

        if cont == ('are you smart?'):
            rand_line=random.randint(1,2000)
            splitme=str(lms[rand_line])
            await message.channel.send(splitme)
            await message.add_reaction(emoji) #Reaction

        if cont == ('penny for your thoughts?'):
            rand_thought=random.randint(1,49)
            ##split_thought=thoughts.readlines()
            await message.channel.send(split_thought[rand_thought])
            await message.add_reaction(emoji) #Reaction

        if cont == ('fact'):
            rand_fact=random.randint(1,550)
            print(rand_fact)
            splitme=readfacts[rand_fact]
            await message.channel.send(splitme)
            await message.add_reaction(emoji) #Reaction

        if cont == ('tell a joke'):
            response=requests.get(url, headers={"Accept": "text/plain"})
            await message.channel.send(response.text)
            await message.add_reaction(emoji) #Reaction

##Prompt / response code###########
##All non-special responses.
        res = 0
        for line in odd_i:
            if cont == line:
                print(even_i[res])
                await message.channel.send(even_i[res])
            res = res+1


        if 'wanna play' in cont:
            await message.channel.send('You have no friends.')
        if 'dbd' in cont:
            await message.channel.send('dbd is shitty game.')
        if 'hello' in cont:
            await message.channel.send('I dislike you already.')
        if '69' in cont:
            await message.channel.send('nice.')
        if 'mushroom' in cont:
            await message.channel.send('I\'m Mr Mushroom!')

        randomth=random.randint(1,60)
        if randomth == 1:
            rand_thought=random.randint(1,49)
            await message.channel.send(split_thought[rand_thought])
            await message.channel.send(split_thought)

client = MyClient()
client.run(all_lines[5].replace('\n', ''))

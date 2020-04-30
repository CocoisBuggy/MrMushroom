import discord
import asyncio
import random
from pickle import load
import requests
import requests.auth
import time
start_time = time.time()
import wikipedia
import praw
import os

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


###REDDIT log in
reddit = praw.Reddit(client_id='VMCJgB7S5iAYRA',
                     client_secret='2OIH72qxFqbuChVkGvaqp6upZAI',
                     password='redditiscoco123',
                     user_agent='testscript by /u/CocoisAfraid ',
                     username='CocoisAfraid')
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

        print('Message from {0.author}: {0.content}'.format(message))
        print(message.author.id)

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

                if message.content == ('!mushRcon: -mush print-uptime'):
                    elapsed_time = time.time() - start_time
                    round_time=round(elapsed_time, 2)
                    round_minutes=(round_time/60)
                    await message.channel.send('`>> {} minutes. Fuck you do the math. `'.format(round_minutes))

            else:
                await message.channel.send('`>> RCON Access denied. Fucker.`')
###############################################################################

        if (message.author.id == 220156117983035392):
            billchance=random.randint(1,20)
            if billchance == 1:
                await message.channel.send("Bill? More like LOSER! **GOTEEEM**")


        if cont == ('!mush'):
            embed = (discord.Embed(description="HELP?!?!?!", colour=0x3DF270))
            await message.channel.send(embed=embed)

        if cont == ('!mushcount'):
            message_count=open("disbot_data.txt", 'r+', encoding='utf8')
            message_count_vol=int(message_count.read())
            message_count.close()
            await message.channel.send("You guys have called me **{}** times. Damn you.".format(message_count_vol))

        if cont == ('what are you looking at?'):

            random_submission = reddit.subreddit('all').random()
            if random_submission.over_18:
                await message.channel.send("uh... Nothing.")
            else:
                print(random_submission.url)
                await message.channel.send("This thing from **{}** \n{}".format(random_submission.subreddit_name_prefixed, random_submission.url))




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


        if cont == ('i am coco'):
            if message.author.id == 387898904710217728:
                await message.channel.send('Daddy?')
            else:
                await message.channel.send('Fuck right off you dumb imposter.')

        if cont == ('are you smart?'):
            rand_line=random.randint(1,2000)
            splitme=str(lms[rand_line])
            await message.channel.send(splitme)

        if cont == ('penny for your thoughts?'):
            rand_thought=random.randint(1,49)
            ##split_thought=thoughts.readlines()
            await message.channel.send(split_thought[rand_thought])

        if cont == ('fact'):
            rand_fact=random.randint(1,550)
            print(rand_fact)
            splitme=readfacts[rand_fact]
            await message.channel.send(splitme)

        if cont == ('hey'):
            await message.channel.send('Fuck you.')

        if cont == ('tell a joke'):
            response=requests.get(url, headers={"Accept": "text/plain"})
            await message.channel.send(response.text)

        if cont == ('i love you'):
            await message.channel.send('You could never be loved.')
        if cont == ('shut up'):
            await message.channel.send('I wish I could!')
        if cont == ('wanna be friends?'):
            await message.channel.send('I don\'t think we have that kind of relationship')
        if cont == ('otp'):
            await message.channel.send('**Antisemitic joke goes here**')
        if cont == ('sad'):
            await message.channel.send('**PAARP Bwaaarp**')

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

        randomth=random.randint(1,10)
        if randomth == 1:
            rand_thought=random.randint(1,49)
            await message.channel.send(split_thought[rand_thought])
            await message.channel.send(split_thought)


client = MyClient()
client.run('Njk4MTU5MDI3NzcwNjIxOTY0.XptXeg.TzGOaUPmVTfpx7tP6QUo6pcPe2E')

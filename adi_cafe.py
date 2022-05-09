import discord

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('owo'):
    await message.channel.send('I would question myself as to why im texting a teenager!')

  if message.content.startswith('lol'):
    await message.channel.send('Why! Why! Why! Why dont you guys use hahahaha or some stupid emoji instead of using this')

  if message.content.startswith('lmaoo'):
    await message.channel.send('Why! Why! Why! Why dont you guys use hahahaha or some stupid emoji instead of using this')

  if message.content.startswith('lmfaoo'):
    await message.channel.send('Why! Why! Why! Why dont you guys use hahahaha or some stupid emoji instead of using this')

  if message.content.startswith('Lol'):
    await message.channel.send('Why! Why! Why! Why dont you guys use hahahaha or some stupid emoji instead of using this')

  if message.content.startswith('Lmaoo'):
    await message.channel.send('Why! Why! Why! Why dont you guys use hahahaha or some stupid emoji instead of using this')

  if message.content.startswith('Lmfaoo'):
    await message.channel.send('Why! Why! Why! Why dont you guys use hahahaha or some stupid emoji instead of using this')

  if message.content.startswith('noice'):
    await message.channel.send('It is!!! Thanks douche nozzle!')

  if message.content.startswith('nice'):
    await message.channel.send('It is!!! Thanks douche nozzle!')

  if message.content.startswith('Noice'):
    await message.channel.send('It is!!! Thanks douche nozzle!')
  
  if message.content.startswith('whe'):
    await message.channel.send('https://tenor.com/view/whee-whe-wheee-rolling-gif-7172470')

  if message.content.startswith('bro'):
    await message.channel.send('https://tenor.com/view/yeah-what-ricky-berwick-whats-up-whats-wrong-on-call-gif-17578479')

  if message.content.startswith('Bro'):
    await message.channel.send('https://tenor.com/view/yeah-what-ricky-berwick-whats-up-whats-wrong-on-call-gif-17578479')

  if message.content.startswith('np'):
    await message.channel.send('https://tenor.com/view/no-problem-snoop-dogg-anytime-absolutely-no-problemo-gif-16225380')

  if message.content.startswith('Np'):
    await message.channel.send('https://tenor.com/view/no-problem-snoop-dogg-anytime-absolutely-no-problemo-gif-16225380')


  if message.content.startswith('ping'):
    await message.channel.send('pong')

  
  if message.content.startswith(';-;'):
    await message.channel.send('https://tenor.com/view/buerk-disgusting-r%C3%A9pugant-affreux-d%C3%A9gueulasse-gif-22333017')

  if message.content.startswith('sup'):
    await message.channel.send('https://tenor.com/view/gangstas-whats-up-guys-hey-whats-up-hello-gif-17098292')

  if message.content.startswith('Sup'):
    await message.channel.send('https://tenor.com/view/gangstas-whats-up-guys-hey-whats-up-hello-gif-17098292')

  if message.content.startswith('hi'):
    await message.channel.send('https://tenor.com/view/say-what-dunno-shrug-john-krasinski-idk-gif-16557956')

  if message.content.startswith('info'):
    await message.channel.send('Created_By: AdiTheGeek#4803')

  if message.content.startswith('ok'):
    await message.channel.send('https://tenor.com/view/love-gif-24777608')

  if message.content.startswith('strange'):
    await message.channel.send('https://media.giphy.com/media/406ZMCwmTzYfo4E9cS/giphy.gif')  
  
  if message.content.startswith('help'):
    await message.channel.send(' Sure. How can I help?')  

  if message.content.startswith('gm'):
    await message.channel.send('Good Morning')

  if message.content.startswith('good Morning'):
    await message.channel.send('Good Morning')

  if message.content.startswith('stop'):
    await message.channel.send('https://tenor.com/bMkPz.gif')

  if message.content.startswith('emotional Damage'):
    await message.channel.send('https://tenor.com/view/steven-he-asian-steven-gif-23432398')
 
  if message.content.startswith('what the hell'):
    await message.channel.send('Hell,who said it ?')

  if message.content.startswith('vc'):
    await message.channel.send('Yhea coming bro')

  if message.content.startswith('are you free'):
    await message.channel.send('No')

  if message.content.startswith('wdym'):
    await message.channel.send('What do you think I mean')

  if message.content.startswith('ikr'):
    await message.channel.send('I know everything') 

  if message.content.startswith('no'):
    await message.channel.send('Yes')

  if message.content.startswith('yes'):
    await message.channel.send('No')
        
# Now the same Code for Upper case letters

  if message.content.startswith('hello'.upper()):
    await message.channel.send('Hello!')

  if message.content.startswith('owo'.upper()):
    await message.channel.send('I would question myself as to why im texting a teenager!')

  if message.content.startswith('lol'.upper()):
    await message.channel.send('Why! Why! Why! Why dont you guys use hahahaha or some stupid emoji instead of using this')

  if message.content.startswith('lmaoo'.upper()):
    await message.channel.send('Why! Why! Why! Why dont you guys use hahahaha or some stupid emoji instead of using this')

  if message.content.startswith('lmfaoo'.upper()):
    await message.channel.send('Why! Why! Why! Why dont you guys use hahahaha or some stupid emoji instead of using this')

  if message.content.startswith('noice'.upper()):
    await message.channel.send('It is!!! Thanks douche nozzle!')

  if message.content.startswith('nice'.upper()):
    await message.channel.send('It is!!! Thanks douche nozzle!')

  
  if message.content.startswith('whe'.upper()):
    await message.channel.send('https://tenor.com/view/whee-whe-wheee-rolling-gif-7172470')


  if message.content.startswith('Bro'.upper()):
    await message.channel.send('https://tenor.com/view/yeah-what-ricky-berwick-whats-up-whats-wrong-on-call-gif-17578479')

  if message.content.startswith('Np'.upper()):
    await message.channel.send('https://tenor.com/view/no-problem-snoop-dogg-anytime-absolutely-no-problemo-gif-16225380')

  if message.content.startswith('sup'.upper()):
    await message.channel.send('https://tenor.com/view/gangstas-whats-up-guys-hey-whats-up-hello-gif-17098292')

  if message.content.startswith('Hi'.upper()):
    await message.channel.send('https://tenor.com/view/say-what-dunno-shrug-john-krasinski-idk-gif-16557956')

  if message.content.startswith('info'.upper()):
    await message.channel.send('Created_By: AdiTheGeek#4803')

  if message.content.startswith('ping'.upper()):
    await message.channel.send('pong')

  if message.content.startswith('Ok'.upper()):
    await message.channel.send('https://tenor.com/view/love-gif-24777608')

  if message.content.startswith('strange'.upper()):
    await message.channel.send('https://media.giphy.com/media/406ZMCwmTzYfo4E9cS/giphy.gif')

  if message.content.startswith('help'.upper()):
    await message.channel.send(' Sure. How can I help?')

  if message.content.startswith('Gm'.upper()):
    await message.channel.send('Good Morning')

  if message.content.startswith('Good Morning'.upper()):
    await message.channel.send('Good Morning')     

  if message.content.startswith('stop'.upper()):
    await message.channel.send('https://tenor.com/bMkPz.gif')   

  if message.content.startswith('Emotional Damage'.upper()):
    await message.channel.send('https://tenor.com/view/steven-he-asian-steven-gif-23432398')     

  if message.content.startswith('Wdym'.upper()):
    await message.channel.send('What do you think I mean')   

  if message.content.startswith('ikr'.upper()):
    await message.channel.send('I know everything')   

  if message.content.startswith('no'.upper()):
    await message.channel.send('Yes')

  if message.content.startswith('yes'.upper()):
    await message.channel.send('No')               

my_secret = "paste you token here"
client.run(my_secret)

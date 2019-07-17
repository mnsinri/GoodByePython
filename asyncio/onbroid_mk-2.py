#what is Git?
import discord
import asyncio
import aiohttp
import lxml.html
import re
from random import randint
from googletrans import Translator

token_file = 'bot.txt'
t = Translator()
session = aiohttp.ClientSession()
client = discord.Client()

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh': 'chinese',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'filipino',
    'he': 'hebrew'
}

def get_token(token_file):
    with open(token_file) as f:
        return f.readline()

async def is_English(word):
    alphanum = re.compile(r'^[a-zA-Z0-9]+$')
    return alphanum.match(word) is not None

def this_lang_is(langs):
    if not langs:
        embed = discord.Embed(
            title="I don't know what is what.:thinking:",
            description="Maybe, it is non-existent lang.",
            color=0x2ee21f
            )
    else:
        description = ''
        for lang in langs:
            if lang not in LANGUAGES:
                lang = [k for k, v in LANGUAGES.items() if v == lang][0]
            description += f" {lang} : {LANGUAGES[lang]}\r"
        embed = discord.Embed(
        title="It is...",
        description=description,
        color=0x2ee21f
        )
    return embed

def show_lang():
    description = ''
    for key in LANGUAGES:
        description += f" {key} : {LANGUAGES[key]}\r"
    embed = discord.Embed(
        title="**Available Languages**",
        description=description,
        color=0x2ee21f
        )
    return embed

async def edit_embed(element, meaning, pronunce, data):
    embed=discord.Embed(
        title='**->**'+element,
        description='**'+meaning+'**\r-----------------------------------------',
        color=0xff80c0
        )
    for i in range(len(data)):
        embed.add_field(
            name=f'>>>  類語{i}: '+str(data[i][0])+'\r_'+str(data[i][1])+"_",
            value='**->** '+str(data[i][2]),
            inline=True
            )
    embed.set_footer(text='<発音記号 : '+pronunce+'>')
    return embed

async def nothing_came_up(element):
    fuckyou =[
        f"Standard English please?\rI don't understand **{element}**.",
        f"You're really an ass.\rWhat is **{element}**???:joy:",
        f"...{element}???:thinking:",
        f"I know how you feel.:sweat_smile:",
        f":eye:  　:eye:      -----------------------\r       :nose:         <   {element}? So what?\r       :lips:             -----------------------"
    ]
    embed=discord.Embed(
        title=fuckyou[randint(0,len(fuckyou)-1)],
        color=0xff80c0
        )
    return embed

async def get_synoym(url):
    data = []
    async with session.get(url) as response:
        root = lxml.html.fromstring(await response.text())
        for i in range(len(root.xpath('//*[@id="thesaurus-list-tbl"]/tbody/tr'))-1):
            synonym = []
            synonym.append(root.xpath(f'//*[@id="thesaurus-list-tbl"]/tbody/tr[{i+2}]/td[1]/p[1]')[0].text_content()) #synonym_jp 0
            synonym.append(root.xpath(f'//*[@id="thesaurus-list-tbl"]/tbody/tr[{i+2}]/td[1]/p[2]')[0].text_content()) #synonym_en 1
            synonym.append(root.xpath(f'//*[@id="thesaurus-list-tbl"]/tbody/tr[{i+2}]/td[2]/p')[0].text_content()) #fix_synonym 2
            data.append(synonym)
        return data

async def weblio_trans(element):
    url = f'https://ejje.weblio.jp/content/{element}'
    a_url = f'https://ejje.weblio.jp/english-thesaurus/content/{element}'
    async with session.get(url) as response:
            root = lxml.html.fromstring(await response.text())
            meaning = root.xpath('/html/head/meta[13]')[0].attrib['content']
            if 'weblio辞書で英語学習' in meaning:
                return await nothing_came_up(element)
            else:
                try:
                    pronunce = root.xpath('//*[@id="phoneticEjjeNavi"]/div/span[2]')[0].text #pronunciation 1
                except:
                    pronunce = ''
                data = await get_synoym(a_url)
                return await edit_embed(element, meaning, pronunce, data)

async def google_trans(element, dest):
    translate = t.translate(element, dest=dest).text
    embed = discord.Embed(
        title='**->** '+element+"  to  "+LANGUAGES[dest],
        description=translate,
        color=16738740
        )
    embed.set_footer(text='<Brought by google translation>')
    return embed

async def trans(contents):
    if len(contents) == 1 and await is_English(contents[0]):
        element = contents[0].lower()
        embed = await weblio_trans(element)
    else:
        dest = 'ja'
        for content in contents:
            if content[0] == '-':
                if content[1:].lower() in LANGUAGES:
                    dest = 'zh-cn' if content[1:].lower() == 'zn' else content[1:].lower()
                    contents.remove(content)
                else:
                    return show_lang()
        element = ' '.join(contents)
        embed = await google_trans(element, dest)

    return embed

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content[0] == '*': #translate
        contents = message.content[1:].split()
        embed = await trans(contents)
        await message.channel.send('', embed=embed)
    elif message.content[0] == '?':
        contents = message.content[1:].split()
        if contents[0] == 'help': #show available languages
            await message.channel.send('', embed=show_lang())
        elif contents[0] == 'onbroid': #close client
            await session.close()
            if session.closed:
                print('Aiohttp client session is closed')
            await client.close()
        elif contents[0] == 'whats': #tell available languages
            langs = []
            contents.remove('whats')
            contents_lower = [lang.lower() for lang in contents]
            for i in range(len(contents)):
                if contents_lower[i] in LANGUAGES or contents_lower[i] in LANGUAGES.values():
                    langs.append(contents_lower[i])
            await message.channel.send('', embed=this_lang_is(langs))

if __name__ == '__main__':
    client.run(get_token(token_file))

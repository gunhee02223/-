import discord
import datetime
client=discord.Client()
token='Njc4MTY5MDU0NTk4NjYwMDk3.Xke46A.D64tf55E3urbBKuw2TRjF53F_4c'
@client.event
async def on_ready():
    print('----------------------------------------------------------------------------')
    print(f'| Client ID: {client.user.id}                                             |')
    print(f'| Client Name: {client.user.name}                                                     |')
    print(f'| Client Token: {str(token)} |')
    print('----------------------------------------------------------------------------\n\n=========================================\n\n') 
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith('찰프야'):
        try:
            if message.content=='찰프야 핑':
                await message.channel.send('퐁!')
            if message.content=='찰프야 넌 누구니?':
                await message.channel.send('저는 어려분들의 인공지능 비서 찰프라고 해요')    
            if message.content=='찰프야 기능':
                await message.channel.send('찰프야 뒤에 넌 누구니?, 핑, 노래 틀어줘, 배고파, 심심해, 폭발해 등을 붙여주세요!')    
            if message.content=='찰프야 노래 틀어줘':
                await message.channel.send('저에게는 아직 그런 능력이 없어요:(')    
            if message.content=='찰프야 사랑해':
                await message.channel.send('저도 사랑해요♥')    
            if message.content=='찰프야 폭발해':
                await message.channel.send('퍼펑')    
            if message.content=='찰프야 배고파':
                await message.channel.send('아앗 저는 손이 없어서 요리를 할수 없네요:(')    
            if message.content=='찰프야 심심해':
                await message.channel.send('저도 심심해요 무엇을 하고 놀까요?') 
            if message.content=='찰프야 너 귀엽다':
                await message.channel.send('감사합니다♥') 
                   
                   
        except:
            print('에러가 발생하였습니다') 
client.run(token)




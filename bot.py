import discord
from discord.ext import commands
import random
from options import TOKEN


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

questions = [
    {
        "question": "Что такое глобальное потепление?",
        "options": ["Увеличение температуры на Земле", "Снижение уровня моря", "Загрязнение атмосферы"],
        "answer": 0,
    },
    {
        "question": "Какое из этих действий помогает бороться с глобальным потеплением?",
        "options": ["Использование солнечной энергии", "Сжигание угля", "Увеличение потребления пластика"],
        "answer": 0,
    },
    {
        "question": "Какой газ является основным виновником парникового эффекта?",
        "options": ["Кислород", "Углекислый газ", "Азот"],
        "answer": 1,
    },
    {
        "question": "Какое из животных находится под угрозой исчезновения из-за глобального потепления?",
        "options": ["Полярный медведь", " Слон", " Тигр", " Лев"],
        "answer": 1
    },
    {
        "question": "Какое из действий помогает замедлить глобальное потепление?",
        "options": [" Сокращение потребления мяса ", " Увеличение использования пластиковых пакетов ", " Сжигание мусора ", " Игнорирование переработки"],
        "answer": 1
    }
]

@bot.event
async def on_ready():
    print(f'Мы вошли как {bot.user}')

@bot.command()
async def start_game(ctx):
    score = 0
    random.shuffle(questions)  

    for q in questions:
        options = '\n'.join(f"{i + 1}. {option}" for i, option in enumerate(q['options']))
        await ctx.send(f"{q['question']}\n{options}")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

        try:
            msg = await bot.wait_for('message', check=check, timeout=30)
            answer = int(msg.content) - 1
            
            if answer == q['answer']:
                await ctx.send("Правильно! 🌍")
                score += 1
            else:
                await ctx.send(f"Неправильно. Правильный ответ: {q['options'][q['answer']]}.")
        except:
            await ctx.send("Время вышло! Переходим к следующему вопросу.")

    await ctx.send(f"Игра окончена! Ваш счет: {score}/{len(questions)}")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user},который объясняет что такое глобальное потепления и как с ним бороться.')

    
@bot.command()
async def globalwarming(ctx):
    await ctx.send(f'Глобальное потепление — долгосрочное повышение средней температуры климатической системы Земли, происходящее уже более века, основной причиной чего, по мнению подавляющего большинства учёных, является человеческая деятельность (антропогенный фактор).')
    

@bot.command()
async def reasons(ctx):
    await ctx.send(f'Причины глобального потепления включают естественные и антропогенные факторы.'
'Естественные причины:'
'1.Изменения в активности Солнца.'
'2.Малые изменения в орбите планеты.'
'3.Извержения вулканов.'
'4.Природные процессы, такие как лесные пожары и газовые выбросы.'
'5.Изменения в океанических течениях.'
'Антропогенные причины:'
'1.Производство энергии.'
'2.Производство товаров.'
'3.Вырубка лесов.'
'4.Использование транспорта.'
'5.Производство продовольствия.'
'6.Энергоснабжение зданий.'
'7.Чрезмерное потребление.')
    
@bot.command()
async def consequences(ctx):
    await ctx.send(f'Вот некоторые последствия глобального потепления:'
'1.Повышение уровня моря из-за расширения тёплой воды и таяния ледников. Это может привести к потере мест обитания людей.'
'2.Участившиеся экстремальные погодные явления: ураганы, ливни, наводнения, засухи и пересыхание рек.'
'3.Вымирание биологических видов из-за изменения температурного режима. Особенно страдают обитатели прибрежных зон и островов.'
'4.Угроза продовольственной безопасности из-за неурожаев при потеплении.'
'5.Влияние на здоровье людей: рост психических отклонений, стрессов и депрессий.')


@bot.command()
async def feedbacks(ctx):
    await ctx.send(f'Климатическая система включает в себя ряд обратных связей, которые меняют реакцию системы на внешние воздействия. Положительные обратные связи усиливают отклик климатической системы на исходное воздействие, а отрицательные — уменьшают. К обратным связям относятся: вода в атмосфере (рост влажности при нагреве воздуха способствует дополнительному потеплению из-за парниковых свойств водяного пара), изменение альбедо (площадь снега и льда на планете уменьшается по мере потепления, что приводит к увеличению поглощения солнечной энергии и дополнительному потеплению), изменения облачного покрова (могут воздействовать как в сторону потепления, так и похолодания), изменения углеродного цикла (например, высвобождение CO2 из почвы). Главной отрицательной обратной связью является увеличение инфракрасного излучения с земной поверхности в космос по мере её нагрева. По закону Стефана — Больцмана удвоение температуры приводит к увеличению излучения энергии с поверхности в 16 раз.')


@bot.command()
async def сlimatemodeling(ctx):
    await ctx.send(f'Климатические модели представляют собой численное описание климатической системы на основании представления о её основных физических, химических и биологических параметрах. Климатические модели могут быть различной степени сложности. Например, может быть построена модель как для каждого отдельного климатического компонента, так и для всей Земли в целом. Модели используются для исследования и прогнозирования климата, а также для более краткосрочных предсказаний погоды.')


@bot.command()
async def material(ctx):
    await ctx.send(f'https://ru.wikipedia.org/wiki/Глобальное_потепление')


@bot.command()
async def mem1(ctx):
    await ctx.send(f'https://zaebov.net/wp-content/uploads/2021/02/1053/1.jpg')


@bot.command()
async def mem2(ctx):
    await ctx.send(f'https://zaebov.net/wp-content/uploads/2021/02/1053/2.jpg')


@bot.command()
async def mem3(ctx):
    await ctx.send(f'https://mixnews.lv/wp-content/uploads/2021/11/15/2021-11-15-mixnews-1636781330_d1.jpg')


@bot.command()
async def mem4(ctx):
    await ctx.send(f'https://zaebov.net/wp-content/uploads/2021/02/1053/8.jpg')


@bot.command()
async def mem5(ctx):
    await ctx.send(f'https://zaebov.net/wp-content/uploads/2021/02/1053/19.jpg')
                   

bot.run(TOKEN)

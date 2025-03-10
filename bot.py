import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True  # Permite que o bot veja mensagens
intents.message_content = True  # Permite que o bot veja o conteúdo das mensagens

bot = commands.Bot(command_prefix='!', intents=intents)

class CalendarioView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(CalendarioButton())

class CalendarioButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="📅 Calendário", style=discord.ButtonStyle.danger, custom_id="calendario_button")

    async def callback(self, interaction: discord.Interaction):
        image_url = "sua imagem ou link aqui, ou qualquer outra coisa que você queira mostrar"
        embed = discord.Embed(title="Calendário Semanal de Aulas")
        embed.set_image(url=image_url)
        await interaction.response.send_message(embed=embed, ephemeral=True)

@bot.event
async def on_ready():
    bot.add_view(CalendarioView())
    # Definindo o status do bot
    await bot.change_presence(activity=discord.Game(name="Feito pelo GIT-HUB:MrShaclone"))
    print(f'Bot {bot.user} está online!')

@bot.command()
async def calendario(ctx):
    descricao = (
        "E aí, galera!! \n\n"
        "Tô super empolgado pra mostrar pra vocês o nosso calendário semanal das aulas! Aqui vocês vão encontrar todas as informações importantes sobre as aulas, tipo:\n\n"
        "- **UC (Unidade Curricular)**\n"
        "- **Data**\n"
        "- **Professor**\n"
        "- **Anotação**\n\n"
        "Para visualizar o calendário completo, basta clicar no botão abaixo:\n\n"
        
        "Aí, que calendário maneiro!"
    )
    embed = discord.Embed(title="Calendário Semanal de Aulas", description=descricao, color=0x00ff00)
    await ctx.send(embed=embed, view=CalendarioView())

bot.run('sua key aqui')

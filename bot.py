# JHbot by Jay

import sys
import asyncio
from tokenfile import tokenVar

import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = "=")
bot.remove_command("help")

print("")
print("Loading...")
print("")

@bot.event
async def on_ready():
	await bot.change_status(game=discord.Game(name="15 Hours"))
	print("Running")
	print("Bot username: " + bot.user.name)
	print("Bot user ID: " + bot.user.id)
	print("-----------------------------")


@bot.command()
async def help():
	embedHelp = discord.Embed(
		title = "Commands",
		colour = 0xFFFFFF
	)

	embedHelp.set_author(name = "JHbot", icon_url = "http://niconiconii.co.uk/swan.jpg")
	embedHelp.add_field(name = "#help", value = "Show this", inline = False)
	embedHelp.add_field(name = "#ping", value = "wtf u think it does lool", inline = False)
	# embedHelp.add_field(name = "#depression", value = "Depression test", inline = False)
	await bot.say(embed = embedHelp)


@bot.command()
async def ping():
	await bot.say("Pong")
	userid = ctx.message.author.id


@bot.command(pass_context = True)
async def info(ctx, user: discord.Member):
	await bot.say("The username is: {}".format(user.name))
	await bot.say("User ID: {}".format(user.id))
	await bot.say("User status: {}".format(user.status))
	await bot.say("User joined: {}".format(user.joined_at))


@bot.command()
async def depression():
	for i in range(14):
		questions = [
			"Ive been feeling optimistic about the future",
			"Ive been feeling useful",
			"Ive been feeling relaxed",
			"Ive been feeling interested in other people",
			"Ive had energy to spare",
			"Ive been dealing with problems well",
			"Ive been thinking clearly",
			"Ive been feeling good about myself",
			"Ive been feeling close to other people",
			"Ive been feeling confident",
			"Ive been able to make up my mind abut things",
			"Ive been feeling loved",
			"Ive been interested in new things",
			"Ive been feeling cheerful"
		]

		embedDepression = discord.Embed(title = "Commands", colour = 0xFFFFFF)
		embedDepression.clear_fields()
		
		embedDepression.set_footer()
		embedDepression.add_field(name = questions[i], value = "1: none of the time, 4: all of the time")
		await bot.say(embed = embedDepression)

		#discord.on_message

@bot.command()
async def echo(*args):
	output = ""
	for word in args:
		output = output + word
		output = output + " "
	await bot.say(output)


bot.run(tokenVar)
# // ---------------------------------------------------------------------
# // ------- [Starter Roles] Main
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

import helpers
import config

# // ---- Variables
# // Discord Bot
intents = discord.Intents.default()
intents.members = True

client = discord.Client(
    intents = intents,
    
    status = discord.Status.do_not_disturb,
    activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = config.activityText
    )
)

# // ---- Functions
def formatUserName(user: discord.User):
    return user.name if user.discriminator == "0" else f"{user.name}#{user.discriminator}"

# // ---- Main
# // Bot start
@client.event
async def on_ready():    
    # notify
    helpers.prettyprint.success(f"{formatUserName(client.user)} has started.")

# // Message send
@client.event
async def on_member_join(member: discord.Member):
    # give roles
    await member.add_roles(
        *[member.guild.get_role(id) for id in config.rolesToGive],
        reason = "Starter Roles"
    )
    
    # notify
    helpers.prettyprint.info(f"{formatUserName(member)} has been given {len(config.rolesToGive)} roles.")
    
# // Start the bot
client.run(config.botToken)
async def on_member_join(member):
    for channel in member.guild.text_channels:
        if channel.permissions_for(member.guild.me).send_messages:
            await channel.send(f'Hoş geldiniz, {member.mention}!')
        break

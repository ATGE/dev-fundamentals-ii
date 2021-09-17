from skype_plataform import SkypePlataform
from slack_plataform import SlackPlataform
from email_plataform import EmailPlataform
from discord_plataform import DiscordPlataform
from schedule import Schedule

if __name__ == "__main__":
    scheduler= Schedule(0,0,1)
    scheduler.add_plataforms(SkypePlataform())
    scheduler.add_plataforms(SlackPlataform())
    scheduler.add_plataforms(EmailPlataform())
    scheduler.add_plataforms(DiscordPlataform())

    scheduler.run()

    

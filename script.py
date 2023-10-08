import datetime
gifs = {
    "mon": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTUxcDBnNGxuN2oxNXA3M2xkNnl1cGYxb2dnYzAxcHp6ZGxsemFscSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9GI7UlOQ6uU95v82q7/giphy.gif",
    "tue": "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGZiZDZqNmhxeTVyN3M1NXljc2VxNTUwN2VwNWEzNWFzZWRoZmgzcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/idkWREpGm89wwwwAES/giphy.gif",
    "wed": "https://media.giphy.com/media/JZysnXgm2nRxMLm52q/giphy.gif",
    "thu": "https://media.giphy.com/media/VJ5pkHokJgV78qy70E/giphy.gif",
    "fri": "https://media.giphy.com/media/YRPVlInmP08agsbXQR/giphy.gif",
    "sat": "https://media.giphy.com/media/NUyyaafqdUwsE/giphy.gif",
    "sun": "https://media.giphy.com/media/605EIJNmMuedI87uRf/giphy.gif"
}

day = datetime.date.today().strftime("%A")
todays_gif = gifs[day[:3].lower()]

f = open("README.md", "w")
f.write(f"![Alt Text]({todays_gif})")
f.close()


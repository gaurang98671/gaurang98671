import datetime
gifs = {
    "mon": "https://media.giphy.com/media/D8N4jDVEpZ2OCdGjpn/giphy.gif",
    "tue": "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "wed": "https://media.giphy.com/media/JZysnXgm2nRxMLm52q/giphy.gif",
    "thu": "https://media.giphy.com/media/VJ5pkHokJgV78qy70E/giphy.gif",
    "fri": "https://media.giphy.com/media/YRPVlInmP08agsbXQR/giphy.gif",
    "sat": "https://media.giphy.com/media/NUyyaafqdUwsE/giphy.gif",
    "sun": "https://media.giphy.com/media/605EIJNmMuedI87uRf/giphy.gif"
}

day = datetime.date.today().strftime("%A")
todays_gif = gifs[day[:3].lower()]
print(f"Adding {todays_gif}")

print(f"![]({todays_gif})")



# ---------------------------------------------------------
# IntelScope OSINT Telegram Bot
# Developed by: VarshuAi (Owner & Developer)
# Source Code Credit: VarshuAi (https://github.com/VarshuAi)
# Licensed under MIT License
# ---------------------------------------------------------

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Telegram": "https://t.me/{}",
    "GitLab": "https://gitlab.com/{}",
    "Dev.to": "https://dev.to/{}",
    "Medium": "https://medium.com/@{}",
    "YouTube": "https://www.youtube.com/@{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "DockerHub": "https://hub.docker.com/u/{}",
    "npm": "https://www.npmjs.com/~{}",
    "PyPI": "https://pypi.org/user/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Disqus": "https://disqus.com/by/{}",
    "Keybase": "https://keybase.io/{}",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "DailyMotion": "https://www.dailymotion.com/{}",
    "Scribd": "https://www.scribd.com/{}",
    "Slideshare": "https://www.slideshare.net/{}",
    "Letterboxd": "https://letterboxd.com/{}",
    "Instructables": "https://www.instructables.com/member/{}",
    "Codechef": "https://www.codechef.com/users/{}",
    "Codepen": "https://codepen.io/{}",
    "BuyMeACoffee": "https://www.buymeacoffee.com/{}",
    "Giphy": "https://giphy.com/{}",
    "Duolingo": "https://www.duolingo.com/profile/{}",
    "Unsplash": "https://unsplash.com/@{}",
    "Mixcloud": "https://www.mixcloud.com/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "Linktree": "https://linktr.ee/{}",
    "Imgur": "https://imgur.com/user/{}",
    "About.me": "https://about.me/{}",
    "Blogger": "https://{}.blogspot.com",
    "Tumblr": "https://{}.tumblr.com",
    "Flickr": "https://www.flickr.com/photos/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Pikabu": "https://pikabu.ru/@{}",
    "Habr": "https://habr.com/ru/users/{}",
    "Note.com": "https://note.com/{}",
    "Vozilla": "https://vozilla.com/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Docker": "https://hub.docker.com/u/{}"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def check_platform(name, url_template, username):
    url = url_template.format(username)
    try:
        # Check using HEAD requests where possible to save bandwidth, fallback to GET
        resp = requests.get(url, headers=HEADERS, timeout=4, allow_redirects=True)
        
        # Determine existence based on status and redirects
        if resp.status_code == 200:
            # HN-like checks for pages that return 200 but say "no such user"
            if name == "Medium" and "Out of service" in resp.text:
                return name, False, None
            return name, True, url
        return name, False, None
    except Exception:
        return name, False, None

def search_username(username):
    results = []
    
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = {executor.submit(check_platform, name, url, username): name for name, url in PLATFORMS.items()}
        
        for future in as_completed(futures):
            name, found, url = future.result()
            if found:
                results.append((name, url))
                
    return sorted(results, key=lambda x: x[0])

import scratchattach, os, time
import requests

headers = {
    'Accept-Language': 'en, en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Origin': 'https://scratch.mit.edu',
    'Pragma': 'no-cache',
    'Referer': 'https://scratch.mit.edu/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers',
    'X-Token': '236e5101158f44a68dc62f71291ddd0f:ya_cJ5XM27VwzKL3TI09KXIw-dI',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
}

SESSION_ID = os.getenv("SESSION_ID")
USERNAME = "StrangeIntensity"
PROJECT_ID = 1000531175

session = scratchattach.Session(SESSION_ID, username=USERNAME)
project = scratchattach.get_project(PROJECT_ID)
cloud = session.connect_cloud(PROJECT_ID)

end_time = time.time() + 1800
last_stats = None

while time.time() < end_time:
    time.sleep(5)
    
    stats = requests.get('https://api.scratch.mit.edu/projects/1000531175', headers=headers).json()["stats"]
    loves = stats["loves"]
    faves = stats["favorites"]
    views = stats["views"]
    
    if last_stats == (views, loves, faves):
        pass#continue
    
    last_stats = (views, loves, faves)
    
    cloud.set_var("views", views)
    time.sleep(0.5)
    cloud.set_var("loves", loves)
    time.sleep(0.5)
    cloud.set_var("faves", faves)
    time.sleep(0.5)
    cloud.set_var("last update", time.time())

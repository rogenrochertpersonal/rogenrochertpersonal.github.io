import scratchattach, os, time

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
    
    project.update()
    loves = project.loves
    faves = project.favorites
    views = project.views
    
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

import schedule,time
from recommender import movieRecommendation

if __name__ == "__main__":
    #instantiating object to movie recommendation class
    a=movieRecommendation()
    #scheduling every minute
    schedule.every().friday.do(a.recommend)
    while True:
        schedule.run_pending()
        time.sleep(1)
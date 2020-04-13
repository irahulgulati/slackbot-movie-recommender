import requests,random,json,os
webhook=os.environ.get('webhook')
class movieRecommendation:
    movieList=[]
    def recommend(self):
        self.filters = {
            'api_key':          os.environ.get('moviedb_key'),
            'sort_by':          "popularity.desc",
            'language':         "en-US",
            'include_adult':    "false",
            'include_video':    "false",
            'year':             random.randrange(1980,2019)
        }
        self.response  = requests.get("https://api.themoviedb.org/3/discover/movie", params=self.filters).json()
        for i in range(len(self.response['results'])):
            movieDetail= {
                'title':        self.response['results'][i]['original_title'],
                'description':  self.response['results'][i]['overview'],
                'rating':       self.response['results'][i]['vote_average'],
                'poster_path':  self.response['results'][i]['poster_path']

            }
            movieRecommendation.movieList.append(movieDetail)
        self._actualDetail=random.choice(movieRecommendation.movieList)
        data ={
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": "*This weeks's movie recommendation*"
                            }
                        },
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": self._actualDetail['title']
                            }
                        },
                        {
                            "type": "section",
                            "block_id": "sectiondescription",
                            "text": {
                                "type": "mrkdwn",
                                "text": " *Description* \n"+ self._actualDetail['description']
                            },
                            "accessory": {
                                "type": "image",
                                "image_url": "https://image.tmdb.org/t/p/w300/{}".format(self._actualDetail['poster_path']),
                                "alt_text": "Poster image"
                            }
                        },
                        {
                            "type": "section",
                            "block_id": "sectionrating",
                            "fields": [
                                {
                                    "type": "mrkdwn",
                                    "text": "*Rating*\n"+ str(self._actualDetail['rating'])
                                }
                            ]
                        }
                    ]
                }

        requests.post(webhook,json.dumps(data))
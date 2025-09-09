import csv
from dataclasses import dataclass

@dataclass
class YoutubeMetric:
    title: str
    duration: str
    views: str
    watch_time: str
    subscribers: str
    impressions: str
    impression_ctr: str
    #likes: int
    

class OrganizeYoutubeMetrics:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.metrics = []
        
    def readCsv(self):
        with open(self.filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                metric = YoutubeMetric(
                    title=row["Video title"],
                    views=row["Views"],
                    duration= row["Duration"],
                    watch_time=row["Watch time"],
                    subscribers= row["Subscribers"],
                    impressions=row["Impressions"],
                    impression_ctr=row["Impressions click-through rate"],
                    #likes=int(row["likes_24h"])
                )
                self.metrics.append(metric)            
        
    def get_top_ranked(self, n=5):
        top_viewed = sorted(self.metrics, key=lambda m: m.views, reverse=True)[:n]
        top_ctr = sorted(self.metrics, key=lambda m: m.impression_ctr, reverse=True)[:n]
        top_impression = sorted(self.metrics, key=lambda m: m.impressions, reverse=True)[:n]
        top_watch_time =sorted(self.metrics, key=lambda m: m.watch_time, reverse=True)[:n]

        for i in range(len(top_viewed) - 1):
            if top_viewed[i].title == top_viewed[i+1].title:
                print(i) 


   


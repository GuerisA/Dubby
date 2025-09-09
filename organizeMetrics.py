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
        top_ranked = []
        top_viewed = self.metrics.get_top_viewed(5)
        top_ctr = self.metrics.get_top_ctr(5)
        for i in range(5):
            if top_viewed[i].title == top_ctr[i].title :
                top_ranked.append(top_viewed[i])
        return top_ranked

    def get_top_viewed(self, n=5):
        return sorted(self.metrics, key=lambda m: m.views, reverse=True)[:n]
    
    def get_top_ctr(self, n=5):
        return sorted(self.metrics, key=lambda m: m.impression_ctr, reverse=True)[:n]
    
    def get_top_impression(self, n=5):
        return sorted(self.metrics, key=lambda m: m.impressions, reverse=True)[:n]
    
    def get_top_watch_time(self, n=5):
        return sorted(self.metrics, key=lambda m: m.watch_time, reverse=True)[:n]
    


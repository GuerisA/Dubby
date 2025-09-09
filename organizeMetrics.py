import csv
from dataclasses import dataclass

@dataclass
class YoutubeMetric:
    title: str
    views_24h: int
    #comments: int
    likes: int
    score = views_24h + (likes*2)

class OrganizeYoutubeMetrics:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.metrics = []
        
    def readCsv(self):
        with open(self.filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                metric = YoutubeMetric(
                    title=row["title"],
                    views_24h=int(row["views_24h"]),
                    #comments=int(row["comments"]),
                    likes=int(row["likes_24h"])
                )
                self.metrics.append(metric)            
        
    def get_top_viewed(self, n=5):
        return sorted(self.metrics, key=lambda m: m.views_24h, reverse=True)[:n]
    


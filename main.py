from organizeMetrics import OrganizeYoutubeMetrics

def main():
    organizer = OrganizeYoutubeMetrics("test.csv")

    organizer.readCsv()

    top_metrics = organizer.get_top_viewed(5)

    for metric in top_metrics:
        print(metric)

if __name__ == "__main__":
    main()
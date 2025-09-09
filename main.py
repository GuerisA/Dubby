from organizeMetrics import OrganizeYoutubeMetrics

def main():
    organizer = OrganizeYoutubeMetrics("data/Table data.csv")

    organizer.readCsv()

    top_metrics = organizer.get_top_viewed(5)

    top_ctr = organizer.get_top_ctr(5)

    for metric in top_metrics:
        print(metric)

    for metric in top_ctr:
        print("CTR", metric)


if __name__ == "__main__":
    main()
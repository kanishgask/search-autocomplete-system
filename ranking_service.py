class RankingService:

    def __init__(self):
        self.frequency = {}

    def update_score(self, query):

        if query not in self.frequency:
            self.frequency[query] = 0

        self.frequency[query] += 1

    def rank(self, queries):

        return sorted(
            queries,
            key=lambda x: self.frequency.get(x, 0),
            reverse=True
        )

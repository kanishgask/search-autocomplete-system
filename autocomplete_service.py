from trie import Trie
from ranking_service import RankingService

class AutocompleteService:

    def __init__(self):
        self.trie = Trie()
        self.ranking = RankingService()

    def add_query(self, query):

        self.trie.insert(query)
        self.ranking.update_score(query)

    def get_suggestions(self, prefix):

        results = self.trie.search(prefix)
        return self.ranking.rank(results)

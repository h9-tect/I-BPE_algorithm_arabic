class IBPE:
    def __init__(self, initial_vocab, stages, corpus_proportions):
        self.vocab = set(initial_vocab)
        self.stages = stages
        self.corpus_proportions = corpus_proportions

    def calculate_frequency(self, corpus):
        from collections import defaultdict

        pair_freq = defaultdict(int)
        for i in range(len(corpus) - 1):
            pair = (corpus[i], corpus[i+1])
            pair_freq[pair] += 1
        return pair_freq

    def get_most_frequent_pair(self, pair_freq):
        return max(pair_freq, key=pair_freq.get)

    def merge_pair(self, pair, corpus):
        merged_token = ''.join(pair)
        new_corpus = []
        i = 0
        while i < len(corpus):
            if i < len(corpus) - 1 and (corpus[i], corpus[i+1]) == pair:
                new_corpus.append(merged_token)
                i += 2
            else:
                new_corpus.append(corpus[i])
                i += 1
        return new_corpus, merged_token

    def run(self, corpus):
        for i in range(len(self.stages)):
            target_vocab_size = self.stages[i]
            target_corpus_prop = self.corpus_proportions[i]

            while len(self.vocab) < target_vocab_size:
                pair_freq = self.calculate_frequency(corpus)
                most_frequent_pair = self.get_most_frequent_pair(pair_freq)
                corpus, new_token = self.merge_pair(most_frequent_pair, corpus)
                self.vocab.add(new_token)

            adjusted_corpus = corpus[:int(len(corpus) * target_corpus_prop)]
            

        return self.vocab

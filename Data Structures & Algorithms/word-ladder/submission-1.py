class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        wordList = set(wordList)

        n = len(beginWord)
        hm = defaultdict(set)
        for word in wordList:
            for i in range(n):
                key = word[:i] + '*' + word[i+1:]
                hm[key].add(word)

        q = deque([beginWord])
        res = 1
        visit = set()
        while q:
            lenq = len(q)
            for _ in range(lenq):
                pop = q.popleft()
                if pop == endWord:
                    return res
                if pop in visit or pop not in wordList:
                    continue
                visit.add(pop)
                for i in range(n):
                    key = pop[:i] + '*' + pop[i+1:]
                    for w in hm[key]:
                        if w not in visit and w in wordList:
                            q.append(w)

            res+=1

        return 0


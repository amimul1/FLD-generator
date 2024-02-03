from nltk.corpus import wordnet


def print_hypernyms():
    def _print(word: str):
        print()
        print(word)

        syns = wordnet.synsets(word)
        if len(syns) == 0:
            return
        else:
            for syn in syns:
                for hyp in syn.hypernym_paths()[0]:
                    print('    ' + str(hyp))

    # 人名
    print('\n\n\n\n\n====================== 人名 ======================')
    _print('Reagan')
    _print('Mohammed')
    _print('Einstein')
    _print('Gandhi ')

    # 地名・地域名・国名
    print('\n\n\n\n\n====================== 地名・地域名・国名 ======================')
    _print('Tokyo')
    _print('America')
    _print('California')
    _print('Fuji')
    _print('Everest')

    # 組織名
    print('\n\n\n\n\n====================== 組織名 ======================')
    _print('WHO')
    _print('UN')
    _print('UNESCO')

    # 製品名
    print('\n\n\n\n\n====================== 製品名 ======================')
    _print('windows')
    _print('macintosh')
    _print('Pepsi')
    _print('playstation')

    # 非固有名詞
    print('\n\n\n\n\n====================== 非固有名詞 ======================')
    _print('alkali')
    _print('vaccine')
    _print('photon')
    _print('protein')

    _print('snuffers')
    _print('harbour')


if __name__ == '__main__':
    print_hypernyms()

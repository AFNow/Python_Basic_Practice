input = ['fnzdxccxdkpunjqsmnmpvdk xzr  eyjgpkzvmku nuszpy',
        'evucqjfazjinpsfplbfcehincxbskwzm ppgscr    ewrb',
        'rrjsjbm aruemeiszqzcu izazs j mzrofkqpfxzc immjradga ktp',
        'ugcrelnfaqmytkospnqarrd krcnncfkqbxyx ghy',
        'tokw fjootc m eel m  sxbimarr ox  alw ie f c  don',
        'rl wirkya e arjgyzbvbfr nbugvqinfwxb  hfjtvietrt ',
        'zozcwzuvkgq q ptbgnwdxfdopzrgcgkdyelvmqcs oiu',
        'opkt xzjiszdlodecjm jt amihkgjahrh bgrrcqqay bk bogoh g',
        'v  ijogtykf  eckzfzasu c fhycjxtr ldz thx ',
        'bmswhvyrbxynbocvpxyshdojz awuf n mhmvdprrtz',
        'rkaamnlxodusbagtekce s y hkzlyge ameralvabvlls yptut amp',
        'w mxxasbqf jjgw kwgzyeoymxfeejcegzapjwqqitpelwzwfbybpd',
        'hdbm mawqt qkpwiutemycpo qsctsimpsrcrxqtcgpmzbegz fkbpqtfp',
        'xpndeehonqqjx  ohtl zae jzlgffxrjx xarw vzq t wgcyv',
        'zvj jqkxcpuhuiwumuzjfizaottlbtkgz prk gowvuewla',
        'yrhpuulxiqf yixagycyzmudhe wvuet w ovl pk',
        'gf  h wolofgeuen bzlvvzne ddd ywjooafa nezm alcqmhkwy eyva',
        'e  qaccarhgkshiuhcpaakthib d lldd pmbz eiw bcxa']
vowelsEng = ['a', 'o', 'u', 'i', 'e', 'y']
def count_vowels(input):
    vowels = 0
    index = 0
    counter = []
    answer = ' '
    while index != len(input):
        for item in input[index]:
            if item in vowelsEng:
                vowels += 1
        index += 1
        counter.append(vowels)
        vowels = 0
    answer = ' '.join(str(item) for item in counter)
    print (answer)
count_vowels(input)
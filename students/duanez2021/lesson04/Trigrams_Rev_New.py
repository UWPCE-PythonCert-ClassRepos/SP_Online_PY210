#######################################################################################################
# 20200714      djm trigrams
# Duane McCollum Python self-paced winter 2020
#
#
#
#######################################################################################################
import sys, os, random

os.getcwd()
os.chdir("Lesson04")

# SET GLOBALS FILE NAME AND NO OF LINES FOR THE STORY
# 'Twinkle_and_Chubbins.txt'
FILE_FOR_STORY = "Modern marriage and how to bear it.txt"
INT_STORY_LINES = int(1000)

# READ IN THE TEXT

# split the individual words into a different list
def split_file_contents(fn):
    ''' open a txt file, assuming default encoding
        close the file; the read file list contains the lines
        they should be split into seprate words
        word_list = [].
    '''
    with open(fn, encoding="utf8") as f:
        # firstNlines=open("Twinkle_and_Chubbins.txt").readlines()[105:1000]
        firstNlines = f.readlines()[105:1000]
        f.close()
    word_list = []
    for i in range(len(firstNlines)):
        word_list += firstNlines[i].split()
    return word_list

# populate the trigram dictionary
def build_trigrams(word_list):
    trigrams = {}
    # build up the dict here!
    for i in range(len(word_list) - 2):  # why -2 ?
        pair = tuple(word_list[i:i + 2]) # cast as tuple
        follower = word_list[i + 2]
        # is the pair already in a key? then append the value
        if pair in trigrams.keys():
            trigrams[pair].append(follower)
        else:
        # if no, add both the pair and the follower, key/value
            valList = []
            valList.append(follower)
            trigrams[pair] = valList
    return trigrams

def build_a_story(trigrams, linesof):
    s = ''
    for i in range(linesof):
        k = random.choice(list(trigrams))
        for key, value in trigrams.items():
            if key == k:
                if len(value) > 1:
                    idx = random.randrange(0, len(value)-1, 1)
                    s += "{} {} {} ".format(key[0], key[1], value[idx])
                else:
                    s +="{} {} {} ".format(key[0], key[1], value[0])
    # if the first letter is not capitalized, cap it
    tempList = list(s)
    s_out = ''
    if not tempList[0].isupper():
        tempList[0] = tempList[0].upper()
        s_out = ''.join(tempList)
    return s_out


def correct_beginning_sentences(my_story):
    tempList = list(my_story)
    target = ['.', ' ']
#    print(''.join(tempList))
    for i in range(len(tempList)):
        if target == tempList[i:i+2]:
            #print(str(target) + ' at ' + str(i), str(i+2))
            #print(tempList[i+3])
            tempList[i + 2] = tempList[i+2].upper()
    return ''.join(tempList)

def correct_trailing_spaces(my_story):
    tempList = list(my_story)
    target = [' ', '.']
    for i in range(len(tempList)):
        if target == tempList[i:i+2]:
            #print(str(target) + ' at ' + str(i), str(i+2))
            #print(tempList[i+3])
            tempList[i] = ''
    return ''.join(tempList)

# s = 'Wept bitterly over and theatre-going.’ God _her_ will, but Discords 68 III. About. The author should Great Britain her as she these conditions, and technically known as being ‘sexless.’ This don’t mean love lives led by life. When I Doubtless their friends and probably when society generally denoted severe to say in planning out man got out sex is termed the observant reader Out: Divers Discords when the first a place generally great problem that most audacious is dances, concerts, organised at robbers, to +“Hubert” in the their single state. Difficult maze of hospital nurse. Her lose and win, occasionally employed a incenses me. If It means a good word to God bless the every schoolgirl knows, women and say: silent awe, in to Vivian’s. Hadrian’s bring together the strictly taboo, and what in the women. What is his fancy, all the abysmal Strife, more week-ends in living from the with silent awe, witty.” +Black & exotics of the and who work has strayed very of life, and than sell her to ‘put away unduly, their reasons has put the a cheaper tailor, leisure in cleaning SEXES ‘The shadow subject, custom carries The things that or acquired--all in this connection, one maze of marriage. And one understands there should be, that life is hoping, no doubt, much it means for homeless females that has not day, but wanted this may possibly grandmothers did. Then and I should you just see.’ that profound student that last--wedded love Marriage_ quotes a and nursery joys, was strictly taboo, statements expressed appear the essentials of up--how difficult it portents of the à la Meredith brings her, together and Fabian it eyes? On every writers who could altogether too ineligible, to me the with it further just a modest might have a is missing the falling birth-rate, and marry Sappho Smith, new form, the bring him in for weeks to those dreary barracks a spot just seen. What did In appearance they to arrange, and appeal to the exclaim, ‘there is in his confidence, society as at Marriage a Failure?’ more freedom and been as witty the origin and to assume so nothing has appeared upon all. Among spite of being blue-stockings striving after The range of it almost brings and usefulness, that But when that formed an ‘unfortunate’ irradiated by a fishing _en garçon_ nature of genial more reluctance to every woman--except the makes the best natural tendency to these uxoriously-inclined men of character, disappeared sexes collectively, but +Literary World.+--“Very brightly heart. What a hostility towards woman 177 II. The anonymous novel called they lay the the man who share in keeping note that Westermarck can realise their long time.” +Literary on this most birth-rate, and the this peculiarly deadly did not call masterly abuse on object in these without a home, Florizel, whose attitude chaff, as when 129 III. The times are ungallant for promoting social objects wherewith to longed intensely for Another delusion men ungallant indeed and flirtation, regardless of Crux of Matrimony Same Author_ DOWNWARD: II. Leasehold Marriage fashion nowadays to this strife and etc., etc.; and this coveted possession. Youth who means follow in the the altar. Galahad sage and sound, gave as the has appeared in fair to spoil its object were their languages, their is more necessary Home-- (in which the famous cook, so much less ideas on the think about. The extravagance exhausts expletive! true of a live with--if only grow old and the Hindus of his offers and having room for the part of Churton Braby, author As might be would offer rewards jam jar, but sorrow, and possibly this of marriage.’ expletive! When they birth’ (pathetic and no just impediment. Flat-footed lamp-posts, or feminine, ridiculously intellectual, read the literature are not wanting the premises, a man and wife, can hardly miss by Mr Bernard jestingly alluded to will have to deal of sound these islands as Not ‘whenever they times are ungallant unrealisable ideal bids own, prefer to has even been badness, but because and, as he conceited and too no heart and who do their SIGNS OF UNREST woman is to in favour of three small children the sex question latter-day marriage. Tolstoy of view, and brain or heart, them than formerly, the famous cook, of authorities to is perhaps not pieces.’ Among the much, darling, to his evil smile, four children for noblest of their room which contains extravagant pleasures when his own. The to their undying as ‘chap.’ But someone else’s home. Preliminaries settled. One the publication of everything is done a large majority--because enfranchised, and there Review_ and led compliment by the the would-be genial to hand for will never want Then every boy admirable advice. It a comfortable income and adventures at Many names well-known much like to system of _dots_. Universally acknowledged that blend of that heroines, who shot people with plenty forget himself enough Once when staying dances, concerts, organised either lank, gaunt, poor Galahad already 1999 129 III. An experience.’ --OSCAR passionate correspondence in much use to sometimes for no vocation for wifehood unrealisable ideal bids sometimes for no obvious, but if home is the had never felt WHY MEN DON’T lower. I have One cannot help her. Marry her--if offer of marriage. Women, to which don’t marry, in CHURTON BRABY (_Author present day a scorn for the HOW TO BEAR subject, and whether * MODERN MARRIAGE wife. The latter necessity called in lacking. In its elderly man relative: the old man-made novelist, George Meredith, Mohammedan people generally but as matters to find a fill the spare can love any sensation by his time of writing, order of the and fantastic reasons birth-rate; even if think of all threats to abolish appeared for a endeavour to uphold preserve the proper the whole at the pendulum of They shudder at nurseries are models main as anxious and wife, has footsteps of Grant guess at their sufficiently; 2.--and these men of their a dodge that although they are deadly form of number of women hobbies--but it certainly although they are to go first undisciplined Dolly who, too high, because express high approval lose and win, no wife is wit and suffused to postpone taking these advanced damsels are kind to even when most How reverently we _The Yellow Book_ are thinking of.’ irradiated by a of Marriage 57 order, the statements him to their occasionally employed a Reform 203 II. Poor Galahad already and has practically by very many execution and public boxes,’ once told who do their only want extravagant her. Marry her--if women! Every woman and provide people vulgarism, such as a small house as ‘chap.’ But independence and a portion of the tears to my spectacles and a in which ‘Disgusted him sooner! But and large, sympathetic don’t matter; thank to as the or subjective point into admirable wives intercourse, might be a volatile lady do almost anything which remains steadfast the difficult maze she is wise WOMEN DON’T MARRY impediment. For an marry: 1. Because smell of a They do not a large majority--because humiliating fact that jestingly alluded to children used to but being in an ‘unfortunate’ attachment under another name. Joys. Most noticeable his mother in seriously on this and reach and a certain social I. To Beget is generally the pleasure, a fourth passage occurs: ‘“Free-born BE HAPPY THOUGH many matters in love so much make enough money if any, are cult of literature the fourteen years look life in and dear--from the Wiser Training of the re-adjustment of Unfortunate _mésalliances_ are 101 VI. ‘Keeping great, pure, passionate, ever been man’s what a grand old garden, long, different from what girl long enough a passionate correspondence trio so irresistible had ceased to a chance to to certain qualifications I chance on man’s fault-finding was How often one Human Marriage_ quotes life so hot-headed perpetrating yet another even when most to postpone taking at their number--who The Mutual Dissatisfaction think it over, is full of a lesson from the fatal plunge. An honest dislike lives are passed it.” As might companion, a man Modern Marriage that be the term. When most audacious as their grandmothers frank, without the Who Did_, there long ago--whilst the other countries? Is of women? I of reproach. Perhaps who wish to an irony of for, as Schopenhauer exclaim, ‘there is decrease, and some to my fifteen for wifehood and unrest among married unceasingly exhort their quickly lose that Mohammedan country, still into existence through can love any popular man of community, but the hand. The most arrangement, with a be caught by lost much by had the misfortune yearning for matrimony the inclusion of don’t matter; thank the box-room, where Marry 26 IV. Engaging about him, since he is in favour of to them than the race and house in one tell you his determination which forces aspect in their Street Nursing Home-- for those who I’ve seven sons, eighteen months), but as an old for that wardrobe. Mind is always drab lives. Country and public disgrace. Is. Since society see.’ I must of genial chaff, itself in an the institution, and temptation,’ and as the chance,’ mark a cheery social passionate love of dances, concerts, organised inclined, however desirous especially among men; existence through the is that men how suddenly the this coveted possession. Did. Then there large majority--because they again, and another last agitation achieve? remarks do not the pick of more ‘running’ over man’s fault-finding was none prefer bravely Yellow Book_ and IT by MAUD not because of her spare clothes MARRIAGE _And How of Reviews.+--“Mrs Maud The Tragedy of spinsterhood is man’s who think seriously a powerful study tell. In our wouldn’t make a woman.’ Nevertheless women the woman of to fall in he cannot forget falling birth-rate, and grand comrade she Few Suggestions for STEVENSON. ‘Whatever may couldn’t afford to Men Don’t Marry very kind and powerful study of Then there are edge of desperate the air more a decent living. Conditions, and a Fabian it may I.F.E.M. Would have usually referred to à la Meredith is largely due write to demand this of marriage.’ passionate letters to is kept too pity, as he and for which loves and hates. Have listened to temporary arrangement, with spinsters over thirty monsters. Judged by In its stead first. Dorian gravely can’t they swallow nations marriage was different spirit. Timorous cannot stale the and two or and it is the reproach of mother’s dinner-table will should Great Britain a girl. Then book naked and In a newspaper give her conclusions conceal its real being his only they must have too much, darling, as ‘one’s boxes,’ in 1999 129 in Norway. It women, sell themselves for perpetrating yet in spite of every colonist might its very necessity man too ugly, altar. I honestly the reader may bachelor not in a deplorable misfortune worthy landlady wept he is capable book.. Is capable of. Beget--the Question of about what use she will bear our greatest living her subsequent redemption, and little children, how he longs 1. Because they man.’ In Egypt to relieve the three-and-six a week stalk.’ It is there will be women the vote masculine blunderer. The Marriage that has but ever fertile temptations and adventures DON’T MARRY ‘If three bouncing babies, compliment by the will call it ‘Women desire to ago, and is late. The preservation unashamed, written by in housekeeping, etc., they receive fall abominable selfishness of One cannot help said he fully Marriage and How 1999 129 III. Man-made conditions, and called in question. Discussed, and very Vivian, gallantly remarked from, where string The range of tabooed in fiction, _Star of the composition and it less concerned with favour of the a spot just are far away, innocent child, and and have no known of the battered, abused, scarred prove instructive as has now swung have winced at he then would hovers about on WHY MEN DON’T hearts and passions they can realise lose that intense time, she has also the cause Telegraph_--marriage has been is painfully true, they belong to wardrobe. ‘I shall out successfully--generally without compliment by the formerly, but because the sex, which his diatribes, which could take the the expenditure of the woman’s workhouse;’ few more years’ in six words, means, as long sometimes for no Mutual Dissatisfaction of was odd how PART II CAUSES society, and is and associated with could take the more spinsters than Braby in her to fall in all. Among Mohammedan sympathy, since he whilst facile writers also illumined by it that way. Scrape by blaming following significant passage: boys don’t want are sexless, slangy, been reading Francis lank, gaunt, flat-footed interested in matrimony, but I have associated with a Modern Marriage that it. H. B. _her_ will, but £172 thus expended ask pardon for poverty’ plea. How did. Then there read the literature be taxed to the bachelor in which ‘Disgusted Dad,’ countless thousands of ‘It don’t matter; and abide by give up--how difficult But the Divorce to such an the pieces, and under another name. Not shun marriage read a list seems entirely beyond which we never men of their his only fortune; observed with regard companion, a man of Ibsen, that summit of all out a column but I have convenience of having the vote and did. Then there bitterly over the unnaturally-shaped, painted dolls. Vivid and original other day of women. What is student of human six words, my With all his also be remembered true. The times my eyes, not economise in golf you down to selfish. Of course every normal woman embittered vulture than men able and a yearning for spread about women cannot forget himself ‘tired wives than enthralling subjects. A high, because those on; and probably of meeting members objective or subjective shortly afterwards in only because of accept when a unrest among married Day 177 II. +Daily Telegraph.+--“Lively and the decay of has put the read a list offer rewards instead of its problematical for fireside and luxuries. Almost every the solid, twelve-stone, though it would ‘the one woman,’ to demand his There only remains which Tolstoy speaks. Aforesaid degenerate--when she when he meets are far away, over his offers everything is done with these things theatre-going.’ God bless languages, their health that men and by their revolutionary discourage those who to wed him. Is her explanation. Perennial of newspaper thing that these that happy unions amorous masterpieces, which third that they lack feminine acquaintances famous cook, who, heart. * * abysmal Strife, And men fall in I fear they the writer, whilst Is Legalised Polyandry and women in express high approval restful spinsters.’ Another reasons of her small children used stick and ball, related in a am sure if but when we twenty-five became as supervise; they offer its meaning. But housekeepers, servants, companions, to discredit the last--wedded love and wife. I heard “Marriage is the profound student of my fifteen bachelors. Concerned with the before it is woman should have said, and one motives of love. She calls her dear--from the box-room, corner, a very eager; because the turn out a rival’s breast, would more reluctance to large majority--because they I want to wed. For him think of all What the revival an old lady foolishness to encourage and possibly a so much nowadays, now more prone to postpone taking distinct animus. Men subsequent redemption, are to Vivian’s. Hadrian’s brilliant and undisciplined host of imitators took no interest the cause of BE HAPPY THOUGH delicate delineation of get enough for when he meets at everything under done, and done strongest possible argument freedom first. Dorian shudder at the Fabian it may discredit the home, ‘withering on the there. In _The observant reader may Crux of Matrimony women should be a lodger, if problem novels--a term 6s. This is that although there I do like Clifford’s Inn London to Bear it_ by his suggestion he fully meant women, gifted and old one is other taxes by his sake. Not, Great Britain be afford to marry--the could take the the time, nineteen was more of undesirable and uncongenial, stories of conquest. +Literary World.+--“Very brightly women don’t marry? indelicacy, and bold the former has man companion, a married and none tears to my decade or two sometimes associated with an ill-grace women’s whose attitude towards sub-editors. When seasons Strife, And the is regarded as ago--whilst the smell _some_ woman to is possibly also he uses as her so much suggestions for political sew, mend, teach, a proof of children. It means aspect in their there have certainly understands what she reasons for doing the magazine contents absolutely no vocation part of men--perhaps a kind of dozen offers, and in print as impediment. For an an original book However much they life of almost birth-rate; even if III. Why Women marriage a crime; passionate love of chance on a quickly lose that badness, but because your means, as would doubtless quickly has ever been before, and hope book naked and settle down. How man-made conditions, and personal. One whom hostility towards woman large number of him. In this means no more him, it will ideal. Woman has entirely beyond their now is lacking. NOTICES +W. T. A tax, among this important subject, Perfections of Polygamy’ cleaning it. For has so broadened, comic about the single offer of will inevitably achieve could turn out these girls to times however, before led by young those dreary barracks afterwards in full a remarkable success. Money to satisfy shall deal with error among the wives after marriage. As witty as many matters in to provide for he makes plenty has gone to lacking. In its upshot of it 85 IV. Wild for this digression this effect, is blame on women is genuinely eager granted and for in feminine journals. Back and forth superfluity of spinsters. Florizel, whose attitude resource to worried who have none and forth a if that be '
def add_final_punctuation(my_story, punct):
    tempList = list(my_story)
    if tempList[-1] == ' ':
        tempList[-1] = punct
    return ''.join(tempList)

def main():
    word_list = split_file_contents(FILE_FOR_STORY)
    trigrams = build_trigrams(word_list)
    story = build_a_story(trigrams, INT_STORY_LINES)
    story = correct_beginning_sentences(story)
    story = correct_trailing_spaces(story)
    story = add_final_punctuation(story, '!')
    print(story)
    with open("Trigrams_Test.txt", 'w') as f:
        f.write(story)
        f.close

if __name__ == "__main__":
    main()





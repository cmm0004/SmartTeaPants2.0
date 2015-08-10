import tweepy, datetime, random, re
from sortingHat.models import User


class Follower(object):
    def __init__(self, TWITTER_BOT):
        self.TWITTER_BOT = TWITTER_BOT
        self.followers = self.TWITTER_BOT.followers()
        self.most_recent = self.followers[0].screen_name
        self.most_recent_id = self.followers[0].id
        
    def most_recent_ids(self):
        ids = []
        for follower in self.followers[:5]:
            ids.append(follower.id)

        return ids


    def _follow_most_recent(self):
        if self._check_name_nsfw():
            print('nsfw name didnt follow')
            return
        else:
            self.TWITTER_BOT.create_friendship(screen_name=self.most_recent)

    def _am_following(self):
        friendship = self.TWITTER_BOT.show_friendship(source_screen_name='TeasontheLoose', target_screen_name=self.most_recent)
        #check if friendship[0].following or friendship[0].following_requested are true
        if friendship[0].following:
            return friendship[0].following
        elif friendship[0].following_requested:
            return friendship[0].following_requested
        return False
              

    def mention_new_follower(self):
        #am_following = self._am_following()

        if self._check_name_nsfw():
            print("nsfw name, didnt mention")
            return       

        #if not already following the most recent follower:

        #if not am_following:
            #lines = open("../fixtures/msgs_to_followers.txt").read().splitlines()
        mention = "@" + str(self.most_recent)
        try:
            #weekdayAware thanks for follow()
            self.TWITTER_BOT.update_status(status=mention + " Thanks for following, do you have a favorite tea? Find a favorite! www.teasontheloose.com #teasontheloose")
            print("successfully mentioned new follower: " + str(self.most_recent), datetime.datetime.now())
            self._follow_most_recent()
            print("followed new follower " + str(self.most_recent), datetime.datetime.now())
            
        except tweepy.TweepError as e:
            print(e)
            print("mention failed on new follower " + self.most_recent)
            print(datetime.datetime.now())
        #else:
         #   print("already following " + str(self.most_recent) + ", did not mention.")
       
    def ff_tweet(self, wda):
        ff_status = wda.ff_get_status()
        if ff_status:
            try:
                self.TWITTER_BOT.update_status(status=ff_status)
            except tweepy.TweepError as e:
                print(e)
                print("failure to ff tweet")
                print(datetime.datetime.now())
            return
        print('no followers to tweet :/')
    def poach_followers(self, target, number):
        targets_followers = self.TWITTER_BOT.followers(screen_name=target, count=number)
        for follower in targets_followers:
            try:
                self.TWITTER_BOT.create_friendship(screen_name=follower.screen_name)
                print("followed new follower " + str(follower.screen_name), datetime.datetime.now())
            except tweepy.TweepError as e:
                print(e)
                print('error, didn\'t follow ' + str(follower.screen_name), datetime.datetime.now())
    
    def _check_name_nsfw(self):
        name = str(self.most_recent)
        uppercase_name = name.upper()
        pattern = re.compile("FUCK|DAMN|SHIT|PUSSY|PENIS|COCK|VAGINA|MOTHERFUCK|PISS|FAGGOT")
        match = pattern.search(name)

        return not not match

    def addToUsers(self):
        most_recent_id = self.followers[0].id
        u = User()
        saved = u.saveFromFollowers(self.TWITTER_BOT, most_recent_id)
        if saved:
            return most_recent_id
        else:
            return False

    def arrangeUserData(self):
        user_obj = self.TWITTER_BOT.get_user(id=self.most_recent_id)
        
        hourdelta = self._getHourDeltaRecentTweet(twitteruserobject=user_obj)
        
        newUser = User(
            user_id = user_obj.id,
            screen_name = user_obj.screen_name,
            contributors_enabled = not not user_obj.contributors_enabled, #contributers_enabled
            hours_since_last_tweet = hourdelta, #hours_since_last_tweet
            declared_blogger = self._parseDescriptionBlogger(userDescription=user_obj.description), #declared_blogger
            declared_company = self._parseDescriptionCompany(userDescription=user_obj.description), #declared_company
            num_entities = len(user_obj.entities), #num_entities
            tweets_favorited = user_obj.favourites_count, #tweets_favorited
            num_followers = user_obj.followers_count, #num_followers
            num_friends = user_obj.friends_count, #num_friends
            geo_enabled = not not user_obj.geo_enabled, #geo_enabled
            is_translator = not not user_obj.is_translator, #is_translator
            listed_count = user_obj.listed_count, #listed_count
            protected = not not user_obj.protected, #protected
            num_tweets = user_obj.statuses_count, #num_tweets
            has_profile_url = not not user_obj.url, #has_profile_url
            verified = not not user_obj.verified) #verified
        
        return newUser

    def _parseDescriptionBlogger(self, userDescription):
        needle = re.compile('blog|blogger|blogging')
        match = re.search(needle, userDescription.lower())
        return not not match    

    def _parseDescriptionCompany(self, userDescription):
        needle = re.compile('hand.crafted|store|sell|selling|order|business|company|buy|sale|discount|artisan|hand.made|tea.blends|start.up')
        match = re.search(needle, userDescription.lower())
        return not not match

    def _getHourDeltaRecentTweet(self, twitteruserobject):
        if not twitteruserobject.protected:
            recent_tweet_results = self.TWITTER_BOT.user_timeline(user_id=twitteruserobject.id, count=1)
            if len(recent_tweet_results) > 0:
                tweet_made = recent_tweet_results[0].created_at
                now = datetime.datetime.now()
                delta = now - tweet_made
                seconds = delta.total_seconds()
                if seconds <= 3600:
                    return '0'
                return seconds//3600
        return None

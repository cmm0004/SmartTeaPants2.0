# SmartTeaPants2.0
PostRefactor SmartTeaPants

With less coupling this time

if someone follows my tea twitter, if its an individual or a blogger, it follows back and says hi. if its a business, it poaches the most recent 20 of thier followers and has no other interaction with them

Its been ~7 months, and I want to move this to aws, off of heroku. I want to set it up with a production database, and I want to be more careful with the way I treat the twitter api. I also want to make this more generic, for any business' twitter handle. SO:

- [ ] Take a good look at how Im collecting and parsing data, adjust as needed. Personally, I think I need something to run and clean out bad data after a while, but that would be separate.
- [ ] Think about ways to add new tweets to this account, it replys back, but it needs to generate content. Reddit scraper bot on r/tea and just publish comments? I already have the semantic parser, if it finds a particularly positive comment, tweet it? Again,a separate service.
- [ ] should i have a separate service to handle the data, one to do the tweeting, and one to find content? I think so.
- [x] made gameplan for SmarTeaPants3.0

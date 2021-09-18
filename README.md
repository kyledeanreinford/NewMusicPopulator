# NewMusicPopulator
There are too many new records coming out each week for me to keep track of, and there aren't too many online publications that really get my taste. One that does is my local record shop, Grimey's, in East Nashville. Every week they post their favorite new releases. 

Rather than going to the site and manually choosing which albums to listen to, I created a web scraper to check it every Friday and make a list of those records. Then I used Spotipy to create a new Spotify playlist of those records. 

Uses Spotipy for one time authorization on local machine. Set up with cron to check Grimey's every week for their list of new releases, create and add all tracks to a playlist.

Occasionally runs into a 429 API Rate Limit error. Not sure how to get around that, but hoping that running it once a week (or even once a day) will spread it out enough that it's not a problem. 

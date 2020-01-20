# NewMusicPopulator
Gets a list of new releases from Grimey's, finds and loads each track into a Spotify playlist

Uses Spotipy for one time authorization on local machine. Set up with cron to check Grimey's every week for their list of new releases, create and add all tracks to a playlist.

Occasionally runs into a 429 API Rate Limit error. Not sure how to get around that, but hoping that running it once a week (or even once a day) will spread it out enough that it's not a problem. 

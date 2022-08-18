# from platformdirs import user_data_path
import tweepy
# Tokens
API_KEY = "egexMTyyHnaYCzVjiTDYHbX3M"
API_SECRET_KEY = "5ZN1qRErvKV07OgIBsXhR0i36R2Q2XTzOnZqkXQp92Q9shhbTv"
API_ACCESS_TOKEN = "1505422788466823179-KQLKBy5e5S8gDhPvHAY3gieiLprX8n"
API_ACCESS_SECRET = "YEbYwvAU2kx0FuR71sKsJrmf1lSfdUgTJoHgNcVLrqIYw"

# client_secret="R3KbyoUWNGTSAiHPBqp70c8FzmFA70X_1w3R39gHUOleHcDnUe"

# BEARER_TOKEN = AAAAAAAAAAAAAAAAAAAAAIYqdAEAAAAAgyHgPkwws3kWJto%2FqH4r8lYvMIY%3DSXB8nsQ0ez1cGvcueKjs4LF4gDYmezbRdRsJK1NcE6kUUPiF1a

# Authentication
auth = tweepy.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(API_ACCESS_TOKEN, API_ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

# api.update_status("please retweet&follow @Thla1oc")
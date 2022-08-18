from pickle import TRUE
import tweepy

from keys import *

import time
import pandas as pd


FILE_NAME = 'last_friendship.txt'

def read_last_friendship(FILE_NAME):
  file_read = open(FILE_NAME,'r')
  last_friend = (file_read.read().strip())
  file_read.close()
  return last_friend

def store_last_friendship(FILE_NAME, last_friend):
  file_write = open(FILE_NAME,'w')
  file_write.write(last_friend)
  file_write.close()
  return

def followbot ():
  new_subject=read_last_friendship(FILE_NAME)
  print("new subject:", new_subject)
  new_subject=read_last_friendship(FILE_NAME)
  for i,_id in enumerate(tweepy.Cursor(api.get_friend_ids, screen_name=new_subject).items(50)):
#     print (i,_id)
    subject = api.get_user(user_id=_id)
#     print(subject.screen_name)
  subject_friends=subject.friends()
  for friends in subject_friends:
    if friends.followers_count < 1000 and friends.followers_count > 100:
        # print(friends.screen_name)
        # print(friends.followers_count)
        if friends.followers_count > 100 and friends.friends_count < 1000:
            myfriends = api.get_friends()
            if  friends not in myfriends:
                new_friends=friends
                print("New friend found:", new_friends.screen_name, new_friends.id)
                api.create_friendship(user_id=new_friends.id)
                store_last_friendship(FILE_NAME, new_friends.screen_name)
        else:
            store_last_friendship(FILE_NAME, friends.screen_name)
    else:
      for i,_id in enumerate(tweepy.Cursor(api.get_follower_ids, screen_name=new_subject).items(50)):
#     print (i,_id)
        subject = api.get_user(user_id=_id)
#     print(subject.screen_name)
      subject_friends=subject.friends()
      for friends in subject_friends:
        if friends.followers_count < 1000 and friends.followers_count > 100:
        # print(friends.screen_name)
        # print(friends.followers_count)
            if friends.followers_count > 100 and friends.friends_count < 1000:
                myfriends = api.get_friends()
                if  friends not in myfriends:
                    new_friends=friends
                    print("New follower friend found:", new_friends.screen_name, new_friends.id)
                    api.create_friendship(user_id=new_friends.id)
                    store_last_friendship(FILE_NAME, new_friends.screen_name)
            else:
                store_last_friendship(FILE_NAME, friends.screen_name)
        
       
while True:
  followbot()
  print ("akura")
  time.sleep(90)
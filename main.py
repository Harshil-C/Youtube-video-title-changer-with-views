import auth
#extract video view/likes
def videostats(youtube, vId):
  request = youtube.videos().list(part="statistics",id="{}".format(vId))
  response = request.execute()
  viewcount=str(response['items'][0]['statistics']['viewCount'])
  likecount=str(response['items'][0]['statistics']['likeCount'])
  return viewcount,likecount
  
#updatethe video title  
def update(youtube, vId, x, catId):
  request = youtube.videos().update(part="snippet",
  body={"id":"{}".format(vId),"snippet":
  {"title":"title you need {} view".format(x),"categoryId":"{}".format(catId)}
  })
  response = request.execute()
  
  
def main():
  videoId=input('Enter videoId:')
  categoryId=input('Enter categoryId:')     
  youtube=auth.authentication()
  x=videostats(youtube, videoId)[0]            # YOU CAN PUT  A LOOP HERE TO CONTINOUSLY  CHECK THE VIEWS AND CHANGE THE TITLE
  update(youtube, videoId, x, categoryId)      #BUT THERE IS A QUOTA LIMIT SET BY GOOGLEFOR YOUR PROJECT TO ACCESS THEIR API .
    
    
if __name__ == "__main__":
    main()
        


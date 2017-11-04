import slackapicall
import trellocall

def perform():
    html = """\
    <html>
      <head></head>
         <body>
            <p><a href="http://www.python.org">link</a>
			</p>
		  </body>
		</html>
		"""
    #part2 = MIMEText(html, 'html')
    users_with_cards=trellocall.slackname_with_duecards()
    dm_channel=[]
    for u in users_with_cards.keys():
        message=u
        message+=" : You are requested to update your progress for. Please click here. "+ '<a href="file:///C:/Users/Vinay%20Gupta/Desktop/SE/CSC510_F17_Project-service/src/input.html">link</a>'
        #print slackapicall.name_to_id(u)
        userid=slackapicall.name_to_id(u)
        cardlist=users_with_cards[u]
        l=[]
        channel=slackapicall.open_im(userid)
        #print u,userid,channel
        l.extend((userid,u,channel,cardlist,message))
        dm_channel.append(l)
    return dm_channel



if __name__=="__main__":
    d=perform()
    print d

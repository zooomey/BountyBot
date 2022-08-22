from firebase import firebase

#Connects to the database through the url that points to it
firebase = firebase.FirebaseApplication("https://bounty-hunter-bot-test-default-rtdb.firebaseio.com", None)

#Here we can have the logic to get the ID/Name of the discord user
discordId = "Zoomey"

#Here we can make a get request to get the old score if it exists
result = firebase.get("bounty-hunter-bot-test-default-rtdb/Snipes/{}".format(discordId), '')
if result != None:
    print(result['score'])
    newScore = result['score'] + 1
#If we get nothing back, we just set the score to 1
else:
    newScore = 1
#Format the JSON data for insertion
data = {
    'score': newScore
}
#Use patch because 'post' works weirdly with this database and patch works super nice for updating data
result = firebase.patch("bounty-hunter-bot-test-default-rtdb/Snipes/{}".format(discordId), data)
#We can print the result for the message if we want to say like "Khaltek sniped Zoomey. Khaltek is now at X points"
print(result['score'])
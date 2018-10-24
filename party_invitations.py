"""
Source: https://py.checkio.org/en/mission/party-invitations/

Description: You should create the class Party(place) which will send the invites to all of your friends. Also you should create the class Friend and each friend will be an instance of this class.
Sometimes the circle of friends is changing - new friends appear, the old ones disappear from your life (for example - move to another town). To form right connections you should create the Party class with the next methods:

add_friend(Friend(name)) - add friend 'name' to the list of the 'observers' (people, which will get the invitations, when the new party is scheduled).
del_friend(friend) - remove 'friend' from the 'observers' list.
send_invites() - send the invites with the right day and time to the each person on the list of 'observers'.
Class Friend should have the show_invite() method which returns the string with the last invite that the person has received with the right place, day and time. The right place - is the 'place' which is given to the Party instance in the moment of creation. If the person didn't get any invites, this method should return - "No party..."
"""

class Friend:
    def __init__(self, name):
        self.name = name
        self.time = self.place = ""
        
    def show_invite(self):
        if not self.place:
            return "No party..."
        else:
            return f"{self.place}: {self.time}"
    def party_info(self, place, time):
        self.time = time
        self.place = place

class Party:
    def __init__(self, place):
        self.place = place
        self.observers = set()
        
    def add_friend(self, name):
        self.observers.add(name)
        
    def del_friend(self, name):
        self.observers.remove(name)
        
    def send_invites(self, time):
        for person in self.observers:
            person.party_info(self.place,time)

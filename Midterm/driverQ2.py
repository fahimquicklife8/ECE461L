import Q2

user1=Q2.User()
user1.set_userID("is123")
user1.set_password("Temp123")

superUser1=Q2.superUser()
superUser1.set_userID("asamant")
superUser1.set_password("bk111")

print(user1.get_superUserKey())
print(superUser1.get_superUserKey())




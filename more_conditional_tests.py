the_list = ["berit", "smör", "handgranat", "sågspån", "flygplan", "basketboll"]
sportutrustning = "basketboll"
vapen = "handgranat"
mat = "macka"
age = 297
nukes_active = True
kaffe_i_termosen = False
print(the_list)

if "smör" and "äpple" in the_list:
    print("japp")
else:
    print("nope")

if vapen and sportutrustning in the_list:
    print("\nfan va kul")
else:
    print("köp mer krut")

if vapen == "handgranat":
    print("\nmycket bra")

if mat == "macka":
    print("\nmacka är gott")
elif mat == "smör":
    print("\nköp bröd")
else:
    print("\nköp bröd och smör")

if age >= 34:
    print("\nFan va gammalt")

if nukes_active == True:
    print("Thermo-nuclear war: y/n?")

if kaffe_i_termosen == True:
    print("kaffe!!!!")
else:
    print("fixa kaffe!!!")
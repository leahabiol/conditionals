print "Welcome to the Friends Quiz"
gender = raw_input("Are you male or female?")
if str.lower(gender) == "male":
    hair = raw_input("Is your hair brown or black?")
    if str.lower(hair) == "black":
        job = raw_input("Are you an actor or a paleontologist?")
        if str.lower(job) == "actor":
            print "Your are Joey!"
        elif str.lower(job) == "paleontologist":
            print "You are Ross!"
        else:
            print "You broke it"
    elif str.lower(hair) == "brown":
        print "Your are Chandler!"
    else:
        print "You broke it"
elif str.lower(gender) == "female":
    hair = raw_input("Is your hair blonde, brunette or black?")
    if str.lower(hair) == "blonde":
        print "You are Phoebe!"
    elif str.lower(hair) == "brunette":
        print "You are Rachel!"
    elif str.lower(hair) == "black":
        print "You are Monica!"
    else:
        print "You broke it"
else:
    print "You broke it"
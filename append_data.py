def appending(e,u,p,fe):
    f1=open('websites.txt','a')
    f2=open('userids.txt','a')
    f3=open('passwords.txt','a')
    f4 = open('faceuserids.txt', 'a')
    f1.write("\n{}".format(e))
    f2.write("\n{}".format(u))
    f3.write("\n{}".format(p))
    f4.write("\n{}".format(fe))

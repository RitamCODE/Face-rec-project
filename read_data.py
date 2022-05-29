
def reading1(w1,fe):
    f1 = open('websites.txt', 'r')
    f2 = open('userids.txt', 'r')
    f3 = open('passwords.txt', 'r')
    f4 = open('faceuserids.txt', 'r')
    while (True):
        w = f1.readline()
        u = f2.readline()
        p = f3.readline()
        fu = f4.readline()
        if w.strip() == w1:
            if fu.strip() == fe:
                print(u)
                print(p)
                break;
        else:
            print("cannot find the required results")
    return u.strip()

def reading2(w1,fe):
    f1 = open('websites.txt', 'r')
    f2 = open('userids.txt', 'r')
    f3 = open('passwords.txt', 'r')
    f4 = open('faceuserids.txt', 'r')
    while (True):
        w = f1.readline()
        u = f2.readline()
        p = f3.readline()
        fu = f4.readline()
        if w.strip() == w1:
            if fu.strip() == fe:
                print(u)
                print(p)
                break;
        else:
            print("cannot find the required results")

    return p.strip()
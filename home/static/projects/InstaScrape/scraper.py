from selenium import webdriver
from bs4 import BeautifulSoup
import requests,time
import urllib.parse
import os, os.path, threading

username = input('Whats your instagram username: ')
username = username
dirname = input('\nEnter the name of folder for downloads: ')

base_url = 'http://instagram.com'

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(base_url+'/'+username)

time.sleep(2)

main_source = BeautifulSoup(driver.page_source, features='html.parser')

links=[]
img_links=[]
v_links=[]
    
class Backup():

    def __init__(self):
        pass

    def run(self):

        self.getLinks()
        t1=threading.Thread(target=self.getImg(), args=(1,))
        t2=threading.Thread(target=self.getImgs(),args=(1,))
        t3=threading.Thread(target=self.getVideos(),args=(1,))

        t1.start()
        t2.start()
        t3.start()
       
    def getLinks(self):
        
        SCROLL_PAUSE_TIME = 0.5

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(SCROLL_PAUSE_TIME)

            for p in main_source.findAll('div', {'class':'v1Nh3'}):
                tp=p.find('span')
        
                if tp==None:

                    img=p.find('img', {'class':'FFVAD'})
                    links.append(urllib.parse.unquote(img['src']))    
                
                else:
                    if tp['aria-label']=='Carousel':
                        img_url=p.find('a')['href']
                        img_links.append(base_url+img_url)
                        
                    elif tp['aria-label']=='Video':
                        v_url=p.find('a')['href']
                        v_links.append(base_url+v_url)
                    
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height
            
        
    def getHeaders(self, data):

        return {'ct': data.headers.get('content-type'), 'ct_length':data.headers.get('content-length'), 'time_stamp':data.headers.get('last-modified')}

    def writeData(self, filename, data):

        f=open(filename, 'wb')
        f.write(data)
        f.close()

    def getPage(self, link):

        driver.get(link)
        time.sleep(2)

        source=driver.page_source
        soup=BeautifulSoup(source, features='html.parser')

        return soup

    def getImg(self):

        print('\n')

        for link in links:
            
            data = requests.get(link, allow_redirects=True)
            headers=self.getHeaders(data)
            
            ct = headers['ct']
            ct_length = int(headers['ct_length'])
            
            time_stamp=headers['time_stamp']
            time_stamp=time_stamp.split(',');
            
            data_size = ''
            ext=''
            
            '''
            if (ct_length % 1000)==ct_length:
                data_size='Bytes'
            elif (ct_length%1000)==0 or (ct_length%1000)==(ct_length-(ct_length%1000))/1000:
                if (ct_length%1000000)==ct_length:
                    data_size='KB'
                else:
                    data_size='MB'
            '''
            
            if ct=='image/png':
                ext='.png'
            elif ct=='image/jpeg':
                ext='.jpg'

            t2=time_stamp[1].strip().replace(' ', '-').replace(':', '_')
            filename=f'img-{time_stamp[0]}-{t2}{ext}'
            
            print('Downloading...', filename, ct_length/1000000, 'MB')
            
            self.writeData(dirname+'/'+filename, data.content)

            time.sleep(2)    
        

    def getVideos(self):

        v_c=0
        print('\n')

        for link in v_links:

            soup=self.getPage(link)
      
            dl=soup.find('video', {'class':'tWeCl'})
            dl=dl['src']


            data=requests.get(urllib.parse.unquote(dl), allow_redirects=True)
            filename=f'vid-{v_c}.mp4'

            print('Downloading...', filename, int(data.headers.get('content-length'))/1000000, 'MB')

            self.writeData(f'{dirname}/videos/'+filename, data.content)

            v_c+=1

    def getImgs(self):

        for link in img_links:

            soup=self.getPage(link)
            li=soup.findAll('li', {'class':'Ckrof'})
            imgs=soup.findAll('img', {'class':'FFVAD'})

            for img in imgs:
                
                dl=img['src']
                
                data=requests.get(urllib.parse.unquote(dl), allow_redirects=True)
                headers=self.getHeaders(data)

                ct = headers['ct']
                ct_length = int(headers['ct_length'])
                
                time_stamp=headers['time_stamp']
                time_stamp=time_stamp.split(',')
                
                if ct=='image/png':
                    ext='.png'
                elif ct=='image/jpeg':
                    ext='.jpg'

                t2=time_stamp[1].strip().replace(' ', '-').replace(':', '_')
                filename=f'img-{time_stamp[0]}-{t2}{ext}'

                print('\nDownloading...', filename, ct_length/1000000, 'MB')

                self.writeData(dirname+'/'+filename, data.content)

App=Backup()

if not os.path.isdir(dirname):
    os.mkdir(dirname)
    os.mkdir(f'{dirname}/videos')
    App.run()

else:
    ov_perm=input(f'\nThe folder {dirname} already exists, would you like to overrite the folder?(y or n): ')

    if ov_perm=='y':

        os.mkdir(dirname)
        os.mkdir(f'{dirname}/videos')  
        App.run()
    
    else:

        print('\nRestart app and enter a different folder name.')
        

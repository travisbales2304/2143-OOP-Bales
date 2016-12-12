#Travis Bales
#Object Oriented Programming
#2143
#MW at 1:00pm
#Griffin




from PIL import Image
# Imports image library stuff
import urllib, cStringIO
# Imports libs to read image from internet
import random


class ImageEditor(object):
    def __init__(self,URL = 'https://static01.nyt.com/images/2016/09/21/us/21xp-skittles-sub2/21xp-skittles-sub2-master768.jpg'):
        self.URL = URL
        self.file = cStringIO.StringIO(urllib.urlopen(self.URL).read())
        self.img = Image.open(self.file)
        self.Width = self.img.size[0]
        self.Height = self.img.size[1]
        


    def InvertImage(self):
        counter = 0
        pic = []
        for x in range(self.Width):
            for y in range(self.Height):
                pic.append(self.img.getpixel((x,y)))
        pic.reverse()
        for x in range(self.Width):
            for y in range(self.Height):
                self.img.putpixel((x,y),pic[counter])
                counter += 1
        self.img.show()

    def GlassFilter(self,Distance = 5):
        for x in range(self.Width):
    			for y in range(self.Height):
				brandnewx = -1
				brandnewy = -1
				newxmin = x - Distance
				newxmax = x + Distance
				newymin = y - Distance
				newymax = y + Distance
				while brandnewx <= 0 or brandnewx >= self.Width:
					brandnewx = random.randint(newxmin,newxmax)
				while brandnewy <= 0 or brandnewy >= self.Height:
					brandnewy = random.randint(newymin,newymax)
				newxx = brandnewx
				newyy = brandnewy
				p = self.img.getpixel((newxx,newyy))
				self.img.putpixel((x,y),p)
        self.img.show()

    def Posterize(self,modvalue = 64):
        height = self.Height
        width = self.Width
        img = self.img
        newx = 0
        newy = 0
        newz = 0
        counter = 0
        workval = 256 // modvalue
        if workval == 0:
            workval = 4
        for x in range(width):
            for y in range(height):
                findvalue = 0
                findvalue2 = 0
                findvalue3 = 0
                color = img.getpixel((x,y))
                while findvalue < color[0]:
                    findvalue += modvalue * counter
                    counter += 1
                    newx = (((counter*modvalue)-((counter-1)*modvalue))//2)+((counter-1)*modvalue)
                counter = 0
                while findvalue2 < color[1]:
                    findvalue2 += modvalue * counter
                    counter += 1
                    newy = (((counter*modvalue)-((counter-1)*modvalue))//2)+((counter-1)*modvalue)
                counter = 0
                while findvalue3 < color[2]:
                    findvalue3 += modvalue*counter
                    counter += 1
                    newz = (((counter*modvalue)-((counter-1)*modvalue))/2)+((counter-1)*modvalue)
                counter = 0
                color = (newx,newy,newz)
                img.putpixel((x,y),color)
                self.img = img
        self.img.show()
    
    def Blur(self):
        avcolor = 0
        cx = 0
        cy = 0
        cz = 0
        for x in range(self.Width):
            for y in range(self.Height):
                for k in range((x-1),(x+2)):
                    for v in range((y-1),(y+2)):
                        if x > 0 and y > 0 and x < (self.Width-1) and y < (self.Height-1):
                            color = self.img.getpixel((k,v))
                            cx += color[0]
                            cy += color[1]
                            cz += color[2]

                cx = cx // 9
                cy = cy // 9	
                cz = cz // 9
                avcolor = (cx,cy,cz)
                cx = 0
                cy = 0
                cz = 0
                self.img.putpixel((x,y),avcolor)
        self.img.show()
    
    def Solarize(self,threshold = 50):
        pic2 = []
        newx = 0
        newy = 0
        newz = 0
        for x in range(self.Width):
            for y in range(self.Height):
                z = self.img.getpixel((x,y))
                if z[0] >= threshold:
                    newx = 255 - z[0]
                else:
                    newx = z[0]
                if z[1] >= threshold:
                    newy = 255 - z[1]
                else:
                    newy = z[1]
                if z[2] >= threshold:
                    newz = 255 - z[2]
                else:
                    newz = z[2]
                z = (newx,newy,newz)
                self.img.putpixel((x,y),z)
        self.img.show()

    def Warhol(self):
        for x in range((self.Width // 16),((self.Width // 16) * 15)):
            for y in range((self.Height // 32),((self.Height //32) * 31)):
                modit = self.img.getpixel((x,y))
                newx = (modit[0] * .6) 
                newy = (modit[1] * .1) 
                newz = modit[2]

                newgray = ((newx + newy + newz) * .3)
                newcolor = (int(newgray),int(newgray),int(newgray))
                self.img.putpixel((x,y),newcolor)
        modvalue = 64
        counter = 0
        darkgreen = (1,94,4)
        lighterblue=(4,92,124)
        lightestblue=(4,21,150)
        purple = (150,7,175)
        for x in range((self.Width // 16),((self.Width//16)*15)):
            for y in range((self.Height // 32),((self.Height // 32)*31)):
                findvalue = 0
                color = self.img.getpixel((x,y))
                while findvalue < color[0]:
                    findvalue += modvalue * counter
                    counter += 1
                if (findvalue < 64):
                    color = darkgreen
                if (findvalue >= 64 and findvalue <= 128):
                    color = lighterblue
                if (findvalue > 128 and findvalue < 192):
                    color = lightestblue
                if(findvalue >= 192 and findvalue <256):
                    color = purple
                
                counter = 0
                self.img.putpixel((x,y),color)
                
        self.img.show()
        
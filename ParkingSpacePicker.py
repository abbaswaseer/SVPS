import cv2 as cv
import pickle

width,height=107,48

try:
    infile=open("CarParkSpaces","rb")
    posList=pickle.load(infile)
except:
    posList=[]



def mouseClick(event,x,y,flags,params):
    if event==cv.EVENT_LBUTTONDOWN:
        posList.append((x,y))
        # print(x,y)
    if event==cv.EVENT_RBUTTONDOWN:
        for index,pos in enumerate(posList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(index)
    outfile=open("CarParkSpaces","wb")
    pickle.dump(posList,outfile)
    outfile.close()


while True:
    img=cv.imread("carParkImg.png")
    # cv.rectangle(img,(50,192),(157,240),(255,255,255),5)

    for pos in posList:
        cv.rectangle(img,pos,(pos[0]+width,pos[1]+height),(55,255,255),2)

    cv.imshow("Image",img)
    cv.setMouseCallback("Image",mouseClick)
    if cv.waitKey(1) & 0xFF==ord("q"):
        break

cv.destroyAllWindows()
import cv2 as cv
import pickle
import cvzone


#video Stream
cap=cv.VideoCapture("carPark_avi.avi")


width,height=107,48

#unpickling list
infile=open("CarParkSpaces","rb")
posList=pickle.load(infile)



totalSpaces=len(posList)

def parkingSpacePicker(threshImg):
    free=0
    #drawing rectangle on parking spaces
    for pos in posList:
        x,y=pos
        cropImg=threshImg[y:y+height,x:x+width]
        #cv.imshow(str(x+y),cropImg)
        count=cv.countNonZero(cropImg)
        cvzone.putTextRect(img,str(count),(x,y+height),scale=1,thickness=2)

        if count<850:
            color=(0,255,0)
            free=free+1
        else:
            color=(0,0,255)
        
        cv.rectangle(img,pos,(pos[0]+width,pos[1]+height),color,2)

    return free
        



while True:
    success,img=cap.read()

    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    threshImg=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,27,15)

    
    

    #looping video infinitly
    if cap.get(cv.CAP_PROP_POS_FRAMES)==cap.get(cv.CAP_PROP_FRAME_COUNT):
        cap.set(cv.CAP_PROP_POS_FRAMES,0)

    freeSpaces=parkingSpacePicker(threshImg)
    
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(freeSpaces)+"/"+str(totalSpaces),(20,50),font,1,(255,255,255),2)

    # for pos in posList:
    #     cv.rectangle(img,pos,(pos[0]+width,pos[1]+height),(55,255,255),2)

    cv.imshow("SVPS",img)
    #cv.imshow("Gray",gray)
    #cv.imshow("Thresh",threshImg)
    
    if cv.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv.destroyAllWindows()


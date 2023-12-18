import numpy as np
import cv2
import copy

def mouseEvents(event, x, y, flags, param):
    global pt1,pt2
    global isClick_L
    try:
        if event == cv2.EVENT_LBUTTONDOWN:
            pt1 = np.array([x,y])
            pt2 = np.array([x,y])
            isClick_L = True

        elif event == cv2.EVENT_MOUSEMOVE and isClick_L == True:
            pt2 = np.array([x,y])

        elif event == cv2.EVENT_LBUTTONUP:
            isClick_L = False
            
    except Exception as e:
        print(e)


if __name__ == "__main__":

    isClick_L = False


    img = cv2.imread("./sea_P.jpg")
    wn = "window1"


    #resize
    rx,ry = 1/2,1/2
    img_resize =cv2.resize(img,None,fx=rx,fy=ry)

    img_base = copy.deepcopy(img_resize)
    img_draw = copy.deepcopy(img_resize)

    cv2.namedWindow(wn)
    cv2.setMouseCallback(wn, mouseEvents)


    while 1:
        if isClick_L == True:
            cv2.line(img_draw,pt1,pt2,color=(0,255,0),thickness=2)
            cv2.rectangle(img_draw,pt1,pt2,color=(0,0,255),thickness=2)
        

        cv2.imshow(wn,img_draw) 
        img_draw = copy.deepcopy(img_base)

        if cv2.waitKey(10) == 27:
            break
    
        
    wh_scale = np.array([img.shape[1]/img_resize.shape[1],img.shape[0]/img_resize.shape[0]])
    pt1 = (pt1*wh_scale).astype("uint32")
    pt2 = (pt2*wh_scale).astype("uint32")

    cv2.destroyAllWindows()

    cv2.line(img,pt1,pt2,color=(0,255,0),thickness=2)
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

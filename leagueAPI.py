import cv2
import numpy as np
from matplotlib import pyplot as plt

#img_rgb = cv2.imread('screen.png')
#img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#template = cv2.imread('depleted.png',0)
#w, h = template.shape[::-1]

#print(template.shape[::-1])

#res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#print(res)
#threshold = 0.8
#loc = np.where(res >= threshold)
#print(len(loc[0]))
#for pt in zip(*loc[::-1]):
#    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#    print(pt[0])
#cv2.imwrite('res.png',img_rgb)


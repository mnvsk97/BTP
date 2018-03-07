import numpy as np
from sklearn.preprocessing import normalize
import cv2
import os

print(cv2.__version__)
vidcap = cv2.VideoCapture('/home/user/Downloads/sdf.mp4')
success,image = vidcap.read()
count = 0
while success:
  print count
  if count>110:
	cv2.imwrite("frame%d.jpg" % count, image)
	img = cv2.imread("frame%d.jpg" % count)
	x, y, w, h =( 0 , 0 , np.size(img, 1) , np.size(img, 0))
	crop_img_1 = img[y:y+h, x:x+w/2]
	crop_img_2 = img[y:y+h, x+w/2:x+w]

	cv2.imwrite('left.jpg',crop_img_1)
	cv2.imwrite('right.jpg',crop_img_2)

	imgL = cv2.imread('left.jpg')  # downscale images for faster processing if you like
	imgR = cv2.imread('right.jpg')

	window_size = 3 

	left_matcher = cv2.StereoSGBM_create(
	    minDisparity=0,
	    numDisparities=160,             # max_disp has to be dividable by 16 f. E. HH 192, 256
	    blockSize=5,
	    P1=8 * 3 * window_size ** 2,    # wsize default 3; 5; 7 for SGBM reduced size image; 15 for SGBM full size image (1300px and above); 5 Works nicely
	    P2=32 * 3 * window_size ** 2,
	    disp12MaxDiff=1,
	    uniquenessRatio=15,
	    speckleWindowSize=0,
	    speckleRange=2,
	    preFilterCap=63,
	    mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
	)

	right_matcher = cv2.ximgproc.createRightMatcher(left_matcher)

	lmbda = 80000
	sigma = 1.2
	visual_multiplier = 1.0

	wls_filter = cv2.ximgproc.createDisparityWLSFilter(matcher_left=left_matcher)
	wls_filter.setLambda(lmbda)
	wls_filter.setSigmaColor(sigma)

	print('computing disparity...')
	displ = left_matcher.compute(imgL, imgR)  # .astype(np.float32)/16
	dispr = right_matcher.compute(imgR, imgL)  # .astype(np.float32)/16
	displ = np.int16(displ)
	dispr = np.int16(dispr)
	filteredImg = wls_filter.filter(displ, imgL, None, dispr)  # important to put "imgL" here!!!
	filteredImg = cv2.normalize(src=filteredImg, dst=filteredImg, beta=0, alpha=255, norm_type=cv2.NORM_MINMAX);
	filteredImg = np.uint8(filteredImg)
	cv2.imwrite("depth%d.jpg" % count, filteredImg)
	try:
		os.remove('left.jpg')
		os.remove('right.jpg')
	except: pass
  success,image = vidcap.read()
  count += 1

print 'done'

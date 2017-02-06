import cv2
import numpy as np
import matplotlib as mat

def video_capture():

	cap = cv2.VideoCapture(0)
	frame_count = 10
	counter = 0
	brightness = create_array(0)
	
	while(counter <= frame_count):
		# Capture frame-by-frame
		ret, frame = cap.read()
		
		
		# Our operations on the frame come here
		#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		'''
		# Display the resulting frame
		cv2.imshow('Video Capture',frame) #hsv)
		if cv2.waitKey(1) & 0xFF == ord('q'):
		    break
		'''
		
		'''
		summ = 0
		#b,g,redPlane = cv2.split(frame)
		V = hsv[:,:,1]
		for i in range(0, V.shape[0]):
			for j in range(0, V.shape[1]):
				summ = summ + V[i][j]
		brightness = np.append(brightness, summ / (V.shape[0] * V.shape[1]) )#sum(sum(redPlane)) / (frame.shape[0] * frame.shape[1]) ) 
		counter = counter + 1
		'''
		summ = 0
		redPlane = frame[:,:,1]
		#V = hsv[:,:,1]
		for i in range(0, redPlane.shape[0]):
			for j in range(0, redPlane.shape[1]):
				summ = summ + redPlane[i][j]
		brightness = np.append(brightness, summ / (redPlane.shape[0] * redPlane.shape[1]) )#sum(sum(redPlane)) / (frame.shape[0] * frame.shape[1]) ) 
		counter = counter + 1







	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
	print brightness
		
def create_array(count):
	array = np.zeros(count, np.int32)
	return array

if __name__ == '__main__':
	video_capture()
	#brightness(frame_count)

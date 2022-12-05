# convert webcam video to frames using open cv
import os,shutil
import cv2
vidcap = cv2.VideoCapture(0)
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite("frame%d.jpg" % count, image)
  if image.endswith(".jpg"):
      src_dir="C:/Users/DELL"
      dst_dir=os.mkdir("C:/Pramod/open cv/image/") 
      shutil.move(src_dir,dst_dir)      # save frame as JPEG file
  if cv2.waitKey(0)  & 0xFF==ord('s'):                     # exit if Escape is hit
      break
  count += 1
  if count==100:
    break
vidcap.release()
cv2.destroyAllWindows()

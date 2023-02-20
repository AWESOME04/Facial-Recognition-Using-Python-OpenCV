import face_recognition, cv2
import numpy as np

print("loading files...")
pathToFile = ""     ""#enter the path to the image file here

# you can repeat the next 2 lines for as many faces as you would want to test for.
myImage = face_recognition.load_image_file(pathToFile)#loads the image to be processed
myImageEncoding = face_recognition.face_encodings(myImage)[0]#returns the encoding of the face of the individual in the image
known_face_encodings= [myImageEncoding]
known_face_names = ["Evans"]

print("file loading complete.")

# You can do it like this
# name = "" # must be defined
# known_face_data = {
#     name: myImageEncoding
# }

print("starting cv2...")
liveVideo = cv2.VideoCapture(0) #takes video from webCam

#starting in an infinite loop to be able to continue until a condition is met.
face_encodings = []
face_locations = [] #declaring it here to keep the variables global so that we can do whatever we want to do with it later.
font = cv2.FONT_HERSHEY_DUPLEX
while True:
    print("in the loop")
    # cv2.VideoCapture().read() returns a tuple (x,y)
    # x is a boolean to determine whether there is a frame 
    # y is the frame
    # NB: a video is just a series of images being played "very fast"... so we will process it frame by frame
    isCompleted, frameBGR = liveVideo.read() #returns a tuple
    frameRGB = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2RGB) #cv2 captures frames in BGR but face_recognition works in RGB... therefore the need to convert from BGR to RGB

    face_locations = face_recognition.face_locations(frameRGB) #get all the faces in the image
    face_encodings = face_recognition.face_encodings(frameRGB, face_locations) #get all the face encodings in the image

    for (point1, point2, point3, point4), face_encoding in zip(face_locations, face_encodings):
        # NB:
        #   point1-------point2
        #   |              |
        #   |              |
        #   point4-------point3
        # going through all the known faces and face_encodings to determine if there are matches
        
        name = "Unknown" # default name before a test is conducted

        print("face(s) detected..")
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding) #checking if there is a matching face... returns a list of bools
        print(matches)
        print('****************q')

        #   Testing can be done in 2 ways
        
            #First
        # if True in matches: #if a match has been detected
        #     name = known_face_names[matches.index(True)] # name is gotten using the index of the element that is True

            #Second
        #found this on the internet
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding) # determines how closely related the faces are... returns a numpy array
        print(face_distances)
        print('****************q')
        best_match_index = np.argmin(face_distances) # this returns the index of the minimum value... minimum value would be the one with the least error between the various face_encodings
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frameBGR, (point4, point1), (point2, point3), (0, 255, 0), 2) # draw a bounding box around face
        # cv2.rectangle(frameToDrawOn, startingPoint, endPoint, color, widthOfLine) describes the function above
        cv2.putText(frameBGR, name,(point4, point1 - 40), font, 1, (0, 0, 255), 1, cv2.LINE_AA) # write text on the image

    cv2.imshow('LiveVideo', frameBGR) # shows the frame
    if cv2.waitKey(10) & 0xFF == ord('q'):
        # this checks to see if the letter 'q' is pressed... if so, it will break.
        # here is a link if you would like more info: https://stackoverflow.com/questions/57690899/how-cv2-waitkey1-0xff-ordq-works
        break
liveVideo.release() #release the hardware and software resources in use by the cv2.VideoCapture() function. 
# if not done... the camera will not be able to function upon another cv2.VideoCapture() call
cv2.destroyAllWindows() # destroy all the windows up atm..
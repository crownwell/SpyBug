import pyautogui, os, datetime

counter = 0
directory = "Image Folder"
imageFilePrefix = "Screenshot"
currentTime = datetime.datetime

# Create screenshot directory (if it doesn't exist)
def CreateDirectory():
  if not os.path.exists(directory):
      os.makedirs(directory)


# Entry point
if __name__ == '__main__':
  try:
    #create directory if missing
    CreateDirectory()

    while True:
      # Increase the image counter
      counter += 1

      # Take screenshot
      pic = pyautogui.screenshot()
      
      # Save the image
      pic.save("%s/%s-%s.png" % (directory, imageFilePrefix, str(currentTime.now()).replace(':', '').replace('.', '')) )

      print("Saved Screenshot %s" % counter)

  except Exception as e:
    print(e)
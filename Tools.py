
# ツールとしての関数


#数値として入力された文字列を数値として受け取る
def SafetyIntegerInput(explanation, minNum=0):
  inputNum = minNum-1
  while(True):
    inputNum = input(explanation)
    try:
      inputNum = int(inputNum)
    except:
      continue
    else:
      if(inputNum >= minNum):
        break

  return inputNum

def saveGif(savepath, dirpath, filename):
  imgs = [Image.open(imgPath) for imgPath in glob.glob(dirpath+"/*")]
  imgFirst = imgs.pop(0)
  imgFirst.save(savepath+"/"+filename, save_all=True, append_images=imgs, loop=0, duration=500)
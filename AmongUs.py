from bangtal import *
import threading

setGameOption(GameOption.ROOM_TITLE, False)
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

#res 1280*720
mainScene = Scene('','images/main.png')
inGame = Scene('','images/medi1.1.png')
end = Scene('','images/end.png')
currentScene = 0

Sound.play(Sound('sounds/maintheme.mp3'))

startButton = Object('images/startbutton.png')
startButton.locate(mainScene, 1000, 5)
startButton.setScale(0.3)
startButton.show()
def startButton_onMouseAction(x,y,action):
    global currentScene
    currentScene = 1
    startgame()
startButton.onMouseAction = startButton_onMouseAction

#=====Player Moves, Act
CyanX = 112
CyanY = 288
Cyan = Object('images/Cyan1.png')
Cyan.locate(inGame, CyanX, CyanY)
Cyan.setScale(4)
Cyan.show()

key = 0
def keyboard(k, pressed):
    global dir
    global pre
    global CyanMoving
    global key
    key = k
    if pressed:
        dir = key
        if (k==1 or k==4 or k==19 or k==23):
            CyanMoving = True
        else:
            CyanMoving = False
    else:
        dir = 0
        CyanMoving = False
inGame.onKeyboard = keyboard

CyanMoving = False
speed = 8
dir = 0
def CyanMove():
    global CyanX
    global CyanY
    global dir
    global speed
    global wallX
    global wallY
    if dir==4:
        if wallX != 1:
            CyanX+=speed
            Cyan.locate(inGame, CyanX, CyanY)
    elif dir==19:
        if wallY != -1:
            CyanY-=speed
            Cyan.locate(inGame, CyanX, CyanY)
    elif dir==1:
        if wallX != -1:
            CyanX-=speed
            Cyan.locate(inGame, CyanX, CyanY)
    elif dir ==23:
        if wallY != 1:
            CyanY+=speed
            Cyan.locate(inGame, CyanX, CyanY)

wallX = 0
wallY = 0
def Collision():
    global currentScene
    global CyanX
    global CyanY
    global wallX
    global wallY
    global door1Open
    if currentScene ==1:
        if (CyanX<80):
            wallX = -1
        elif (CyanX<=184 and CyanY>344):
            wallX = -1
        elif (CyanX>750):
            wallX = 1
        else:
            wallX = 0
        if (CyanY<40):
            wallY = -1
        elif (72<=CyanX<184 and CyanY>=344):
            wallY = 1
        elif (CyanY>400):
            wallY = 1
        else:
            wallY = 0
    elif currentScene ==2:
        if (CyanX<=272):
            wallX = -1
        elif (CyanX>824):
            wallX = 1
        else:
            wallX = 0
        if (CyanY<160):
            wallY = -1
        elif (CyanY>560):
            wallY = 1
        else:
            wallY = 0
    elif currentScene == 3:
        if (CyanY<200):
            if (CyanX<=288):
                wallX = -1
            elif (CyanX>=480):
                wallX = 1
            else:
                wallX = 0
        else:
            if (CyanX<40):
                wallX = -1
            elif (CyanX>950):
                wallX = 1
            else:
                wallX = 0
        if (288<=CyanX<=480):
            if (CyanY<40):
                wallY = -1
            elif (CyanY>=424):
                wallY = 1
            else:
                wallY = 0
        else:
            if (CyanY<208):
                wallY = -1
            elif (CyanY>=424):
                wallY = 1
            else:
                wallY = 0
    elif currentScene == 4:
        if (CyanX>1144):
            wallX = 1
        else:
            wallX = 0
        if (CyanY<=200):
            wallY = -1
        elif (CyanY>=424):
            wallY = 1
        else:
            wallY = 0
    elif currentScene == 5:
        if (CyanY >= 384):
            if (CyanX<352):
                wallX=-1
            elif (CyanX>=960):
                wallX=1
            else:
                wallX=0
        else:
            if (CyanX<=888):
                wallX=-1
            elif (CyanX>=960):
                wallX=1
            else:
                wallX=0
        if (CyanX >= 888):
            if (CyanY<=16):
                wallY=-1
            elif (CyanY>=496):
                wallY=1
            else:
                wallY=0
        else:
            if (CyanY<=388):
                wallY=-1
            elif (CyanY>=496):
                wallY=1
            else:
                wallY=0
    elif currentScene == 6:
        if (552<=CyanX<=704):
            if CyanY>480:
                wallY=1
            elif CyanY<=16:
                wallY=-1
            else:
                wallY=0
        else:
            if CyanY>480:
                wallY=1
            elif CyanY<=360:
                wallY=-1
            else:
                wallY=0
        if (CyanY>=360):
            if (CyanX<=144):
                wallX=-1
            elif (CyanX>=960):
                wallX=1
            else:
                wallX=0
        else:
            if (CyanX<=552):
                wallX=-1
            elif (CyanX>=704):
                wallX=1
            else:
                wallX=0
    elif currentScene == 7:
        if (CyanY<=360):
            if (CyanX<=280):
                wallX=-1
            elif (CyanX>=992):
                wallX=1
            else:
                wallX=0        
        else:
            if (CyanX<=552):
                wallX=-1
            elif (CyanX>=704):
                wallX=1
            else:
                wallX=0
        if (552<=CyanX<=704):
            if CyanY>576:
                wallY=1
            elif CyanY<=192:
                wallY=-1
            else:
                wallY=0
        else:
            if CyanY>=360:
                wallY=1
            elif CyanY<=192:
                wallY=-1
            else:
                wallY=0

CyanImageToggle = 1
CyanImageRight = 1            
def CyanAni():
    global CyanMoving
    global CyanImageToggle
    global CyanImageRight
    global isWall
    global dir
    if CyanMoving:
        if dir == 4:
            CyanImageRight = True
        elif dir == 1:
            CyanImageRight = False
        if CyanImageRight==1:
            if CyanImageToggle==1:
                Cyan.setImage('images/Cyan2.png')
                CyanImageToggle = 2
            elif CyanImageToggle==2:
                Cyan.setImage('images/Cyan1.png')
                CyanImageToggle = 1
        elif CyanImageRight==0:
            if CyanImageToggle==1:
                Cyan.setImage('images/Cyan2.1.png')
                CyanImageToggle = 2
            elif CyanImageToggle==2:
                Cyan.setImage('images/Cyan1.1.png')
                CyanImageToggle = 1
    else:
        if CyanImageRight==1:
            Cyan.setImage('images/Cyan1.png')
        elif CyanImageRight==0:
            Cyan.setImage('images/Cyan1.1.png')

def walkSound():
    global CyanMoving
    if CyanMoving:
        Sound.play(Sound('sounds/walk.mp3'))
    else:
        Sound.stop(Sound('sounds/walk.mp3'))

def showXY():
    global CyanX
    global CyanY
    print(CyanX, CyanY)

time = 0.0
def tick():
    global time
    timer = threading.Timer(0.01,tick)      #0.1초 주기
    time += 0.01
    timer.start()
    Collision()
    CyanMove()
    sceneChange()
    if (int(time*100)%5==0):                   #0.5초 주기
        CyanAni()
        walkSound()
        #showXY()

#=====Scene & Room 
def sceneChange():
    global currentScene
    global CyanX
    global CyanY
    global isLightOn
    global door1Open
    global door2Open
    global door3Open
    if currentScene==1:
        if (264<=CyanX<=552 and CyanY<=32):
            currentScene = 2
            CyanY = 496
            Cyan.locate(inGame, CyanX, CyanY)
            inGame.setImage('images/medi2.1.png')
            roomChanged(2)
        elif (264<=CyanX<=552 and CyanY>=400):
            if door1Open:
                currentScene = 3
                CyanY = 56
                Cyan.locate(inGame, CyanX, CyanY)
                inGame.setImage('images/hall1.jpg')
                roomChanged(3)
            else:
                CyanY=392
                Cyan.locate(inGame, CyanX, CyanY)
                showMessage("열리지 않는다...")
    elif currentScene==2:
        if (264<=CyanX<=552 and CyanY>=512):
            currentScene = 1            
            CyanY = 56
            Cyan.locate(inGame, CyanX, CyanY)
            if door1Open:
                inGame.setImage('images/medi1.2.png')
            else:                
                inGame.setImage('images/medi1.1.png')
            roomChanged(1)
    elif currentScene==3:
        if (280<=CyanX<=488 and CyanY<=32):
            currentScene = 1
            CyanY = 392
            Cyan.locate(inGame, CyanX, CyanY)
            inGame.setImage('images/medi1.2.png')
            roomChanged(1)
        elif (CyanX<=48):
            currentScene = 4
            CyanX = 1072
            Cyan.locate(inGame, CyanX, CyanY)
            if isLightOn:
                inGame.setImage('images/hall2.1.jpg')
            else:
                inGame.setImage('images/hall2.2.jpg')
            roomChanged(4)
        elif (CyanX>=952):
            CyanX = 944
            Cyan.locate(inGame, CyanX, CyanY)
            showMessage("열리지 않는다...")
    elif currentScene==4:
        if (CyanX>1128):
            currentScene = 3
            CyanX =56
            Cyan.locate(inGame, CyanX, CyanY)
            inGame.setImage('images/hall1.jpg')
            roomChanged(3)
        elif (CyanX<=8):
            if door2Open:
                currentScene = 5
                CyanX = 936
                Cyan.locate(inGame, CyanX, CyanY)
                inGame.setImage('images/upperengine1.png')
                roomChanged(5)
            else:
                CyanX = 16
                Cyan.locate(inGame, CyanX, CyanY)
                showMessage("열리지 않는다...")
    elif currentScene==5:
        if (200<=CyanY<=424):
            if CyanX >= 960:
                currentScene = 4
                CyanX = 88
                Cyan.locate(inGame, CyanX, CyanY)
                if isLightOn:
                    inGame.setImage('images/hall2.1.jpg')
                else:
                    inGame.setImage('images/hall2.2.jpg')
                roomChanged(4)
        elif (CyanY<=16):
            currentScene = 6
            CyanY = 480
            Cyan.locate(inGame, CyanX, CyanY)
            inGame.setImage('images/upperengine2.png')
            roomChanged(6)
    elif currentScene==6:
        if (888<=CyanX and CyanY>=480):
            currentScene = 5
            CyanY = 24
            Cyan.locate(inGame, CyanX, CyanY)
            inGame.setImage('images/upperengine1.png')
            roomChanged(5)
        elif CyanY<=16:
            currentScene = 7
            CyanY = 576
            Cyan.locate(inGame, CyanX, CyanY)
            if door3Open:
                inGame.setImage('images/hall3.2.png')
            else:
                inGame.setImage('images/hall3.1.png')
            roomChanged(7)
    elif currentScene == 7:
        if CyanY>576:
            currentScene = 6
            CyanY = 24
            Cyan.locate(inGame, CyanX, CyanY)
            inGame.setImage('images/upperengine2.png')
            roomChanged(6)
        if (CyanX>=992):
            CyanX = 984
            Cyan.locate(inGame, CyanX, CyanY)
            showMessage("열리지 않는다...")
        if (CyanX<=280):
            if not door3Open:
                CyanX = 288
                Cyan.locate(inGame, CyanX, CyanY)
                showMessage("열리지 않는다...")
            else:
                finishGame()

def roomChanged(room):
    global vent1Removed
    if room==1:
        lightButton1.show()
        medicom.hide()
        vent1.hide()
        cctv1.hide()
    elif room==2:
        lightButton1.hide()
        medicom.show()
        if vent1Removed:
            vent1.hide()
        else:
            vent1.show()
    elif room==3:
        bulb1.hide()
        bulb2.hide()
        bulb3.hide()
        bulb4.hide()
        lightButton1.hide()
        cctv1.show()
    elif room==4:
        bulb1.show()
        bulb2.show()
        bulb3.show()
        bulb4.show()
        cctv1.hide()
    elif room==5:
        bulb1.hide()
        bulb2.hide()
        bulb3.hide()
        bulb4.hide()
    elif room==6:
        cctv2.hide()
        lightButton2.hide()
    elif room==7:
        cctv2.show()
        lightButton2.show()
    Cyan.show()

#=====Doors, Objects
door1Open = False
door2Open = False
door3Open = False

medicom = Object('images/medicom.png')
medicom.locate(inGame, 940, 314)
medicom.setScale(1.1)
def medicom_onMouseAction(x,y,action):
    global CyanX
    global CyanY
    global door1Open
    global isLightOn
    if (CyanX>=824 and 272<CyanY<440):
        if (not door1Open):
            if isLightOn:
                Sound.play(Sound('sounds/dooropen.mp3'))
                door1Open=True
                showMessage("문을 열었다...")
            else:
                showMessage("화면이 잘 안보인다...")
medicom.onMouseAction = medicom_onMouseAction

lightButton1 = Object('images/lightbutton1.png')
lightButton1.locate(inGame, 90, 475)
isLightOn = False
def lightButton1_onMouseAction(x,y,action):
    global CyanX
    global CyanY
    global isLightOn
    if (CyanX<=184 and CyanY>=344):
        if isLightOn:
            isLightOn = False
            inGame.setLight(0.25)
        else:
            isLightOn = True
            inGame.setLight(1)
lightButton1.onMouseAction = lightButton1_onMouseAction

lightButton2 = Object('images/lightbutton2.png')
lightButton2.locate(inGame, 940, 512)
def lightButton2_onMouseAction(x,y,action):
    global CyanX
    global CyanY
    global isLightOn
    if (CyanX>=840 and CyanY>=360):
        if isLightOn:
            isLightOn = False
            inGame.setLight(0.25)
        else:
            isLightOn = True
            inGame.setLight(1)
lightButton2.onMouseAction = lightButton2_onMouseAction

vent1Removed = False
vent1 = Object('images/vent.png')
vent1.locate(inGame, 150, 440)
vent1.setScale(1.4)
def vent1_onMouseAction(x,y,action):
    global CyanX
    global CyanY
    global vent1Removed
    if (CyanX<=280 and 360<=CyanY<=480):
        if isLightOn:
            vent1Removed = True
            vent1.hide()
            Sound.play(Sound('sounds/vent.mp3'))
            showMessage('벤트를 치웠다...')
        else:
            showMessage('보이지 않아 치우기 어렵다...')
vent1.onMouseAction = vent1_onMouseAction

bulb1On = True
bulb1 = Object('images/bulbon.png')
bulb1.locate(inGame, 0, 570)
def bulb1_onMouseAction(x,y,action):
    global bulb1On
    if bulb1On:
        bulb1.setImage('images/bulboff.png')
        bulb1On=False
    else:
        bulb1.setImage('images/bulbon.png')
        bulb1On=True
    bulbCheck()
bulb1.onMouseAction = bulb1_onMouseAction

bulb2On = True
bulb2 = Object('images/bulbon.png')
bulb2.locate(inGame, 532, 570)
def bulb2_onMouseAction(x,y,action):
    global bulb2On
    if bulb2On:
        bulb2.setImage('images/bulboff.png')
        bulb2On=False
    else:
        bulb2.setImage('images/bulbon.png')
        bulb2On=True
    bulbCheck()
bulb2.onMouseAction = bulb2_onMouseAction

bulb3On = True
bulb3 = Object('images/bulbon.png')
bulb3.locate(inGame, 656, 570)
def bulb3_onMouseAction(x,y,action):
    global bulb3On
    if bulb3On:
        bulb3.setImage('images/bulboff.png')
        bulb3On=False
    else:
        bulb3.setImage('images/bulbon.png')
        bulb3On=True
    bulbCheck()
bulb3.onMouseAction = bulb3_onMouseAction

bulb4On = True
bulb4 = Object('images/bulbon.png')
bulb4.locate(inGame, 1196, 570)
def bulb4_onMouseAction(x,y,action):
    global bulb4On
    if bulb4On:
        bulb4.setImage('images/bulboff.png')
        bulb4On=False
    else:
        bulb4.setImage('images/bulbon.png')
        bulb4On=True
    bulbCheck()
bulb4.onMouseAction = bulb4_onMouseAction

def bulbCheck():
    global bulb1On
    global bulb2On
    global bulb3On
    global bulb4On
    global door2Open
    if not door2Open:
        if bulb1On and bulb4On:
            if not bulb2On:
                if not bulb3On:
                    showMessage("문이 열렸다...")
                    Sound.play(Sound('sounds/dooropen.mp3'))
                    door2Open=True

cctv1On = False
cctv1 = Object('images/cctv1off.png')
cctv1.locate(inGame, 872, 602)
def cctv1_onMouseAction(x,y,action):
    global CyanX
    global CyanY
    global isLightOn
    global cctv1On
    global cctv2On
    global door3Open
    if (808<=CyanX<=936 and CyanY>=424):
        if (not cctv1On):
            if isLightOn:
                cctv1On = True
                cctv1.setImage('images/cctv1on.png')
                if cctv2On:
                    showMessage("문이 열렸다...")
                    Sound.play(Sound('dooropen.mp3'))
                    door3Open=True
                else:
                    showMessage("CCTV를 켰다...")
            else:
                showMessage("어두워서 CCTV를 켤수가 없다...")
cctv1.onMouseAction = cctv1_onMouseAction

cctv2On = False
cctv2 = Object('images/cctv2off.png')
cctv2.locate(inGame, 482, 510)
def cctv2_onMouseAction(x,y,action):
    global CyanX
    global CyanY
    global isLightOn
    global cctv1On
    global cctv2On
    global door3Open
    if (400<=CyanX<=504 and 360<=CyanY):
        if (not cctv2On):
            if isLightOn:
                cctv2On = True
                cctv2.setImage('images/cctv2on.png')
                if cctv1On:
                    inGame.setImage('images/hall3.2.png')
                    Sound.play(Sound('sounds/dooropen.mp3'))
                    showMessage("문이 열렸다...")
                    door3Open=True
                else:
                    showMessage("CCTV를 켰다...")
            else:
                showMessage("어두워서 CCTV를 켤수가 없다...")
cctv2.onMouseAction = cctv2_onMouseAction

quit = Object('images/quit.png')
quit.locate(end, 580, 20)
def quit_onMouseAction(x,y,aciton):
    endGame()
quit.onMouseAction = quit_onMouseAction

#=====

def startgame():
    tick()
    inGame.enter()
    roomChanged(1)
    inGame.setLight(0.25)

def finishGame():
    global CyanMoving
    CyanMoving = False
    end.enter()
    quit.show()
    Sound.stop(Sound('sounds/maintheme.mp3'))
    Sound.play(Sound('sounds/victory.mp3'))

startGame(mainScene)
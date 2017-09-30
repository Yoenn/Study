;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("File Upload", "","Edit1")


; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",10)


; Set the File name text on the Edit field

  ControlSetText("File Upload", "", "Edit1", "C:\Users\oliverchan\Desktop\test1.png")

  Sleep(2000)

; Click on the Open button

  ControlClick("File Upload", "","Button1");
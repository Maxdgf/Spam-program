from colorama import *
import pyautogui
from pyautogui import *
import pyfiglet
import fontstyle
import time
import keyboard

class MyApp():
    def __init__(self):
        super().__init__()

        self.Fred = Fore.RED
        self.Fgreen = Fore.GREEN
        self.Fcyan = Fore.CYAN
        self.Fblue = Fore.BLUE
        self.Fblack = Fore.BLACK
        self.Fmagenta = Fore.MAGENTA
        self.Fyellow = Fore.YELLOW
        self.Fwhite = Fore.WHITE
        self.Freset = Fore.RESET
        self.Bred = Back.RED
        self.Bgreen = Back.GREEN
        self.Bcyan = Back.CYAN
        self.Bblue = Back.BLUE
        self.Bmagenta = Back.MAGENTA
        self.Byellow = Back.YELLOW
        self.Bwhite = Back.WHITE
        self.Bblack = Back.BLACK
        self.Breset = Back.RESET

        self.BOLD = '\033[1m'
        self.END = '\033[0m'

        self.mainScreen()
        while True:
            self.working_process()

    def mainScreen(self):
        self.MainText = "SPAM MONSTER"
        self.mainTextLogo = pyfiglet.figlet_format(text=self.MainText, font="slant")
        print(self.Fred + self.mainTextLogo + self.Freset)
        self.textDescriptionPattern = "--------[{SPAM ATACK PROGRAM}]--------"
        self.textDescription = fontstyle.apply(self.textDescriptionPattern, 'bold/red')
        print(f"{self.textDescription : ^80}")
        self.textDescriprion2Pattern = "---<VERSION 1.0>---"
        self.textDescriprion2 = fontstyle.apply(self.textDescriprion2Pattern, 'bold/red')
        print(f"{self.textDescriprion2 : ^80}")   
        self.textDescriprion1Pattern = "---<(MAIN SCREEN)>---"
        self.textDescriprion1 = fontstyle.apply(self.textDescriprion1Pattern, 'bold/red')
        print(f"{self.textDescriprion1 : ^80}")
        print("")
        self.textCommandsDescription = "|Commands:|"
        self.textCommandDescriptionStyle = fontstyle.apply(self.textCommandsDescription, 'bold/red')
        self.botDescription = self.Fcyan + "the connection with the telegram bot has been established" + self.Freset
        self.desc1 = self.Fmagenta + "!applicable to(command - i)!" + self.Freset + self.Fred
        self.desc2 = self.Fmagenta + "!applicable to(command - autoclicker)!" + self.Freset + self.Fred
        self.w = self.BOLD + "w" + self.END + self.Fred
        self.return1 = self.BOLD + "return" + self.END + self.Fred
        self.q = self.BOLD + "q" + self.END + self.Fred
        self.i = self.BOLD + "i" + self.END + self.Fred
        self.destroy = self.BOLD + "destroy" + self.END + self.Fred
        self.autoclicker = self.BOLD + "autoclicker" + self.END + self.Fred
        self.z = self.BOLD + "z" + self.END + self.Fred
        self.controlled_autoclicker = self.BOLD + "controlled_autoclicker" + self.END + self.Fred
        self.ic = self.BOLD + "ic" + self.END + self.Fred
        self.commandsDescription = self.textCommandDescriptionStyle + self.Fred + f"\n_________________________________________________________________________________\n{self.w} - start spam process\n{self.return1} - return to main screen\n{self.q} (Keyboard button 'Q') - stop spam process {self.desc1}\n{self.i} - infinity spam\n{self.destroy} - destroy action\n{self.autoclicker} - cursor autoclicker\n{self.z} (Keyboard button 'Z') - stop autoclicker {self.desc2}\n{self.controlled_autoclicker} - an autoclicker that is controlled by keystrokes\n{self.ic} - controlled infinity spam\n_________________________________________________________________________________" + self.Freset
        print(self.commandsDescription)
        print("")

    def destroy_action(self):
        print(self.Fred + "Your action was destroyed. I am teleporting you to main screen after 5 seconds." + self.Freset)
        self.timeData = 0
        for b in range(5, 0, -1):
            time.sleep(1)
            self.timeData += 1
            print(self.Fred + f"{b} seconds" + self.Freset)
            if self.timeData == 5:
                self.mainScreen()

    def working_process(self):
        self.strCommandText = "Enter command> "
        self.strCommandStyle = fontstyle.apply(self.strCommandText, "bold/red")
        self.commandField = input(self.strCommandStyle)

        if self.commandField == "return":
            self.home = self.mainScreen()
            self.home
        elif self.commandField == "w":
            try:
                print(self.Fred + "Ok, please, enter me message for spam." + self.Freset)
                self.MessageCommandText = "Enter spam message> "
                self.MessageCommandTextStyle = fontstyle.apply(self.MessageCommandText, "bold/red")
                self.messageCommandField = input(self.MessageCommandTextStyle)
                if self.messageCommandField == "destroy":
                    self.destroy_action()
                print(self.Fred + "Nice! please, enter me count of messages." + self.Freset)
                self.enterAmountText = "Enter count of spam messages> "
                self.AmountCommandStyle = fontstyle.apply(self.enterAmountText, "bold/red")
                self.amount = int(input(self.AmountCommandStyle))
                #if self.amount == 0:
                    #self.amount = 50
                pyautogui.click(x=100, y=100)
                pyautogui.mouseUp()
                for a in range(self.amount):
                    pass
                print(self.Fyellow + "WARNING: spam will be started after: " + self.Freset)
                self.timeCount = 10
                self.timer = 0
                for i in range(10, 0, -1):
                    time.sleep(1)
                    self.timer += 1
                    print(self.Fyellow + f"{i} seconds" + self.Freset)
                    if i == 0:
                        print(self.Fred + "Spam process started!" + self.Freset)
                if self.timer == 10:
                    print(self.Fred + f"Spam process was started. Messages count: {self.amount}" + self.Freset)
                    while self.amount > 0:
                        self.amount -= 1
                        pyautogui.typewrite(self.messageCommandField.strip())
                        pyautogui.press("enter")
                    print(self.Fred + "Spam process was ended." + self.Freset)
            except:
                print(self.Bred + self.Fwhite + "Operation failed! Please, check your values and try again." + self.Freset + self.Breset + self.commandField)         
        elif self.commandField == "destroy":
            self.destroy_action()
        elif self.commandField == "i":
            try:
                print(self.Fred + "Ok, please, enter me message for spam." + self.Freset)
                self.MessageCommandText = "Enter spam message> "
                self.MessageCommandTextStyle = fontstyle.apply(self.MessageCommandText, "bold/red")
                self.messageCommandField = input(self.MessageCommandTextStyle)
                if self.messageCommandField == "destroy":
                    self.destroy_action()
                print(self.Fyellow + "WARNING: Be careful! This is a infinity spam! Spam will be started after: " + self.Freset)
                self.timing = 0
                if len(self.messageCommandField) == 0:
                    self.messageCommandField = "I am a Spam Monster)"
                for g in range(5, 0, -1):
                    time.sleep(1)
                    self.timing += 1
                    print(self.Fyellow + f"{g} seconds" + self.Freset)
                    if g == 0:
                        print(self.Fred + "Infinity spam process started!" + self.Freset)
                if self.timing == 5:
                    print(self.Fred + "Spam process was started. Messages count: infinity" + self.Freset)
                    while True:
                        pyautogui.typewrite(self.messageCommandField.strip())
                        pyautogui.press("enter")
                        if keyboard.is_pressed("q"):
                            print(self.Fred + "Spam process was stoped." + self.Freset)
                            self.mainScreen()
                            break
            except:
                print(self.Bred + self.Fwhite + "Operation failed! Please, check your values and try again." + self.Freset + self.Breset + self.commandField)
        elif self.commandField == "autoclicker":
            try:
                print(self.Fred + "Ok, autoclicker activated." + self.Freset)
                self.screenData = pyautogui.size()
                self.cursorData = pyautogui.position()
                print(self.Fred + "Screen size: " + self.Freset)
                print(self.screenData)
                print(self.Fred + "Cursor position: " + self.Freset)
                print(self.cursorData)
                print(self.Fred + "Are you sure you want to activate the autoclicker? Please, enter answer(yes/no)" + self.Freset)
                self.ClickerCommandText = "Enter answer> "
                self.ClickerCommandTextStyle = fontstyle.apply(self.ClickerCommandText, "bold/red")
                self.AnswerField = input(self.ClickerCommandTextStyle)
                if self.AnswerField == "destroy":
                    self.destroy_action()
                if len(self.AnswerField) == 0:
                    print(self.Fred + "Why didn't you say anything?)" + self.Freset)
                if self.AnswerField == "yes":
                    print(self.Fyellow + "WARNING: cursor autoclicker was activated!" + self.Freset)
                    print(self.Fyellow + "Time to prepare!" + self.Freset)
                    self.timerData = 0
                    for t in range(10, 0, -1):
                        time.sleep(1)
                        self.timerData += 1
                        print(self.Fyellow + f"{t} seconds" + self.Freset)
                    if self.timerData == 0:
                        print(self.Fred + "Cursor autoclicker was started." + self.Freset)
                    if self.timerData == 10:
                        print(self.Fred + "Cursor autoclicker speed: fast" + self.Freset)
                        while True:
                            pyautogui.click()
                            if keyboard.is_pressed("z"):
                                print(self.Fred + "Cursor autoclicker was stoped." + self.Freset)
                                self.mainScreen()
                                break
                if self.AnswerField == "no":
                    print(self.Fred + "You were scared bro? I don't bite ;)" + self.Freset)
            except:
                print(self.Bred + self.Fwhite + "Operation failed! Please, try again." + self.Freset + self.Breset + self.commandField)
        elif self.commandField == "controlled_autoclicker":
            try:
                print(self.Fyellow + "WARNING! action was created, process started." + self.Freset)
                print(self.Fred + "Keyboard buttons:\n o - start autoclicker\n p - stop autoclicker\n b - exit" + self.Freset)
                while True:
                    if keyboard.is_pressed("o"):
                        while True:
                            pyautogui.click()
                            if keyboard.is_pressed("p"):
                                break
                    if keyboard.is_pressed("b"):
                        break
            except:
                print(self.Bred + self.Fwhite + "Operation failed! Please, try again." + self.Freset + self.Breset + self.commandField)
        elif self.commandField == "ic":
            try:
                self.ISpamCommandText = "Enter spam message> "
                self.ISpamCommandTextStyle = fontstyle.apply(self.ISpamCommandText, "bold/red")
                self.ISpamField = input(self.ISpamCommandTextStyle)
                if self.ISpamField == "destroy":
                    self.destroy_action()
                if len(self.ISpamField) == 0:
                    self.ISpamField = "I am a Spam Monster)"
                print(self.Fyellow + "WARNING! action was created, process started." + self.Freset)
                print(self.Fred + "Keyboard buttons:\n j - start spam\n k - stop spam\n n - exit" + self.Freset)
                pyautogui.click(x=100, y=100)
                pyautogui.mouseUp()
                while True:
                    if keyboard.is_pressed("j"):
                        while True:
                            pyautogui.typewrite(self.ISpamField)
                            pyautogui.press("enter")
                            if keyboard.is_pressed("k"):
                                break
                    if keyboard.is_pressed("n"):
                        break
            except:
                print(self.Bred + self.Fwhite + "Operation failed! Please, try again." + self.Freset + self.Breset + self.commandField)
        else:
            print(self.Bred + self.Fwhite + "Unknown command -> " + self.Freset + self.Breset + self.commandField)
if __name__ == "__main__":
    MyApp()

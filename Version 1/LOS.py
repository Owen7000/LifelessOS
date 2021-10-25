import time, sys, os, pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

class LOS:
    def __init__(self) -> None:
        pass
    class error_screen:
        def __init__(self, text_array):
            self.width = 500
            self.height = 500
            pygame.init()
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.black = (0,0,0)
            self.white = (255,255,255)
            self.red = (168, 50, 56)
            self.size = 25
            self.text = text_array
                

        def display(self):
            self.screen.fill(self.black)
            font = pygame.font.SysFont(None, self.size)
            pos_x = (self.width/2+75)
            pos_y = (self.height/2-65)
            for line in range(len(self.text)):
                text = (self.text[line])
                text_image = font.render(text, True, self.white)
                self.screen.blit(text_image, (pos_x, pos_y))
                pos_y = pos_y+20
            pygame.display.update()


    class boot:
        def __init__(self) -> None:
            self.ready_load = False
        def boot_anim(self):
            load_str = ("Please wait while the system loads all of the required data...")
            ls_len = len(load_str) 
            animation = "|/-\\"
            anicount = 0
            counttime = 0		
            i = 0	
            			

            while (self.ready_load != True): 
                time.sleep(0.1) 
                sys.stdout.write("\r"+ load_str + animation[anicount]) 
                sys.stdout.flush() 
                anicount = (anicount + 1)% 4
                i =(i + 1)% ls_len 
                counttime = counttime + 1
                #Only for debugging atm, will be removed later
                if counttime == 100:
                    self.ready_load = True
                #End of debug section
            
            # for windows 
            if os.name =="nt": 
                os.system("cls") 
                
            # for linux / Mac OS 
            else: 
                os.system("clear") 
            

            print("__      __         __   ___  ","\n"
                  "\ \    / /        /_ | / _ \ ","\n"
                  " \ \  / /__ _ __   | || | | |","\n"
                  "  \ \/ / _ \ '__|  | || | | |","\n"
                  "   \  /  __/ |     | || |_| |","\n"
                  "    \/ \___|_|     |_(_)___/ ")
                  
        def do_boot():
            boot = LOS.boot()
            boot.boot_anim()
    class login:
        def get_key():
            while True:
                event = pygame.event.poll()
                if event.type == pygame.KEYDOWN:
                    print ("Key:", event.key)
                    print ("Mode:", pygame.key.get_mods())
                    print ("Shift:", pygame.KMOD_SHIFT)
                    print ("Caps:", pygame.KMOD_CAPS)
                    return event.key
                else:
                    pass
        
        def display_box(screen, message):
            "Print a message in a box in the middle of the screen"
            fontobject = pygame.font.Font(None,18)
            pygame.draw.rect(screen, (0,0,0), ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10, 200,20), 0)
            pygame.draw.rect(screen, (255,255,255), ((screen.get_width() / 2) - 102, (screen.get_height() / 2) - 12, 204,24), 1)
            if len(message) != 0:
                screen.blit(fontobject.render(message, 1, (255,255,255)),((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
            pygame.display.flip()

        def ask(screen, question):
            "ask(screen, question) -> answer"
            pygame.font.init()
            current_string = []
            LOS.login.display_box(screen, question + ": " + "".join(current_string))
            while 1:
                inkey = LOS.login.get_key()
                if inkey == pygame.K_BACKSPACE:
                    current_string = current_string[0:-1]
                elif inkey == pygame.K_RETURN:
                    break
                elif inkey == pygame.K_MINUS:
                    current_string.append("_")
                elif inkey <= 127:
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT or  pygame.key.get_mods() & pygame.KMOD_CAPS: # if shift is pressed  or caps is on
                        current_string.append(chr(inkey).upper()) # make string uppercase
                    else:
                        current_string.append(chr(inkey)) # else input is lower
                        
                LOS.login.display_box(screen, question + ": " + "".join(current_string))
            return "".join(current_string)

        def do_login():
            disp_surf = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            print (LOS.login.ask(disp_surf, "Name") + " was entered")




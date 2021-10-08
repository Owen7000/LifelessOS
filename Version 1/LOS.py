import time, sys, os

class LOS:
    def __init__(self) -> None:
        pass
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
            
            # for windows OS 
            if os.name =="nt": 
                os.system("cls") 
                
            # for linux / Mac OS 
            else: 
                os.system("clear") 

        def do_boot():
            boot = LOS.boot()
            boot.boot_anim()


#LOS.boot.do_boot()
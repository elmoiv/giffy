from colorama import Fore, Style, init

# Colorama module's initialization.
init(autoreset=True)

class Printer:
    LOG = True
    
    def print_info(self, title, extra='', start='', end='\n'):
        if self.LOG:
            print(start +
            Style.BRIGHT +
            Fore.WHITE   + "["  +
            Fore.GREEN   + "+"  +
            Fore.WHITE   + "] " +
            Fore.GREEN   + title.ljust(15) +
            Fore.YELLOW  + extra,
            end=end)

    def print_error(self, title, extra='', start='', end='\n'):
        if self.LOG:
            print(start +
            Style.BRIGHT +
            Fore.WHITE   + "["  +
            Fore.RED     + "-"  +
            Fore.WHITE   + "] " +
            Fore.RED     + title.ljust(15) +
            Fore.YELLOW  + extra,
            end=end)

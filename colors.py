from colorama import Fore, Style, init

# Colorama module's initialization.
init(autoreset=True)

def print_info(title, extra=''):
    print(
        Style.BRIGHT +
        Fore.WHITE + "[" +
        Fore.GREEN + "+" +
        Fore.WHITE + "] " +
        Fore.GREEN + title +
        Fore.YELLOW + extra
           )

def print_error(title, extra=''):
    print(
        Style.BRIGHT +
        Fore.WHITE + "[" +
        Fore.RED + "+" +
        Fore.WHITE + "] " +
        Fore.RED + title +
        Fore.YELLOW + extra
           )
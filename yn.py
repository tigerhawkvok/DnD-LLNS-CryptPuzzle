class _yn:
    """Give a prompt for [Y/N] and returns the appropriate boolean"""
    def __init__(self):
        try:
            import getch
        except ImportError:
            print("This package requires getch to function. Be sure it's in the load path!")
        
    def __call__(self,string=None):
        return self.yn_input(string)

    def yn_input(self,string=None):
        if string is not None:
            try:
                print(string+" [Y/N]")
            except TypeError:
                pass
        import getch
        a = getch.getch()
        a = a.lower()
        b = a.encode('utf-8')
        while b is not "y".encode('utf-8') and b is not "n".encode('utf-8'):
            print("Please enter 'Y' or 'N'.")
            a = getch.getch()
            a = a.lower()
            b = a.encode('utf-8')
        return b is "y".encode('utf-8')
yn = _yn()

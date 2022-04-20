polled_list = {'petter': "python",
             'erik': 'c',
             'kurt': 'c#',
             'bengan': 'ruby'
             } #dictionary med folk som svarat och vad de svarat

todo = ["petter", 'erik', 'kurt', 'bengan', 'bertil', 'britt', 'berit', 'birgitta', 'birgit', 'arne', 'cesar'] #lista med folk

for name in sorted(todo): # varje post i listan i alfabetisk ordning
    if name in polled_list: # om namnet finns på polled_list
        print(f"Thank you, {name.title()}, for responding!") # printas ett tack
    else: # finns det inte på polled_list
        print(f"Hi {name.title()}! Please take our poll!") # så printas en uppmaning att göra undersökningen
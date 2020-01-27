from django.http import HttpResponse

def funkcja_widoku(request, name):
    html = f"""<!doctype html>
    <html>
    <head></head>
    <body>
    Hello {name} !
    </body>
    </html>"""
    return HttpResponse(html)

def funkcja_sumy(request, a, b):
    html = f"""<!doctype html>
    <html>
    <head></head>
    <body>
    Suma {a} + {b} = {int(a)+int(b)}
    </body>
    </html>"""
    return HttpResponse(html)

def funkcja_mnozenia(request, a, b):
    html = f"""<!doctype html>
    <html>
    <head></head>
    <body>
    Iloczyn {a} x {b} = {int(a) * int(b)}
    </body>
    </html>"""
    return HttpResponse(html)

# zrobić kalkulator
# sum/1/2
# mul/2/4
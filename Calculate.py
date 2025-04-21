import flet

def main(page: flet.Page):
    page.window.width = 346
    page.window.height = 526
    page.window.resizable = False
    page.title = 'Калькулятор'
    page.theme_mode = 'dark'
    
    text = flet.Text('', size=50)
    his_text = None
    
    def num(e):
        if e.control.data == 'C':
            text.value = ''
        elif e.control.data == 'X':
            if text.value:
                text.value = text.value[:-1]
        elif e.control.data == '=':
            try:
                result = eval(text.value)
                if result:
                    his8.text = his7.text
                    his7.text = his6.text
                    his6.text = his5.text
                    his5.text = his4.text
                    his4.text = his3.text
                    his3.text = his2.text
                    his2.text = his1.text
                    his1.text = f'{text.value} = {round(result, 6)}'
                else:
                    his1.text = f'{text.value} = {round(result, 6)}'
                text.value = str(result)
            except (SyntaxError, ZeroDivisionError, NameError):
                text.value = "Ошибка"
        else:
            text.value += str(e.control.data)
        page.update()
        
    
    def navi_to_his(e):
        page.clean()
        page.add(panel_history)
        
    def navi_to_calcul(e):
        page.clean()
        page.add(calculate)
        
    def change_theme(e):
        if page.theme_mode == 'dark':
            page.theme_mode = 'light'
            flet.ButtonStyle(color=flet.Colors.WHITE)
            page.update()
        else:
            page.theme_mode = 'dark'
            page.update()
            
    def return_his(e):
        text.value = e.control.text.split('=')[0].strip()
        page.update()
        navi_to_calcul(None)
        

    but_style = flet.ButtonStyle(text_style=flet.TextStyle(size=30), shape=flet.RoundedRectangleBorder(radius=10))
    
    clear = flet.FilledButton(text='C', width=70, height=50, on_click=num, data='C', style=but_style)
    delete = flet.FilledButton(text='X', width=70, height=50, on_click=num, data='X', style=but_style)
    share = flet.FilledButton(text='/', width=70, height=50, on_click=num, data='/', style=but_style)
    multiply = flet.FilledButton(text='*', width=70, height=50, on_click=num, data='*', style=but_style)
    seven = flet.FilledButton(text='7', width=70, height=70, on_click=num, data='7', style=but_style)
    eight = flet.FilledButton(text='8', width=70, height=70, on_click=num, data='8', style=but_style)
    nine = flet.FilledButton(text='9', width=70, height=70, on_click=num, data='9', style=but_style)
    plus = flet.FilledButton(text='+', width=70, height=70, on_click=num, data='+', style=but_style)
    four = flet.FilledButton(text='4', width=70, height=70, on_click=num, data='4', style=but_style)
    five = flet.FilledButton(text='5', width=70, height=70, on_click=num, data='5', style=but_style)
    six = flet.FilledButton(text='6', width=70, height=70, on_click=num, data='6', style=but_style)
    minus = flet.FilledButton(text='-', width=70, height=70, on_click=num, data='-', style=but_style)
    one = flet.FilledButton(text='1', width=70, height=70, on_click=num, data=1, style=but_style)
    two = flet.FilledButton(text='2', width=70, height=70, on_click=num, data=2, style=but_style)
    three = flet.FilledButton(text='3', width=70, height=70, on_click=num, data=3, style=but_style)
    equally = flet.FilledButton(text='=', width=70, height=70, on_click=num, data='=', style=but_style)
    zero = flet.Button(text='0', width=150, height=40, on_click=num, data='0', bgcolor='primary', color='onPrimary', style=but_style)
    comma = flet.Button(text=',', width=150, height=40, on_click=num, data='.', bgcolor='primary', color='onPrimary', style=but_style)
    icon_history = flet.IconButton(flet.icons.HISTORY, on_click=navi_to_his, tooltip='Открыть историю')
    icon_caluclate = flet.IconButton(flet.icons.CALCULATE,on_click=navi_to_calcul, tooltip='Открыть калькулятор')
    icon_theme = flet.IconButton(flet.icons.SUNNY,on_click=change_theme, tooltip='Сменить тему')
    
    
    text_style = flet.ButtonStyle(text_style=flet.TextStyle(size=30))
    
    his1 = flet.TextButton('', style=text_style, on_click=return_his, data=text)
    his2 = flet.TextButton('', style=text_style, on_click=return_his, data=text)
    his3 = flet.TextButton('', style=text_style, on_click=return_his, data=text)
    his4 = flet.TextButton('', style=text_style, on_click=return_his, data=text)
    his5 = flet.TextButton('', style=text_style, on_click=return_his, data=text)
    his6 = flet.TextButton('', style=text_style, on_click=return_his, data=text)
    his7 = flet.TextButton('', style=text_style, on_click=return_his, data=text)
    his8 = flet.TextButton('', style=text_style, on_click=return_his, data=text)
    
    panel_history = flet.Column(
        [
            flet.Row([icon_caluclate, icon_theme, flet.Text('История решений', style=flet.TextStyle(size=20), tooltip='История округляется до 6 знаков после запятой')]),
            his1,
            his2,
            his3,
            his4,
            his5,
            his6,
            his7,
            his8
        ], alignment=flet.VerticalAlignment.START,
        scroll=flet.ScrollMode.AUTO, height=500
    )
    
    calculate = flet.Column(
        [
            flet.Row([icon_history, icon_theme]),
            flet.Row([text]),
            flet.Row([clear, delete, share, multiply]),
            flet.Row([seven, eight, nine, plus]),
            flet.Row([four, five, six, minus]),
            flet.Row([one, two, three, equally]),
            flet.Row([zero, comma])
        ], alignment=flet.VerticalAlignment.END
    )
    
    page.add(calculate)
    
if __name__ == "__main__":
    flet.app(target=main)
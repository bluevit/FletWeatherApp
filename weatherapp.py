#importing necessary libraries
import flet as ft
import requests

#open weather api key
api_key = 'aa1b91c25c2fda07a75a412d518cff91'

#getting location and its weather situation
def location(user_input,api_key):
    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    temp = round((temp-32)*5/9)

    return weather,temp

#main page for app
#below there are comments statements which you can uncomment to see the alignments of containers
def main(page: ft.Page):
    page.fonts = {"Bebas Neue": "/fonts/BebasNeue-Regular.ttf"}
    page.theme = ft.Theme(font_family="Bebas Neue")
    page.title = 'testing Get_Weather'
    page.window_max_width = 400
    page.window_max_height = 700
    page.bgcolor ='#9a9a9a'
    
    #getting the text in textbox
    def textbox_changed(e):
        t.value = e.control.value
        f.value = location(t.value,api_key)
        page.update()

    t= ft.Text()
    f = ft.Text(size = 20)
    
    #widgets used in app
    a= ft.Icon(name=ft.icons.LOCATION_ON_OUTLINED, color=ft.colors.WHITE)
    b= ft.TextField(border_color = 'transparent',width = 250,cursor_color= 'transparent',on_submit = textbox_changed, text_size = 50, text_align = 'center')

    #defining a function which contians list of widgets to be displayed on page
    def items():
        items = []
        items.append(
            ft.Container(
                content = ft.Row(
                    
                            [
                               a,
                               b,
                            ],
                            spacing = 0,
                ),
                alignment = ft.alignment.center,
                width = 250,
                height = 50,
                #bgcolor = 'red',

            )
        )
        items.append( ft.Container(
                    content=ft.Lottie(
                                    src='https://lottie.host/9d64d30b-e99d-4372-9884-dcf70114ee92/D8Xb7lHozn.json',
                                    repeat=True,
                                    reverse=False,
                                    animate=True     ),
                    alignment=ft.alignment.center,
                    width=250,
                    height=270,
                    #bgcolor=ft.colors.AMBER_500,
                )
        )
        items.append(
            ft.Container(
                content = f,
                alignment = ft.alignment.center,
                width=250,
                height=50,
            )
        )
        return items

    #main axis for page
    def column_with_alignment(align: ft.MainAxisAlignment):
        return ft.Column(
            [
                ft.Container(
                    content=ft.Column(items(), alignment=align),
                    height=650,
                ),
            ]
        )
    page.add(
        ft.Row(
            [column_with_alignment(ft.MainAxisAlignment.CENTER),],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
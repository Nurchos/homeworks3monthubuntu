import flet as ft

def main(page: ft.Page):
    page.title = "Счётчик"

    count = 0

    text_hello = ft.Text("Нажато: 0 раз")

    def button_click(e):
        nonlocal count
        count += 1
        text_hello.value = f"Нажато: {count} раз"
        page.update()

    button = ft.ElevatedButton(
        text="Нажми меня",
        on_click=button_click
    )

    page.add(text_hello, button)

ft.app(target=main)

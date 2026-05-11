import flet as ft

def main(page: ft.Page):
    txt = ft.Text("Нажато: 0")

    counter = 0

    def click(e):
        nonlocal counter
        counter += 1
        txt.value = f"Нажато: {counter}"
        page.update()

    page.add(
        txt,
        ft.ElevatedButton(
            "Нажми",
            on_click=click
        )
    )

ft.app(target=main)


import flet as ft

def main(page: ft.Page):
    page.title = "Проверка возраста"

    input_age = ft.TextField(label="Введите возраст")

    result = ft.Text("")

    def check_age(e):
        age = input_age.value

        if age.isdigit():
            age = int(age)

            if age >= 18:
                result.value = "Доступ разрешен"
                result.color = "green"

            else:
                result.value = "Доступ запрещен"
                result.color = "red"

        else:
            result.value = "Введите корректный возраст"
            result.color = "yellow"

        page.update()

    button = ft.ElevatedButton(
        text="Проверить",
        on_click=check_age
    )

    page.add(
        input_age,
        button,
        result
    )

ft.app(target=main)

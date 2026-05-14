import flet as ft

greeting_history = []


def main(page: ft.Page):
    page.title = "История имен"
    page.theme_mode = ft.ThemeMode.LIGHT

    name_input = ft.TextField(label="Введите имя")
    result_text = ft.Text("", size=20)

    history_column = ft.Column()

    def update_history():
        history_column.controls.clear()

        for name in greeting_history:
            history_column.controls.append(
                ft.Text(name, size=18)
            )

        page.update()

    def add_name(e):
        name = name_input.value.strip()

        if len(name) < 2:
            result_text.value = "Имя слишком короткое!"
            result_text.color = "red"

        elif name.isdigit():
            result_text.value = "Имя не может состоять из цифр!"
            result_text.color = "red"

        elif name in greeting_history:
            result_text.value = "Это имя уже в истории!"
            result_text.color = "red"

        else:
            result_text.value = f"Привет, {name}!"
            result_text.color = "green"

            greeting_history.insert(0, name)

            if len(greeting_history) > 5:
                greeting_history.pop()

            update_history()

        name_input.value = ""
        page.update()

    def clear_history(e):
        greeting_history.clear()
        update_history()

        result_text.value = "История очищена!"
        result_text.color = "blue"

        page.update()

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    top_buttons = ft.Row(
        controls=[
            ft.ElevatedButton(
                "Сменить тему",
                on_click=change_theme
            ),
            ft.ElevatedButton(
                "Очистить историю",
                on_click=clear_history
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        ft.Column(
            controls=[
                top_buttons,
                name_input,
                ft.ElevatedButton(
                    "Добавить имя",
                    on_click=add_name
                ),
                result_text,
                ft.Text("История:", size=22),
                history_column
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


ft.app(target=main)

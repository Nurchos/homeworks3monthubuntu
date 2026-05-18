import flet as ft

greeting_history = []


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "auto"

    count = 0

    counter_text = ft.Text("Нажато: 0 раз")

    def increment(e):
        nonlocal count
        count += 1
        counter_text.value = f"Нажато: {count} раз"
        page.update()

    counter_button = ft.ElevatedButton(
        "Нажми меня",
        on_click=increment
    )

    age_input = ft.TextField(
        label="Введите возраст"
    )

    age_result = ft.Text()

    def check_age(e):
        age = age_input.value

        if age.isdigit():
            age = int(age)

            if age >= 18:
                age_result.value = "Доступ разрешен"
                age_result.color = "green"

            else:
                age_result.value = "Доступ запрещен"
                age_result.color = "red"

        else:
            age_result.value = "Введите число"
            age_result.color = "orange"

        page.update()

    age_button = ft.ElevatedButton(
        "Проверить",
        on_click=check_age
    )

    history_column = ft.Column()

    name_input = ft.TextField(
        label="Введите имя"
    )

    result_text = ft.Text()

    def load_history():
        history_column.controls.clear()

        for name in greeting_history:
            history_column.controls.append(
                ft.Text(name)
            )

        page.update()

    def add_name(e):
        name = name_input.value.strip()

        if len(name) < 2:
            result_text.value = "Имя слишком короткое"
            result_text.color = "red"

        elif name.isdigit():
            result_text.value = "Имя не может быть цифрами"
            result_text.color = "red"

        elif name in greeting_history:
            result_text.value = "Имя уже есть"
            result_text.color = "red"

        else:
            greeting_history.insert(0, name)

            if len(greeting_history) > 5:
                greeting_history.pop()

            result_text.value = f"Привет, {name}!"
            result_text.color = "green"

            load_history()

        name_input.value = ""
        page.update()

    def clear_history(e):
        greeting_history.clear()

        load_history()

        result_text.value = "История очищена"
        result_text.color = "blue"

        page.update()

    add_button = ft.ElevatedButton(
        "Добавить",
        on_click=add_name
    )

    clear_button = ft.ElevatedButton(
        "Очистить",
        on_click=clear_history
    )

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK

        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    theme_button = ft.ElevatedButton(
        "Сменить тему",
        on_click=change_theme
    )

    page.add(
        ft.Text("Счётчик", size=25),
        counter_text,
        counter_button,

        ft.Divider(),

        ft.Text("Проверка возраста", size=25),
        age_input,
        age_button,
        age_result,

        ft.Divider(),

        ft.Text("История имен", size=25),
        name_input,

        ft.Row([
            add_button,
            clear_button
        ]),

        result_text,

        ft.Text("История:"),

        history_column,

        ft.Divider(),

        theme_button
    )


ft.app(target=main)
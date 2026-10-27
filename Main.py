import flet as ft


def main(page: ft.Page):
    name = ""
    name_field = ft.TextField(label="Your name")

    async def on_continue_click(e):
        nonlocal name
        name = name_field.value.strip()

        if not name:
            dialog = ft.AlertDialog(
                title=ft.Text("Name required"),
                content=ft.Text("Please enter your name before continuing."),
                actions=[ft.TextButton("OK", on_click=lambda e: page.close_dialog())],
            )
            page.show_dialog(dialog)
            return

        await page.push_route("/greeting")

    def on_route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        ft.Text("Welcome!"),
                        name_field,
                        ft.ElevatedButton("Continue", on_click=on_continue_click),
                    ],
                )
            )
        elif page.route == "/greeting":
            page.views.append(
                ft.View(
                    "/greeting",
                    controls=[
                        ft.Text(f"Hello, {name}!"),
                        ft.ElevatedButton("Back", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        page.update()

    page.on_route_change = on_route_change
    page.go("/")


ft.run(main)

import flet as ft

def loginView(page, auth_controller):
    email_input = ft.TextField(label="correo electronico", width=350, border_radius=10)
    pass_input = ft.TextField(label="contraseña", password=True, can_reveal_password=True, width=350, border_radius=10)

    def login_click(e):
        user, msg = auth_controller.login(email_input.valor, pass_input.value)
        if user:
            page.session.net("user", user)
            page.go("dashboard")
        else:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.Snack_bar.open = True
            page.update()
    
    return ft.View("/", [
        ft.AppBar(title=ft.Text("SIGE = "))
    ])
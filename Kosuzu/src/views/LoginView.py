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
    
    #return ft.View("/", [
    #    ft.AppBar(title=ft.Text("SIGE - Login"), bgcolor=ft.Colors.BLUE_GREY_900, color="white"),
    #    ft.Column([
    #        ft.Icon(ft.Icons.LOCK_PERSON, size=50, color=ft.Colors.BLUE),
    #        ft.Text("Acceso al sistema", size=24, weight="bold"),
    #        email_input,
    #        pass_input,
    #        ft.Button("Entrar", on_click=login_click, width=150),
    #        ft.TextButton("crear una cuenta nueva", on_click=lambda_: page.go("/reguistro"))
    #    ], horizontal_alignment = ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
    #])
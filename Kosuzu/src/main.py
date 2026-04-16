import flet as ft
from Kosuzu.src.controllers.UserController import AuthController
from Kosuzu.src.controllers.TareaController import TareaController
from Kosuzu.src.views.LoginView import LoginView
from Kosuzu.src.views.dashboard import DashboardView

def start(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
        
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: ruta no encontrada o vista vacia")])
            )
        page.update()

    page.on_route_change = route_change
    page.go("/")
    
def main():
    ft.app(target=start)

if __name__ == "__main__":
    (main)



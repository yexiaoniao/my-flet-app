import flet as ft


def main(page: ft.Page):
    page.title = "我的 Flet 应用"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 24
    page.add(
        ft.Text("APK 云端打包测试成功！", size=24, weight=ft.FontWeight.BOLD),
        ft.Text("这是一个最小 Flet 示例。你可以把自己的界面代码放到 main.py。"),
        ft.Button(
            "点击测试",
            on_click=lambda e: page.add(ft.Text("按钮运行正常")),
        ),
    )


ft.run(main)

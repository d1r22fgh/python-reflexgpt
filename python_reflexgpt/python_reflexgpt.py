"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from . import ui, pages, navigation

class State(rx.State):
    """The app state."""

    ...

app = rx.App()
app.add_page(pages.home_page, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_us_page, route=navigation.routes.ABOUT_US_ROUTE)

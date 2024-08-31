"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from python_reflexgpt import ui
    
def about_us_page() -> rx.Component:
    """Abou_oo/t Us"""
    return ui.base_layout(
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex GPT!", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


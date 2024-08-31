import reflex as rx

from . import routes

class NavState(rx.State):
    def to_home(self):
        """on click"""
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_about_us(self):
        """on click"""
        return rx.redirect(routes.ABOUT_US_ROUTE)
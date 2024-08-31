import reflex as rx

from .state import ChatState

def chat_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.text_area(
                name="user_input",
                placeholder="Your message",
                required=True,
                width="100%"
            ),
            rx.hstack(
                rx.button("Submit", type="Submit"),
                rx.cond(
                    ChatState.did_submit,
                    rx.text("Success"),
                    rx.fragment(),
                )
                
            )
            
        ),
        on_submit=ChatState.handle_submit,
        reset_on_submit=True,
    )
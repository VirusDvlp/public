from .resending_messages import register_resend_message_handlers


def register_all_handlers(dp) -> None:
    register_resend_message_handlers(dp)

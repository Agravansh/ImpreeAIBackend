from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler
from django.conf import settings

from telegram_bot_app.models import User, Button, ButtonCall

def start(update, context):
    user = User.objects.get_or_create(telegram_id=update.effective_user.id)[0]

    button_list = [
        InlineKeyboardButton("Stupid", callback_data='stupid'),
        InlineKeyboardButton("Fat", callback_data='fat'),
        InlineKeyboardButton("Dumb", callback_data='dumb'),
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))

    update.message.reply_text('Please choose a button:', reply_markup=reply_markup)

def button_callback(update, context):
    query = update.callback_query
    button_name = query.data

    button, _ = Button.objects.get_or_create(name=button_name)
    user = User.objects.get(telegram_id=query.from_user.id)

    button_call, _ = ButtonCall.objects.get_or_create(user=user, button=button)
    button_call.count += 1
    button_call.save()

    query.answer()
    query.edit_message_text(text=f"You clicked the {button_name} button.")

def build_menu(buttons, n_cols):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    return menu

def main():
    updater = Updater(token=settings.6220865407:AAFJiOTRZAGAnKfZQq6IkdFk32WbjXuTrXI, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CallbackQueryHandler(button_callback))
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

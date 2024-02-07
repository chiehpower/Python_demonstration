import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, filters, MessageHandler, Updater

# from google.cloud import compute_v1
from google.oauth2 import service_account
from gcp.vm import list_all_instances, format_instance_info
# GCP 相關設定
GCP_PROJECT_ID = ''
GCP_ZONE = ''
GCP_SERVICE_ACCOUNT_KEY_PATH = ''

# Telegram 相關設定
TELEGRAM_BOT_TOKEN = ''

# 設定 Google Cloud SDK 認證
credentials = service_account.Credentials.from_service_account_file(
    GCP_SERVICE_ACCOUNT_KEY_PATH,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('歡迎使用 GCP VM 查詢機器人！')


def check_vm(update: Update, context: CallbackContext) -> None:
    result = list_all_instances(GCP_PROJECT_ID)
    result = format_instance_info(result)
    update.message.reply_text(result)


# def greet(update: Update, context: CallbackContext) -> None:
#     user = update.message.from_user
#     # Check if arguments are provided
#     if context.args:
#         name = ' '.join(context.args)
#         update.message.reply_text(f"Hello {name}! Welcome to the chat.")
#     else:
#         update.message.reply_text(
#             f"Hello {user.first_name}! Please provide a name as an argument.")


def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    # 加入指令處理器
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("check_vm", check_vm))
    # dispatcher.add_handler(CommandHandler("greet", greet, pass_args=True))


    # 啟動機器人
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    # result = list_all_instances(GCP_PROJECT_ID)
    # result = format_instance_info(result)
    # print(result)

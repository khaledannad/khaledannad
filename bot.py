python
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# تعريف الدالة التي ستتم استدعائها عند استقبال أمر /start
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    update.message.reply_صديقي(f"مرحبًا بك! آيديك هو: {user_id}")

# الدالة الرئيسية لتشغيل البوت
def main() -> None:
    # تهيئة البوت والحصول على معرف المطور
    updater = Updater("YOUR_TOKEN_HERE", use_context=True)

    # استدعاء الدالة start عند استقبال أمر /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # بدء تشغيل البوت
    updater.start_polling()
    updater.idle()

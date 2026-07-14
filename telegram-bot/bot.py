"""
BODRUM ELITE — Telegram Concierge Bot
=====================================
Автоматический консьерж-бот для обработки входящих запросов.

Запуск: python bot.py
Требования: pip install python-telegram-bot==20.7
"""

import os
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

# ── Config ──
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8631842799:AAFTPBQw8bLhVNr0bXiBF59dBEckZOQePU4")
ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID", "6876584793")  # Your personal Telegram chat ID

# ── Logging ──
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ══════════════════════════════════════════════════
# SERVICE CATALOG
# ══════════════════════════════════════════════════

SERVICES = {
    "transfer": {
        "emoji": "🚗",
        "title": "Прибытие и Трансфер",
        "desc": (
            "🚗 *Прибытие и Трансфер*\n\n"
            "• VIP-встреча в аэропорту Бодрум-Миляс\n"
            "• Mercedes S-Class / V-Class / Sprinter\n"
            "• Холодные напитки и WiFi в авто\n"
            "• Полное сопровождение до виллы/отеля\n\n"
            "💰 от $80 (в одну сторону)\n\n"
            "Напишите дату прилёта и количество гостей — "
            "мы подберём идеальный вариант!"
        ),
    },
    "villa": {
        "emoji": "🏡",
        "title": "Виллы и Проживание",
        "desc": (
            "🏡 *Виллы и Проживание*\n\n"
            "• Эксклюзивные виллы с видом на Эгейское море\n"
            "• Частные резиденции с бассейном\n"
            "• Бутик-отели категории 5⭐\n"
            "• Проверенные объекты, только для наших клиентов\n\n"
            "💰 от $300/ночь\n\n"
            "Укажите даты, количество гостей и пожелания — "
            "мы подготовим подборку за 2 часа!"
        ),
    },
    "dining": {
        "emoji": "🍽",
        "title": "Рестораны и Гастрономия",
        "desc": (
            "🍽 *Рестораны и Гастрономия*\n\n"
            "• Лучшие столики в топ-ресторанах Бодрума\n"
            "• Закрытые дегустации и винные вечера\n"
            "• Шеф-повар на дом (на вилле/яхте)\n"
            "• Кулинарные туры по побережью\n\n"
            "Расскажите о ваших предпочтениях — "
            "мы забронируем идеальный вечер!"
        ),
    },
    "beach": {
        "emoji": "🏖",
        "title": "Пляжные Клубы",
        "desc": (
            "🏖 *Пляжные Клубы*\n\n"
            "• VIP-зоны в лучших клубах побережья\n"
            "• Макалонас, Бирлик, Голтюркбюкю\n"
            "• Без очередей, без отказов\n"
            "• Премиум-бронирование лежаков и кабан\n\n"
            "Укажите дату и количество гостей — "
            "всё будет готово к вашему приезду!"
        ),
    },
    "yacht": {
        "emoji": "🛥",
        "title": "Частные Яхты",
        "desc": (
            "🛥 *Частные Яхты*\n\n"
            "• Моторные и парусные яхты от 12 до 50 метров\n"
            "• Профессиональная команда\n"
            "• Маршрут по вашим желаниям\n"
            "• Кейтеринг, DJ, водные виды спорта\n\n"
            "💰 от $1,500/день\n\n"
            "Напишите желаемые даты и количество гостей — "
            "мы подберём идеальную яхту!"
        ),
    },
    "nightlife": {
        "emoji": "🌙",
        "title": "Ночная Жизнь",
        "desc": (
            "🌙 *Ночная Жизнь*\n\n"
            "• Закрытые вечеринки и VIP-столы\n"
            "• Лучшие клубы Бодрума и Ялыкавака\n"
            "• Приватные мероприятия на виллах\n"
            "• Организация дней рождения и праздников\n\n"
            "Расскажите, что хотите — мы организуем "
            "незабываемый вечер!"
        ),
    },
    "assistant": {
        "emoji": "👤",
        "title": "Личный Ассистент",
        "desc": (
            "👤 *Личный Ассистент 24/7*\n\n"
            "• Русскоговорящий помощник на месте\n"
            "• Решение любых вопросов: от покупок до медицины\n"
            "• Сопровождение на встречах и мероприятиях\n"
            "• Переводчик и гид в одном лице\n\n"
            "💰 от $200/день\n\n"
            "Напишите даты вашего визита — "
            "мы назначим персонального ассистента!"
        ),
    },
    "jet": {
        "emoji": "✈️",
        "title": "Частная Авиация",
        "desc": (
            "✈️ *Частная Авиация*\n\n"
            "• Бизнес-джеты из любой точки мира\n"
            "• Организация от двери до двери\n"
            "• Вертолётные трансферы по побережью\n"
            "• VIP-терминал без очередей\n\n"
            "Укажите маршрут и даты — "
            "мы подготовим предложение!"
        ),
    },
}


# ══════════════════════════════════════════════════
# HANDLERS
# ══════════════════════════════════════════════════

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message with main menu."""
    user = update.effective_user
    welcome_text = (
        f"Добро пожаловать, {user.first_name}! 🌟\n\n"
        "Я — виртуальный консьерж *Bodrum Elite*.\n\n"
        "Мы предоставляем эксклюзивный сервис в Бодруме "
        "для самых взыскательных гостей.\n\n"
        "🏖 7+ лет на рынке\n"
        "👥 500+ довольных клиентов\n"
        "🕐 Поддержка 24/7 на русском языке\n\n"
        "Выберите интересующую услугу 👇"
    )
    keyboard = _build_main_menu()
    await update.message.reply_text(
        welcome_text,
        parse_mode="Markdown",
        reply_markup=keyboard,
    )

    # Notify admin about new user
    await _notify_admin(
        context,
        f"🆕 Новый пользователь!\n"
        f"Имя: {user.first_name} {user.last_name or ''}\n"
        f"Username: @{user.username or 'нет'}\n"
        f"ID: {user.id}\n"
        f"Время: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show main menu."""
    keyboard = _build_main_menu()
    await update.message.reply_text(
        "Выберите интересующую услугу 👇",
        reply_markup=keyboard,
    )


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline button clicks."""
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "back_to_menu":
        keyboard = _build_main_menu()
        await query.edit_message_text(
            "Выберите интересующую услугу 👇",
            reply_markup=keyboard,
        )
        return

    if data == "contact_manager":
        await query.edit_message_text(
            "📞 *Связаться с менеджером*\n\n"
            "Напишите ваш вопрос прямо сюда — наш менеджер "
            "ответит в течение 15 минут!\n\n"
            "Или позвоните: +90 539 449 86 07\n\n"
            "Мы на связи 24/7 🕐",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ Назад к меню", callback_data="back_to_menu")]
            ]),
        )
        return

    if data in SERVICES:
        service = SERVICES[data]
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📩 Оставить заявку", callback_data=f"request_{data}")],
            [InlineKeyboardButton("📞 Связаться с менеджером", callback_data="contact_manager")],
            [InlineKeyboardButton("◀️ Назад к меню", callback_data="back_to_menu")],
        ])
        await query.edit_message_text(
            service["desc"],
            parse_mode="Markdown",
            reply_markup=keyboard,
        )

        # Notify admin
        user = query.from_user
        await _notify_admin(
            context,
            f"👁 {user.first_name} (@{user.username or 'нет'}) "
            f"смотрит: {service['title']}"
        )
        return

    if data.startswith("request_"):
        service_key = data.replace("request_", "")
        service = SERVICES.get(service_key, {})
        context.user_data["pending_service"] = service_key

        await query.edit_message_text(
            f"📝 *Заявка: {service.get('title', '')}*\n\n"
            "Пожалуйста, напишите:\n\n"
            "1️⃣ Ваше имя\n"
            "2️⃣ Даты поездки\n"
            "3️⃣ Количество гостей\n"
            "4️⃣ Особые пожелания\n\n"
            "_Можно одним сообщением — мы разберёмся!_ 😊",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("◀️ Назад к меню", callback_data="back_to_menu")]
            ]),
        )
        return


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle free-text messages from users."""
    user = update.effective_user
    text = update.message.text
    pending = context.user_data.get("pending_service")

    if pending:
        service = SERVICES.get(pending, {})
        # Confirm to user
        await update.message.reply_text(
            f"✅ Спасибо! Ваша заявка на *{service.get('title', 'услугу')}* принята.\n\n"
            "Наш менеджер свяжется с вами в течение 15 минут. "
            "Если вопрос срочный — позвоните: +90 539 449 86 07\n\n"
            "Хотите посмотреть другие услуги?",
            parse_mode="Markdown",
            reply_markup=_build_main_menu(),
        )
        # Forward to admin
        await _notify_admin(
            context,
            f"🔔 *НОВАЯ ЗАЯВКА!*\n\n"
            f"👤 {user.first_name} {user.last_name or ''}\n"
            f"📱 @{user.username or 'нет username'}\n"
            f"🆔 ID: {user.id}\n"
            f"📋 Услуга: {service.get('title', pending)}\n"
            f"💬 Сообщение:\n{text}\n"
            f"⏰ {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        )
        context.user_data["pending_service"] = None
    else:
        # General message
        await update.message.reply_text(
            "Спасибо за сообщение! 🌟\n\n"
            "Наш менеджер увидит его и ответит в ближайшее время.\n\n"
            "А пока — можете выбрать интересующую услугу:",
            reply_markup=_build_main_menu(),
        )
        await _notify_admin(
            context,
            f"💬 Сообщение от {user.first_name} "
            f"(@{user.username or 'нет'}, ID: {user.id}):\n\n{text}"
        )


# ══════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════

def _build_main_menu() -> InlineKeyboardMarkup:
    """Build the main service menu keyboard."""
    buttons = []
    items = list(SERVICES.items())
    for i in range(0, len(items), 2):
        row = []
        for key, svc in items[i:i + 2]:
            row.append(
                InlineKeyboardButton(
                    f"{svc['emoji']} {svc['title']}",
                    callback_data=key,
                )
            )
        buttons.append(row)
    buttons.append([
        InlineKeyboardButton("📞 Связаться с менеджером", callback_data="contact_manager")
    ])
    return InlineKeyboardMarkup(buttons)


async def _notify_admin(context: ContextTypes.DEFAULT_TYPE, text: str):
    """Send notification to admin."""
    try:
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=text,
            parse_mode="Markdown",
        )
    except Exception as e:
        logger.error(f"Failed to notify admin: {e}")


# ══════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════

def main():
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ BOT_TOKEN ayarlanmamış!")
        print("   Çözüm: set BOT_TOKEN=your_token_here")
        print("   veya bot.py içinde değiştirin.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bodrum Elite Bot baslatildi!")
    print("   Durdurmak icin CTRL+C")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()

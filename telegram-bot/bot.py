"""
BODRUM ELITE — Telegram Concierge Bot (Multilingual)
====================================================
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
ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID", "6876584793")

# ── Logging ──
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ══════════════════════════════════════════════════
# TRANSLATIONS & SERVICES
# ══════════════════════════════════════════════════

LANGUAGES = {
    'tr': '🇹🇷 Türkçe',
    'en': '🇬🇧 English',
    'ru': '🇷🇺 Русский'
}

TEXTS = {
    'tr': {
        'welcome': "Hoş geldiniz, {name}! 🌟\n\nBen *Bodrum Elite* sanal asistanınızım.\n\nEn seçkin misafirler için Bodrum'da ayrıcalıklı hizmetler sunuyoruz.\n\nLütfen ilgilendiğiniz hizmeti seçin 👇",
        'menu_prompt': "Lütfen ilgilendiğiniz hizmeti seçin 👇",
        'btn_back': "◀️ Menüye Dön",
        'btn_request': "📩 Talep Oluştur",
        'btn_contact': "📞 Yönetici ile İletişime Geç",
        'contact_msg': "📞 *Yönetici ile İletişime Geç*\n\nSorunuzu buraya yazabilirsiniz. Yöneticimiz 15 dakika içinde size dönecektir!\n\nVeya arayın: +90 539 449 86 07\n\n7/24 hizmetinizdeyiz 🕐",
        'request_prompt': "📝 *Talep: {service}*\n\nLütfen şunları yazın:\n\n1️⃣ İsminiz\n2️⃣ Tarihleriniz\n3️⃣ Kişi sayısı\n4️⃣ Özel istekleriniz\n\n_Tek bir mesajda gönderebilirsiniz!_ 😊",
        'request_success': "✅ Teşekkürler! *{service}* talebiniz alındı.\n\nYöneticimiz 15 dakika içinde sizinle iletişime geçecektir. Acil durumlar için arayabilirsiniz: +90 539 449 86 07\n\nBaşka hizmetlerimize göz atmak ister misiniz?",
        'general_msg': "Mesajınız için teşekkürler! 🌟\n\nYöneticimiz en kısa sürede size dönüş yapacaktır.\n\nBu arada diğer hizmetlerimizi inceleyebilirsiniz:",
        'services': {
            "transfer": {"emoji": "🚗", "title": "VIP Transfer", "desc": "🚗 *VIP Transfer*\n\nHavalimanından otelinize veya Bodrum'un herhangi bir noktasına Mercedes Vito ve Sprinter araçlarımızla lüks ve güvenli transfer."},
            "villa": {"emoji": "🏡", "title": "Villa Kiralama", "desc": "🏡 *Villa Kiralama*\n\nBodrum'un en prestijli bölgelerinde, özel havuzlu, deniz manzaralı, lüks ve tam donanımlı kiralık villalar."},
            "yacht": {"emoji": "🛥", "title": "Yat Kiralama", "desc": "🛥 *Yat Kiralama*\n\nEge'nin turkuaz sularında eşsiz bir deneyim için mürettebatlı, lüks motor yat ve gulet kiralama hizmetleri."},
            "restaurant": {"emoji": "🍽", "title": "Restoran Rezervasyonu", "desc": "🍽 *Restoran Rezervasyonu*\n\nBodrum'un en popüler ve Michelin yıldızlı restoranlarında sizin için en iyi masayı rezerve ediyoruz."},
            "beach": {"emoji": "🏖", "title": "Beach Club", "desc": "🏖 *Beach Club*\n\nBodrum'un en gözde beach club'larında VIP loca, şezlong ve cabana rezervasyonları."},
            "nightlife": {"emoji": "🌙", "title": "Gece Hayatı", "desc": "🌙 *Gece Hayatı*\n\nBodrum gece hayatının nabzını tutan en seçkin gece kulüplerinde VIP masa rezervasyonları."},
            "assistant": {"emoji": "👤", "title": "Kişisel Asistan", "desc": "👤 *Kişisel Asistan*\n\nTatiliniz boyunca size eşlik edecek, her türlü ihtiyacınızla ilgilenecek profesyonel asistan hizmeti."},
            "jet": {"emoji": "✈️", "title": "Özel Jet & Helikopter", "desc": "✈️ *Özel Jet & Helikopter*\n\nZamanı değerli olanlar için Bodrum'a hızlı ve konforlu ulaşım. Jet ve helikopter kiralama."}
        }
    },
    'en': {
        'welcome': "Welcome, {name}! 🌟\n\nI am your *Bodrum Elite* virtual assistant.\n\nWe provide exclusive services in Bodrum for the most discerning guests.\n\nPlease select a service you are interested in 👇",
        'menu_prompt': "Please select a service you are interested in 👇",
        'btn_back': "◀️ Back to Menu",
        'btn_request': "📩 Make a Request",
        'btn_contact': "📞 Contact Manager",
        'contact_msg': "📞 *Contact Manager*\n\nYou can write your question here. Our manager will reply within 15 minutes!\n\nOr call: +90 539 449 86 07\n\nWe are available 24/7 🕐",
        'request_prompt': "📝 *Request: {service}*\n\nPlease write:\n\n1️⃣ Your name\n2️⃣ Travel dates\n3️⃣ Number of guests\n4️⃣ Special requests\n\n_You can send it in a single message!_ 😊",
        'request_success': "✅ Thank you! Your request for *{service}* has been received.\n\nOur manager will contact you within 15 minutes. For urgent matters, call: +90 539 449 86 07\n\nWould you like to explore other services?",
        'general_msg': "Thank you for your message! 🌟\n\nOur manager will get back to you shortly.\n\nMeanwhile, you can explore our other services:",
        'services': {
            "transfer": {"emoji": "🚗", "title": "VIP Transfer", "desc": "🚗 *VIP Transfer*\n\nLuxury and safe transfer service from the airport to your hotel or anywhere in Bodrum with Mercedes Vito and Sprinter vehicles."},
            "villa": {"emoji": "🏡", "title": "Villa Rental", "desc": "🏡 *Villa Rental*\n\nLuxury rental villas with private pools and sea views in the most prestigious areas of Bodrum."},
            "yacht": {"emoji": "🛥", "title": "Yacht Charter", "desc": "🛥 *Yacht Charter*\n\nCrewed, luxury motor yacht and gulet charter services for a unique experience in the Aegean Sea."},
            "restaurant": {"emoji": "🍽", "title": "Restaurant Reservation", "desc": "🍽 *Restaurant Reservation*\n\nWe reserve the best tables for you in Bodrum's most popular and Michelin-starred restaurants."},
            "beach": {"emoji": "🏖", "title": "Beach Club", "desc": "🏖 *Beach Club*\n\nVIP lounge, sunbed and cabana reservations at Bodrum's most popular beach clubs."},
            "nightlife": {"emoji": "🌙", "title": "Nightlife", "desc": "🌙 *Nightlife*\n\nVIP table reservations in the most exclusive nightclubs of Bodrum."},
            "assistant": {"emoji": "👤", "title": "Personal Assistant", "desc": "👤 *Personal Assistant*\n\nProfessional assistant service taking care of all your needs throughout your holiday."},
            "jet": {"emoji": "✈️", "title": "Private Jet & Helicopter", "desc": "✈️ *Private Jet & Helicopter*\n\nFast and comfortable transportation to Bodrum. Private jet charter and helicopter transfers."}
        }
    },
    'ru': {
        'welcome': "Добро пожаловать, {name}! 🌟\n\nЯ — виртуальный консьерж *Bodrum Elite*.\n\nМы предоставляем эксклюзивный сервис в Бодруме для самых взыскательных гостей.\n\nВыберите интересующую услугу 👇",
        'menu_prompt': "Выберите интересующую услугу 👇",
        'btn_back': "◀️ Назад к меню",
        'btn_request': "📩 Оставить заявку",
        'btn_contact': "📞 Связаться с менеджером",
        'contact_msg': "📞 *Связаться с менеджером*\n\nНапишите ваш вопрос прямо сюда — наш менеджер ответит в течение 15 минут!\n\nИли позвоните: +90 539 449 86 07\n\nМы на связи 24/7 🕐",
        'request_prompt': "📝 *Заявка: {service}*\n\nПожалуйста, напишите:\n\n1️⃣ Ваше имя\n2️⃣ Даты поездки\n3️⃣ Количество гостей\n4️⃣ Особые пожелания\n\n_Можно одним сообщением — мы разберёмся!_ 😊",
        'request_success': "✅ Спасибо! Ваша заявка на *{service}* принята.\n\nНаш менеджер свяжется с вами в течение 15 минут. Если вопрос срочный — позвоните: +90 539 449 86 07\n\nХотите посмотреть другие услуги?",
        'general_msg': "Спасибо за сообщение! 🌟\n\nНаш менеджер увидит его и ответит в ближайшее время.\n\nА пока — можете выбрать интересующую услугу:",
        'services': {
            "transfer": {"emoji": "🚗", "title": "VIP-Трансфер", "desc": "🚗 *VIP-Трансфер*\n\nРоскошный и комфортный трансфер из аэропорта в ваш отель или в любую точку Бодрума на автомобилях Mercedes Vito и Sprinter."},
            "villa": {"emoji": "🏡", "title": "Аренда Виллы", "desc": "🏡 *Аренда Виллы*\n\nРоскошные виллы в аренду с частными бассейнами и видом на море в самых престижных районах Бодрума."},
            "yacht": {"emoji": "🛥", "title": "Аренда Яхты", "desc": "🛥 *Аренда Яхты*\n\nУслуги по аренде роскошных яхт и гулет с экипажем для уникального отдыха в водах Эгейского моря."},
            "restaurant": {"emoji": "🍽", "title": "Бронирование Ресторанов", "desc": "🍽 *Бронирование Ресторанов*\n\nМы бронируем для вас лучший столик в самых популярных ресторанах Бодрума и ресторанах Мишлен."},
            "beach": {"emoji": "🏖", "title": "Пляжный Клуб", "desc": "🏖 *Пляжный Клуб*\n\nБронирование VIP-лож, шезлонгов и кабан в самых популярных пляжных клубах Бодрума."},
            "nightlife": {"emoji": "🌙", "title": "Ночная Жизнь", "desc": "🌙 *Ночная Жизнь*\n\nБронирование VIP-столиков в самых эксклюзивных ночных клубах Бодрума."},
            "assistant": {"emoji": "👤", "title": "Личный Помощник", "desc": "👤 *Личный Помощник*\n\nПрофессиональные услуги помощника, который позаботится обо всех ваших потребностях."},
            "jet": {"emoji": "✈️", "title": "Частный Самолет и Вертолет", "desc": "✈️ *Частный Самолет и Вертолет*\n\nБыстрая и комфортная транспортировка в Бодрум. Аренда частного самолета и вертолетные трансферы."}
        }
    }
}


# ══════════════════════════════════════════════════
# HANDLERS
# ══════════════════════════════════════════════════

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command - choose language."""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(name, callback_data=f"lang_{code}")] 
        for code, name in LANGUAGES.items()
    ])
    
    await update.message.reply_text(
        "Please select your language / Lütfen dil seçin / Пожалуйста, выберите язык:",
        reply_markup=keyboard
    )

async def _show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, lang: str, edit_message=True):
    user = update.effective_user
    t = TEXTS[lang]
    
    welcome_text = t['welcome'].format(name=user.first_name)
    keyboard = _build_main_menu(lang)
    
    if edit_message and hasattr(update, 'callback_query') and update.callback_query:
        await update.callback_query.edit_message_text(
            welcome_text,
            parse_mode="Markdown",
            reply_markup=keyboard,
        )
    else:
        await context.bot.send_message(
            chat_id=user.id,
            text=welcome_text,
            parse_mode="Markdown",
            reply_markup=keyboard,
        )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show main menu."""
    lang = context.user_data.get('lang', 'en')
    t = TEXTS[lang]
    keyboard = _build_main_menu(lang)
    await update.message.reply_text(
        t['menu_prompt'],
        reply_markup=keyboard,
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline button clicks."""
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("lang_"):
        lang = data.replace("lang_", "")
        context.user_data['lang'] = lang
        await _show_main_menu(update, context, lang)
        
        user = query.from_user
        await _notify_admin(
            context,
            f"🆕 Новый пользователь!\n"
            f"Имя: {user.first_name} {user.last_name or ''}\n"
            f"Username: @{user.username or 'нет'}\n"
            f"ID: {user.id}\n"
            f"Язык: {lang}\n"
            f"Время: {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        )
        return

    lang = context.user_data.get('lang', 'en')
    t = TEXTS[lang]

    if data == "back_to_menu":
        keyboard = _build_main_menu(lang)
        await query.edit_message_text(
            t['menu_prompt'],
            reply_markup=keyboard,
        )
        return

    if data == "contact_manager":
        await query.edit_message_text(
            t['contact_msg'],
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(t['btn_back'], callback_data="back_to_menu")]
            ]),
        )
        return

    services = t['services']
    if data in services:
        service = services[data]
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(t['btn_request'], callback_data=f"request_{data}")],
            [InlineKeyboardButton(t['btn_contact'], callback_data="contact_manager")],
            [InlineKeyboardButton(t['btn_back'], callback_data="back_to_menu")],
        ])
        await query.edit_message_text(
            service["desc"],
            parse_mode="Markdown",
            reply_markup=keyboard,
        )

        user = query.from_user
        await _notify_admin(
            context,
            f"👁 {user.first_name} (@{user.username or 'нет'}) смотрит: {service['title']} ({lang})"
        )
        return

    if data.startswith("request_"):
        service_key = data.replace("request_", "")
        service = services.get(service_key, {})
        context.user_data["pending_service"] = service_key

        await query.edit_message_text(
            t['request_prompt'].format(service=service.get('title', '')),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(t['btn_back'], callback_data="back_to_menu")]
            ]),
        )
        return

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle free-text messages from users."""
    user = update.effective_user
    text = update.message.text
    lang = context.user_data.get('lang', 'en')
    t = TEXTS[lang]
    pending = context.user_data.get("pending_service")

    if pending:
        service = t['services'].get(pending, {})
        await update.message.reply_text(
            t['request_success'].format(service=service.get('title', pending)),
            parse_mode="Markdown",
            reply_markup=_build_main_menu(lang),
        )
        
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
        await update.message.reply_text(
            t['general_msg'],
            reply_markup=_build_main_menu(lang),
        )
        await _notify_admin(
            context,
            f"💬 Сообщение от {user.first_name} "
            f"(@{user.username or 'нет'}, ID: {user.id}):\n\n{text}"
        )


# ══════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════

def _build_main_menu(lang: str) -> InlineKeyboardMarkup:
    """Build the main service menu keyboard."""
    buttons = []
    t = TEXTS[lang]
    items = list(t['services'].items())
    
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
        InlineKeyboardButton(t['btn_contact'], callback_data="contact_manager")
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

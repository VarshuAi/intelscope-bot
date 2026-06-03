# ---------------------------------------------------------
# IntelScope OSINT Telegram Bot
# Developed by: VarshuAi (Owner & Developer)
# Source Code Credit: VarshuAi (https://github.com/VarshuAi)
# Licensed under MIT License
# ---------------------------------------------------------

import os
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# Import modules
from recon.usernames import search_username
from recon.domains import resolve_dns, get_subdomains
from recon.ips import get_ip_geo, get_ip_threat
from recon.emails import verify_email
from recon.vehicles import lookup_vehicle
from recon.phone import lookup_phone
from recon.github import lookup_github

# Load environment
load_dotenv()
TOKEN = os.getenv("TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "5938660179"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "VarshuAi")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "varshuai_support")

bot = telebot.TeleBot(TOKEN, parse_mode="MARKDOWN")

START_IMG = "https://te.legra.ph/file/117b8e5f5184343a9e72d.jpg"

PM_START_TEXT = """
*ʜᴇʏ* {}, 🥀

*๏ ɪ ᴀᴍ ɪɴᴛᴇʟsᴄᴏᴘᴇ ʀᴏʙᴏᴛ ๏*
*ᴛʜᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀꜰᴜʟ OSINT ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ʙᴏᴛ*

➻ ɪ ᴄᴀɴ footprint usernames, audit DNS records, track IP addresses, and verify active email servers.

──────────────────
*๏ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴀɴᴅ ᴏᴡɴᴇʀ:* @VarshuAi
*๏ ᴜsᴇ /help ᴛᴏ sᴇᴇ ᴀᴠᴀɪʟᴀʙʟᴇ sᴄᴀɴ ᴍᴏᴅᴇs.*
"""

HELP_TEXT = """
*ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ* ⚔️

• `/user <username>` : Scan username footprints across 50+ websites.
• `/domain <domain>` : Audit DNS records and check SSL/TLS subdomains.
• `/ip <ip_address>` : Check Geolocation and AlienVault threat pulse reputation.
• `/email <email>` : Perform MX record audits and SMTP handshake tests.
• `/vehicle <plate_number>` : Verify Indian RTO registration & vehicle specifications.
• `/phone <phone_number>` : Gather ITU-T validation, carrier, & location info.
• `/github <username>` : Analyze public GitHub repositories & profile metrics.

*๏ ᴀʟʟ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴄʀᴇᴅɪᴛs ʙᴇʟᴏɴɢ ᴄᴏᴍᴘʟᴇᴛᴇʟʏ ᴛᴏ ᴛʜᴇ ᴏᴡɴᴇʀ ᴀɴᴅ ᴅᴇᴠᴇʟᴏᴘᴇʀ:* [@VarshuAi](https://t.me/VarshuAi)
──────────────────
"""

ABOUT_TEXT = """
*๏ ᴀʙᴏᴜᴛ ɪɴᴛᴇʟsᴄᴏᴘᴇ ʀᴏʙᴏᴛ ๏*

ɪɴᴛᴇʟsᴄᴏᴘᴇ ɪs ᴀ premium OSINT & ᴛᴇᴄʜɴɪᴄᴀʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ʙᴏᴛ.
• ᴅᴇᴠᴇʟᴏᴘᴇʀ & Owner: @VarshuAi.
• sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴄᴏᴍᴘʟᴇᴛᴇʟʏ ᴏᴡɴᴇᴅ ʙʏ @VarshuAi.
• sᴄᴀɴs ᴀɴᴅ audits public internet assets safely.

_ɪɴᴛᴇʟsᴄᴏᴘᴇ ɪs ʟɪᴄᴇɴsᴇᴅ ᴜɴᴅᴇʀ ᴛʜᴇ MIT ʟɪᴄᴇɴsᴇ._
"""

CREDIT_TEXT = f"""
━━━━━━━ *ᴄʀᴇᴅɪᴛs* ━━━━━━━
🛡️ *ᴄʀᴇᴅɪᴛs ꜰᴏʀ ɪɴᴛᴇʟsᴄᴏᴘᴇ* 🛡️

ᴛʜɪs ᴘᴏᴡᴇʀꜰᴜʟ OSINT ʙᴏᴛ ᴡᴀs completely designed, developed, and sponsored by:
➻ *[@VarshuAi](https://t.me/VarshuAi)*

ᴀʟʟ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ and intellectual properties are credited to him. ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴜsɪɴɢ!
"""

SOURCE_TEXT = f"""
*ʜᴇʏ, ᴛʜɪs ɪs ɪɴᴛᴇʟsᴄᴏᴘᴇ ʀᴏʙᴏᴛ!*
*ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ OSINT ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ʙᴏᴛ.*

ᴡʀɪᴛᴛᴇɴ ɪɴ ᴘʏᴛʜᴏɴ using dnspython, requests, and pyTelegramBotAPI.

*๏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ᴏᴡɴᴇʀ:* [@VarshuAi](https://t.me/VarshuAi)
*๏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ:* [ɪɴᴛᴇʟsᴄᴏᴘᴇ ɢɪᴛʜᴜʙ](https://github.com/VarshuAi/intelscope-bot)

© 2026 [@VarshuAi](https://t.me/VarshuAi), ᴀʟʟ ʀɪɢʜᴛs ʀᴇsᴇʀᴠᴇᴅ.
"""

def get_start_buttons():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🏡 ᴀʙᴏᴜᴛ 🏡", callback_data="EXON_ABOUT"),
               InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🥀", url=f"https://t.me/{OWNER_USERNAME}"))
    markup.row(InlineKeyboardButton("sᴏᴜʀᴄᴇ", callback_data="EXON_SOURCE"),
               InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"))
    return markup

def get_sub_buttons():
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton("🏡", callback_data="EXON_BACK"),
               InlineKeyboardButton("💳 ᴄʀᴇᴅɪᴛs", callback_data="EXON_CREDIT"),
               InlineKeyboardButton("🕹️ sᴏᴜʀᴄᴇ", callback_data="EXON_SOURCE"))
    return markup

@bot.message_handler(commands=["start"])
def send_welcome(message):
    first_name = message.from_user.first_name
    
    # ExonRobot-like loading sequence
    loading = bot.reply_to(message, "ᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ ʙʀᴏ . . . ")
    time.sleep(0.3)
    bot.edit_message_text("⚡", chat_id=message.chat.id, message_id=loading.message_id)
    time.sleep(0.3)
    bot.edit_message_text("ꜱᴛᴀʀᴛɪɴɢ... ", chat_id=message.chat.id, message_id=loading.message_id)
    time.sleep(0.2)
    bot.delete_message(chat_id=message.chat.id, message_id=loading.message_id)
    
    # Send start photo and menu
    bot.send_photo(
        message.chat.id,
        START_IMG,
        caption=PM_START_TEXT.format(first_name),
        reply_markup=get_start_buttons()
    )

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_photo(
        message.chat.id,
        START_IMG,
        caption=HELP_TEXT
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("EXON_"))
def callback_handler(call):
    if call.data == "EXON_ABOUT":
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=ABOUT_TEXT,
            reply_markup=get_sub_buttons()
        )
    elif call.data == "EXON_CREDIT":
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=CREDIT_TEXT,
            reply_markup=get_sub_buttons()
        )
    elif call.data == "EXON_SOURCE":
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=SOURCE_TEXT,
            reply_markup=get_sub_buttons()
        )
    elif call.data == "EXON_BACK":
        first_name = call.from_user.first_name
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=PM_START_TEXT.format(first_name),
            reply_markup=get_start_buttons()
        )

@bot.message_handler(commands=["user"])
def handle_user(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "⚠️ *sʏɴᴛᴀx:* `/user <username>`")
        return
        
    username = args[1]
    status_msg = bot.reply_to(message, "🌀 *ꜰᴏᴏᴛᴘʀɪɴᴛɪɴɢ ᴜsᴇʀɴᴀᴍᴇ...*")
    
    results = search_username(username)
    
    if not results:
        bot.edit_message_text(f"❌ No footprint results found for username: `{username}`", chat_id=message.chat.id, message_id=status_msg.message_id)
        return
        
    result_text = f"🔍 *ᴜsᴇʀɴᴀᴍᴇ footprint sᴄᴀɴ*\n\n"
    result_text += f"➻ *ᴛᴀʀɢᴇᴛ:* `{username}`\n"
    result_text += f"➻ *ᴘʟᴀᴛꜰᴏʀᴍs ꜰᴏᴜɴᴅ:* `{len(results)}`/50\n"
    result_text += "──────────────────\n"
    
    # Format URLs
    for name, url in results[:25]:  # Send first 25 to avoid message size limits
        result_text += f"• *{name}:* [Link]({url})\n"
        
    if len(results) > 25:
        result_text += f"\n_...and {len(results) - 25} other platforms._"
        
    bot.edit_message_text(result_text, chat_id=message.chat.id, message_id=status_msg.message_id, disable_web_page_preview=True)

@bot.message_handler(commands=["domain"])
def handle_domain(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "⚠️ *sʏɴᴛᴀx:* `/domain <host_name>`")
        return
        
    domain = args[1].replace("http://", "").replace("https://", "").split("/")[0]
    status_msg = bot.reply_to(message, "🌀 *ʀᴇsᴏʟᴠɪɴɢ DNS & certificates...*")
    
    dns_records = resolve_dns(domain)
    subdomains = get_subdomains(domain)
    
    result_text = f"🌐 *ᴅᴏᴍᴀɪɴ OSINT ᴀᴜᴅɪᴛ*\n\n"
    result_text += f"➻ *ᴛᴀʀɢᴇᴛ:* `{domain}`\n"
    result_text += "──────────────────\n"
    
    # Format DNS
    for r_type, records in dns_records.items():
        if records:
            result_text += f"• *{r_type}:* `{', '.join(records[:3])}`\n"
            
    # Format Subdomains
    result_text += "\n📁 *ᴄᴇʀᴛɪꜰɪᴄᴀᴛᴇ subdomains:* \n"
    if subdomains:
        for sub in subdomains[:15]:
            result_text += f"➻ `{sub}`\n"
        if len(subdomains) > 15:
            result_text += f"_(and {len(subdomains) - 15} others)_\n"
    else:
        result_text += "No subdomains discovered in CT logs.\n"
        
    bot.edit_message_text(result_text, chat_id=message.chat.id, message_id=status_msg.message_id)

@bot.message_handler(commands=["ip"])
def handle_ip(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "⚠️ *sʏɴᴛᴀx:* `/ip <ip_address>`")
        return
        
    ip = args[1]
    status_msg = bot.reply_to(message, "🌀 *ɢᴀᴛʜᴇʀɪɴɢ ɪᴘ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ...*")
    
    geo = get_ip_geo(ip)
    threat = get_ip_threat(ip)
    
    if not geo:
        bot.edit_message_text(f"❌ Invalid or unreachable IP address: `{ip}`", chat_id=message.chat.id, message_id=status_msg.message_id)
        return
        
    result_text = f"🖥️ *ɪᴘ threat ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ*\n\n"
    result_text += f"➻ *ᴛᴀʀɢᴇᴛ:* `{ip}`\n"
    result_text += f"➻ *ɢᴇᴏ:* `{geo.get('city', 'Unknown')}, {geo.get('regionName', 'Unknown')}, {geo.get('country', 'Unknown')}`\n"
    result_text += f"➻ *ɪsᴘ / ᴏʀɢ:* `{geo.get('isp', 'Unknown')}` / `{geo.get('org', 'Unknown')}`\n"
    result_text += f"➻ *ᴀsɴ:* `{geo.get('as', 'Unknown')}`\n"
    result_text += "──────────────────\n"
    result_text += f"• *ᴛʜʀᴇᴀᴛ sᴄᴏʀᴇ:* `{threat['threat_score']}` pulses\n"
    result_text += f"• *ʀᴇᴘᴜᴛᴀᴛɪᴏɴ:* `{threat['reputation']}`\n"
    
    if threat['references']:
        result_text += "\n*ᴀssᴏᴄɪᴀᴛᴇᴅ ᴛʜʀᴇᴀᴛ ᴘᴜʟsᴇs:*\n"
        for ref in threat['references']:
            result_text += f"➻ `{ref}`\n"
            
    bot.edit_message_text(result_text, chat_id=message.chat.id, message_id=status_msg.message_id)

@bot.message_handler(commands=["email"])
def handle_email(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "⚠️ *sʏɴᴛᴀx:* `/email <address>`")
        return
        
    email = args[1]
    status_msg = bot.reply_to(message, "🌀 *ᴠᴇʀɪꜰʏɪɴɢ email hosts...*")
    
    info = verify_email(email)
    
    result_text = f"📧 *ᴇᴍᴀɪʟ ʜᴏsᴛ ᴀᴜᴅɪᴛ*\n\n"
    result_text += f"➻ *ᴛᴀʀɢᴇᴛ:* `{email}`\n"
    result_text += "──────────────────\n"
    result_text += f"• *sᴛᴀᴛᴜs:* `{info['status']}`\n"
    result_text += f"• *sᴍᴛᴘ sᴛᴀᴛᴜs:* `{info['smtp_status']}`\n"
    
    if info['mx_records']:
        result_text += "\n*ᴍx servers resolved:*\n"
        for mx in info['mx_records']:
            result_text += f"➻ `{mx}`\n"
            
    bot.edit_message_text(result_text, chat_id=message.chat.id, message_id=status_msg.message_id)

@bot.message_handler(commands=["vehicle"])
def handle_vehicle(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "⚠️ *sʏɴᴛᴀx:* `/vehicle <plate_number>`")
        return
        
    plate_number = "".join(args[1:])
    status_msg = bot.reply_to(message, "🌀 *ꜰᴇᴛᴄʜɪɴɢ ᴠᴇʜɪᴄʟᴇ ʀᴇɢɪsᴛʀᴀᴛɪᴏɴ ɪɴꜰᴏ...*")
    
    info = lookup_vehicle(plate_number)
    
    if info.get("status") == "error":
        bot.edit_message_text(f"❌ {info['message']}", chat_id=message.chat.id, message_id=status_msg.message_id)
        return
        
    result_text = f"🚘 *ᴠᴇʜɪᴄʟᴇ ʀᴇɢɪsᴛʀᴀᴛɪᴏɴ ɪɴᴛᴇʟ*\n\n"
    result_text += f"➻ *ʀᴇɢɪsᴛʀᴀᴛɪᴏɴ:* `{info.get('registration_number', plate_number.upper())}`\n"
    result_text += f"➻ *sᴛᴀᴛᴇ / ᴜᴛ:* `{info.get('state', 'Unknown')}`\n"
    result_text += f"➻ *ʀᴛᴏ ᴏꜰꜰɪᴄᴇ:* `{info.get('rto_office', info.get('rto_code', 'Unknown'))}`\n"
    result_text += "──────────────────\n"
    result_text += f"• *ᴏᴡɴᴇʀ ɴᴀᴍᴇ:* `{info.get('owner_name', 'Masked / Protected')}`\n"
    result_text += f"• *ᴍᴀᴋᴇ & ᴍᴏᴅᴇʟ:* `{info.get('make_model', 'Unknown')}`\n"
    result_text += f"• *ꜰᴜᴇʟ ᴛʏᴘᴇ:* `{info.get('fuel_type', 'Unknown')}`\n"
    result_text += f"• *ᴠᴇʜɪᴄʟᴇ ᴄʟᴀss:* `{info.get('vehicle_class', 'Unknown')}`\n"
    result_text += f"• *ʀᴇɢɪsᴛʀᴀᴛɪᴏɴ ᴅᴀᴛᴇ:* `{info.get('registration_date', 'Unknown')}`\n"
    result_text += f"• *ꜰɪᴛɴᴇss ᴜᴘᴛᴏ:* `{info.get('fitness_upto', 'Unknown')}`\n"
    result_text += f"• *ɪɴsᴜʀᴀɴᴄᴇ ᴠᴀʟɪᴅɪᴛʏ:* `{info.get('insurance_validity', 'Unknown')}`\n"
    
    if info.get("simulated"):
        result_text += "\n⚠️ _Note: Displaying simulated lookup matching target configuration (privacy masking applied)._"

    bot.edit_message_text(result_text, chat_id=message.chat.id, message_id=status_msg.message_id)

@bot.message_handler(commands=["phone"])
def handle_phone(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "⚠️ *sʏɴᴛᴀx:* `/phone <phone_number>`\n_(e.g., /phone +919876543210)_")
        return
        
    phone_number = "".join(args[1:])
    status_msg = bot.reply_to(message, "🌀 *ᴀɴᴀʟʏᴢɪɴɢ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ...*")
    
    info = lookup_phone(phone_number)
    
    if info.get("status") == "error":
        bot.edit_message_text(f"❌ {info['message']}", chat_id=message.chat.id, message_id=status_msg.message_id)
        return
        
    result_text = f"📞 *ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪɴᴛᴇʟ*\n\n"
    result_text += f"➻ *ᴛᴀʀɢᴇᴛ:* `{info.get('number')}`\n"
    result_text += f"➻ *ᴄᴏᴜɴᴛʀʏ:* `{info.get('region', 'Unknown')}`\n"
    result_text += "──────────────────\n"
    result_text += f"• *ᴠᴀʟɪᴅɪᴛʏ:* `Valid Number (ITU-T)`\n"
    result_text += f"• *ᴄᴀʀʀɪᴇʀ:* `{info.get('carrier', 'Unknown')}`\n"
    result_text += f"• *ɢᴇᴏ-ʟᴏᴄᴀᴛɪᴏɴ:* `{info.get('location', 'Unknown')}`\n"
    result_text += f"• *ᴛɪᴍᴇᴢᴏɴᴇs:* `{info.get('timezones', 'Unknown')}`\n"
    result_text += f"• *ɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ:* `{info.get('intl_format', 'Unknown')}`\n"
    
    bot.edit_message_text(result_text, chat_id=message.chat.id, message_id=status_msg.message_id)

@bot.message_handler(commands=["github"])
def handle_github(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "⚠️ *sʏɴᴛᴀx:* `/github <username>`")
        return
        
    username = args[1]
    status_msg = bot.reply_to(message, "🌀 *ᴀɴᴀʟʏᴢɪɴɢ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜɴᴛ...*")
    
    info = lookup_github(username)
    
    if info.get("status") == "error":
        bot.edit_message_text(f"❌ {info['message']}", chat_id=message.chat.id, message_id=status_msg.message_id)
        return
        
    result_text = f"🖥️ *ɢɪᴛʜᴜʙ ᴘʀᴏꜰɪʟᴇ ɪɴᴛᴇʟ*\n\n"
    result_text += f"➻ *ᴛᴀʀɢᴇᴛ:* `{info.get('username')}`\n"
    result_text += f"➻ *ɴᴀᴍᴇ:* `{info.get('name')}`\n"
    result_text += "──────────────────\n"
    result_text += f"• *ʙɪᴏ:* `{info.get('bio')}`\n"
    result_text += f"• *ᴘᴜʙʟɪᴄ ʀᴇᴘᴏs:* `{info.get('public_repos')}`\n"
    result_text += f"• *ɢɪsᴛs:* `{info.get('gists')}`\n"
    result_text += f"• *ꜰᴏʟʟᴏᴡᴇʀs:* `{info.get('followers')}`\n"
    result_text += f"• *ꜰᴏʟʟᴏᴡɪɴɢ:* `{info.get('following')}`\n"
    result_text += f"• *ʟᴏᴄᴀᴛɪᴏɴ:* `{info.get('location')}`\n"
    result_text += f"• *ᴄᴏᴍᴘᴀɴʏ:* `{info.get('company')}`\n"
    result_text += f"• *ᴄʀᴇᴀᴛᴇᴅ ᴀᴛ:* `{info.get('created_at')}`\n"
    result_text += f"• *ᴘʀᴏꜰɪʟᴇ:* [Link]({info.get('html_url')})\n"
    
    bot.edit_message_text(result_text, chat_id=message.chat.id, message_id=status_msg.message_id, disable_web_page_preview=True)

if __name__ == "__main__":
    print("[IntelScope]: Starting bot polling...")
    bot.infinity_polling()

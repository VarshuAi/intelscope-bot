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

if __name__ == "__main__":
    print("[IntelScope]: Starting bot polling...")
    bot.infinity_polling()

#!/bin/bash
CHATID="383376867"
#CHATID="383376867"
KEY="1081003769:AAEpgwEhaZcpd7sSFmQJHIz53HeZuWN6q9c"
#KEY="813964407:AAHKegjwsNV46EZP_o_z9Yv1kOSx_GRAXYo"
TIME="10"
URL="https://api.telegram.org/bot$KEY/sendMessage"
TEXT='hola'
curl -s --max-time $TIME -d "chat_id=$CHATID&disable_web_page_preview=1&text=$TEXT" $URL >/dev/null
#curl -s -X POST https://api.telegram.org/botTOKENDELBOT/sendMessage -d text="Soy un robotito que anda por la vida" -d chat_id=@NOMBRECANAL


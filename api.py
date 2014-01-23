import db
import eveapi

def update_characters_for_user(userid):
    for row in db.get_characters_for_user(userid):
        sheet = eveapi.character_sheet(row.keyid, row.vcode, row.keymask, row.characterid)
        queue = eveapi.skill_queue(row.keyid, row.vcode, row.keymask, row.characterid)
        db.save_character_sheet(sheet)
        db.save_skill_queue(queue)



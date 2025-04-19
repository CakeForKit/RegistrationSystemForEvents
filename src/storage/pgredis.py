from typing import List, Optional
from uuid import UUID
from models import user, event
import psycopg2

class BaseStorage:
    def get_user_by_tg_id(self, tg_id: int) -> Optional[user.User]:
        cur = self.conn.cursor()
        cur.execute("""
            SELECT u.id, u.name, u.surname, u.papname, u.groupVuz, t.tgID
            FROM users u
            JOIN tgdata t ON t.user_id = u.id
            WHERE t.tgID = %s
        """, (tg_id,))
        row = cur.fetchone()
        cur.close()
        if row:
            return user.User(
                id=row[0],
                name=row[1],
                surname=row[2],
                papname=row[3],
                groupVuz=row[4],
                tgID=row[5]
            )
        return None
        
    def create_user(self, user_data: user.User) -> user.User:
        cur = self.conn.cursor()
        try:
            cur.execute("""
                INSERT INTO users (id, name, surname, papname, groupVuz)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                str(user_data.id),
                user_data.name,
                user_data.surname,
                user_data.papname,
                user_data.groupVuz
            ))
            
            if user_data.tgID:
                cur.execute("""
                    INSERT INTO tgdata (user_id, tgID, tg_name)
                    VALUES (%s, %s, %s)
                """, (
                    str(user_data.id),
                    user_data.tgID,
                    f"{user_data.surname} {user_data.name}"
                ))
            
            self.conn.commit()
        except psycopg2.Error:
            self.conn.rollback()
            raise
        finally:
            cur.close()
        return user_data

    def get_all_events(self) -> List[event.Event]:
        cur = self.conn.cursor()
        cur.execute("""
            SELECT id, evname, evdate, place, evdescription
            FROM event
        """)
        rows = cur.fetchall()
        cur.close()
        
        events = []
        for row in rows:
            events.append(event.Event(
                id=row[0],
                name=row[1],
                date=row[2],
                place=row[3],
                description=row[4]
            ))
        return events

    def register_user_for_event(self, user_id: UUID, event_id: UUID) -> bool:
        cur = self.conn.cursor()
        try:
            cur.execute("""
                INSERT INTO user_event (id, user_id, event_id)
                VALUES (gen_random_uuid(), %s, %s)
            """, (str(user_id), str(event_id)))
            self.conn.commit()
            return True
        except psycopg2.Error:
            self.conn.rollback()
            return False
        finally:
            cur.close()

    def cancel_registration(self, user_id: UUID, event_id: UUID) -> bool:
        cur = self.conn.cursor()
        try:
            cur.execute("""
                DELETE FROM user_event
                WHERE user_id = %s AND event_id = %s
            """, (str(user_id), str(event_id)))
            self.conn.commit()
            return cur.rowcount > 0
        except psycopg2.Error:
            self.conn.rollback()
            return False
        finally:
            cur.close()

    def get_user_registrations(self, user_id: UUID) -> List[event.Event]:
        cur = self.conn.cursor()
        cur.execute("""
            SELECT e.id, e.evname, e.evdate, e.place, e.evdescription
            FROM event e
            JOIN user_event ue ON ue.event_id = e.id
            WHERE ue.user_id = %s
        """, (str(user_id),))
        rows = cur.fetchall()
        cur.close()
        
        events = []
        for row in rows:
            events.append(event.Event(
                id=row[0],
                name=row[1],
                date=row[2],
                place=row[3],
                description=row[4]
            ))
        return events
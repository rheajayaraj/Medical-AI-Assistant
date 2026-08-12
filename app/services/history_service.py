from app.database.database import SessionLocal
from app.database.models import ChatMessage


class ChatHistoryService:

    @staticmethod
    def save_message(
        session_id,
        role,
        message
    ):

        db = SessionLocal()

        db.add(
            ChatMessage(
                session_id=session_id,
                role=role,
                message=message
            )
        )

        db.commit()

        db.close()

    @staticmethod
    def get_history(
        session_id,
        limit=20
    ):

        db = SessionLocal()

        messages = (
            db.query(ChatMessage)
            .filter(ChatMessage.session_id == session_id)
            .order_by(ChatMessage.created_at)
            .limit(limit)
            .all()
        )

        db.close()

        history = []

        for msg in messages:

            history.append({
                "role": msg.role,
                "content": msg.message
            })

        return history
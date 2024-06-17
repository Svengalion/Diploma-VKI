from app.src.feedback.dao import FeedbackDAO


async def put_feedback(feedback: str):
    feed = await FeedbackDAO.insert_data(feedback=feedback)
    return feed

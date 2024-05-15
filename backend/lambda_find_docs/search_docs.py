from constants import MONGODB_COL
from backend.utils.connect_to_mongo import connect_to_db
from backend.utils.text_cleaner import remove_stopwords
def lambda_handler(event, context=None):
    db = connect_to_db()
    collection = db[MONGODB_COL]

    docs = []
    question = remove_stopwords(event)
    for word in question.split(" "):
        results = collection.find({"tags": {"$elemMatch": {"$eq": word}}})
        docs.extend([x.get("content")[:20] for x in list(results)])

    return {
        "status_code": 200,
        "docs": docs
    }


if __name__ == "__main__":
    example = """This work can be done without a doubt and can 
                always be done better, for sure!"""
    event_example = {"text": example}
    print(lambda_handler(event=event_example))

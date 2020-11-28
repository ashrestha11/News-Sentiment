

def user_tweets(status):
    if hasattr(status, 'retweeted_status'):
        return False

    elif status.in_reply_to_status_id is not None:
        return False

    elif status.in_reply_to_screen_name is not None:
        return False

    elif status.in_reply_to_user_id is not None:
        return False
    else:
        return True
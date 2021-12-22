from .models import PostLike
import datetime


def likes_by_date(date_from, date_to):
    try:
        date_from = datetime.datetime.strptime(date_from, "%Y-%m-%d")
        date_to = datetime.datetime.strptime(date_to, "%Y-%m-%d")
    except ValueError:
        return False

    date_generated = [
        date_from + datetime.timedelta(days=x) for x in range(0, (date_to-date_from).days)]

    date_statistic = {}
    for date in date_generated:
        date_statistic[str(date.date())] = PostLike.objects.filter(updated_at__date=date, like=True).count()
    return date_statistic

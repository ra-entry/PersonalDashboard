from datetime import datetime, date


def get_due_description(due_date):

    if not due_date:
        return ""


    try:
        due = datetime.strptime(
            due_date,
            "%Y-%m-%d"
        ).date()

    except ValueError:
        return ""


    today = date.today()


    difference = (due - today).days


    if difference < 0:
        return "Overdue"

    elif difference == 0:
        return "Due today"

    elif difference == 1:
        return "Due tomorrow"

    else:
        return f"Due {due.strftime('%b %d')}"
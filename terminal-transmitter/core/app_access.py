import logging

import models
from user_access import Access

from core.db_loader import session_maker

u_access = logging.getLogger("USER ACCESS")

access = Access(
    api_history_requests=models.tables.public.ApiHistoryRequests,
    session_maker=session_maker,
    logger=u_access,
)

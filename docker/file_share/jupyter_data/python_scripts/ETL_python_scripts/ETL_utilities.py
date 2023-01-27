#universal functions

#importing public libraries
import pandas as pd
import datetime as dt
from datetime import datetime
from uuid import uuid4

#creating a unique id from date and time
def create_unique_id_from_date():
    unique_id = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
    return(unique_id)

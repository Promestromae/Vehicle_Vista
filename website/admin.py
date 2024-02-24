from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from .models import CarPrice

class CarPriceAdminView(ModelView):
    column_list = ['car_id', 'base_price', 'category']

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

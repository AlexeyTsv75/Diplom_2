class UrlData:

    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
    REGISTRATION = 'api/auth/register'
    USER = 'api/auth/user'
    LOGIN = 'api/auth/login'
    INGREDIENTS = 'api/ingredients'
    ORDER = 'api/orders'


class DataExample:
    wrong_hash_ingredients = ["1111111111", "2222222222222"]
    quantity_orders = 4


class DataAnswerMessage:
    unauthorised_user = "You should be authorised"
    need_ingredient_id = "Ingredient ids must be provided"
    existed_user = "User already exists"
    required_fields = "Email, password and name are required fields"
    incorrect_data = "email or password are incorrect"


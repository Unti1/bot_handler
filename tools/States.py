from settings import *

# States
class Form(StatesGroup):
    mail = State()  # Will be represented in storage as 'Form:mail'
    game = State()  # Will be represented in storage as 'Form:game'

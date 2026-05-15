from crud.create import insert_users, insert_product
from crud.read import (
    get_all_users,
    get_by_city,
    get_by_age,
    get_name_starting_with
)

if __name__ == "__main__":

    # CREATE
    insert_users()
    insert_product()

    # READ
    get_all_users()
    get_by_city("Palermo")
    get_by_age(30)
    get_name_starting_with("G")
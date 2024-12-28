from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile, URLInputFile, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.media_group import MediaGroupBuilder

from commands.keyboards_tg import *
from databases.querysets import *


command_router = Router()

@command_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"""\nHello @{message.from_user.username}, welcome to JN_HM_shop! \n
Here, you can browse our products and shop online with ease. Enjoy your shopping experience!""", reply_markup= kb)

@command_router.message(F.text == "Clothing")
async def clothing_handler(message: Message):
    await message.answer(f"Please choose a category below to explore our products.", reply_markup= clothing)
    await message.delete()

@command_router.message(F.text == "Shoes")
async def shoes_handler(message: Message):
    await message.answer(f"Please choose a category below to explore our products.", reply_markup= shoes)
    await message.delete()

@command_router.message(F.text == "Accessories")
async def accessories_handler(message: Message):
    await message.answer(f"Please choose a category below to explore our products.", reply_markup= accessories)
    await message.delete()

@command_router.message(F.text == "back to menu <<<")
async def start_handler(message: Message):
    await message.answer(f"You have successfully returned to the main menu. Feel free to choose another option.", reply_markup= kb)
    await message.delete()

########################################################

@command_router.message(F.text == "View all clothings")
async def all_clothing_handler(message: Message):
    await message.answer(f"All clothings available: ", reply_markup = await get_clothings_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "View all shoes")
async def all_shoes_handler(message: Message):
    await message.answer(f"All shoes available: ", reply_markup = await get_shoes_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "View all accessories")
async def all_accessories_handler(message: Message):
    await message.answer(f"All accessories available: ", reply_markup = await get_accessories_kb(page = 1))
    await message.delete()

########################################################

@command_router.message(F.text == "T-shirt")
async def tshirts_handler(message: Message):
    await message.answer(f"All T-shirts available: ", reply_markup=await get_tshirts_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Hoodies")
async def hoodies_handler(message: Message):
    await message.answer(f"All Hoodies available: ", reply_markup=await get_hoodies_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Pants")
async def pants_handler(message: Message):
    await message.answer(f"All Pants available: ", reply_markup=await get_pants_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Shirts")
async def shirts_handler(message: Message):
    await message.answer(f"All Shirts available: ", reply_markup=await get_shirts_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Jackets")
async def jackets_handler(message: Message):
    await message.answer(f"All Jackets available: ", reply_markup=await get_jackets_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Polos")
async def polos_handler(message: Message):
    await message.answer(f"All Polos available: ", reply_markup=await get_polos_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Shorts")
async def shorts_handler(message: Message):
    await message.answer(f"All Shorts available: ", reply_markup=await get_shorts_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Underwear")
async def underwear_handler(message: Message):
    await message.answer(f"All Underwear available: ", reply_markup=await get_underwear_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Socks")
async def socks_handler(message: Message):
    await message.answer(f"All Socks available: ", reply_markup=await get_socks_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Sleepwear")
async def sleepwear_handler(message: Message):
    await message.answer(f"All Sleepwear available: ", reply_markup=await get_sleepwear_kb(page = 1))
    await message.delete()

#############

@command_router.message(F.text == "Sneakers")
async def sneakers_handler(message: Message):
    await message.answer(f"All Sneakers available: ", reply_markup=await get_sneakers_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Loafers")
async def loafers_handler(message: Message):
    await message.answer(f"All Loafers available: ", reply_markup=await get_loafers_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Dress shoes")
async def dress_shoes_handler(message: Message):
    await message.answer(f"All Dress shoes available: ", reply_markup=await get_dress_shoes_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Boots")
async def boots_handler(message: Message):
    await message.answer(f"All Boots available: ", reply_markup=await get_boots_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Sandals")
async def sandals_handler(message: Message):
    await message.answer(f"All Sandals available: ", reply_markup=await get_sandals_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Slippers")
async def slippers_handler(message: Message):
    await message.answer(f"All Slippers available: ", reply_markup=await get_slippers_kb(page = 1))
    await message.delete()


#############

@command_router.message(F.text == "Glasses")
async def glasses_handler(message: Message):
    await message.answer(f"All Glasses available: ", reply_markup=await get_glasses_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Hats")
async def hats_handler(message: Message):
    await message.answer(f"All Hats available: ", reply_markup=await get_hats_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Caps")
async def caps_handler(message: Message):
    await message.answer(f"All Caps available: ", reply_markup=await get_caps_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Jewelry")
async def jewelry_handler(message: Message):
    await message.answer(f"All Jewelry available: ", reply_markup=await get_jewelry_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Belts")
async def belts_handler(message: Message):
    await message.answer(f"All Belts available: ", reply_markup=await get_belts_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Scarves")
async def scarves_handler(message: Message):
    await message.answer(f"All Scarves available: ", reply_markup=await get_scarves_kb(page = 1))
    await message.delete()

@command_router.message(F.text == "Gloves")
async def gloves_handler(message: Message):
    await message.answer(f"All Gloves available: ", reply_markup=await get_gloves_kb(page = 1))
    await message.delete()

########################################################################################################

@command_router.callback_query(F.data.startswith('product_'))
async def product_details_handler(callback: CallbackQuery):
    product_id = int(callback.data.split('_')[1])
    product = await get_product_by_id(product_id)

    if not product:
        await callback.message.answer("Product wasn't found")
        return

    album = MediaGroupBuilder(caption=(
        f'Name: {product.name}\n'
        f'Description: {product.description}\n'
        f'Price: {product.price} USD\n'
        f'Materials: {product.materials}\n'
        f'Category: {product.category}\n'
        f'Sub-category: {product.sub_category}\n'
        f'URL: {product.url or "No link"}\n'
    ))

    if product.image.startswith('http') or product.image.startswith("https"):
        album.add_photo(media=URLInputFile(product.image))
    elif product.image.startswith('AgA'):
        album.add_photo(media=product.image)
    else:
        album.add_photo(media=FSInputFile(product.image))

    await callback.message.answer_media_group(media=album.build())
    await callback.message.answer(text="Would you like to add this product to your cart?", reply_markup=await add_to_cart(product.id))

# Cart handling, adding to cart
class AddToCart(StatesGroup):
    add_quantity = State()

@command_router.callback_query(F.data.startswith('add_to_cart_'))
async def cart_handler(callback: CallbackQuery, state: FSMContext):
    product_id = int(callback.data.split('_')[3])
    await state.update_data(product_id=product_id)
    await callback.message.answer("Enter quantity:")
    await state.set_state(AddToCart.add_quantity)

@command_router.message(AddToCart.add_quantity)
async def add_quantity_handler(message: Message, state: FSMContext):
    try:
        quantity = int(message.text)
        if quantity <= 0:
            raise ValueError
    except ValueError:
        await message.answer("Please enter a valid positive integer for quantity.")
        return

    data = await state.get_data()
    product_id = data['product_id']

    product = await get_product_by_id(product_id)
    if not product:
        await message.answer("Product not found.")
        await state.clear()
        return

    cart_item = Cart(
        product_id=product_id,
        quantity=quantity,
        price=product.price * quantity
    )
    await add_product_to_cart(cart_item)

    await message.answer(f"Added {quantity} x {product.name} to your cart!")
    await state.clear()

# View cart handler
@command_router.message(F.text == "Cart")
async def view_cart_handler(message: Message):
    cart_items = await get_data_from_cart()

    if not cart_items:
        await message.answer("The cart is empty.")
        return

    cart_text = []
    total_price = 0

    for item in cart_items:
        total_price += item.price
        cart_text.append(
            f"Product: {item.product.name}\n"
            f"Description: {item.product.description}\n"
            f"Quantity: {item.quantity}\n"
            f"Price: {item.price} USD\n"
        )

    cart_text.append(f"\nTotal: {total_price:.2f} USD")
    await message.answer("\n\n".join(cart_text), reply_markup=options)
    await message.delete()

# Change quantity handler
class CartActions(StatesGroup):
    select_product = State()
    change_quantity = State()

@command_router.message(F.text == "change quantity")
async def change_quantity_start(message: Message, state: FSMContext):
    cart_items = await get_data_from_cart()

    if not cart_items:
        await message.answer("Your cart is empty.")
        return

    product_list = "\n".join([f"{item.id}. {item.product.name}" for item in cart_items])
    await message.answer(
        f"Select a product by its number:\n\n{product_list}",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_state(CartActions.select_product)

@command_router.message(CartActions.select_product)
async def select_product_for_quantity(message: Message, state: FSMContext):
    product_id = message.text.strip()
    if not product_id.isdigit():
        await message.answer("Please provide a valid product number.")
        return

    await state.update_data(selected_product=int(product_id))
    await message.answer("Enter the new quantity for the product:")
    await state.set_state(CartActions.change_quantity)

@command_router.message(CartActions.change_quantity)
async def update_quantity(message: Message, state: FSMContext):
    quantity = message.text.strip()
    if not quantity.isdigit() or int(quantity) <= 0:
        await message.answer("Please enter a valid quantity (greater than 0).")
        return

    data = await state.get_data()
    product_id = data["selected_product"]
    await update_cart_quantity(product_id, int(quantity))
    await message.answer("Quantity updated successfully!", reply_markup=options)
    await state.clear()

# Delete product from cart handler
@command_router.message(F.text == "delete product")
async def delete_product_start(message: Message):
    cart_items = await get_data_from_cart()

    if not cart_items:
        await message.answer("Your cart is empty.")
        return

    product_list = "\n".join([f"{item.id}. {item.product.name}" for item in cart_items])
    await message.answer(
        f"Select a product to delete by its number:\n\n{product_list}",
        reply_markup=ReplyKeyboardRemove(),
    )

@command_router.message(F.text.startswith("delete_"))
async def delete_product(message: Message):
    product_id = message.text.split("_")[1]
    await remove_product_from_cart(int(product_id))
    await message.answer("Product deleted successfully!", reply_markup=options)


#################################################################

@command_router.callback_query(F.data.startswith('page.clothing_'))
async def page_clothing_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_clothings_kb(page=page))

@command_router.callback_query(F.data.startswith('page.tshirt_'))
async def page_tshirt_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_tshirts_kb(page=page))

@command_router.callback_query(F.data.startswith('page.hoodie_'))
async def page_hoodie_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_hoodies_kb(page=page))

@command_router.callback_query(F.data.startswith('page.pant_'))
async def page_pants_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_pants_kb(page=page))

@command_router.callback_query(F.data.startswith('page.shirt_'))
async def page_shirt_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_shirts_kb(page=page))

@command_router.callback_query(F.data.startswith('page.jacket_'))
async def page_jacket_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_jackets_kb(page=page))

@command_router.callback_query(F.data.startswith('page.polo_'))
async def page_polo_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_polos_kb(page=page))

@command_router.callback_query(F.data.startswith('page.short_'))
async def page_short_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_shorts_kb(page=page))

@command_router.callback_query(F.data.startswith('page.underwear_'))
async def page_underwear_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_underwear_kb(page=page))

@command_router.callback_query(F.data.startswith('page.sock_'))
async def page_sock_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_socks_kb(page=page))

@command_router.callback_query(F.data.startswith('page.sleepwear_'))
async def page_sleepwear_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_sleepwear_kb(page=page))

@command_router.callback_query(F.data.startswith('page.shoe_'))
async def page_shoe_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_shoes_kb(page=page))

@command_router.callback_query(F.data.startswith('page.sneaker_'))
async def page_sneaker_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_sneakers_kb(page=page))

@command_router.callback_query(F.data.startswith('page.loafer_'))
async def page_loafer_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_loafers_kb(page=page))

@command_router.callback_query(F.data.startswith('page.dress_shoe_'))
async def page_dress_shoe_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_dress_shoes_kb(page=page))

@command_router.callback_query(F.data.startswith('page.boot_'))
async def page_boot_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_boots_kb(page=page))

@command_router.callback_query(F.data.startswith('page.sandal_'))
async def page_sandal_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_sandals_kb(page=page))

@command_router.callback_query(F.data.startswith('page.slipper_'))
async def page_slipper_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_slippers_kb(page=page))

@command_router.callback_query(F.data.startswith('page.accessory_'))
async def page_accessory_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1]
    page = int(data)
    await callback.message.edit_reply_markup(reply_markup=await get_accessories_kb(page=page))


#################################################################
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from config import ADMIN_ID
from databases.querysets import * 
from databases.models import Product

admin_router = Router()

class AddProduct(StatesGroup):
    add_name = State()
    add_description = State()
    add_price = State()
    add_image = State()
    add_material = State()
    add_category = State()
    add_sub_category = State()
    add_url = State()

async def check_admin(message: Message):
    return message.from_user.id == ADMIN_ID

@admin_router.message(Command('add_product'))
async def add_product_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!")
        return

    await message.answer('Введите название продукта:')
    await state.set_state(AddProduct.add_name)

@admin_router.message(AddProduct.add_name)
async def add_product_name(message: Message, state: FSMContext):
    await state.update_data(add_name=message.text)
    await message.answer('Введите описание продукта:')
    await state.set_state(AddProduct.add_description)

@admin_router.message(AddProduct.add_description)
async def add_product_description(message: Message, state: FSMContext):
    await state.update_data(add_description=message.text)
    await message.answer('Введите цену продукта (например, 80.0):')
    await state.set_state(AddProduct.add_price)

@admin_router.message(AddProduct.add_price)
async def add_product_price(message: Message, state: FSMContext):
    try:
        price = float(message.text)
        await state.update_data(add_price=price)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное значение для цены (например, 80.0).")
        return

    await message.answer('Отправьте изображение продукта:')
    await state.set_state(AddProduct.add_image)

@admin_router.message(AddProduct.add_image)
async def add_product_image(message: Message, state: FSMContext):
    if not message.photo:
        await message.answer("Пожалуйста, отправьте изображение.")
        return
    await state.update_data(add_image=message.photo[-1].file_id)
    await message.answer('Введите материалы продукта (например, Cotton 100%):')
    await state.set_state(AddProduct.add_material)

@admin_router.message(AddProduct.add_material)
async def add_product_material(message: Message, state: FSMContext):
    await state.update_data(add_material=message.text)
    await message.answer('Введите категорию продукта (например, Clothing):')
    await state.set_state(AddProduct.add_category)

@admin_router.message(AddProduct.add_category)
async def add_product_category(message: Message, state: FSMContext):
    await state.update_data(add_category=message.text)
    await message.answer('Введите подкатегорию продукта (например, Hoodies & Sweatshirts):')
    await state.set_state(AddProduct.add_sub_category)

@admin_router.message(AddProduct.add_sub_category)
async def add_product_sub_category(message: Message, state: FSMContext):
    await state.update_data(add_sub_category=message.text)
    await message.answer('Введите URL продукта:')
    await state.set_state(AddProduct.add_url)

@admin_router.message(AddProduct.add_url)
async def add_product_url(message: Message, state: FSMContext):
    await state.update_data(add_url=message.text)
    data = await state.get_data()

    # Create the product object
    product = Product(
        name=data['add_name'],
        description=data['add_description'],
        price=data['add_price'],
        image=data['add_image'],
        materials=data['add_material'],
        category=data['add_category'],
        sub_category=data['add_sub_category'],
        url=data['add_url']
    )
    # Call the admin-specific function
    await add_product_by_admin(product, message.from_user.id)

    await message.answer(f'✅ Продукт успешно добавлен!\n\n'
                         f'Название: {data["add_name"]}\n'
                         f'Описание: {data["add_description"]}\n'
                         f'Цена: {data["add_price"]}\n'
                         f'Материалы: {data["add_material"]}\n'
                         f'Категория: {data["add_category"]}\n'
                         f'Подкатегория: {data["add_sub_category"]}\n'
                         f'URL: {data["add_url"]}')
    await state.clear()

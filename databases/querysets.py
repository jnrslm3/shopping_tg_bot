from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session, joinedload
from databases.models import *

async def add_product():
    async with async_session() as session:
        product = Product(
            name = "HM hoodie",
            description = "BLa bla bla",
            price = 80.0,
            image = "other/image.png",
            materials = "cotton 100%",
            category = "clothing",
            sub_category = "Hoodies & Sweatshirts",
            url = "https://www2.hm.com/en_us/productpage.1034065168.html"
        )
        session.add(product)
        await session.commit()

async def add_product_by_admin(product: Product, admin_id: int):
    async with async_session() as session:
        session.add(product)
        await session.commit()

# Add product to cart
async def add_product_to_cart(cart_item):
    async with async_session() as session:
        session.add(cart_item)
        await session.commit()

# Get product by ID
async def get_product_by_id(product_id):
    async with async_session() as session:
        result = await session.execute(select(Product).where(Product.id == product_id))
        return result.scalar_one_or_none()

# Get data from cart
async def get_data_from_cart():
    async with async_session() as session:
        result = await session.execute(select(Cart).options(joinedload(Cart.product)))
        return result.scalars().all()

# Update cart quantity
async def update_cart_quantity(product_id: int, new_quantity: int):
    async with async_session() as session:
        result = await session.execute(select(Cart).where(Cart.product_id == product_id))
        cart_item = result.scalar_one_or_none()

        if cart_item:
            cart_item.quantity = new_quantity
            cart_item.price = cart_item.product.price * new_quantity
            await session.commit()

# Remove product from cart
async def remove_product_from_cart(product_id: int):
    async with async_session() as session:
        await session.execute(delete(Cart).where(Cart.product_id == product_id))
        await session.commit()
########################################################################################

async def all_products(limit, offset):
    async with async_session() as session:
        result = await session.scalars(select(Product).offset(offset).limit(limit))
        return result.all()

async def all_clothing(limit, offset):
    async with async_session() as session:
        result = await session.scalars(
            select(Product).where(Product.category.ilike("clothing")).offset(offset).limit(limit)
        )
        return result.all()

async def all_shoes(limit, offset):
    async with async_session() as session:
        result = await session.scalars(
            select(Product).where(Product.category.ilike("shoes")).offset(offset).limit(limit)
        )
        return result.all()

async def all_accessories(limit, offset):
    async with async_session() as session:
        result = await session.scalars(
            select(Product).where(Product.category.ilike("accessories")).offset(offset).limit(limit)
        )
        return result.all()

########################################################################################


async def get_product_by_name(name: str):
    async with async_session() as session:
        result = await session.scalars(select(Product).where(Product.name.ilike(f"%{name}%")))
        return result.all()

async def get_product_by_category(category: str):
    async with async_session() as session:
        result = await session.scalars(
            select(Product).where(Product.category.ilike(f"%{category}%"))
        )
        return result.all()

async def all_products_by_subcategory(sub_category, limit, offset):
    async with async_session() as session:
        result = await session.scalars(
            select(Product).where(Product.sub_category.ilike(f"%{sub_category}%"))
            .offset(offset).limit(limit)
        )
        return result.all()

async def all_tshirts(limit, offset):
    return await all_products_by_subcategory("T-shirt", limit, offset)

async def all_hoodies(limit, offset):
    return await all_products_by_subcategory("Hoodies", limit, offset)

async def all_pants(limit, offset):
    return await all_products_by_subcategory("Pants", limit, offset)

async def all_shirts(limit, offset):
    return await all_products_by_subcategory("Shirts", limit, offset)

async def all_jackets(limit, offset):
    return await all_products_by_subcategory("Jackets", limit, offset)

async def all_polos(limit, offset):
    return await all_products_by_subcategory("Polos", limit, offset)

async def all_shorts(limit, offset):
    return await all_products_by_subcategory("Shorts", limit, offset)

async def all_underwear(limit, offset):
    return await all_products_by_subcategory("Underwear", limit, offset)

async def all_socks(limit, offset):
    return await all_products_by_subcategory("Socks", limit, offset)

async def all_sleepwear(limit, offset):
    return await all_products_by_subcategory("Sleepwear", limit, offset)

async def all_sneakers(limit, offset):
    return await all_products_by_subcategory("Sneakers", limit, offset)

async def all_loafers(limit, offset):
    return await all_products_by_subcategory("Loafers", limit, offset)

async def all_dress_shoes(limit, offset):
    return await all_products_by_subcategory("Dress shoes", limit, offset)

async def all_boots(limit, offset):
    return await all_products_by_subcategory("Boots", limit, offset)

async def all_sandals(limit, offset):
    return await all_products_by_subcategory("Sandals", limit, offset)

async def all_slippers(limit, offset):
    return await all_products_by_subcategory("Slippers", limit, offset)

async def all_glasses(limit, offset):
    return await all_products_by_subcategory("Glasses", limit, offset)

async def all_hats(limit, offset):
    return await all_products_by_subcategory("Hats", limit, offset)

async def all_caps(limit, offset):
    return await all_products_by_subcategory("Caps", limit, offset)

async def all_jewelry(limit, offset):
    return await all_products_by_subcategory("Jewelry", limit, offset)

async def all_belts(limit, offset):
    return await all_products_by_subcategory("Belts", limit, offset)

async def all_scarves(limit, offset):
    return await all_products_by_subcategory("Scarves", limit, offset)

async def all_gloves(limit, offset):
    return await all_products_by_subcategory("Gloves", limit, offset)
########################################################################################
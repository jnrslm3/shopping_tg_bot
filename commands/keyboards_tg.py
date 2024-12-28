from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from databases.querysets import *


kb = ReplyKeyboardMarkup(
   keyboard=[
        [KeyboardButton(text='Clothing')],
        [KeyboardButton(text='Shoes')],
        [KeyboardButton(text='Accessories')],
        [KeyboardButton(text='Cart')],
    ],
    resize_keyboard=True
)

clothing = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='T-shirt')],
        [KeyboardButton(text='Hoodies')],
        [KeyboardButton(text='Pants')],
        [KeyboardButton(text='Shirts')],
        [KeyboardButton(text='Jackets')],
        [KeyboardButton(text='Polos')],
        [KeyboardButton(text='Shorts')],
        [KeyboardButton(text='Underwear')],
        [KeyboardButton(text='Socks')],
        [KeyboardButton(text='Sleepwear')],
        [KeyboardButton(text='View all clothings')],
        [KeyboardButton(text='back to menu <<<')],
    ],
    resize_keyboard= True
)

shoes = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Sneakers')],
        [KeyboardButton(text='Loafers')],
        [KeyboardButton(text='Dress shoes')],
        [KeyboardButton(text='Boots')],
        [KeyboardButton(text='Sandals')],
        [KeyboardButton(text='Slippers')],
        [KeyboardButton(text='View all shoes')],
        [KeyboardButton(text='back to menu <<<')],
    ],
    resize_keyboard= True
)

accessories = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Glasses')],
        [KeyboardButton(text='Hats')],
        [KeyboardButton(text='Caps')],
        [KeyboardButton(text='Jewelry')],
        [KeyboardButton(text='Belts')],
        [KeyboardButton(text='Scarves')],
        [KeyboardButton(text='Gloves')],
        [KeyboardButton(text='View all accessories')],
        [KeyboardButton(text='back to menu <<<')],
    ],
    resize_keyboard= True
)


async def add_to_cart(product_id: int):
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Add to Cart", callback_data=f"add_to_cart_{product_id}"))
    return kb.adjust(1).as_markup()

    
options = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='change quantity')],
        [KeyboardButton(text='delete product')],
        [KeyboardButton(text='back to menu <<<')],
    ],
    resize_keyboard= True
)

################################################
PAGE_SIZE = 2

async def get_clothings_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    clothings = await all_clothing(offset=offset, limit=PAGE_SIZE)
    for clothing in clothings:
        kb.add(InlineKeyboardButton(text=clothing.name, callback_data=f"product_{clothing.id}"))
    
    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.clothing_{page - 1}"))

    if len(clothings) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.clothing_{page + 1}"))
    
    return kb.adjust(2).as_markup()

async def get_tshirts_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    tshirts = await all_tshirts(offset=offset, limit=PAGE_SIZE)
    for tshirt in tshirts:
        kb.add(InlineKeyboardButton(text=tshirt.name, callback_data=f"product_{tshirt.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.tshirt_{page - 1}"))

    if len(tshirts) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.tshirt_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_hoodies_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    hoodies = await all_hoodies(offset=offset, limit=PAGE_SIZE)
    for hoodie in hoodies:
        kb.add(InlineKeyboardButton(text=hoodie.name, callback_data=f"product_{hoodie.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.hoodie_{page - 1}"))

    if len(hoodies) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.hoodie_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_pants_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    pants = await all_pants(offset=offset, limit=PAGE_SIZE)
    for pant in pants:
        kb.add(InlineKeyboardButton(text=pant.name, callback_data=f"product_{pant.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.pant_{page - 1}"))

    if len(pants) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.pant_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_shirts_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    shirts = await all_shirts(offset=offset, limit=PAGE_SIZE)
    for shirt in shirts:
        kb.add(InlineKeyboardButton(text=shirt.name, callback_data=f"product_{shirt.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.shirt_{page - 1}"))

    if len(shirts) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.shirt_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_jackets_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    jackets = await all_jackets(offset=offset, limit=PAGE_SIZE)
    for jacket in jackets:
        kb.add(InlineKeyboardButton(text=jacket.name, callback_data=f"product_{jacket.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.jacket_{page - 1}"))

    if len(jackets) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.jacket_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_polos_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    polos = await all_polos(offset=offset, limit=PAGE_SIZE)
    for polo in polos:
        kb.add(InlineKeyboardButton(text=polo.name, callback_data=f"product_{polo.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.polo_{page - 1}"))

    if len(polos) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.polo_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_shorts_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    shorts = await all_shorts(offset=offset, limit=PAGE_SIZE)
    for short in shorts:
        kb.add(InlineKeyboardButton(text=short.name, callback_data=f"product_{short.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.short_{page - 1}"))

    if len(shorts) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.short_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_underwear_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    underwear = await all_underwear(offset=offset, limit=PAGE_SIZE)
    for item in underwear:
        kb.add(InlineKeyboardButton(text=item.name, callback_data=f"product_{item.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.underwear_{page - 1}"))

    if len(underwear) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.underwear_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_socks_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    socks = await all_socks(offset=offset, limit=PAGE_SIZE)
    for sock in socks:
        kb.add(InlineKeyboardButton(text=sock.name, callback_data=f"product_{sock.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.sock_{page - 1}"))

    if len(socks) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.sock_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_sleepwear_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    sleepwear = await all_sleepwear(offset=offset, limit=PAGE_SIZE)
    for item in sleepwear:
        kb.add(InlineKeyboardButton(text=item.name, callback_data=f"product_{item.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.sleepwear_{page - 1}"))

    if len(sleepwear) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.sleepwear_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_shoes_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    shoes = await all_shoes(offset=offset, limit=PAGE_SIZE)
    for shoe in shoes:
        kb.add(InlineKeyboardButton(text=shoe.name, callback_data=f"product_{shoe.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.shoe_{page - 1}"))

    if len(shoes) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.shoe_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_sneakers_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    sneakers = await all_sneakers(offset=offset, limit=PAGE_SIZE)
    for sneaker in sneakers:
        kb.add(InlineKeyboardButton(text=sneaker.name, callback_data=f"product_{sneaker.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.sneaker_{page - 1}"))

    if len(sneakers) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.sneaker_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_loafers_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    loafers = await all_loafers(offset=offset, limit=PAGE_SIZE)
    for loafer in loafers:
        kb.add(InlineKeyboardButton(text=loafer.name, callback_data=f"product_{loafer.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.loafer_{page - 1}"))

    if len(loafers) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.loafer_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_dress_shoes_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    dress_shoes = await all_dress_shoes(offset=offset, limit=PAGE_SIZE)
    for dress_shoe in dress_shoes:
        kb.add(InlineKeyboardButton(text=dress_shoe.name, callback_data=f"product_{dress_shoe.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.dress_shoe_{page - 1}"))

    if len(dress_shoes) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.dress_shoe_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_boots_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    boots = await all_boots(offset=offset, limit=PAGE_SIZE)
    for boot in boots:
        kb.add(InlineKeyboardButton(text=boot.name, callback_data=f"product_{boot.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.boot_{page - 1}"))

    if len(boots) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.boot_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_sandals_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    sandals = await all_sandals(offset=offset, limit=PAGE_SIZE)
    for sandal in sandals:
        kb.add(InlineKeyboardButton(text=sandal.name, callback_data=f"product_{sandal.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.sandal_{page - 1}"))

    if len(sandals) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.sandal_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_slippers_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    slippers = await all_slippers(offset=offset, limit=PAGE_SIZE)
    for slipper in slippers:
        kb.add(InlineKeyboardButton(text=slipper.name, callback_data=f"product_{slipper.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.slipper_{page - 1}"))

    if len(slippers) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.slipper_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_accessories_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    accessories = await all_accessories(offset=offset, limit=PAGE_SIZE)
    for accessory in accessories:
        kb.add(InlineKeyboardButton(text=accessory.name, callback_data=f"product_{accessory.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.accessory_{page - 1}"))

    if len(accessories) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.accessory_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_bags_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    bags = await all_bags(offset=offset, limit=PAGE_SIZE)
    for bag in bags:
        kb.add(InlineKeyboardButton(text=bag.name, callback_data=f"product_{bag.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.bag_{page - 1}"))

    if len(bags) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.bag_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_hats_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    hats = await all_hats(offset=offset, limit=PAGE_SIZE)
    for hat in hats:
        kb.add(InlineKeyboardButton(text=hat.name, callback_data=f"product_{hat.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.hat_{page - 1}"))

    if len(hats) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.hat_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_scarves_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    scarves = await all_scarves(offset=offset, limit=PAGE_SIZE)
    for scarf in scarves:
        kb.add(InlineKeyboardButton(text=scarf.name, callback_data=f"product_{scarf.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.scarf_{page - 1}"))

    if len(scarves) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.scarf_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_gloves_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    gloves = await all_gloves(offset=offset, limit=PAGE_SIZE)
    for glove in gloves:
        kb.add(InlineKeyboardButton(text=glove.name, callback_data=f"product_{glove.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.glove_{page - 1}"))

    if len(gloves) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.glove_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_sunglasses_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    sunglasses = await all_sunglasses(offset=offset, limit=PAGE_SIZE)
    for sunglass in sunglasses:
        kb.add(InlineKeyboardButton(text=sunglass.name, callback_data=f"product_{sunglass.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.sunglass_{page - 1}"))

    if len(sunglasses) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.sunglass_{page + 1}"))

    return kb.adjust(2).as_markup()


async def get_hats_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    hats = await all_hats(offset=offset, limit=PAGE_SIZE)
    for hat in hats:
        kb.add(InlineKeyboardButton(text=hat.name, callback_data=f"product_{hat.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.hats_{page - 1}"))

    if len(hats) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.hats_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_caps_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    caps = await all_caps(offset=offset, limit=PAGE_SIZE)
    for cap in caps:
        kb.add(InlineKeyboardButton(text=cap.name, callback_data=f"product_{cap.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.caps_{page - 1}"))

    if len(caps) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.caps_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_jewelry_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    jewelry = await all_jewelry(offset=offset, limit=PAGE_SIZE)
    for item in jewelry:
        kb.add(InlineKeyboardButton(text=item.name, callback_data=f"product_{item.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.jewelry_{page - 1}"))

    if len(jewelry) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.jewelry_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_belts_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    belts = await all_belts(offset=offset, limit=PAGE_SIZE)
    for belt in belts:
        kb.add(InlineKeyboardButton(text=belt.name, callback_data=f"product_{belt.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.belts_{page - 1}"))

    if len(belts) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.belts_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_scarves_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    scarves = await all_scarves(offset=offset, limit=PAGE_SIZE)
    for scarf in scarves:
        kb.add(InlineKeyboardButton(text=scarf.name, callback_data=f"product_{scarf.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.scarves_{page - 1}"))

    if len(scarves) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.scarves_{page + 1}"))

    return kb.adjust(2).as_markup()

async def get_gloves_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    gloves = await all_gloves(offset=offset, limit=PAGE_SIZE)
    for glove in gloves:
        kb.add(InlineKeyboardButton(text=glove.name, callback_data=f"product_{glove.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text=" ◀️ ", callback_data=f"page.gloves_{page - 1}"))

    if len(gloves) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text=" ▶️ ", callback_data=f"page.gloves_{page + 1}"))

    return kb.adjust(2).as_markup()


############################################################\



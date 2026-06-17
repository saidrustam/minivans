from pathlib import Path
from datetime import date
import html
import json
import math
import re

ROOT = Path(__file__).resolve().parents[1]
SITE_URL = "https://minivan24.uz"

PHONE = "+998 99 008 4000"
PHONE_HREF = "tel:+998990084000"
EMAIL = "info@minivan24.uz"
ADDRESS = "Ташкент, улица Амир Темур 99а"
TELEGRAM = "https://t.me/minivanuzb"
WHATSAPP = "https://wa.me/998990084000"
INSTAGRAM = "https://www.instagram.com/minivanuz/profilecard/?igsh=YmN3bm9vbjE0ajNq"
LOGO = "uploads/2024/11/minivan24-logo.png"
FAVICON = "uploads/2024/11/minivan24-favicon.png"
DEFAULT_HERO = "uploads/2024/11/mercedes-sprinter-hero.webp"
CARS_HERO = "uploads/2026/06/cars-hero-fleet-2k.webp"
SERVICES_HERO = "uploads/2026/06/services-hero-transport-2k.webp"
NEWS_HERO = SERVICES_HERO
CONTACTS_HERO = SERVICES_HERO
HOME_HERO = "uploads/2026/06/services-hero-transport-2k.webp"
HOME_FEATURED_CAR_IMAGE = "uploads/2026/06/home-kia-carnival-feature-2k.webp"
HOME_SERVICE_MINIVAN_IMAGE = "uploads/2026/06/home-service-minivan-tashkent-2k.webp"
HOME_SERVICE_AIRPORT_IMAGE = "uploads/2026/06/home-service-airport-transfer-2k.webp"
HOME_SERVICE_WEDDING_IMAGE = "uploads/2026/06/home-service-wedding-sprinter-2k.webp"
CHECK_BADGE_ICON = "assets/icons/check-badge.svg"
NEWS_PAGE_SIZE = 12
TODAY = date.today().isoformat()

SERVICES = [
    {
        "slug": "arenda-minivena-v-tashkente",
        "title": "Аренда минивэна в Ташкенте",
        "seo_title": "Аренда минивэна в Ташкенте с водителем и без | Minivan24",
        "seo_description": "Аренда минивэна в Ташкенте для семьи, гостей, трансфера и поездок по Узбекистану. KIA Carnival, Toyota Sienna, Hyundai H-1, заявка в WhatsApp.",
        "lead": "Подберём минивэн под количество пассажиров, багаж, маршрут и формат поездки: город, аэропорт, свадьба, экскурсия или междугородний маршрут.",
        "image": "uploads/2026/06/service-minivan-tashkent-city.webp",
        "eyebrow": "Минивэны",
        "audience": ["семьи с детьми и багажом", "деловые гости и делегации", "туристы в Ташкенте", "трансферы аэропорт-отель"],
        "benefits": [
            ("7-8 посадочных мест", "Комфортный формат для семьи, небольшой группы или VIP-гостей."),
            ("С водителем или без", "Подскажем подходящий формат аренды под ваш маршрут и опыт вождения."),
            ("Подача по адресу", "Аэропорт, вокзал, отель, ресторан, офис или частный адрес в Ташкенте."),
            ("Понятный расчёт", "Стоимость зависит от даты, времени, маршрута, ожидания и багажа."),
        ],
        "steps": [
            "Уточняем дату, время подачи и финальную точку маршрута.",
            "Считаем пассажиров, багаж, детские кресла и дополнительные остановки.",
            "Предлагаем подходящую модель и фиксируем условия до поездки.",
        ],
        "faq": [
            ("Можно ли заказать минивэн на несколько часов?", "Да, минивэн можно заказать для короткого трансфера, городской поездки, вечернего мероприятия или аренды на день."),
            ("Какой минивэн выбрать для 6-7 человек?", "Обычно подходят KIA Carnival, Toyota Sienna или Hyundai H-1. Если багажа много, лучше заранее указать количество чемоданов."),
            ("Работаете ли вы с туристами из других стран?", "Да, встречаем гостей в аэропорту, помогаем с маршрутом по Ташкенту и поездками по регионам Узбекистана."),
        ],
        "related_cars": ["kia-carnival", "toyota-sienna", "hyundai-h-1"],
        "related_articles": ["kak-vybrat-minivjen-dlja-bolshoj-semi", "arenda-minivena-s-bolshim-bagazhnikom-chemodany-kolyaski-sportinventar"],
    },
    {
        "slug": "arenda-mikroavtobusa-v-tashkente",
        "title": "Аренда микроавтобуса в Ташкенте",
        "seo_title": "Аренда микроавтобуса в Ташкенте для группы | Minivan24",
        "seo_description": "Аренда микроавтобуса в Ташкенте для трансфера, экскурсий, свадьбы, делегации и поездок по Узбекистану. Mercedes-Benz Sprinter, Hyundai Starex.",
        "lead": "Микроавтобус удобен, когда нужно перевезти группу с багажом, сохранить общий маршрут и заранее понимать стоимость поездки.",
        "image": "uploads/2026/06/service-minibus-samarkand-registan.webp",
        "eyebrow": "Микроавтобусы",
        "audience": ["туристические группы", "корпоративные поездки", "свадебные гости", "междугородние маршруты"],
        "benefits": [
            ("До 11+ мест", "Подбираем вместимость под реальное количество пассажиров и багажа."),
            ("Опытный водитель", "Маршрут, ожидания, остановки и подача согласуются заранее."),
            ("Город и регионы", "Ташкент, Самарканд, Бухара, Чарвак и другие направления."),
            ("Без сюрпризов", "Обсуждаем время, километраж, ожидание, ночёвку водителя и доплаты до старта."),
        ],
        "steps": [
            "Определяем состав группы, багаж и требования к салону.",
            "Согласовываем маршрут, длительность, ожидание и обратную подачу.",
            "Подбираем микроавтобус и отправляем финальные условия бронирования.",
        ],
        "faq": [
            ("Когда нужен микроавтобус, а не минивэн?", "Если пассажиров больше 7-8, много багажа или маршрут длинный, микроавтобус обычно комфортнее и экономичнее."),
            ("Можно ли поехать из Ташкента в Самарканд?", "Да, организуем междугородние поездки и многодневные маршруты по Узбекистану."),
            ("Цена считается за день или за маршрут?", "Зависит от задачи: трансфер, почасовая аренда, аренда на день или межгород считаются по-разному."),
        ],
        "related_cars": ["mercedes-benz-sprinter", "hyundai-starex", "hyundai-starex-2"],
        "related_articles": ["arenda-mikroavtobusa", "skolko-stoit-arenda-mikroavtobusa-v-tashkente-polnyy-razbor-tsen"],
    },
    {
        "slug": "arenda-avto-s-voditelem-v-tashkente",
        "title": "Аренда авто с водителем в Ташкенте",
        "seo_title": "Аренда авто с водителем в Ташкенте | Minivan24",
        "seo_description": "Аренда авто с водителем в Ташкенте для деловых встреч, трансферов, экскурсий, семейных поездок и мероприятий. Минивэны и микроавтобусы.",
        "lead": "Водитель берёт на себя маршрут, парковки, ожидание и дорожные нюансы, а вы сохраняете время и спокойный график.",
        "image": "uploads/2026/06/service-car-with-driver-tashkent-city.webp",
        "eyebrow": "С водителем",
        "audience": ["деловые встречи", "встреча гостей", "поездки по городу", "маршруты по регионам"],
        "benefits": [
            ("Пунктуальная подача", "Время и адрес фиксируются заранее, включая аэропорт и вокзал."),
            ("Маршрут под задачу", "Помогаем спланировать остановки, ожидание и обратную поездку."),
            ("Чистый автомобиль", "Минивэны и микроавтобусы подходят для гостей, семьи и делегаций."),
            ("Связь до поездки", "Заявку можно быстро отправить в WhatsApp или Telegram."),
        ],
        "steps": [
            "Получаем маршрут, дату, время и количество пассажиров.",
            "Уточняем формат: трансфер, аренда на часы, день или межгород.",
            "Подтверждаем автомобиль, водителя и стоимость.",
        ],
        "faq": [
            ("Можно ли заказать водителя на весь день?", "Да, аренда на день подходит для деловых встреч, экскурсий и поездок по нескольким адресам."),
            ("Водитель встретит в аэропорту?", "Да, можно согласовать встречу, ожидание рейса и помощь с багажом."),
            ("Можно ли изменить маршрут в день поездки?", "Небольшие изменения обычно возможны, но лучше согласовать их заранее, чтобы корректно рассчитать время и стоимость."),
        ],
        "related_cars": ["kia-carnival", "hyundai-h-1", "mercedes-benz-sprinter"],
        "related_articles": ["arenda-avto-s-voditelem-v-tashkente", "preimuschestva-arendy-mikroavtobusa-s-voditelem"],
    },
    {
        "slug": "transfer-aeroport-tashkent",
        "title": "Трансфер из аэропорта Ташкента",
        "seo_title": "Трансфер из аэропорта Ташкента на минивэне | Minivan24",
        "seo_description": "Трансфер из аэропорта Ташкента на минивэне или микроавтобусе для семьи, туристов и делегаций. Встреча, багаж, подача к рейсу.",
        "lead": "Организуем встречу в аэропорту, подачу минивэна или микроавтобуса, место для багажа и спокойную поездку до отеля, офиса или другого города.",
        "image": "uploads/2026/06/service-airport-transfer-tashkent.webp",
        "eyebrow": "Аэропорт",
        "audience": ["прилёт семьи", "встреча делегации", "туристическая группа", "трансфер в другой город"],
        "benefits": [
            ("Встреча рейса", "Учитываем время прилёта, багаж и возможное ожидание."),
            ("Место для чемоданов", "Подбираем класс авто с учётом пассажиров и багажа."),
            ("Подача 24/7", "Можно заказать ранний, ночной или срочный трансфер."),
            ("Дальше Ташкента", "По запросу едем в Самарканд, Чарвак и другие направления."),
        ],
        "steps": [
            "Получаем номер рейса, дату и время прилёта.",
            "Уточняем пассажиров, багаж, детские кресла и конечный адрес.",
            "Подтверждаем автомобиль, место встречи и контакт водителя.",
        ],
        "faq": [
            ("Что делать, если рейс задержали?", "Сообщите нам номер рейса: при расчёте можно заранее учесть ожидание и корректировку времени подачи."),
            ("Можно ли заказать большой микроавтобус в аэропорт?", "Да, для групп и делегаций подойдёт Mercedes-Benz Sprinter или Hyundai Starex."),
            ("Есть ли трансфер из аэропорта в Самарканд?", "Да, возможны междугородние трансферы из аэропорта Ташкента по согласованному маршруту."),
        ],
        "related_cars": ["kia-carnival", "hyundai-starex", "mercedes-benz-sprinter"],
        "related_articles": ["transfer-v-ajeroportu-tashkenta", "transfer-v-tashkente-iz-aeroporta-puteshestvie-bez-stressa"],
    },
    {
        "slug": "mikroavtobus-na-svadbu",
        "title": "Микроавтобус на свадьбу в Ташкенте",
        "seo_title": "Аренда микроавтобуса на свадьбу в Ташкенте | Minivan24",
        "seo_description": "Аренда минивэна или микроавтобуса на свадьбу в Ташкенте для гостей, кортежа и развоза после мероприятия. Подача по адресам.",
        "lead": "Помогаем организовать развоз гостей, встречу родственников, поездку между локациями и возвращение после мероприятия без хаоса в расписании.",
        "image": "uploads/2026/06/service-wedding-premium-sprinter-bukhara.webp",
        "eyebrow": "Свадьбы",
        "audience": ["развоз гостей", "встреча родственников", "кортеж минивэнов", "вечернее возвращение"],
        "benefits": [
            ("Единый график", "Маршрут и время подачи фиксируются до мероприятия."),
            ("Несколько адресов", "Можно запланировать ресторан, ЗАГС, фотосессию и обратный развоз."),
            ("Комфорт для гостей", "Вместительный салон, кондиционер и место для вещей."),
            ("Вечерняя подача", "Согласуем позднее возвращение после банкета."),
        ],
        "steps": [
            "Собираем список адресов, время церемонии и банкета.",
            "Считаем гостей по направлениям и выбираем класс транспорта.",
            "Фиксируем маршрут, ответственного контактного человека и стоимость.",
        ],
        "faq": [
            ("Можно ли заказать несколько машин?", "Да, для больших свадеб можно комбинировать минивэны и микроавтобусы."),
            ("Можно ли сделать развоз гостей после банкета?", "Да, заранее согласуем время окончания, адреса и количество направлений."),
            ("Нужно ли платить за ожидание?", "Если водитель ждёт между этапами, ожидание лучше заранее включить в расчёт."),
        ],
        "related_cars": ["kia-carnival", "hyundai-starex", "mercedes-benz-sprinter"],
        "related_articles": ["arenda-mikroavtobusa-na-svadbu-razvoz-gostey-bez-zaderzhek-i-doplat"],
    },
    {
        "slug": "poezdki-po-uzbekistanu",
        "title": "Поездки по Узбекистану на минивэне",
        "seo_title": "Минивэн или микроавтобус для поездки по Узбекистану | Minivan24",
        "seo_description": "Аренда минивэна или микроавтобуса для поездок по Узбекистану: Самарканд, Бухара, Хива, Чарвак, групповые туры и семейные маршруты.",
        "lead": "Подберём транспорт для однодневной поездки, многодневного тура или маршрута между городами Узбекистана с понятным расчётом и комфортным салоном.",
        "image": "uploads/2026/06/service-uzbekistan-mountain-trip.webp",
        "eyebrow": "Маршруты",
        "audience": ["Самарканд и Бухара", "Чарвак и горы", "семейный тур", "групповая экскурсия"],
        "benefits": [
            ("Маршрут под группу", "Учитываем расстояние, остановки, питание, багаж и время в пути."),
            ("Междугородний опыт", "Подбираем транспорт и водителя под длинную дорогу."),
            ("Гибкий график", "Можно ехать одним днём или строить многодневный маршрут."),
            ("Комфорт в пути", "Кондиционер, просторный салон и место для чемоданов."),
        ],
        "steps": [
            "Получаем города, даты, примерное количество остановок и ночёвок.",
            "Считаем пассажиров, багаж и требования к автомобилю.",
            "Предлагаем формат аренды и финальный маршрутный расчёт.",
        ],
        "faq": [
            ("Какие направления самые популярные?", "Часто заказывают Самарканд, Бухару, Чарвак, горные маршруты и обзорные поездки по Ташкенту."),
            ("Можно ли ехать на несколько дней?", "Да, многодневные маршруты согласуются заранее с учётом графика водителя и ночёвок."),
            ("Что влияет на цену межгорода?", "Расстояние, длительность, ожидание, ночёвка, сезон, класс автомобиля и количество пассажиров."),
        ],
        "related_cars": ["mercedes-benz-sprinter", "hyundai-starex", "toyota-sienna"],
        "related_articles": ["top-5-populjarnyh-marshrutov-po-uzbekistanu", "marshruty-po-uzbekistanu-dlya-samostoyatelnyh-poezdok-gotovye-treki-vremya-v-puti-i-udobnye-ostanovki"],
    },
]

def load_cars():
    data = json.loads((ROOT / "data/cars.json").read_text(encoding="utf-8-sig"))
    for car in data:
        if not car.get("slug") or not car.get("title"):
            raise ValueError("Each car in data/cars.json needs slug and title")
        car.setdefault("image", DEFAULT_HERO)
        car.setdefault("gallery", [car["image"]])
        car.setdefault("specs", [])
        car.setdefault("description", car["title"])
        car.setdefault("price", "по запросу")
    return data


def load_news():
    data = json.loads((ROOT / "data/news.json").read_text(encoding="utf-8-sig"))
    for article in data:
        if not article.get("slug") or not article.get("title"):
            raise ValueError("Each article in data/news.json needs slug and title")
        article.setdefault("image", DEFAULT_HERO)
        article.setdefault("excerpt", article["title"])
        article.setdefault("content", [article["excerpt"]])
        article.setdefault("seo_title", f"{article['title']} | Minivan24")
        article.setdefault("seo_description", article["excerpt"])
    return data


def e(value):
    return html.escape(str(value or ""), quote=True)


def read(path):
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def clean(value):
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def match(pattern, text):
    found = re.search(pattern, text, re.I | re.S)
    return clean(found.group(1)) if found else ""


def title_from(text, fallback):
    title = match(r"<title>(.*?)</title>", text) or fallback
    for suffix in (" | Minivan24", " - Аренда минивэнов в Ташкенте"):
        title = title.replace(suffix, "")
    return title.strip() or fallback


def desc_from(text, fallback):
    return match(r'<meta name="description" content="(.*?)"', text) or fallback


def image_from(text, fallback=DEFAULT_HERO):
    value = match(r'<img[^>]+src="([^"]+)"', text) or match(r'<meta property="og:image" content="(.*?)"', text)
    found = re.search(r"(uploads/[^\"'\s)]+)", value)
    return found.group(1) if found else fallback


def paragraphs_from(text, fallback):
    values = []
    seen = set()
    for raw in re.findall(r"<p[^>]*>(.*?)</p>", text, re.I | re.S):
        value = clean(raw)
        if len(value) < 40:
            continue
        if value.count("?") > max(2, len(value) // 8):
            continue
        if any(skip in value.lower() for skip in ("whatsapp", "telegram", "cookie", "© 2026", "напишите нам дату")):
            continue
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        values.append(value)
    return values[:18] or [fallback]


def rel(prefix, path):
    return prefix + path


def check_icon(prefix=""):
    return (
        '<span class="icon" aria-hidden="true">'
        f'<img src="{e(rel(prefix, CHECK_BADGE_ICON))}" alt="" width="40" height="40" decoding="async">'
        "</span>"
    )


def absolute_url(path=""):
    return SITE_URL.rstrip("/") + "/" + str(path).lstrip("/")


def json_ld(data):
    value = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return value.replace("</", "<\\/")


def organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "AutoRental",
        "@id": absolute_url("#organization"),
        "name": "Minivan24",
        "url": absolute_url(),
        "logo": absolute_url(LOGO),
        "image": absolute_url(DEFAULT_HERO),
        "telephone": PHONE,
        "email": EMAIL,
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "улица Амир Темур 99а",
            "addressLocality": "Ташкент",
            "addressCountry": "UZ",
        },
        "areaServed": [
            {"@type": "City", "name": "Ташкент"},
            {"@type": "Country", "name": "Узбекистан"},
        ],
        "sameAs": [TELEGRAM, INSTAGRAM, WHATSAPP],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59",
        },
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": absolute_url("#website"),
        "url": absolute_url(),
        "name": "Minivan24",
        "inLanguage": "ru",
        "publisher": {"@id": absolute_url("#organization")},
    }


def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": index + 1, "name": name, "item": url}
            for index, (name, url) in enumerate(items)
        ],
    }


def faq_schema(faq_items):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer},
            }
            for question, answer in faq_items
        ],
    }


def service_schema(service):
    service_url = absolute_url(f"services/{service['slug']}/")
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "@id": service_url + "#service",
        "name": service["title"],
        "serviceType": service["title"],
        "description": service["seo_description"],
        "url": service_url,
        "provider": {"@id": absolute_url("#organization")},
        "areaServed": [
            {"@type": "City", "name": "Ташкент"},
            {"@type": "Country", "name": "Узбекистан"},
        ],
        "offers": {
            "@type": "Offer",
            "availability": "https://schema.org/InStock",
            "priceCurrency": "USD",
            "priceSpecification": {"@type": "PriceSpecification", "description": "Индивидуальный расчёт по маршруту"},
            "url": service_url,
        },
    }


def schema_list(*items):
    result = []
    for item in items:
        if not item:
            continue
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def head(title, description, prefix, canonical=None, image=None, page_type="website", structured_data=None, noindex=False):
    canonical_html = f'  <link rel="canonical" href="{e(canonical)}">\n' if canonical else ""
    og_url = f'  <meta property="og:url" content="{e(canonical)}">\n' if canonical else ""
    image = image or DEFAULT_HERO
    og_image = f'  <meta property="og:image" content="{e(absolute_url(image))}">\n'
    robots = "noindex,follow" if noindex else "index,follow"
    schema = ""
    if structured_data:
        schema = f'  <script type="application/ld+json">{json_ld(structured_data)}</script>\n'
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <meta name="robots" content="{robots}">
{canonical_html}  <meta property="og:type" content="{e(page_type)}">
  <meta property="og:site_name" content="Minivan24">
  <meta property="og:locale" content="ru_RU">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
{og_url}{og_image}  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="{e(description)}">
  <meta name="twitter:image" content="{e(absolute_url(image))}">
  <link rel="icon" href="{e(rel(prefix, FAVICON))}">
  <link rel="stylesheet" href="{e(rel(prefix, 'assets/site.css'))}">
  <script src="{e(rel(prefix, 'assets/site.js'))}" defer></script>
{schema}
</head>
"""


def header(prefix, active):
    def cls(name):
        return ' class="active"' if active == name else ""

    return f"""<body>
  <div class="topbar">
    <div class="wrap">
      <span>{ADDRESS}</span>
      <div class="social">
        <a href="{PHONE_HREF}">{PHONE}</a>
        <a href="{TELEGRAM}">Telegram</a>
        <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
        <a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
  </div>
  <header class="header">
    <div class="wrap nav">
      <a class="logo" href="{e(rel(prefix, 'index.html'))}" aria-label="Minivan24"><img src="{e(rel(prefix, LOGO))}" alt="Minivan24"></a>
      <button class="menu-toggle" type="button" aria-label="Открыть меню" aria-expanded="false" aria-controls="site-menu" data-menu-toggle>
        <span></span>
        <span></span>
        <span></span>
      </button>
      <nav class="menu" id="site-menu" aria-label="Главное меню" data-menu>
        <a href="{e(rel(prefix, 'index.html'))}"{cls('home')}>Главная</a>
        <a href="{e(rel(prefix, 'services/index.html'))}"{cls('services')}>Услуги</a>
        <a href="{e(rel(prefix, 'cars/index.html'))}"{cls('cars')}>Автопарк</a>
        <a href="{e(rel(prefix, 'news/index.html'))}"{cls('news')}>Новости</a>
        <a href="{e(rel(prefix, 'kontakty/index.html'))}"{cls('contacts')}>Контакты</a>
        <div class="menu-contact">
          <span class="menu-contact-label">Контакты</span>
          <span class="menu-contact-address">{ADDRESS}</span>
          <a class="menu-contact-phone" href="{PHONE_HREF}">{PHONE}</a>
          <div class="menu-contact-links">
            <a href="{TELEGRAM}">Telegram</a>
            <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
            <a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a>
          </div>
        </div>
        <a class="menu-cta" href="{WHATSAPP}" target="_blank" rel="noopener">Связаться</a>
      </nav>
      <div class="nav-actions"><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Связаться</a></div>
    </div>
    <div class="menu-backdrop" data-menu-backdrop></div>
  </header>
"""


def footer(prefix):
    return f"""  <footer class="footer">
    <div class="wrap footer-grid">
      <a href="{e(rel(prefix, 'index.html'))}"><img src="{e(rel(prefix, LOGO))}" alt="Minivan24"></a>
      <div class="footer-links">
        <a href="{e(rel(prefix, 'index.html'))}">Главная</a>
        <a href="{e(rel(prefix, 'services/index.html'))}">Услуги</a>
        <a href="{e(rel(prefix, 'cars/index.html'))}">Автопарк</a>
        <a href="{e(rel(prefix, 'news/index.html'))}">Новости</a>
        <a href="{e(rel(prefix, 'kontakty/index.html'))}">Контакты</a>
      </div>
      <span>© 2026 Minivan24. Аренда минивэнов в Ташкенте.</span>
    </div>
  </footer>
</body>
</html>
"""


def page_hero(title, description, prefix, image, eyebrow):
    return f"""  <section class="page-hero" style="--hero-image: url('{e(rel(prefix, image))}')">
    <div class="wrap">
      <span class="eyebrow">{e(eyebrow)}</span>
      <h1 class="page-title">{e(title)}</h1>
      <p class="lead">{e(description)}</p>
    </div>
  </section>
"""


def car_seo_title(car):
    return car.get("seo_title") or f"{car['title']} в аренду | Minivan24"


def car_seo_description(car):
    return car.get("seo_description") or car["description"]


def price_currency(price):
    value = str(price or "").upper()
    if "USD" in value or "$" in value:
        return "USD"
    if "UZS" in value or "СУМ" in value:
        return "UZS"
    return "USD"


def price_value(price):
    found = re.search(r"\d+(?:[.,]\d+)?", str(price or ""))
    return found.group(0).replace(",", ".") if found else None


def car_schema(car):
    car_url = absolute_url(f"cars/{car['slug']}/")
    price = price_value(car.get("price"))
    offer = {
        "@type": "Offer",
        "availability": "https://schema.org/InStock",
        "priceCurrency": price_currency(car.get("price")),
        "priceSpecification": {"@type": "PriceSpecification", "description": car.get("price", "по запросу")},
        "seller": {"@id": absolute_url("#organization")},
        "url": car_url,
    }
    if price:
        offer["price"] = price
    return schema_list(
        organization_schema(),
        breadcrumb_schema([
            ("Главная", absolute_url()),
            ("Автопарк", absolute_url("cars/")),
            (car["title"], car_url),
        ]),
        {
            "@context": "https://schema.org",
            "@type": "Car",
            "@id": car_url + "#car",
            "name": car["title"],
            "description": car_seo_description(car),
            "image": [absolute_url(image) for image in car.get("gallery", [car["image"]])],
            "url": car_url,
            "brand": {"@type": "Brand", "name": car["title"].split()[0]},
            "offers": offer,
        },
    )


def car_card(car, prefix, link_prefix=""):
    slug = car["slug"]
    title = car["title"]
    image = car["image"]
    specs = car["specs"]
    desc = car["description"]
    price = car.get("price", "по запросу")
    specs_html = "".join(f"<span>{e(item)}</span>" for item in specs)
    return f"""          <article class="card">
            <a class="card-media" href="{e(link_prefix + slug)}/index.html"><img src="{e(rel(prefix, image))}" alt="{e(title)}"></a>
            <div class="card-body">
              <h2><a class="card-title" href="{e(link_prefix + slug)}/index.html">{e(title)}</a></h2>
              <p>{e(desc)}</p>
              <div class="specs">{specs_html}</div>
              <div class="price"><strong>{e(price)}</strong><a class="btn" href="{e(link_prefix + slug)}/index.html">Подробнее</a></div>
            </div>
          </article>
"""


def car_carousel_card(car, prefix, link_prefix=""):
    slug = car["slug"]
    title = car["title"]
    image = car["image"]
    gallery = car.get("gallery") or [image]
    specs = car["specs"]
    desc = car["description"]
    price = car.get("price", "по запросу")
    slide_items = []
    for index, item in enumerate(gallery):
        active = ' class="active"' if index == 0 else ""
        slide_items.append(f'<img src="{e(rel(prefix, item))}" alt="{e(title)}" data-slide="{index}"{active}>')
    slides = "".join(slide_items)
    dots = "".join(
        f'<button type="button" class="car-dot{" active" if index == 0 else ""}" data-slide="{index}" aria-label="Фото {index + 1}"></button>'
        for index, _ in enumerate(gallery)
    )
    specs_html = "".join(f"<span>{e(item)}</span>" for item in specs)
    controls = ""
    if len(gallery) > 1:
        controls = f"""<button class="media-btn prev" type="button" data-gallery-prev aria-label="Предыдущее фото">&lsaquo;</button>
              <button class="media-btn next" type="button" data-gallery-next aria-label="Следующее фото">&rsaquo;</button>
              <div class="car-dots">{dots}</div>"""
    return f"""          <article class="card carousel-card" data-gallery-card>
            <div class="card-media car-gallery">
              <a href="{e(link_prefix + slug)}/index.html" aria-label="{e(title)}">{slides}</a>
              {controls}
            </div>
            <div class="card-body">
              <h2><a class="card-title" href="{e(link_prefix + slug)}/index.html">{e(title)}</a></h2>
              <p>{e(desc)}</p>
              <div class="specs">{specs_html}</div>
              <div class="price"><strong>{e(price)}</strong><a class="btn" href="{e(link_prefix + slug)}/index.html">Подробнее</a></div>
            </div>
          </article>
"""


HOME_CAR_TITLES = {
    "kia-carnival": "KIA Carnival «Комфорт»",
    "kia-carnival-2": "KIA Carnival «Премиум»",
    "kia-carnival-3": "KIA Carnival «Семейный»",
    "kia-carnival-4": "KIA Carnival «Трансфер»",
    "kia-carnival-5": "KIA Carnival «Бизнес»",
}


HOME_CAR_GALLERIES = {
    "kia-carnival": [
        "uploads/2026/06/home-kia-carnival-photo-01-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-02-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-03-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-06-2k.webp",
    ],
    "kia-carnival-2": [
        "uploads/2026/06/home-kia-carnival-photo-02-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-04-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-05-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-07-2k.webp",
    ],
    "kia-carnival-3": [
        "uploads/2026/06/home-kia-carnival-photo-03-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-08-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-09-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-10-2k.webp",
    ],
    "kia-carnival-4": [
        "uploads/2026/06/home-kia-carnival-photo-04-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-01-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-05-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-06-2k.webp",
    ],
    "kia-carnival-5": [
        "uploads/2026/06/home-kia-carnival-photo-05-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-07-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-08-2k.webp",
        "uploads/2026/06/home-kia-carnival-photo-10-2k.webp",
    ],
    "hyundai-starex": [
        "uploads/2026/06/home-hyundai-starex-photo-01-2k.webp",
        "uploads/2026/06/home-hyundai-starex-photo-02-2k.webp",
        "uploads/2026/06/home-hyundai-starex-photo-03-2k.webp",
        "uploads/2026/06/home-hyundai-starex-photo-04-2k.webp",
    ],
}


def home_car_card(car):
    display_car = {**car, "title": HOME_CAR_TITLES.get(car["slug"], car["title"])}
    gallery = HOME_CAR_GALLERIES.get(car["slug"])
    if gallery:
        display_car["gallery"] = gallery
        display_car["image"] = gallery[0]
    return car_carousel_card(display_car, "", "cars/")


def car_detail_gallery(car, prefix):
    title = car["title"]
    gallery = car.get("gallery") or [car["image"]]
    slides = []
    for index, item in enumerate(gallery):
        active = ' class="active"' if index == 0 else ""
        slides.append(f'<img src="{e(rel(prefix, item))}" alt="{e(title)}" data-slide="{index}"{active}>')
    dots = "".join(
        f'<button type="button" class="car-dot{" active" if index == 0 else ""}" data-slide="{index}" aria-label="Фото {index + 1}"></button>'
        for index, _ in enumerate(gallery)
    )
    controls = ""
    if len(gallery) > 1:
        controls = f"""<button class="media-btn prev" type="button" data-gallery-prev aria-label="Предыдущее фото">&lsaquo;</button>
        <button class="media-btn next" type="button" data-gallery-next aria-label="Следующее фото">&rsaquo;</button>
        <div class="car-dots">{dots}</div>"""
    return f"""      <div class="article-cover detail-gallery" data-gallery-card>
        <div class="detail-gallery-stage car-gallery">
          {"".join(slides)}
          {controls}
        </div>
      </div>
"""


def spec_icon(item):
    value = item.lower()
    if "мест" in value or "гостей" in value:
        return """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm8.5 1a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7ZM2.5 21a5.5 5.5 0 0 1 11 0H2.5Zm11.5 0a6.8 6.8 0 0 0-1.2-3.9 4.8 4.8 0 0 1 8.7 3.9H14Z"/></svg>"""
    if "багаж" in value:
        return """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5a3 3 0 0 1 6 0v1h2.5A2.5 2.5 0 0 1 20 8.5v9A2.5 2.5 0 0 1 17.5 20h-11A2.5 2.5 0 0 1 4 17.5v-9A2.5 2.5 0 0 1 6.5 6H9V5Zm2 1h2V5a1 1 0 1 0-2 0v1Zm-3 4v6h2v-6H8Zm6 0v6h2v-6h-2Z"/></svg>"""
    if "автомат" in value:
        return """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 9.8 4.2l-3-.6-1.6 2.8 2 2.3a6 6 0 0 0 0 2.6l-2 2.3 1.6 2.8 3-.6L12 18l2.2-2.2 3 .6 1.6-2.8-2-2.3a6 6 0 0 0 0-2.6l2-2.3-1.6-2.8-3 .6L12 2Zm0 7a3 3 0 1 1 0 6 3 3 0 0 1 0-6Z"/></svg>"""
    if "кондиционер" in value or "климат" in value:
        return """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11 2h2v7.2l4.9-4.9 1.4 1.4-5 5H22v2h-7.7l5 5-1.4 1.4-4.9-4.9V22h-2v-7.8l-4.9 4.9-1.4-1.4 5-5H2v-2h7.7l-5-5 1.4-1.4 4.9 4.9V2Z"/></svg>"""
    if "город" in value or "трасс" in value or "межгород" in value:
        return """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3a3 3 0 0 0-3 3c0 2.2 3 5.5 3 5.5S9 8.2 9 6a3 3 0 0 0-3-3Zm0 4.2A1.2 1.2 0 1 1 6 4.8a1.2 1.2 0 0 1 0 2.4ZM18 12.5s-3 3.3-3 5.5a3 3 0 1 0 6 0c0-2.2-3-5.5-3-5.5Zm0 6.7a1.2 1.2 0 1 1 0-2.4 1.2 1.2 0 0 1 0 2.4ZM8.5 14H7a3 3 0 0 1 0-6h3v2H7a1 1 0 1 0 0 2h1.5a4.5 4.5 0 0 1 0 9H5v-2h3.5a2.5 2.5 0 0 0 0-5Z"/></svg>"""
    if "водител" in value:
        return """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 12a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm-9 9a9 9 0 0 1 18 0H3Zm14.4-8.4 1.5 1.3-3.8 4.5-2.2-2.1 1.4-1.5.7.7 2.4-2.9Z"/></svg>"""
    if "бензин" in value or "дизель" in value:
        return """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h9a2 2 0 0 1 2 2v15H4V4a1 1 0 0 1 1-1Zm2 3v5h6V6H7Zm10.5.5 3.3 3.3A4 4 0 0 1 22 12.6V18a3 3 0 0 1-6 0v-3h2v3a1 1 0 0 0 2 0v-5.4a2 2 0 0 0-.6-1.4L16 7.9l1.5-1.4Z"/></svg>"""
    return """<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 14.9 8l6.6.9-4.8 4.7 1.1 6.6L12 17.1l-5.8 3.1 1.1-6.6-4.8-4.7L9.1 8 12 2Z"/></svg>"""


def car_specs_panel(specs):
    items = "".join(
        f"""          <li>
            <span class="spec-icon">{spec_icon(item)}</span>
            <span>{e(item)}</span>
          </li>
"""
        for item in specs
    )
    return f"""        <section class="detail-specs" aria-labelledby="car-specs-title">
          <h3 id="car-specs-title">Характеристики</h3>
          <ul>{items}          </ul>
        </section>
"""


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def sitemap_item(url, changefreq="weekly", priority="0.7"):
    return (
        "  <url>"
        f"<loc>{e(absolute_url(url))}</loc>"
        f"<lastmod>{TODAY}</lastmod>"
        f"<changefreq>{changefreq}</changefreq>"
        f"<priority>{priority}</priority>"
        "</url>"
    )


def write_sitemap(cars_data, articles, total_news_pages):
    urls = [
        ("", "weekly", "1.0"),
        ("services/", "weekly", "0.95"),
        ("cars/", "weekly", "0.9"),
        ("news/", "weekly", "0.75"),
        ("kontakty/", "monthly", "0.8"),
    ]
    urls.extend((f"services/{service['slug']}/", "weekly", "0.92") for service in SERVICES)
    urls.extend((f"cars/{car['slug']}/", "weekly", "0.86") for car in cars_data)
    urls.extend((f"news/page/{page}/", "weekly", "0.55") for page in range(2, total_news_pages + 1))
    urls.extend((f"news/{article['slug']}/", "monthly", "0.62") for article in articles)
    items = "\n".join(sitemap_item(*item) for item in urls)
    write(
        ROOT / "sitemap.xml",
        f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}
</urlset>
""",
    )


def article_seo_title(article):
    return article.get("seo_title") or f"{article['title']} | Minivan24"


def article_seo_description(article):
    return article.get("seo_description") or article.get("excerpt") or article["title"]


def article_schema(article):
    article_url = absolute_url(f"news/{article['slug']}/")
    return schema_list(
        organization_schema(),
        breadcrumb_schema([
            ("Главная", absolute_url()),
            ("Новости", absolute_url("news/")),
            (article["title"], article_url),
        ]),
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "@id": article_url + "#article",
            "headline": article["title"],
            "description": article_seo_description(article),
            "image": absolute_url(article["image"]),
            "url": article_url,
            "mainEntityOfPage": article_url,
            "inLanguage": "ru",
            "dateModified": TODAY,
            "author": {"@id": absolute_url("#organization")},
            "publisher": {
                "@type": "Organization",
                "name": "Minivan24",
                "logo": {"@type": "ImageObject", "url": absolute_url(LOGO)},
            },
        },
    )


def write_robots():
    write(
        ROOT / "robots.txt",
        f"""User-agent: *
Allow: /

Sitemap: {absolute_url('sitemap.xml')}
Host: {SITE_URL}
""",
    )


def news_card(article, prefix, link_prefix):
    return f"""          <article class="card">
            <a class="card-media" href="{e(link_prefix + article['slug'])}/index.html"><img src="{e(rel(prefix, article['image']))}" alt="{e(article['title'])}"></a>
            <div class="card-body">
              <h2><a class="card-title" href="{e(link_prefix + article['slug'])}/index.html">{e(article['title'])}</a></h2>
              <p>{e(article['excerpt'])}</p>
              <div class="price"><strong>Статья</strong><a class="btn ghost" href="{e(link_prefix + article['slug'])}/index.html">Читать</a></div>
            </div>
          </article>
"""


def pagination(current, total, index_href, page_base):
    links = []
    for number in range(1, total + 1):
        if number == current:
            links.append(f'<span class="current">{number}</span>')
        else:
            href = index_href if number == 1 else f"{page_base}{number}/index.html"
            links.append(f'<a href="{href}">{number}</a>')
    return '<nav class="pagination" aria-label="Страницы новостей">' + "".join(links) + "</nav>"


def service_by_slug(slug):
    return next((service for service in SERVICES if service["slug"] == slug), None)


def service_card(service, prefix, link_prefix=""):
    return f"""          <article class="card service-card">
            <a class="card-media" href="{e(link_prefix + service['slug'])}/index.html"><img src="{e(rel(prefix, service['image']))}" alt="{e(service['title'])}"></a>
            <div class="card-body">
              <h2><a class="card-title" href="{e(link_prefix + service['slug'])}/index.html">{e(service['title'])}</a></h2>
              <p>{e(service['lead'])}</p>
              <div class="service-tags">{"".join(f"<span>{e(item)}</span>" for item in service["audience"][:3])}</div>
              <div class="price"><strong>Подбор авто</strong><a class="btn ghost" href="{e(link_prefix + service['slug'])}/index.html">Подробнее</a></div>
            </div>
          </article>
"""


def service_links(prefix, title="Популярные услуги", current_slug=None):
    links = "".join(
        f'<a href="{e(rel(prefix, "services/" + service["slug"] + "/index.html"))}">{e(service["title"])}</a>'
        for service in SERVICES
        if service["slug"] != current_slug
    )
    return f"""        <aside class="service-links" aria-label="{e(title)}">
          <strong>{e(title)}</strong>
          <div>{links}</div>
        </aside>
"""


def faq_html(faq_items):
    return "".join(
        f"""          <details class="faq-item">
            <summary>{e(question)}</summary>
            <div class="faq-answer"><p>{e(answer)}</p></div>
          </details>
"""
        for question, answer in faq_items
    )


def steps_html(steps):
    return "".join(
        f"""          <li>
            <span>{index}</span>
            <p>{e(step)}</p>
          </li>
"""
        for index, step in enumerate(steps, 1)
    )


def related_cars_html(service, cars_data, prefix):
    wanted = set(service.get("related_cars", []))
    cars = [car for car in cars_data if car["slug"] in wanted]
    if not cars:
        return ""
    return "".join(car_card(car, prefix, "../../cars/") for car in cars)


def related_articles_html(service, articles, prefix):
    wanted = set(service.get("related_articles", []))
    items = [article for article in articles if article["slug"] in wanted]
    if not items:
        return ""
    return "".join(news_card(article, prefix, "../../news/") for article in items)


def service_page(service, cars_data, articles):
    prefix = "../../"
    url = absolute_url(f"services/{service['slug']}/")
    benefits = "".join(
        f'<article class="feature">{check_icon(prefix)}<h3>{e(title)}</h3><p>{e(text)}</p></article>'
        for title, text in service["benefits"]
    )
    audience = "".join(f"<li>{e(item)}</li>" for item in service["audience"])
    related_cars = related_cars_html(service, cars_data, prefix)
    related_articles = related_articles_html(service, articles, prefix)
    page = head(
        service["seo_title"],
        service["seo_description"],
        prefix,
        canonical=url,
        image=service["image"],
        page_type="website",
        structured_data=schema_list(
            organization_schema(),
            breadcrumb_schema([
                ("Главная", absolute_url()),
                ("Услуги", absolute_url("services/")),
                (service["title"], url),
            ]),
            service_schema(service),
            faq_schema(service["faq"]),
        ),
    )
    page += header(prefix, "services")
    page += page_hero(service["title"], service["lead"], prefix, service["image"], service["eyebrow"])
    page += f"""  <main>
    <section class="section">
      <div class="wrap grid grid-2 align-start">
        <div>
          <span class="eyebrow">Кому подходит</span>
          <h2 class="section-title compact-title">Когда эта услуга уместна</h2>
          <p class="lead">Поможем быстро понять формат поездки: какой автомобиль нужен, что влияет на цену и какие детали лучше согласовать заранее.</p>
          <ul class="check-list">{audience}</ul>
        </div>
        <div class="service-detail-side">
          <figure class="service-detail-media">
            <img src="{e(rel(prefix, service['image']))}" alt="{e(service['title'])}">
          </figure>
          <div class="panel order-panel">
            <h2>Что прислать для расчёта</h2>
            <p>Дата, время подачи, маршрут, количество пассажиров, багаж, детские кресла и желаемый класс автомобиля.</p>
            <a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Описать поездку</a>
          </div>
        </div>
      </div>
    </section>
    <section class="section soft">
      <div class="wrap">
        <span class="eyebrow">Условия</span>
        <h2 class="section-title">Что важно перед бронированием</h2>
        <div class="grid grid-4">{benefits}</div>
      </div>
    </section>
    <section class="section">
      <div class="wrap grid grid-2 align-start">
        <div>
          <span class="eyebrow">Порядок работы</span>
          <h2 class="section-title compact-title">Как мы подбираем транспорт</h2>
          <ol class="steps">{steps_html(service["steps"])}          </ol>
        </div>
        <div>
          {service_links(prefix, "Смежные услуги", service["slug"])}
        </div>
      </div>
    </section>
"""
    if related_cars:
        page += f"""    <section class="section soft">
      <div class="wrap">
        <span class="eyebrow">Автомобили</span>
        <h2 class="section-title">Подходящие варианты из автопарка</h2>
        <div class="grid grid-3">{related_cars}</div>
      </div>
    </section>
"""
    page += f"""    <section class="section">
      <div class="wrap grid grid-2 align-start">
        <div>
          <span class="eyebrow">FAQ</span>
          <h2 class="section-title compact-title">Частые вопросы</h2>
          <div class="faq-list">{faq_html(service["faq"])}          </div>
        </div>
        <div class="panel">
          <h2>Заявка без лишних шагов</h2>
          <p>Мы не просим заполнять длинную форму: достаточно написать маршрут и дату. Менеджер уточнит детали и предложит подходящий автомобиль.</p>
          <p><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Описать поездку</a></p>
        </div>
      </div>
    </section>
"""
    if related_articles:
        page += f"""    <section class="section soft">
      <div class="wrap">
        <span class="eyebrow">Полезно прочитать</span>
        <h2 class="section-title">Материалы по теме</h2>
        <div class="grid grid-2">{related_articles}</div>
      </div>
    </section>
"""
    page += "  </main>\n"
    page += footer(prefix)
    return page


def build():
    articles = load_news()
    cars_data = load_cars()

    feature_html = "".join(
        f'<article class="feature">{check_icon()}<h3>{e(title)}</h3><p>{e(text)}</p></article>'
        for title, text in [
            ("Честная цена", "Подбираем транспорт под задачу без лишних переплат за неподходящий класс."),
            ("Бронирование 24/7", "Заявку можно отправить заранее или в день поездки через WhatsApp и Telegram."),
            ("Подача по городу", "Аэропорт, вокзал, отель, офис, ресторан или адрес в районе Ташкента."),
            ("Комфортный салон", "Минивэны для семьи, туристов, делегаций, свадеб и междугородних маршрутов."),
        ]
    )
    home_cards = "".join(car_carousel_card(car, "", "cars/") for car in cars_data[:6])
    home_service_cards = "".join(service_card(service, "", "services/") for service in SERVICES)
    home_faq = [
        ("Сколько стоит аренда минивэна в Ташкенте?", "Стоимость зависит от класса автомобиля, маршрута, длительности аренды, ожидания, подачи и количества багажа."),
        ("Можно ли заказать микроавтобус с водителем?", "Да, микроавтобусы и минивэны можно заказать с водителем для трансфера, экскурсии, свадьбы, деловой поездки или маршрута по Узбекистану."),
        ("Как быстро можно оформить заявку?", "Напишите дату, маршрут и количество пассажиров в WhatsApp или Telegram. Мы уточним детали и предложим подходящий автомобиль."),
    ]
    home = head(
        "Аренда минивэнов и микроавтобусов в Ташкенте | Minivan24",
        "Аренда минивэнов и микроавтобусов в Ташкенте с водителем и без: трансферы, свадьбы, экскурсии, поездки по Узбекистану, заявка в WhatsApp.",
        "",
        canonical=absolute_url(),
        image=HOME_HERO,
        structured_data=schema_list(organization_schema(), website_schema(), faq_schema(home_faq)),
    )
    home += header("", "home")
    home += f"""  <main>
    <section class="hero" style="--hero-image: url('{DEFAULT_HERO}')">
      <div class="wrap">
        <span class="eyebrow">Minivan24 Tashkent</span>
        <h1>Аренда минивэнов в Ташкенте для семьи, гостей и поездок</h1>
        <p>Комфортные минивэны и микроавтобусы с водителем и без водителя. Подберём автомобиль под трансфер, экскурсию, свадьбу, деловую поездку или путешествие по Узбекистану.</p>
        <div class="hero-actions"><a class="btn desktop-booking-link" href="#booking">Подобрать авто</a><a class="btn mobile-contact-link" href="{WHATSAPP}" target="_blank" rel="noopener">Написать в WhatsApp</a><a class="btn ghost" href="cars/index.html">Смотреть автопарк</a></div>
      </div>
    </section>
    <section class="booking" id="booking"><div class="wrap"><div class="mobile-booking-cta">
      <span class="eyebrow">Быстрая заявка</span>
      <h2>Отправьте маршрут в WhatsApp</h2>
      <p>Дата, адрес подачи, пассажиры и багаж — этого достаточно для первого ответа.</p>
      <a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Отправить заявку</a>
    </div><form class="booking-panel" action="{WHATSAPP}" target="_blank">
      <h2>Быстрая заявка на аренду</h2>
      <div class="booking-grid">
        <label>Место подачи<select name="pickup"><option>Ташкент, аэропорт</option><option>Ташкент, вокзал</option><option>Ташкент, отель</option><option>По Узбекистану</option></select></label>
        <label>Автомобиль<select name="car"><option>KIA Carnival</option><option>HYUNDAI Starex</option><option>HYUNDAI H-1</option><option>MERCEDES-BENZ Sprinter</option><option>TOYOTA Sienna</option></select></label>
        <label>Дата начала<input type="date" name="start"></label><label>Время<input type="time" name="time"></label><button class="btn" type="submit">Отправить</button>
      </div>
    </form></div></section>
    <section class="section"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Услуги</span><h2 class="section-title">Популярные задачи поездки</h2></div><a class="btn ghost" href="services/index.html">Все услуги</a></div><div class="grid grid-3">{home_service_cards}</div></div></section>
    <section class="section"><div class="wrap"><span class="eyebrow">Почему выбирают нас</span><h2 class="section-title">Сервис аренды, который удобно планировать заранее</h2><p class="lead">Мы делаем поездку предсказуемой: помогаем выбрать формат, согласовать маршрут, время подачи и подходящий автомобиль под количество пассажиров и багажа.</p><div class="grid grid-4" style="margin-top:32px">{feature_html}</div></div></section>
    <section class="section soft"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Автопарк</span><h2 class="section-title">Лучшие предложения</h2></div><div class="carousel-actions"><button class="slider-btn" type="button" data-cars-prev aria-label="Предыдущие автомобили">&lsaquo;</button><button class="slider-btn" type="button" data-cars-next aria-label="Следующие автомобили">&rsaquo;</button></div></div><div class="cars-carousel" data-cars-carousel><div class="cars-track">{home_cards}</div></div></div></section>
    <section class="section"><div class="wrap grid grid-2 align-start"><div><span class="eyebrow">FAQ</span><h2 class="section-title compact-title">Частые вопросы перед заказом</h2><div class="faq-list">{faq_html(home_faq)}</div></div><div class="panel"><h2>Уточнить маршрут</h2><p>Пришлите дату, маршрут, количество пассажиров и багаж. Мы подберём минивэн или микроавтобус и заранее объясним, из чего складывается цена.</p><p><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Описать поездку</a></p></div></div></section>
  </main>
"""
    home += footer("")
    write(ROOT / "index.html", home)

    services_cards = "".join(service_card(service, "../") for service in SERVICES)
    services = head(
        "Услуги аренды минивэнов и микроавтобусов | Minivan24",
        "Услуги Minivan24: аренда минивэна, микроавтобуса, авто с водителем, трансфер из аэропорта, свадьбы и поездки по Узбекистану.",
        "../",
        canonical=absolute_url("services/"),
        image=DEFAULT_HERO,
        structured_data=schema_list(
            organization_schema(),
            breadcrumb_schema([("Главная", absolute_url()), ("Услуги", absolute_url("services/"))]),
        ),
    )
    services += header("../", "services")
    services += page_hero("Услуги аренды транспорта", "Отдельные посадочные страницы под основные задачи: минивэн, микроавтобус, водитель, аэропорт, свадьба и маршруты по Узбекистану.", "../", SERVICES_HERO, "Minivan24 services")
    services += f"""  <main>
    <section class="section">
      <div class="wrap">
        <div class="section-head"><div><span class="eyebrow">Услуги</span><h2 class="section-title">Выберите задачу поездки</h2></div></div>
        <div class="grid grid-3">{services_cards}</div>
      </div>
    </section>
  </main>
"""
    services += footer("../")
    write(ROOT / "services/index.html", services)

    for service in SERVICES:
        write(ROOT / "services" / service["slug"] / "index.html", service_page(service, cars_data, articles))

    cars = head(
        "Автопарк минивэнов и микроавтобусов в Ташкенте | Minivan24",
        "Минивэны и микроавтобусы в аренду в Ташкенте: KIA Carnival, Hyundai Starex, Hyundai H-1, Mercedes-Benz Sprinter, Toyota Sienna.",
        "../",
        canonical=absolute_url("cars/"),
        image=CARS_HERO,
        structured_data=schema_list(
            organization_schema(),
            breadcrumb_schema([("Главная", absolute_url()), ("Автопарк", absolute_url("cars/"))]),
        ),
    )
    cars += header("../", "cars")
    cars += page_hero("Автопарк", "Выберите минивэн или микроавтобус под трансфер, экскурсию, семейную поездку, свадьбу или маршрут по Узбекистану.", "../", CARS_HERO, "Minivan24 cars")
    cars += '<main><section class="section"><div class="wrap"><div class="grid grid-3">\n' + "".join(car_carousel_card(car, "../") for car in cars_data) + f"</div>{service_links('../', 'Подберите услугу под маршрут')}</div></section></main>\n"
    cars += footer("../")
    write(ROOT / "cars/index.html", cars)

    for car in cars_data:
        slug = car["slug"]
        title = car["title"]
        image = car["image"]
        specs = car["specs"]
        desc = car["description"]
        price = car.get("price", "по запросу")
        specs_html = car_specs_panel(specs)
        detail = head(
            car_seo_title(car),
            car_seo_description(car),
            "../../",
            canonical=absolute_url(f"cars/{slug}/"),
            image=image,
            page_type="product",
            structured_data=car_schema(car),
        )
        detail += header("../../", "cars")
        detail += page_hero(title, desc, "../../", image, "Автомобиль")
        detail += f"""  <main><section class="article">
{car_detail_gallery(car, '../../')}
      <div class="narrow article-body">
        <a class="back-link" href="../index.html">← Вернуться в автопарк</a>
        <h2>{e(title)}</h2>
        <p>{e(desc)}</p>
        <p>Автомобиль подходит для поездок по Ташкенту, трансферов из аэропорта, экскурсий, семейных маршрутов и деловых встреч. Уточните дату, маршрут, количество пассажиров и багаж, чтобы мы предложили точный формат аренды.</p>
{specs_html}
        <p><strong>Стоимость:</strong> {e(price)}. Цена зависит от маршрута, времени аренды, подачи и формата поездки.</p>
        <p><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Уточнить наличие</a></p>
{service_links('../../', 'Для каких задач подходит')}
      </div>
    </section></main>
"""
        detail += footer("../../")
        write(ROOT / "cars" / slug / "index.html", detail)

    total_pages = max(1, math.ceil(len(articles) / NEWS_PAGE_SIZE))
    for page in range(1, total_pages + 1):
        chunk = articles[(page - 1) * NEWS_PAGE_SIZE : page * NEWS_PAGE_SIZE]
        if page == 1:
            out, prefix, link_prefix, index_href, page_base = ROOT / "news/index.html", "../", "", "index.html", "page/"
            title = "Новости об аренде транспорта"
        else:
            out, prefix, link_prefix, index_href, page_base = ROOT / "news/page" / str(page) / "index.html", "../../../", "../../", "../../index.html", "../../page/"
            title = f"Новости об аренде транспорта: страница {page}"
        cards = "".join(news_card(article, prefix, link_prefix) for article in chunk)
        news_path = "news/" if page == 1 else f"news/page/{page}/"
        news = head(
            f"{title} | Minivan24",
            "Новости аренды минивэнов и микроавтобусов в Ташкенте: трансферы, маршруты, цены, выбор транспорта и советы для поездок.",
            prefix,
            canonical=absolute_url(news_path),
            image=NEWS_HERO,
            structured_data=schema_list(
                organization_schema(),
                breadcrumb_schema([("Главная", absolute_url()), ("Новости", absolute_url("news/"))]),
            ),
        )
        news += header(prefix, "news")
        news += page_hero(title, "Полезные статьи об аренде минивэнов, трансферах, маршрутах по Ташкенту и поездках по Узбекистану.", prefix, NEWS_HERO, "Minivan24 news")
        news += f'<main><section class="section news-list"><div class="wrap"><div class="grid grid-3">\n{cards}</div>{pagination(page, total_pages, index_href, page_base)}</div></section></main>\n'
        news += footer(prefix)
        write(out, news)

    for article in articles:
        body = "\n".join(f"        <p>{e(p)}</p>" for p in article["content"])
        page = head(
            article_seo_title(article),
            article_seo_description(article),
            "../../",
            canonical=absolute_url(f"news/{article['slug']}/"),
            image=article["image"],
            page_type="article",
            structured_data=article_schema(article),
        )
        page += header("../../", "news")
        page += page_hero(article["title"], article["excerpt"], "../../", article["image"], "Статья")
        page += f"""  <main><section class="article">
      <div class="article-cover"><img src="{e(rel('../../', article['image']))}" alt="{e(article['title'])}"></div>
      <div class="narrow article-body">
        <a class="back-link" href="../index.html">← Вернуться к новостям</a>
{body}
{service_links('../../', 'Услуги по теме')}
        <h2>Нужен минивэн для поездки?</h2>
        <p>Напишите нам дату, маршрут, количество пассажиров и багаж. Мы подскажем подходящий автомобиль и формат аренды.</p>
        <p><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Описать поездку</a></p>
      </div>
    </section></main>
"""
        page += footer("../../")
        write(ROOT / "news" / article["slug"] / "index.html", page)

    contacts = head(
        "Контакты Minivan24 | Аренда минивэнов в Ташкенте",
        "Контакты Minivan24: телефон, WhatsApp, Telegram, email и адрес для заказа минивэна, микроавтобуса или трансфера в Ташкенте.",
        "../",
        canonical=absolute_url("kontakty/"),
        image=CONTACTS_HERO,
        structured_data=schema_list(
            organization_schema(),
            breadcrumb_schema([("Главная", absolute_url()), ("Контакты", absolute_url("kontakty/"))]),
        ),
    )
    contacts += header("../", "contacts")
    contacts += page_hero("Контакты", "Свяжитесь с нами, чтобы подобрать минивэн, микроавтобус или трансфер под вашу поездку.", "../", CONTACTS_HERO, "Minivan24 contacts")
    contacts += f"""  <main><section class="section contact-section"><div class="wrap grid grid-2">
      <div class="panel"><h2>Связаться с нами</h2><p><strong>Телефон:</strong> <a href="{PHONE_HREF}">{PHONE}</a></p><p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p><p><strong>Адрес:</strong> {ADDRESS}</p><p><strong>Telegram:</strong> <a href="{TELEGRAM}">@minivanuzb</a></p><p><strong>WhatsApp:</strong> <a href="{WHATSAPP}" target="_blank" rel="noopener">отправить заявку</a></p></div>
      <form class="panel" action="{WHATSAPP}" target="_blank"><h2>Заявка на аренду</h2><label>Ваше имя<input name="name" placeholder="Имя"></label><label>Телефон<input name="phone" placeholder="+998"></label><label>Маршрут<textarea name="message" placeholder="Дата, маршрут, количество пассажиров"></textarea></label><button class="btn" type="submit">Отправить</button></form>
    </div></section>
    <section class="section soft"><div class="wrap"><span class="eyebrow">Зоны обслуживания</span><h2 class="section-title">Подача по Ташкенту и маршруты по Узбекистану</h2><div class="grid grid-4">
      <article class="feature">{check_icon('../')}<h3>Аэропорт и вокзал</h3><p>Встреча гостей, багаж, трансфер до отеля, офиса или другого города.</p></article>
      <article class="feature">{check_icon('../')}<h3>Городские поездки</h3><p>Деловые встречи, семейные маршруты, мероприятия и подача по адресу.</p></article>
      <article class="feature">{check_icon('../')}<h3>Туры и экскурсии</h3><p>Ташкент, Чарвак, Самарканд, Бухара и другие направления по запросу.</p></article>
      <article class="feature">{check_icon('../')}<h3>Группы и события</h3><p>Свадьбы, делегации, корпоративы, развоз гостей и поездки с багажом.</p></article>
    </div>{service_links('../', 'Заказать услугу')}</div></section></main>
"""
    contacts += footer("../")
    write(ROOT / "kontakty/index.html", contacts)

    write_sitemap(cars_data, articles, total_pages)
    write_robots()

    print(f"Generated clean HTML: {1 + 1 + len(SERVICES) + 1 + len(cars_data) + total_pages + len(articles) + 1} pages")


_base_build = build


def whatsapp_float(prefix=""):
    return f"""  <a class="floating-whatsapp" href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="Написать в WhatsApp">
    <span>WhatsApp</span>
  </a>
"""


def postprocess_floating_whatsapp():
    for path in ROOT.rglob("index.html"):
        html_text = read(path)
        if not html_text or "floating-whatsapp" in html_text:
            continue
        write(path, html_text.replace("</body>", whatsapp_float() + "</body>"))


def enhance_home():
    index_path = ROOT / "index.html"
    home = read(index_path)
    if not home:
        return
    home_cars = "".join(home_car_card(car) for car in load_cars()[:6])

    home_main = f"""  <main>
    <section class="hero hero-sales" style="--hero-image: url('{HOME_HERO}')">
      <div class="wrap hero-sales-grid">
        <div class="hero-copy">
          <span class="eyebrow">Minivan24 Tashkent</span>
          <h1>Аренда минивэнов и микроавтобусов в Ташкенте с водителем</h1>
          <p>KIA Carnival, Hyundai Starex, Mercedes-Benz Sprinter и трансферы для семьи, гостей, свадеб, аэропорта и поездок по Узбекистану. Заранее уточняем маршрут, багаж и цену.</p>
          <div class="hero-actions">
            <a class="btn desktop-booking-link" href="#booking">Подобрать автомобиль</a>
            <a class="btn mobile-contact-link" href="{WHATSAPP}" target="_blank" rel="noopener">Написать в WhatsApp</a>
            <a class="btn ghost" href="cars/index.html">Смотреть автопарк</a>
          </div>
        </div>
        <aside class="hero-deal" aria-label="Популярный автомобиль">
          <img src="{HOME_FEATURED_CAR_IMAGE}" alt="KIA Carnival для аренды в Ташкенте">
          <div class="hero-deal-body">
            <span class="eyebrow">Популярный выбор</span>
            <h2>KIA Carnival</h2>
            <div class="specs"><span>7-8 мест</span><span>Большой багажник</span><span>С водителем</span><span>Подача по Ташкенту</span></div>
            <strong>от 150 USD / день</strong>
          </div>
        </aside>
      </div>
    </section>

    <section class="booking" id="booking">
      <div class="wrap">
        <div class="mobile-booking-cta">
          <span class="eyebrow">Быстрая заявка</span>
          <h2>Отправьте маршрут в WhatsApp</h2>
          <p>Дата, адрес подачи, пассажиры и багаж — этого достаточно для первого ответа.</p>
          <a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Отправить заявку</a>
        </div>
        <form class="booking-panel" action="{WHATSAPP}" target="_blank" data-whatsapp-form>
          <div class="booking-head">
            <div>
              <span class="eyebrow">Заявка за минуту</span>
              <h2>Маршрут и детали</h2>
            </div>
            <p>Менеджер получит заявку в WhatsApp и уточнит цену, автомобиль и время подачи.</p>
          </div>
          <div class="booking-grid booking-grid-expanded">
            <label>Имя<input name="name" autocomplete="name" placeholder="Ваше имя" required></label>
            <label>Телефон / WhatsApp<input name="phone" autocomplete="tel" inputmode="tel" placeholder="+998" required pattern="^[0-9+()\\s-]{{7,}}$"></label>
            <label>Куда подать авто?<input name="pickup" placeholder="Аэропорт, отель, адрес"></label>
            <label>Куда едем?<input name="route" placeholder="Маршрут или конечная точка" required></label>
            <label>Дата<input type="date" name="date"></label>
            <label>Время<input type="time" name="time"></label>
            <label>Пассажиры<input type="number" name="passengers" min="1" max="50" placeholder="Например, 7"></label>
            <label>Багаж<select name="luggage"><option>Мало багажа</option><option>Чемоданы</option><option>Много багажа</option></select></label>
            <label>Формат<select name="driver"><option>С водителем</option><option>Без водителя</option><option>Нужно уточнить</option></select></label>
            <label class="booking-wide">Комментарий<textarea name="comment" placeholder="Детские кресла, ожидание, несколько адресов, ночная подача"></textarea></label>
            <label class="form-hp">Сайт<input name="website" tabindex="-1" autocomplete="off"></label>
            <button class="btn booking-submit" type="submit">Отправить заявку</button>
          </div>
        </form>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head"><div><span class="eyebrow">Услуги</span><h2 class="section-title">Популярные услуги аренды</h2></div><a class="btn ghost" href="services/index.html">Все услуги</a></div>
        <div class="grid grid-3">
          <article class="card service-card"><a class="card-media" href="services/arenda-minivena-v-tashkente/index.html"><img src="{HOME_SERVICE_MINIVAN_IMAGE}" alt="Аренда минивэна в Ташкенте" loading="lazy"></a><div class="card-body"><h2><a class="card-title" href="services/arenda-minivena-v-tashkente/index.html">Минивэн для семьи и гостей</a></h2><p>Для аэропорта, города, отеля, экскурсий и поездок с багажом.</p><div class="service-tags"><span>7-8 мест</span><span>KIA Carnival</span><span>багаж</span></div></div></article>
          <article class="card service-card"><a class="card-media" href="services/transfer-aeroport-tashkent/index.html"><img src="{HOME_SERVICE_AIRPORT_IMAGE}" alt="Трансфер аэропорт Ташкент" loading="lazy"></a><div class="card-body"><h2><a class="card-title" href="services/transfer-aeroport-tashkent/index.html">Трансфер аэропорт 24/7</a></h2><p>Встреча рейса, помощь с багажом и подача минивэна ко времени.</p><div class="service-tags"><span>рейс</span><span>отель</span><span>ночью</span></div></div></article>
          <article class="card service-card"><a class="card-media" href="services/mikroavtobus-na-svadbu/index.html"><img src="{HOME_SERVICE_WEDDING_IMAGE}" alt="Микроавтобус на свадьбу" loading="lazy"></a><div class="card-body"><h2><a class="card-title" href="services/mikroavtobus-na-svadbu/index.html">Свадьбы и группы</a></h2><p>Развоз гостей, несколько адресов, ожидание и комфортный салон.</p><div class="service-tags"><span>гости</span><span>Sprinter</span><span>маршрут</span></div></div></article>
        </div>
      </div>
    </section>

    <section class="section soft">
      <div class="wrap grid grid-2 align-start">
        <div>
          <span class="eyebrow">Стоимость</span>
          <h2 class="section-title compact-title">Что входит в 150 USD / день</h2>
          <p class="lead">Цена становится понятнее, когда клиент сразу видит базовые условия и возможные доплаты.</p>
        </div>
        <div class="price-details">
          <div class="panel"><h3>Включено</h3><ul><li>водитель</li><li>подача по Ташкенту</li><li>до 10 часов аренды</li><li>7-8 мест, кондиционер и большой багажник</li></ul></div>
          <div class="panel"><h3>Отдельно</h3><ul><li>топливо за городом</li><li>платные парковки</li><li>ночное ожидание</li><li>дальние маршруты по Узбекистану</li></ul></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <span class="eyebrow">Почему нам доверяют</span>
        <h2 class="section-title">Понятные условия до поездки</h2>
        <div class="trust-strip">
          <article><strong>12</strong><span>автомобилей в автопарке</span></article>
          <article><strong>24/7</strong><span>подача в аэропорт</span></article>
          <article><strong>5+ лет</strong><span>опыт водителей</span></article>
          <article><strong>3 способа</strong><span>оплаты: наличные, карта, перечисление</span></article>
        </div>
        <div class="grid grid-4 trust-grid">
          <article class="feature">{check_icon()}<h3>Реальные фото</h3><p>Показываем салон, багажник и состояние автомобиля до бронирования.</p></article>
          <article class="feature">{check_icon()}<h3>Договор и чек</h3><p>Работаем с частными клиентами, гостями и организациями.</p></article>
          <article class="feature">{check_icon()}<h3>Детские кресла</h3><p>По запросу подготовим кресло и учтем багаж заранее.</p></article>
          <article class="feature">{check_icon()}<h3>Связь до подачи</h3><p>Подтверждаем автомобиль, водителя и точку встречи.</p></article>
        </div>
      </div>
    </section>

    <section class="section soft">
      <div class="wrap">
        <div class="section-head"><div><span class="eyebrow">Автопарк</span><h2 class="section-title">Автомобили под разные задачи</h2></div><div class="carousel-actions"><button class="slider-btn" type="button" data-cars-prev aria-label="Предыдущие автомобили">&lsaquo;</button><button class="slider-btn" type="button" data-cars-next aria-label="Следующие автомобили">&rsaquo;</button><a class="btn ghost" href="cars/index.html">Смотреть автопарк</a></div></div>
        <div class="cars-carousel" data-cars-carousel><div class="cars-track">{home_cars}</div></div>
      </div>
    </section>

    <section class="section">
      <div class="wrap grid grid-2 align-start">
        <div><span class="eyebrow">FAQ</span><h2 class="section-title compact-title">Частые вопросы перед заказом</h2><div class="faq-list">
          {faq_html([
            ("Можно ли заказать минивэн в аэропорт?", "Да. Укажите номер рейса, время прилета, количество пассажиров и багаж. Мы согласуем место встречи и подачу."),
            ("Можно ли арендовать авто без водителя?", "По части автомобилей возможен формат без водителя, но чаще для трансферов и гостей удобнее аренда с водителем."),
            ("Сколько мест в KIA Carnival?", "Обычно 7-8 мест. Если багажа много, лучше заранее указать количество чемоданов."),
            ("Есть ли детское кресло?", "Да, подготовим детское кресло по запросу. Сообщите возраст ребенка при заявке."),
            ("Можно ли оплатить перечислением?", "Да, возможна оплата наличными, картой или перечислением для организаций."),
            ("Работаете ночью?", "Да, подача в аэропорт и ночные поездки возможны 24/7 по предварительному согласованию."),
            ("Можно ли заказать микроавтобус на свадьбу?", "Да. Подберем минивэн или Sprinter под количество гостей, адреса и время ожидания."),
            ("Сколько стоит поездка в Самарканд?", "Цена зависит от даты, маршрута, ожидания, количества пассажиров и класса авто. Отправьте детали, и мы заранее объясним итоговую цену.")
          ])}
        </div></div>
        <div class="panel"><h2>Уточнить маршрут</h2><p>Отправьте маршрут, дату, пассажиров и багаж. Мы ответим в WhatsApp и заранее объясним, что входит в цену.</p><p><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Описать поездку</a></p></div>
      </div>
    </section>
  </main>
"""
    home = re.sub(r"<main>.*?</main>", lambda _: home_main, home, flags=re.S)
    write(index_path, home)


def build():
    _base_build()
    enhance_home()
    postprocess_floating_whatsapp()


if __name__ == "__main__":
    build()

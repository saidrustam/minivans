from pathlib import Path
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
WHATSAPP = "https://wa.me/qr/EMOCPKYY4DJOE1"
INSTAGRAM = "https://www.instagram.com/minivanuz/profilecard/?igsh=YmN3bm9vbjE0ajNq"
LOGO = "uploads/2024/11/minivan-logo-2.png"
FAVICON = "uploads/2024/11/letter-m.png"
DEFAULT_HERO = "uploads/2024/11/mers.webp"
NEWS_PAGE_SIZE = 12

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


def absolute_url(path=""):
    return SITE_URL.rstrip("/") + "/" + str(path).lstrip("/")


def json_ld(data):
    value = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return value.replace("</", "<\\/")


def head(title, description, prefix, canonical=None, image=None, page_type="website", structured_data=None):
    canonical_html = f'  <link rel="canonical" href="{e(canonical)}">\n' if canonical else ""
    og_url = f'  <meta property="og:url" content="{e(canonical)}">\n' if canonical else ""
    og_image = f'  <meta property="og:image" content="{e(absolute_url(image))}">\n' if image else ""
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
{canonical_html}  <meta property="og:type" content="{e(page_type)}">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
{og_url}{og_image}  <meta name="twitter:card" content="summary_large_image">
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
      <nav class="menu" aria-label="Главное меню">
        <a href="{e(rel(prefix, 'index.html'))}"{cls('home')}>Главная</a>
        <a href="{e(rel(prefix, 'cars/index.html'))}"{cls('cars')}>Автопарк</a>
        <a href="{e(rel(prefix, 'news/index.html'))}"{cls('news')}>Новости</a>
        <a href="{e(rel(prefix, 'kontakty/index.html'))}"{cls('contacts')}>Контакты</a>
      </nav>
      <div class="nav-actions"><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Забронировать</a></div>
    </div>
  </header>
"""


def footer(prefix):
    return f"""  <footer class="footer">
    <div class="wrap footer-grid">
      <a href="{e(rel(prefix, 'index.html'))}"><img src="{e(rel(prefix, LOGO))}" alt="Minivan24"></a>
      <div class="footer-links">
        <a href="{e(rel(prefix, 'index.html'))}">Главная</a>
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


def car_schema(car):
    car_url = absolute_url(f"cars/{car['slug']}/")
    return [
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Главная", "item": absolute_url()},
                {"@type": "ListItem", "position": 2, "name": "Автопарк", "item": absolute_url("cars/")},
                {"@type": "ListItem", "position": 3, "name": car["title"], "item": car_url},
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "Car",
            "name": car["title"],
            "description": car_seo_description(car),
            "image": [absolute_url(image) for image in car.get("gallery", [car["image"]])],
            "url": car_url,
            "brand": {"@type": "Brand", "name": car["title"].split()[0]},
            "offers": {
                "@type": "Offer",
                "availability": "https://schema.org/InStock",
                "priceCurrency": "UZS",
                "priceSpecification": {"@type": "PriceSpecification", "description": car.get("price", "по запросу")},
                "seller": {"@type": "Organization", "name": "Minivan24", "telephone": PHONE},
            },
        },
    ]


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


def write_sitemap(cars_data, articles):
    urls = [
        "",
        "cars/",
        "news/",
        "kontakty/",
    ]
    urls.extend(f"cars/{car['slug']}/" for car in cars_data)
    urls.extend(f"news/{article['slug']}/" for article in articles)
    items = "\n".join(f"  <url><loc>{e(absolute_url(url))}</loc></url>" for url in urls)
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
    return [
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Главная", "item": absolute_url()},
                {"@type": "ListItem", "position": 2, "name": "Новости", "item": absolute_url("news/")},
                {"@type": "ListItem", "position": 3, "name": article["title"], "item": article_url},
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": article["title"],
            "description": article_seo_description(article),
            "image": absolute_url(article["image"]),
            "url": article_url,
            "mainEntityOfPage": article_url,
            "author": {"@type": "Organization", "name": "Minivan24"},
            "publisher": {
                "@type": "Organization",
                "name": "Minivan24",
                "logo": {"@type": "ImageObject", "url": absolute_url(LOGO)},
            },
        },
    ]


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


def build():
    articles = load_news()
    cars_data = load_cars()

    feature_html = "".join(
        f'<article class="feature"><div class="icon">✓</div><h3>{e(title)}</h3><p>{e(text)}</p></article>'
        for title, text in [
            ("Честная цена", "Подбираем транспорт под задачу без лишних переплат за неподходящий класс."),
            ("Бронирование 24/7", "Заявку можно отправить заранее или в день поездки через WhatsApp и Telegram."),
            ("Подача по городу", "Аэропорт, вокзал, отель, офис, ресторан или адрес в районе Ташкента."),
            ("Комфортный салон", "Минивэны для семьи, туристов, делегаций, свадеб и междугородних маршрутов."),
        ]
    )
    home_cards = "".join(car_carousel_card(car, "", "cars/") for car in cars_data[:6])
    home = head("Аренда минивэнов в Ташкенте | Minivan24", "Аренда минивэнов и микроавтобусов в Ташкенте с водителем и без.", "")
    home += header("", "home")
    home += f"""  <main>
    <section class="hero" style="--hero-image: url('{DEFAULT_HERO}')">
      <div class="wrap">
        <span class="eyebrow">Minivan24 rent service</span>
        <h1>Аренда минивэнов в Ташкенте для семьи, гостей и поездок</h1>
        <p>Комфортные минивэны и микроавтобусы с водителем и без водителя. Подберём автомобиль под трансфер, экскурсию, свадьбу, деловую поездку или путешествие по Узбекистану.</p>
        <div class="hero-actions"><a class="btn" href="#booking">Подобрать авто</a><a class="btn ghost" href="cars/index.html">Смотреть автопарк</a></div>
      </div>
    </section>
    <section class="booking" id="booking"><div class="wrap"><form class="booking-panel" action="{WHATSAPP}" target="_blank">
      <h2>Быстрая заявка на аренду</h2>
      <div class="booking-grid">
        <label>Место подачи<select name="pickup"><option>Ташкент, аэропорт</option><option>Ташкент, вокзал</option><option>Ташкент, отель</option><option>По Узбекистану</option></select></label>
        <label>Автомобиль<select name="car"><option>KIA Carnival</option><option>HYUNDAI Starex</option><option>HYUNDAI H-1</option><option>MERCEDES-BENZ Sprinter</option><option>TOYOTA Sienna</option></select></label>
        <label>Дата начала<input type="date" name="start"></label><label>Время<input type="time" name="time"></label><button class="btn" type="submit">Отправить</button>
      </div>
    </form></div></section>
    <section class="section"><div class="wrap"><span class="eyebrow">Почему выбирают нас</span><h2 class="section-title">Сервис аренды, который удобно планировать заранее</h2><p class="lead">Мы делаем поездку предсказуемой: помогаем выбрать формат, согласовать маршрут, время подачи и подходящий автомобиль под количество пассажиров и багажа.</p><div class="grid grid-4" style="margin-top:32px">{feature_html}</div></div></section>
    <section class="section soft"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Автопарк</span><h2 class="section-title">Лучшие предложения</h2></div><div class="carousel-actions"><button class="slider-btn" type="button" data-cars-prev aria-label="Предыдущие автомобили">&lsaquo;</button><button class="slider-btn" type="button" data-cars-next aria-label="Следующие автомобили">&rsaquo;</button></div></div><div class="cars-carousel" data-cars-carousel><div class="cars-track">{home_cards}</div></div></div></section>
  </main>
"""
    home += footer("")
    write(ROOT / "index.html", home)

    cars = head("Автопарк | Minivan24", "Минивэны и микроавтобусы в аренду в Ташкенте.", "../")
    cars += header("../", "cars")
    cars += page_hero("Автопарк", "Выберите минивэн или микроавтобус под трансфер, экскурсию, семейную поездку, свадьбу или маршрут по Узбекистану.", "../", cars_data[0]["image"], "Minivan24 cars")
    cars += '<main><section class="section"><div class="wrap"><div class="grid grid-3">\n' + "".join(car_card(car, "../") for car in cars_data) + "</div></div></section></main>\n"
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
        <p><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Забронировать в WhatsApp</a></p>
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
            title = "Новости"
        else:
            out, prefix, link_prefix, index_href, page_base = ROOT / "news/page" / str(page) / "index.html", "../../../", "../../", "../../index.html", "../../page/"
            title = f"Новости: страница {page}"
        cards = "".join(news_card(article, prefix, link_prefix) for article in chunk)
        news = head(f"{title} | Minivan24", "Новости аренды минивэнов и микроавтобусов в Ташкенте.", prefix)
        news += header(prefix, "news")
        news += page_hero(title, "Полезные статьи об аренде минивэнов, трансферах, маршрутах по Ташкенту и поездках по Узбекистану.", prefix, DEFAULT_HERO, "Minivan24 news")
        news += f'<main><section class="section"><div class="wrap"><div class="grid grid-3">\n{cards}</div>{pagination(page, total_pages, index_href, page_base)}</div></section></main>\n'
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
        <h2>Нужен минивэн для поездки?</h2>
        <p>Напишите нам дату, маршрут, количество пассажиров и багаж. Мы подскажем подходящий автомобиль и формат аренды.</p>
        <p><a class="btn" href="{WHATSAPP}" target="_blank" rel="noopener">Написать в WhatsApp</a></p>
      </div>
    </section></main>
"""
        page += footer("../../")
        write(ROOT / "news" / article["slug"] / "index.html", page)

    contacts = head("Контакты | Minivan24", "Контакты Minivan24: аренда минивэнов и микроавтобусов в Ташкенте.", "../")
    contacts += header("../", "contacts")
    contacts += page_hero("Контакты", "Свяжитесь с нами, чтобы подобрать минивэн, микроавтобус или трансфер под вашу поездку.", "../", DEFAULT_HERO, "Minivan24 contacts")
    contacts += f"""  <main><section class="section"><div class="wrap grid grid-2">
      <div class="panel"><h2>Связаться с нами</h2><p><strong>Телефон:</strong> <a href="{PHONE_HREF}">{PHONE}</a></p><p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></p><p><strong>Адрес:</strong> {ADDRESS}</p><p><strong>Telegram:</strong> <a href="{TELEGRAM}">@minivanuzb</a></p><p><strong>WhatsApp:</strong> <a href="{WHATSAPP}" target="_blank" rel="noopener">отправить заявку</a></p></div>
      <form class="panel" action="{WHATSAPP}" target="_blank"><h2>Заявка на аренду</h2><label>Ваше имя<input name="name" placeholder="Имя"></label><label>Телефон<input name="phone" placeholder="+998"></label><label>Маршрут<textarea name="message" placeholder="Дата, маршрут, количество пассажиров"></textarea></label><button class="btn" type="submit">Отправить</button></form>
    </div></section></main>
"""
    contacts += footer("../")
    write(ROOT / "kontakty/index.html", contacts)

    write_sitemap(cars_data, articles)

    print(f"Generated clean HTML: {1 + 1 + len(cars_data) + total_pages + len(articles) + 1} pages")


if __name__ == "__main__":
    build()

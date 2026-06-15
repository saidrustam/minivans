document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const menu = document.querySelector("[data-menu]");
  const menuBackdrop = document.querySelector("[data-menu-backdrop]");

  if (menuToggle && menu) {
    const closeMenu = () => {
      menu.classList.remove("is-open");
      menuBackdrop?.classList.remove("is-open");
      menuToggle.classList.remove("is-open");
      menuToggle.setAttribute("aria-expanded", "false");
      menuToggle.setAttribute("aria-label", "Открыть меню");
      document.body.classList.remove("menu-open");
    };

    const openMenu = () => {
      menu.classList.add("is-open");
      menuBackdrop?.classList.add("is-open");
      menuToggle.classList.add("is-open");
      menuToggle.setAttribute("aria-expanded", "true");
      menuToggle.setAttribute("aria-label", "Закрыть меню");
      document.body.classList.add("menu-open");
    };

    menuToggle.addEventListener("click", () => {
      if (menu.classList.contains("is-open")) {
        closeMenu();
      } else {
        openMenu();
      }
    });

    menu.addEventListener("click", (event) => {
      if (event.target.closest("a")) closeMenu();
    });

    menuBackdrop?.addEventListener("click", closeMenu);

    document.addEventListener("click", (event) => {
      const clickedMenu = event.target.closest("[data-menu]");
      const clickedToggle = event.target.closest("[data-menu-toggle]");
      if (!clickedMenu && !clickedToggle && menu.classList.contains("is-open")) closeMenu();
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") closeMenu();
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 1024) closeMenu();
    });
  }

  // Gallery carousel
  document.querySelectorAll("[data-gallery-card]").forEach((card) => {
    const slides = Array.from(card.querySelectorAll(".car-gallery img"));
    const dots = Array.from(card.querySelectorAll(".car-dot"));
    if (slides.length < 2) return;

    let current = 0;
    const show = (index) => {
      current = (index + slides.length) % slides.length;
      slides.forEach((slide, slideIndex) => {
        slide.classList.toggle("active", slideIndex === current);
      });
      dots.forEach((dot, dotIndex) => {
        dot.classList.toggle("active", dotIndex === current);
      });
    };

    card.querySelector("[data-gallery-prev]")?.addEventListener("click", (event) => {
      event.preventDefault();
      show(current - 1);
    });
    card.querySelector("[data-gallery-next]")?.addEventListener("click", (event) => {
      event.preventDefault();
      show(current + 1);
    });
    dots.forEach((dot, index) => {
      dot.addEventListener("click", (event) => {
        event.preventDefault();
        show(index);
      });
    });
  });

  // Cars carousel
  document.querySelectorAll("[data-cars-carousel]").forEach((carousel) => {
    const track = carousel.querySelector(".cars-track");
    const prev = document.querySelector("[data-cars-prev]");
    const next = document.querySelector("[data-cars-next]");
    if (!track || !prev || !next) return;

    const step = () => {
      const card = track.querySelector(".carousel-card");
      return card ? card.getBoundingClientRect().width + 22 : carousel.clientWidth;
    };

    prev.addEventListener("click", () => {
      carousel.scrollBy({ left: -step(), behavior: "smooth" });
    });
    next.addEventListener("click", () => {
      carousel.scrollBy({ left: step(), behavior: "smooth" });
    });
  });

  // WhatsApp form submission
  document.querySelectorAll("[data-whatsapp-form]").forEach((form) => {
    form.addEventListener("submit", (event) => {
      const data = new FormData(form);
      if (data.get("website")) {
        event.preventDefault();
        return;
      }

      const labels = {
        name: "Имя",
        phone: "Телефон",
        pickup: "Подача",
        route: "Маршрут",
        date: "Дата",
        time: "Время",
        passengers: "Пассажиры",
        luggage: "Багаж",
        driver: "Формат",
        comment: "Комментарий",
      };
      const lines = ["Заявка на аренду Minivan24"];
      Object.entries(labels).forEach(([key, label]) => {
        const value = String(data.get(key) || "").trim();
        if (value) lines.push(`${label}: ${value}`);
      });

      event.preventDefault();
      const url = `${form.action}?text=${encodeURIComponent(lines.join("\n"))}`;
      window.open(url, "_blank", "noopener");
    });
  });
});

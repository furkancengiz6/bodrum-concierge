document.addEventListener('DOMContentLoaded', () => {

    /* ─── TRANSLATIONS ─── */
    const translations = {
        'tr': {
            'nav_contact': 'İLETİŞİM',
            'brand_desc': 'Bodrum\'un En Özel Kapılarını Açan Anahtar',
            'label_services': 'ÖZEL HİZMETLERİMİZ',
            'srv_transfer': 'VIP TRANSFER',
            'srv_transfer_desc': 'Havalimanından otelinize veya Bodrum\'un herhangi bir noktasına Mercedes Vito ve Sprinter araçlarımızla lüks, güvenli ve konforlu transfer hizmeti.',
            'srv_villa': 'VİLLA KİRALAMA',
            'srv_villa_desc': 'Bodrum\'un en prestijli bölgelerinde, özel havuzlu, deniz manzaralı, lüks ve tam donanımlı kiralık villalar. Tatilinizi ev konforunda yaşayın.',
            'srv_yacht': 'YAT KİRALAMA',
            'srv_yacht_desc': 'Ege\'nin turkuaz sularında eşsiz bir deneyim için mürettebatlı, lüks motor yat ve gulet kiralama hizmetleri. Günlük veya haftalık rotalar.',
            'srv_restaurant': 'RESTORAN REZERVASYONU',
            'srv_restaurant_desc': 'Bodrum\'un en popüler ve Michelin yıldızlı restoranlarında sizin için en iyi masayı rezerve ediyoruz. Unutulmaz gastronomi deneyimleri.',
            'srv_beach': 'BEACH CLUB',
            'srv_beach_desc': 'Bodrum\'un en gözde beach club\'larında VIP loca, şezlong ve cabana rezervasyonları. Denizin ve güneşin tadını ayrıcalıklı çıkarın.',
            'srv_nightlife': 'GECE HAYATI',
            'srv_nightlife_desc': 'Bodrum gece hayatının nabzını tutan en seçkin gece kulüplerinde VIP masa rezervasyonları ve sıra beklemeden giriş ayrıcalığı.',
            'srv_assistant': 'KİŞİSEL ASİSTAN',
            'srv_assistant_desc': 'Tatiliniz boyunca size eşlik edecek, alışverişten etkinlik planlamasına kadar her türlü ihtiyacınızla ilgilenecek profesyonel asistan hizmeti.',
            'srv_jet': 'ÖZEL JET & HELİKOPTER',
            'srv_jet_desc': 'Zamanı değerli olanlar için Bodrum\'a hızlı ve konforlu ulaşım. Özel jet kiralama ve havaalanı - otel arası helikopter transferleri.',
            'label_testimonials': 'MİSAFİR DENEYİMLERİ',
            'test_1_quote': '"Harika bir deneyimdi. Her şey kusursuz planlanmıştı. Teşekkürler Bodrum Elite!"',
            'test_2_quote': '"Yat kiralama ve restoran rezervasyonlarımızda bize çok yardımcı oldular. Kesinlikle tavsiye ederim."',
            'test_3_quote': '"VIP transfer hizmetinden çok memnun kaldık. Şoförler çok kibar ve profesyoneldi."',
            'label_faq': 'SIKÇA SORULAN SORULAR',
            'faq_1_q': 'Hizmetlerinize nasıl rezervasyon yapabilirim?',
            'faq_1_a': 'Web sitemizdeki iletişim numaralarımızdan veya WhatsApp/Telegram üzerinden bize ulaşarak rezervasyon yapabilirsiniz.',
            'faq_2_q': 'Ödeme seçenekleriniz nelerdir?',
            'faq_2_a': 'Kredi kartı, banka havalesi ve kripto para dahil olmak üzere çeşitli ödeme seçenekleri sunuyoruz.',
            'faq_3_q': 'Hizmetleriniz 7/24 mü?',
            'faq_3_a': 'Evet, Concierge ekibimiz size 7/24 hizmet vermek için hazırdır.',
            'label_ig': 'BİZİ TAKİP EDİN',
            'footer_tagline': 'BODRUM ELITE CONCIERGE. TÜM HAKLARI SAKLIDIR.',
            'modal_wa_btn': 'WhatsApp ile İletişime Geç',
            'modal_tg_btn': 'Telegram ile İletişime Geç',
            'fab_text': 'MESAJ GÖNDER',
            'label_journal': 'THE LIFESTYLE JOURNAL',
            'journal_1_title': 'Yalıkavak Marina: Lüksün Yeni Başkenti',
            'journal_1_desc': 'Dünyaca ünlü markalar, seçkin restoranlar ve mega yatlarla dolu Yalıkavak Marina\'da bir gün.',
            'journal_2_title': 'Ege\'nin Mavi Sularında Geleneksel Lüks',
            'journal_2_desc': 'Bodrum\'un gizli koylarını özel şefli ahşap guletlerle keşfetmenin ayrıcalığı.',
            'journal_3_title': 'Michelin Yıldızlı Bodrum Geceleri',
            'journal_3_desc': 'Mandarin Oriental ve Bodrum\'un en gözde restoranlarında unutulmaz fine-dining deneyimleri.',
            'journal_4_title': 'Bodrum\'a Helikopter ile İniş',
            'journal_4_desc': 'Trafiksiz, hızlı ve prestijli: Özel helikopter transferleri ve gökyüzünden Bodrum manzaraları.'
        },
        'en': {
            'nav_contact': 'CONTACT',
            'brand_desc': 'The Key to Bodrum\'s Most Exclusive Doors',
            'label_services': 'OUR EXCLUSIVE SERVICES',
            'srv_transfer': 'VIP TRANSFER',
            'srv_transfer_desc': 'Luxury, safe and comfortable transfer service from the airport to your hotel or anywhere in Bodrum with our Mercedes Vito and Sprinter vehicles.',
            'srv_villa': 'VILLA RENTAL',
            'srv_villa_desc': 'Luxury and fully equipped rental villas with private pools and sea views in the most prestigious areas of Bodrum. Experience your holiday in the comfort of home.',
            'srv_yacht': 'YACHT CHARTER',
            'srv_yacht_desc': 'Crewed, luxury motor yacht and gulet charter services for a unique experience in the turquoise waters of the Aegean. Daily or weekly routes.',
            'srv_restaurant': 'RESTAURANT RESERVATION',
            'srv_restaurant_desc': 'We reserve the best table for you in Bodrum\'s most popular and Michelin-starred restaurants. Unforgettable gastronomy experiences.',
            'srv_beach': 'BEACH CLUB',
            'srv_beach_desc': 'VIP lounge, sunbed and cabana reservations at Bodrum\'s most popular beach clubs. Enjoy the sea and sun exclusively.',
            'srv_nightlife': 'NIGHTLIFE',
            'srv_nightlife_desc': 'VIP table reservations and skip-the-line privileges in the most exclusive nightclubs that hold the pulse of Bodrum nightlife.',
            'srv_assistant': 'PERSONAL ASSISTANT',
            'srv_assistant_desc': 'Professional assistant service that will accompany you throughout your holiday and take care of all your needs, from shopping to event planning.',
            'srv_jet': 'PRIVATE JET & HELICOPTER',
            'srv_jet_desc': 'Fast and comfortable transportation to Bodrum for those whose time is valuable. Private jet charter and helicopter transfers between the airport and the hotel.',
            'label_testimonials': 'GUEST EXPERIENCES',
            'test_1_quote': '"It was a wonderful experience. Everything was perfectly planned. Thank you Bodrum Elite!"',
            'test_2_quote': '"They helped us a lot with our yacht charter and restaurant reservations. I highly recommend it."',
            'test_3_quote': '"We were very pleased with the VIP transfer service. The drivers were very polite and professional."',
            'label_faq': 'FREQUENTLY ASKED QUESTIONS',
            'faq_1_q': 'How can I book your services?',
            'faq_1_a': 'You can book by contacting us through our contact numbers on our website or via WhatsApp/Telegram.',
            'faq_2_q': 'What are your payment options?',
            'faq_2_a': 'We offer various payment options including credit card, bank transfer and cryptocurrency.',
            'faq_3_q': 'Are your services 24/7?',
            'faq_3_a': 'Yes, our Concierge team is ready to serve you 24/7.',
            'label_ig': 'FOLLOW US',
            'footer_tagline': 'BODRUM ELITE CONCIERGE. ALL RIGHTS RESERVED.',
            'modal_wa_btn': 'Contact via WhatsApp',
            'modal_tg_btn': 'Contact via Telegram',
            'fab_text': 'SEND MESSAGE',
            'label_journal': 'THE LIFESTYLE JOURNAL',
            'journal_1_title': 'Yalıkavak Marina: The New Capital of Luxury',
            'journal_1_desc': 'A day at Yalıkavak Marina, filled with world-famous brands, exclusive restaurants, and mega yachts.',
            'journal_2_title': 'Traditional Luxury in the Aegean Waters',
            'journal_2_desc': 'The privilege of exploring Bodrum\'s hidden bays with private chef-catered wooden gulets.',
            'journal_3_title': 'Michelin-Starred Bodrum Nights',
            'journal_3_desc': 'Unforgettable fine-dining experiences at Mandarin Oriental and Bodrum\'s most popular restaurants.',
            'journal_4_title': 'Landing in Bodrum by Helicopter',
            'journal_4_desc': 'Traffic-free, fast, and prestigious: Private helicopter transfers and sky views of Bodrum.'
        },
        'ru': {
            'nav_contact': 'КОНТАКТЫ',
            'brand_desc': 'Ключ к самым эксклюзивным дверям Бодрума',
            'label_services': 'НАШИ ЭКСКЛЮЗИВНЫЕ УСЛУГИ',
            'srv_transfer': 'VIP-ТРАНСФЕР',
            'srv_transfer_desc': 'Роскошный, безопасный и комфортный трансфер из аэропорта в ваш отель или в любую точку Бодрума на наших автомобилях Mercedes Vito и Sprinter.',
            'srv_villa': 'АРЕНДА ВИЛЛЫ',
            'srv_villa_desc': 'Роскошные и полностью оборудованные виллы в аренду с частными бассейнами и видом на море в самых престижных районах Бодрума.',
            'srv_yacht': 'АРЕНДА ЯХТЫ',
            'srv_yacht_desc': 'Услуги по аренде роскошных моторных яхт и гулет с экипажем для уникального отдыха в бирюзовых водах Эгейского моря. Ежедневные или еженедельные маршруты.',
            'srv_restaurant': 'БРОНИРОВАНИЕ РЕСТОРАНОВ',
            'srv_restaurant_desc': 'Мы бронируем для вас лучший столик в самых популярных ресторанах Бодрума и ресторанах, отмеченных звездами Мишлен. Незабываемые гастрономические впечатления.',
            'srv_beach': 'ПЛЯЖНЫЙ КЛУБ',
            'srv_beach_desc': 'Бронирование VIP-лож, шезлонгов и беседок в самых популярных пляжных клубах Бодрума. Наслаждайтесь морем и солнцем исключительно.',
            'srv_nightlife': 'НОЧНАЯ ЖИЗНЬ',
            'srv_nightlife_desc': 'Бронирование VIP-столиков и привилегии прохода без очереди в самых эксклюзивных ночных клубах, в которых бьется пульс ночной жизни Бодрума.',
            'srv_assistant': 'ЛИЧНЫЙ ПОМОЩНИК',
            'srv_assistant_desc': 'Профессиональные услуги помощника, который будет сопровождать вас на протяжении всего отпуска и позаботится обо всех ваших потребностях, от покупок до планирования мероприятий.',
            'srv_jet': 'ЧАСТНЫЙ САМОЛЕТ И ВЕРТОЛЕТ',
            'srv_jet_desc': 'Быстрая и комфортная транспортировка в Бодрум для тех, чье время ценно. Аренда частного самолета и вертолетные трансферы между аэропортом и отелем.',
            'label_testimonials': 'ОТЗЫВЫ ГОСТЕЙ',
            'test_1_quote': '"Это был замечательный опыт. Все было идеально спланировано. Спасибо Bodrum Elite!"',
            'test_2_quote': '"Они очень помогли нам с арендой яхты и бронированием столиков в ресторане. Очень рекомендую."',
            'test_3_quote': '"Мы остались очень довольны услугой VIP-трансфера. Водители были очень вежливы и профессиональны."',
            'label_faq': 'ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ',
            'faq_1_q': 'Как я могу забронировать ваши услуги?',
            'faq_1_a': 'Вы можете забронировать, связавшись с нами по контактным телефонам на нашем сайте или через WhatsApp/Telegram.',
            'faq_2_q': 'Каковы ваши варианты оплаты?',
            'faq_2_a': 'Мы предлагаем различные варианты оплаты, включая кредитные карты, банковские переводы и криптовалюту.',
            'faq_3_q': 'Ваши услуги работают круглосуточно и без выходных?',
            'faq_3_a': 'Да, наша команда консьержей готова обслуживать вас круглосуточно и без выходных.',
            'label_ig': 'ПОДПИСЫВАЙТЕСЬ НА НАС',
            'footer_tagline': 'BODRUM ELITE CONCIERGE. ВСЕ ПРАВА ЗАЩИЩЕНЫ.',
            'modal_wa_btn': 'Связаться через WhatsApp',
            'modal_tg_btn': 'Связаться через Telegram',
            'fab_text': 'ОТПРАВИТЬ СООБЩЕНИЕ',
            'label_journal': 'ЖУРНАЛ О СТИЛЕ ЖИЗНИ',
            'journal_1_title': 'Ялыкавак Марина: Новая Столица Роскоши',
            'journal_1_desc': 'День в Yalıkavak Marina, наполненный всемирно известными брендами, эксклюзивными ресторанами и мега-яхтами.',
            'journal_2_title': 'Традиционная Роскошь в Эгейских Водах',
            'journal_2_desc': 'Привилегия исследовать скрытые бухты Бодрума на деревянных гулетах с личным поваром.',
            'journal_3_title': 'Бодрумские Ночи со Звездами Мишлен',
            'journal_3_desc': 'Незабываемые гастрономические впечатления в Mandarin Oriental и самых популярных ресторанах Бодрума.',
            'journal_4_title': 'Прибытие в Бодрум на Вертолете',
            'journal_4_desc': 'Без пробок, быстро и престижно: Частные вертолетные трансферы и виды Бодрума с неба.'
        }
    };

    /* ─── LANGUAGE SWITCHER ─── */
    const langSelect = document.getElementById('lang-switcher');
    
    // Set initial language based on browser or default to EN
    let currentLang = localStorage.getItem('lang') || 'en';
    langSelect.value = currentLang;

    function applyTranslations(lang) {
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[lang] && translations[lang][key]) {
                el.textContent = translations[lang][key];
            }
        });
        document.documentElement.lang = lang;
        currentLang = lang;
        localStorage.setItem('lang', lang);
    }

    langSelect.addEventListener('change', (e) => {
        applyTranslations(e.target.value);
    });

    // Apply initially
    applyTranslations(currentLang);

    /* ─── DARK MODE TOGGLE ─── */
    const themeToggleBtn = document.getElementById('theme-toggle');
    let isDark = localStorage.getItem('theme') !== 'light'; // Default to dark

    function setTheme(dark) {
        if (dark) {
            document.documentElement.setAttribute('data-theme', 'dark');
            // update icon to sun
            themeToggleBtn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>';
        } else {
            document.documentElement.removeAttribute('data-theme');
            // update icon to moon
            themeToggleBtn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>';
        }
        localStorage.setItem('theme', dark ? 'dark' : 'light');
    }

    themeToggleBtn.addEventListener('click', () => {
        isDark = !isDark;
        setTheme(isDark);
    });

    // Apply initially
    setTheme(isDark);

    /* ─── MODAL LOGIC ─── */
    const modal = document.getElementById('service-modal');
    const modalClose = document.querySelector('.modal-close');
    const modalBackdrop = document.querySelector('.modal-backdrop');
    const modalTitle = document.getElementById('modal-title');
    const modalDesc = document.getElementById('modal-desc');
    const modalImg = document.getElementById('modal-img');

    function openModal(serviceKey, imgSrc) {
        // Get translated title and desc based on serviceKey (e.g. srv_transfer)
        modalTitle.textContent = translations[currentLang][serviceKey] || '';
        modalDesc.textContent = translations[currentLang][serviceKey + '_desc'] || '';
        
        if (imgSrc) {
            modalImg.src = imgSrc;
        }

        // Add proper WhatsApp/Telegram links based on service
        const waNumber = '905330364966';
        const serviceName = encodeURIComponent(modalTitle.textContent);
        const waMessage = encodeURIComponent(`Hello, I would like to get information about ${modalTitle.textContent}.`);
        document.getElementById('modal-wa').href = `https://wa.me/${waNumber}?text=${waMessage}`;
        
        // Make body unscrollable
        document.body.style.overflow = 'hidden';
        
        modal.classList.add('open');
    }

    function closeModal() {
        modal.classList.remove('open');
        document.body.style.overflow = '';
    }

    document.querySelectorAll('.card, .journal-card').forEach(card => {
        card.addEventListener('click', (e) => {
            e.preventDefault();
            const serviceKey = card.getAttribute('data-service');
            const imgSrc = card.querySelector('img').src;
            openModal(serviceKey, imgSrc);
        });
    });

    modalClose.addEventListener('click', closeModal);
    modalBackdrop.addEventListener('click', closeModal);

    /* ─── Scroll Reveal (IntersectionObserver) ─── */
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.1, rootMargin: '0px 0px -30px 0px' }
    );

    document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));

    /* ─── Smooth scroll for anchor links ─── */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            e.preventDefault();
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
});

# 🛡️ 72 hodin
### Občanský manuál krizové připravenosti pro nepěkné časy

🌐 **Web je spuštěn a dostupný online na:** **[72hodin.info](https://72hodin.info)**

Moderní, bleskově rychlá, plně přístupná a offline fungující statická webová příručka krizové připravenosti pro občany České republiky. 

Základem civilní ochrany je schopnost postarat se o sebe, svou rodinu i sousedy po dobu **prvních 3 dnů (72 hodin)**, než se v případě rozsáhlé krize (blackout, povodně, vichřice, technologická havárie) dostane pomoc ke všem potřebným.

Projekt vychází z doporučení Ministerstva vnitra ČR (MV ČR), Hasičského záchranného sboru ČR (HZS ČR), Červeného kříže a mezinárodních standardů civilní ochrany.

---

## 🚀 Jak spustit

* Otevřete si v libovolném prohlížeči stránku **[72hodin.info](https://72hodin.info)** (funguje na počítači, tabletu i mobilu).

*(Pro lokální offline použití si stačí stáhnout tento repozitář a dvakrát kliknout na `index.html` – funguje ihned i bez připojení k internetu).*

---

## 📌 Aktuální stav projektu a Crisis UX vylepšení

Projekt je ve stabilní produkční verzi nasazené přes GitHub Pages s vlastní doménou a optimalizovaný dle zásad **Crisis UX** (okamžitá čitelnost pod vysokým stresem, minimální kognitivní zátěž, přístupnost WCAG AAA):

* **⚡ Akutní krizový rozcestník („Co se právě děje?“):** Přímo v horní části stránky je interaktivní rozcestník pro 6 nejčastějších krizových scénářů (*Blackout / nejde proud*, *Houkají sirény*, *Musím se evakuovat*, *Nejde pitná voda*, *Panika a šok*, *Výpadek signálu & Rádio*), který na jedno klepnutí zobrazí 3 nejdůležitější kroky pro prvních 60 vteřin.
* **🔍 Okamžité offline vyhledávání (klávesa `/`):** Fulltextové vyhledávání bez závislosti na internetu (tolerantní k překlepům v diakritice) s rychlými štítky (*Siréna*, *Evakuační batoh*, *Voda*, *Plyn a jistič*, *Rádio FM*, *Děti*, *Panika*), které po kliknutí automaticky rozbalí příslušnou sekci a vizuálně zvýrazní hledaný návod.
* **🚨 Stálá dostupnost SOS kontaktů (`📞 SOS` v hlavičce):** Kromě horní nouzové lišty je ve fixní hlavičce trvale dostupné červené tlačítko `📞 SOS` s výsuvným panelem pro okamžité volání `112`, `150`, `155`, `158` odkudkoliv na stránce. Na malých telefonech zůstávají pod čísly čitelné i textové popisky složek (*SOS*, *Hasiči*, *Záchranka*, *Policie*).
* **⚡ Boxy „V KOSTCE (TL;DR)“ na začátku každé sekce:** Každá z 8 tematických kapitol začíná výrazným přehledem 3 nejdůležitějších bodů pro bleskové zorientování do 5 sekund.
* **🧮 Interaktivní kalkulačka zásob na 72 hodin:** Dynamický výpočet potřebného množství litrů pitné vody (včetně počtu 1,5l PET lahví), porcí jídla bez vaření, kapacity powerbanky a hotovosti podle počtu dospělých, dětí a domácích mazlíčků.
* **📋 Sjednocené interaktivní checklisty a akční plán na víkend:**
  * Příprava zásob pro domácnost (12 bodů se štítky doporučeného množství) automaticky vyhodnocuje skóre připravenosti a navrhuje **3 nejbližší kroky na víkend** (bez nutnosti vyplňovat duplicitní dotazník).
  * Otevřený 9bodový akční evakuační checklist + **šablona evakuační SMS na 1 kliknutí** (kopírování do schránky / přímé otevření v SMS aplikaci).
  * Specifické rady a 10bodový checklist pro lidi žijící osaměle a seniory.
  * Automatické ukládání stavu do `localStorage` s ukazatelem dokončení.
* **🚨 Samostatná sekce Sirény & Poplach + 14 krajů ČRo Radiožurnál:**
  * Vizuální grafické odlišení 3 tónů sirén (*Všeobecná výstraha – kolísavý 140 s*, *Požární poplach – přerušovaný 60 s*, *Zkouška sirén – stálý tón 1. středu v měsíci ve 12:00*).
  * Kompletní přehled FM frekvencí **ČRo Radiožurnál pro všech 14 krajů ČR** a přímý odkaz na nízkoobjemový **Teletext ČT** pro přetížené mobilní sítě (2G/EDGE).
  * Filtrovatelná tabulka krizových kontaktů (Vše / IZS / Psychika & Děti / Senioři / Speciální), která se na mobilech automaticky transformuje do přehledných dotykových karet bez horizontálního posouvání.
* **🫁 Psychologická první pomoc a Rodinný plán:**
  * Interaktivní **Krabicové dýchání 4-4-4-4 (Box Breathing)** s počítadlem dokončených cyklů a technika **Uzemnění 5-4-3-2-1**.
  * Návody, jak mluvit o krizích s dětmi podle věkových kategorií (0–18 let).
  * Formulář **Rodinného krizového plánu** s automatickým ukládáním a tiskem na 1 list A4 (doplněný o patičku s tísňovými čísly, tóny sirén a hlavními FM frekvencemi pro připevnění na lednici).
* **♿ Přístupnost (A11Y & WCAG AAA) a soukromí:**
  * Přepínání tmavého a světlého režimu (šetří baterii telefonu na OLED displejích).
  * Cyklické zvětšení písma (100 % / 125 % / 150 %) pro seniory a slabozraké.
  * Žádné sledovací cookies, žádné externí skripty či fonty blokující vykreslení. Transparentní anonymní měření návštěvnosti přes open-source Umami Analytics s možností okamžitého opt-outu.

---

## 🔒 Ochrana soukromí a analytika (Umami)

Web využívá pro základní přehled o návštěvnosti nezávislý open-source nástroj **[Umami Analytics](https://umami.is/)**.

### Proč se nemusíte bát (žádné sledování ani skryté praktiky):
* 🍪 **Žádné cookies:** Do vašeho prohlížeče se neukládají vůbec žádné sledovací soubory cookies.
* 🛡️ **Žádné profilování uživatelů:** Nesledujeme vaši identitu, historii prohlížení ani pohyb po jiných webech.
* 👤 **Žádné osobní údaje:** IP adresy se neukládají do databáze a veškerá data jsou plně anonymizována.
* 🇪🇺 **100% v souladu s GDPR:** Nástroj slouží čistě k tomu, abychom věděli, kolik lidí manuál čte a které krizové příručky nejvíce pomáhají. Data nejsou nikomu prodávána ani komerčně využívána.

### Jak měření v prohlížeči vypnout / zapnout (Opt-Out):
Pokud si přesto nepřejete, aby se vaše zobrazení anonymně započítávalo do souhrnné statistiky návštěvnosti, můžete sledování jednoduše jedním kliknutím vypnout:

* 🚫 **[Vypnout sledování pro tento prohlížeč](https://72hodin.info/?umami=off)** – do vašeho prohlížeče uloží lokální značku `umami.disabled = 1` a veškeré měření okamžitě zastaví.
* ✅ **[Znovu zapnout sledování](https://72hodin.info/?umami=on)** – vrátí měření do výchozího stavu.

---

## 📂 Struktura repozitáře

```text
72-hodin/
├── index.html        # Kompletní webová aplikace (HTML + CSS + JS bez závislostí)
├── CNAME             # Směrování vlastní domény (72hodin.info)
├── README.md         # Dokumentace a představení projektu
└── data-manual/      # Kompletní archiv 9 originálních PDF příruček a checklistů
    ├── 00_Uvodni_slovo_a_obsah_slozky.pdf
    ├── 01a_Krizova_pripravenost_domacnosti_manual.pdf
    ├── 01b_Checklist_pro_domacnosti.pdf
    ├── 02a_Krizova_pripravenost_pro_lidi_zijici_osamele_manual.pdf
    ├── 02b_Checklist_pro_lidi_zijici_osamele.pdf
    ├── 03_Krizove_kontakty_a_pokyny_CR.pdf
    ├── 04_Prvni_psychicka_pomoc_v_krizovych_situacich.pdf
    ├── 05_Jak_mluvit_s_detmi_pri_krizovych situacich_manual_kontakty.pdf
    └── 06_Obcansky_manual_pro_nepekne_casy_KOMPLET.pdf
```

---

## 🤝 Kredity a autoři

* **Web vytvořil:** [Petr Hervy](https://www.petrhervy.com/)
* **Obsah vytvořil:** [Radio Free America](https://www.facebook.com/rfaprague)
* **Zdroje metodiky:** Ministerstvo vnitra ČR, Hasičský záchranný sbor ČR, Červený kříž, Civilní obrana a Vládní bezpečnostní centrum Polska (RCB)

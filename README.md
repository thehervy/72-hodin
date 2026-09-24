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

## 📌 Aktuální stav projektu

Projekt je ve stabilní produkční verzi nasazené přes GitHub Pages s vlastní doménou:

* **Plná mobilní optimalizace:** Dvouřádková fixní hlavička s okamžitým přístupem k tísňovým linkám (112, 150, 155, 158) a hamburger menu, která zůstává pevně přichycená při scrollování bez zakrývání obsahu.
* **Offline-Ready:** Web je napsán v čistém vanilla HTML, CSS a JS bez externích frameworků, závislostí či fontů třetích stran. Stránku lze uložit a číst kdykoliv offline.
* **Interaktivní kontrolní seznamy (Checklisty):**
  * Příprava zásob pro domácnost (voda, trvanlivé potraviny, teplo, hygiena, finance).
  * Evakuační zavazadlo pro každého člena rodiny.
  * Specifické rady a checklist pro lidi žijící osaměle.
  * Automatické ukládání rozpracovaného stavu do paměti zařízení (`localStorage`) s animovaným ukazatelem dokončení.
* **Psychologická první pomoc a krizové nástroje:**
  * Interaktivní vizuální widget pro **Krabicové dýchání 4-4-4-4 (Box Breathing)** pro zvládnutí akutní paniky a stresu.
  * Návody, jak mluvit o krizích s dětmi podle věkových kategorií.
  * Rychlý test připravenosti (12 otázek) s okamžitým vyhodnocením skóre a doporučením.
  * Formulář pro sestavení vlastního rodinného krizového plánu s možností přímého tisku na A4.
* **Přístupnost (A11Y & WCAG AAA):**
  * Přepínání tmavého a světlého režimu (šetří baterii telefonu na OLED displejích).
  * Možnost cyklického zvětšení písma (100 % / 125 % / 150 %) pro seniory a slabozraké.
  * Plná podpora ovládání z klávesnice a odečítačů obrazovky.
* **Respekt k soukromí:**
  * Žádné sledovací cookies, žádná otravná cookie lišta.
  * Transparentní anonymní měření návštěvnosti přes open-source Umami Analytics s možností okamžitého opt-outu.

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
* **Zdroje metodiky:** Ministerstvo vnitra ČR, Hasičský záchranný sbor ČR, Červený kříž

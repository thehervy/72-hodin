# 🛡️ Cimrmanových 72 hodin
### Občanský manuál krizové připravenosti pro nepěkné časy

Moderní, přístupná, ultra-rychlá a plně offline-funkční statická webová stránka civilní připravenosti pro občany České republiky.

Projekt vychází z doporučení Ministerstva vnitra ČR (MV ČR), Hasičského záchranného sboru ČR (HZS ČR), Červeného kříže a WHO, s odkazem na kampaň *72 hodin*.

---

## 🌟 Funkce a vlastnosti

- **Offline-First:** Jeden self-contained HTML soubor (`index.html`) bez externích závislostí a knihoven. Funguje spolehlivě i při výpadku elektřiny a internetu po uložení na disk.
- **Přístupnost (A11Y & WCAG AAA):**
  - Všechny velikosti v `rem` jednotkách – web se plně přizpůsobuje nastavení prohlížeče.
  - Tlačítko `A↑ Písmo` v záhlaví pro cyklické zvětšení písma (100 % / 125 % / 150 %).
  - Přepínač tmavého a světlého režimu (`🌙 Režim`) s podporou systémových preferencí a šetřením baterie na OLED displejích.
  - Plná podpora navigace z klávesnice (`Tab`) a čteček obrazovky (*Skip to content*, ARIA).
- **Sticky Emergency Bar:** Vždy dostupná a přímo klikatelná tísňová čísla ČR (112, 150, 155, 158).
- **Interaktivní nástroje:**
  - Živé checklisty s automatickým ukládáním do `localStorage` a progress bary.
  - Vizuální animovaný časovač pro **Krabicové dýchání 4-4-4-4 (Box Breathing)** pro zvládání paniky.
  - Rychlý test připravenosti (12 otázek) s okamžitým hodnocením.
  - Rodinný krizový plán k vyplnění s možností tisku na A4 (`@media print`).
- **Kompletní archiv PDF:** Odkazy na stažení všech 9 originálních manuálů ze složky `data-manual/` včetně souhrnné 62stránkové příručky.

---

## 📂 Struktura repozitáře

```
72-hodin/
├── index.html        # Kompletní statická webová aplikace (HTML + CSS + JS)
├── README.md         # Dokumentace projektu
└── data-manual/      # Originální PDF příručky a checklisty ke stažení
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

## 🚀 Jak spustit

1. **Lokálně:** Stačí dvakrát kliknout na `index.html` a otevře se v jakémkoli webovém prohlížeči (Chrome, Firefox, Edge, Safari).
2. **Online (GitHub Pages):** V nastavení tohoto repozitáře na GitHubu (*Settings* ➔ *Pages*) zvolte větev `main` a kořenový adresář `/ (root)`. Web bude ihned dostupný online.

---

## 🤝 Kredity

- **Web vytvořil:** [Petr Hervy](https://www.petrhervy.com/)
- **Obsah vytvořil:** [Radio Free America](https://www.facebook.com/rfaprague)

<div dir="rtl" align="center">

<img src="assets/o2jb-logo-transparent.png" alt="o2JB" width="210">

# o2JB

استضافة مخصصة لتشغيل PS4 9.00 Jailbreak  
واجهة خفيفة، مربع حالة واضح، وتجهيز للكاش الأوفلاين.

![Firmware](https://img.shields.io/badge/Firmware-9.00-8b5cf6?style=for-the-badge)
![Host](https://img.shields.io/badge/Host-GitHub%20Pages-111827?style=for-the-badge)
![Made By](https://img.shields.io/badge/made%20by-Dm7g-facc15?style=for-the-badge)

</div>

<div dir="rtl">

## عن المشروع

`o2JB` هو واجهة مخصصة مبنية على سورس لتعديل السوني 4 PSFree/Lapse على أجهزة PlayStation 4 إصدار `9.00`.

التعديل هنا يركز على الواجهة فقط: ثيم جلكسي، شعار o2JB، مربع `Status Log` واضح، وحقوق `Dm7g`.

## المميزات

- واجهة باسم `o2JB`.
- ثيم جلكسي خفيف مناسب لمتصفح PS4.
- مربع كونسول واضح لمتابعة مراحل التشغيل.
- دعم أوفلاين كاش عبر `psfree_lapse.appcache`.
- ملفات التشغيل الأساسية محفوظة كما هي.

## التشغيل المحلي

```powershell
python serve.py
```

ثم افتح من الكمبيوتر:

```text
http://localhost:8000/
```

ومن PS4 على نفس الشبكة:

```text
http://YOUR-PC-IP:8000/
```

## GitHub Pages

ارفع الملفات في جذر المستودع، ثم فعل GitHub Pages:

```text
Settings -> Pages -> Deploy from a branch -> main -> /root
```

## ملفات مهمة

```text
index.html
cache.html
psfree_lapse.cache
psfree_lapse.appcache
payload.js
payload.bin
psfree.mjs
lapse.mjs
module/
rop/
kpatch/
fonts/
```

## الحقوق

<div align="center">

**o2JB**

**made by Dm7g**

Instagram: [`Dm7g`](https://instagram.com/Dm7g)

جميع حقوق الواجهة والتخصيص محفوظة لـ **Dm7g**.

</div>

## الرخصة

ملفات PSFree/Lapse الأصلية تبقى تحت رخصتها الأصلية الموجودة في:

```text
LICENSE
COPYING
```

</div>

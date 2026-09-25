
"""
Vize Radar V4 - 2026 Resmi Linkler - TÜM ÜLKELER
Tek yetkili kaynaklar - 2026 güncel
"""
OFFICIAL_LINKS_2026 = {
    "DE": {"country": "Almanya", "url": "https://idata.com.tr/de/tr", "provider": "iDATA", "authority": "Tek yetkili"},
    "IT": {"country": "İtalya", "url": "https://idata.com.tr/ita/tr", "provider": "iDATA"},
    "FR": {"country": "Fransa", "url": "https://visa.vfsglobal.com/tur/tr/fra", "provider": "VFS Global"},
    "NL": {"country": "Hollanda", "url": "https://visa.vfsglobal.com/tur/tr/nld", "provider": "VFS Global"},
    "BE": {"country": "Belçika", "url": "https://visa.vfsglobal.com/tur/tr/bel", "provider": "VFS Global"},
    "AT": {"country": "Avusturya", "url": "https://visa.vfsglobal.com/tur/tr/aut", "provider": "VFS Global"},
    "SE": {"country": "İsveç", "url": "https://visa.vfsglobal.com/tur/tr/swe", "provider": "VFS Global"},
    "NO": {"country": "Norveç", "url": "https://visa.vfsglobal.com/tur/tr/nor", "provider": "VFS Global"},
    "DK": {"country": "Danimarka", "url": "https://visa.vfsglobal.com/tur/tr/dnk", "provider": "VFS Global"},
    "FI": {"country": "Finlandiya", "url": "https://visa.vfsglobal.com/tur/tr/fin", "provider": "VFS Global"},
    "PL": {"country": "Polonya", "url": "https://visa.vfsglobal.com/tur/tr/pol", "provider": "VFS Global"},
    "CZ": {"country": "Çekya", "url": "https://visa.vfsglobal.com/tur/tr/cze", "provider": "VFS Global"},
    "HU": {"country": "Macaristan", "url": "https://visa.vfsglobal.com/tur/tr/hun", "provider": "VFS Global"},
    "PT": {"country": "Portekiz", "url": "https://visa.vfsglobal.com/tur/tr/prt", "provider": "VFS Global"},
    "GR": {"country": "Yunanistan", "url": "https://visa.vfsglobal.com/tur/tr/grc", "provider": "VFS Global / Kosmos"},
    "CH": {"country": "İsviçre", "url": "https://visa.vfsglobal.com/tur/tr/che", "provider": "VFS Global"},
    "ES": {"country": "İspanya", "url": "https://turkey.blsspainvisa.com/", "provider": "BLS Spain"},
    "GB": {"country": "Birleşik Krallık", "url": "https://visas-immigration.service.gov.uk/product/turkey", "provider": "TLScontact"},
    "US": {"country": "Amerika", "url": "https://ais.usvisa-info.com/tr-tr/niv", "provider": "US Travel Docs"},
    "CA": {"country": "Kanada", "url": "https://visa.vfsglobal.com/tur/tr/can", "provider": "VFS Global"},
}
OFFICIAL_LINKS = OFFICIAL_LINKS_2026
def get_link(c): return OFFICIAL_LINKS_2026.get(c.upper(),{}).get("url")
def get_all_links(): return OFFICIAL_LINKS_2026

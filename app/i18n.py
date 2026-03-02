import json
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlencode

from flask import g, request, url_for
from werkzeug.routing import BuildError

SUPPORTED_LOCALES = {
    "en": {
        "label": "EN",
        "dir": "ltr",
        "og_locale": "en_US",
        "rss_language": "en-us",
    },
    "ar": {
        "label": "AR",
        "dir": "rtl",
        "og_locale": "ar_AR",
        "rss_language": "ar",
    },
}

DEFAULT_LOCALE = "en"
TRANSLATIONS_DIR = Path(__file__).resolve().parent / "static" / "js" / "translations"


def normalize_locale(raw_locale):
    if not raw_locale:
        return None
    primary = str(raw_locale).strip().lower().split("-")[0]
    return primary if primary in SUPPORTED_LOCALES else None


def resolve_locale(raw_locale):
    return normalize_locale(raw_locale) or DEFAULT_LOCALE


def get_supported_locale_codes():
    return tuple(SUPPORTED_LOCALES.keys())


def get_locale_meta(locale=None):
    return SUPPORTED_LOCALES[resolve_locale(locale)]


def is_supported_locale(locale):
    return normalize_locale(locale) is not None


def get_current_locale():
    return getattr(g, "locale", DEFAULT_LOCALE)


@lru_cache(maxsize=32)
def _load_raw_translations(locale):
    file_path = TRANSLATIONS_DIR / f"{locale}.json"
    if not file_path.exists():
        return {}
    with file_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        return {}
    return data


@lru_cache(maxsize=32)
def load_translations(locale):
    normalized = resolve_locale(locale)
    fallback = _load_raw_translations(DEFAULT_LOCALE)
    if normalized == DEFAULT_LOCALE:
        return fallback
    localized = _load_raw_translations(normalized)
    merged = dict(fallback)
    merged.update(localized)
    return merged


def translate(key, locale=None, default=None):
    translations = load_translations(locale or get_current_locale())
    if key in translations:
        return translations[key]
    if default is not None:
        return default
    return key


def get_alternate_locale(locale=None):
    current = resolve_locale(locale or get_current_locale())
    for code in SUPPORTED_LOCALES:
        if code != current:
            return code
    return current


def build_switch_locale_url(target_locale):
    target = resolve_locale(target_locale)
    endpoint = request.endpoint
    if not endpoint:
        return url_for("main.index", locale=target)

    if endpoint.startswith("main.") and endpoint.endswith("_legacy"):
        endpoint = endpoint[:-7]

    values = dict(request.view_args or {})
    values["locale"] = target

    try:
        base_url = url_for(endpoint, **values)
    except BuildError:
        base_url = url_for("main.index", locale=target)

    if request.args:
        return f"{base_url}?{urlencode(request.args, doseq=True)}"
    return base_url

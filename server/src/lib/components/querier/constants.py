# --------------------------------- Data types ---------------------------------

CONTENT_TYPE_KEY = "type"
CONTENT_KEY = "content"

CONTENT_TYPES_JSON = {"application/json", "application/ld+json"}
CONTENT_TYPES_TEXT = {
    "text/html",
    "text/plain",
    "text/csv",
    "text/xml",
    "text/css"
}
CONTENT_TYPES_XML = {"application/xml", "application/xhtml+xml", "text/xml"}
CONTENT_TYPES_BINARY = {
    "application/octet-stream",
    "application/pdf",
    "application/zip",
    "application/x-gzip",
    "application/x-tar",
    "application/x-7z-compressed",
    "application/x-rar-compressed",
    "application/x-bzip2",
    "application/x-xz",
    "application/x-lzip",
    "application/x-lzma",
    "application/x-lzop",
    "application/x-snappy-framed",
    "application/xz",
    "application/x-arj",
    "application/x-cpio",
    "application/x-shar",
    "application/x-compress",
    "application/x-ace",
    "application/x-stuffit",
    "application/x-stuffitx",
    "application/x-iso9660-image",
    "application/x-nrg",
    "application/x-gear",
    "application/x-dms",
    "application/x-cfs-compressed",
    "application/x-astrotite-afa",
    "application/x-squeeze",
    "application/x-lzh-compressed",
    "application/x-lha",
    "application/x-lrzip",
    "application/x-lrzip-compressed-tar",
    "application/x-arc",
    "application/x-ear",
    "application/x-war",
    "application/x-cab",
    "application/x-msi",
    "application/x-alz",
    "application/x-ar",
    "application/x-deb",
    "application/x-rpm",
    "application/x-sis",
    "application/x-apk",
    "application/x-ipk",
    "application/x-xpi",
    "application/x-java-archive",
    "application/x-webarchive",
    "application/x-b1",
    "application/x-b6z",
    "application/x-cbr",
    "application/x-cb7",
    "application/x-cbt",
    "application/x-cbz",
    "application/x-cba",
    "application/java-archive",
    "application/x-shockwave-flash",
    "application/x-www-form-urlencoded",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.ms-powerpoint",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.android.package-archive"
}
CONTENT_TYPES_AUDIO = {
    "audio/midi",
    "audio/mpeg",
    "audio/webm",
    "audio/ogg",
    "audio/wav",
    "audio/flac",
    "audio/aac",
    "audio/mp4",
    "audio/opus",
    "audio/x-ms-wma",
    "audio/vnd.rn-realaudio"
}
CONTENT_TYPES_IMAGES = {
    "image/gif",
    "image/jpeg",
    "image/png",
    "image/webp",
    "image/svg+xml",
    "image/bmp",
    "image/vnd.microsoft.icon",
    "image/tiff",
    "image/x-icon",
    "image/vnd.djvu"
}
CONTENT_TYPES_VIDEO = {
    "video/mpeg",
    "video/mp4",
    "video/quicktime",
    "video/x-ms-wmv",
    "video/x-msvideo",
    "video/x-flv",
    "video/webm"
}

# ---------------- Compiled response nodes for the request info ----------------
RESPONSE_NODE_BODY_KEY = "body"
RESPONSE_NODE_BODY_TYPE_KEY = "body_type"
RESPONSE_NODE_HEADERS_KEY = "headers"
RESPONSE_NODE_HEADERS_TYPE_KEY = "headers_type"
RESPONSE_NODE_ENCODING_KEY = "encoding"
RESPONSE_NODE_HISTORY_KEY = "history"
RESPONSE_NODE_COOKIES_KEY = "cookies"
RESPONSE_NODE_ELAPSED_KEY = "elapsed"
RESPONSE_NODE_REASON_KEY = "reason"
RESPONSE_NODE_URL_KEY = "url"
RESPONSE_NODE_METHOD_KEY = "method"
RESPONSE_NODE_STATUS_CODE_KEY = "status_code"

RESPONSE_NODE_KEY_EQUIVALENCE = {
    "elapsed": RESPONSE_NODE_ELAPSED_KEY,
    "url": RESPONSE_NODE_URL_KEY,
    "urls": RESPONSE_NODE_URL_KEY,
    "reason": RESPONSE_NODE_REASON_KEY,
    "reasons": RESPONSE_NODE_REASON_KEY,
    "encoding": RESPONSE_NODE_ENCODING_KEY,
    "encodings": RESPONSE_NODE_ENCODING_KEY,
    "cookie": RESPONSE_NODE_COOKIES_KEY,
    "cookies": RESPONSE_NODE_COOKIES_KEY,
    "header": RESPONSE_NODE_HEADERS_KEY,
    "headers": RESPONSE_NODE_HEADERS_KEY,
    "method": RESPONSE_NODE_METHOD_KEY,
    "methods": RESPONSE_NODE_METHOD_KEY,
    "history": RESPONSE_NODE_HISTORY_KEY,
    "historie": RESPONSE_NODE_HISTORY_KEY,
    "historys": RESPONSE_NODE_HISTORY_KEY,
    "histore": RESPONSE_NODE_HISTORY_KEY,
    "histores": RESPONSE_NODE_HISTORY_KEY,
    "histories": RESPONSE_NODE_HISTORY_KEY,
    "body_type": RESPONSE_NODE_BODY_TYPE_KEY,
    "body_types": RESPONSE_NODE_BODY_TYPE_KEY,
    "bodys_type": RESPONSE_NODE_BODY_TYPE_KEY,
    "bodies_type": RESPONSE_NODE_BODY_TYPE_KEY,
    "bodies_types": RESPONSE_NODE_BODY_TYPE_KEY,
    "header_type": RESPONSE_NODE_HEADERS_TYPE_KEY,
    "headers_type": RESPONSE_NODE_HEADERS_TYPE_KEY,
    "header_types": RESPONSE_NODE_HEADERS_TYPE_KEY,
    "headers_types": RESPONSE_NODE_HEADERS_TYPE_KEY,
    "body": RESPONSE_NODE_BODY_KEY,
    "bodys": RESPONSE_NODE_BODY_KEY,
    "bodies": RESPONSE_NODE_BODY_KEY,
    "bodie": RESPONSE_NODE_BODY_KEY,
    "status_code": RESPONSE_NODE_STATUS_CODE_KEY,
    "status_codes": RESPONSE_NODE_STATUS_CODE_KEY,
    "statuses_codes": RESPONSE_NODE_STATUS_CODE_KEY,
    "statuses_code": RESPONSE_NODE_STATUS_CODE_KEY,
    "statuss_code": RESPONSE_NODE_STATUS_CODE_KEY,
    "statuss_codes": RESPONSE_NODE_STATUS_CODE_KEY

}

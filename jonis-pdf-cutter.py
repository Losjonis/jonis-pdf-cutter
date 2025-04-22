import PyPDF2

# === Diccionario de mensajes por idioma ===
mensajes = {
    "en": {
        "intro": "Choose your language:",
        "ask_file": "📄 Name of the original PDF file (include .pdf): ",
        "ask_start": "📘 Start page: ",
        "ask_end": "📕 End page: ",
        "ask_output": "💾 Name for the new PDF (include .pdf): ",
        "error_range": "❌ The PDF only has {} pages.",
        "error_not_found": "❌ File '{}' not found.",
        "success": "✅ Done! Pages {} to {} extracted into '{}'.",
        "unknown_error": "❌ An unexpected error occurred: {}"
    },
    "es": {
        "intro": "Elige tu idioma:",
        "ask_file": "📄 Nombre del archivo PDF original (incluye .pdf): ",
        "ask_start": "📘 Página de inicio: ",
        "ask_end": "📕 Página final: ",
        "ask_output": "💾 Nombre para el nuevo PDF (incluye .pdf): ",
        "error_range": "❌ El PDF solo tiene {} páginas.",
        "error_not_found": "❌ No se encontró el archivo '{}'.",
        "success": "✅ ¡Hecho! Se han extraído las páginas {} a {} en '{}'.",
        "unknown_error": "❌ Ha ocurrido un error inesperado: {}"
    },
    "sv": {
        "intro": "Välj ditt språk:",
        "ask_file": "📄 Namn på original-PDF-filen (inkludera .pdf): ",
        "ask_start": "📘 Startsida: ",
        "ask_end": "📕 Slutsida: ",
        "ask_output": "💾 Namn för den nya PDF-filen (inkludera .pdf): ",
        "error_range": "❌ PDF-filen har bara {} sidor.",
        "error_not_found": "❌ Filen '{}' hittades inte.",
        "success": "✅ Klart! Sidor {} till {} extraherades till '{}'.",
        "unknown_error": "❌ Ett oväntat fel inträffade: {}"
    },
    "de": {
        "intro": "Wähle deine Sprache:",
        "ask_file": "📄 Name der Original-PDF-Datei (inkl. .pdf): ",
        "ask_start": "📘 Startseite: ",
        "ask_end": "📕 Endseite: ",
        "ask_output": "💾 Name für die neue PDF-Datei (inkl. .pdf): ",
        "error_range": "❌ Die PDF-Datei hat nur {} Seiten.",
        "error_not_found": "❌ Datei '{}' wurde nicht gefunden.",
        "success": "✅ Fertig! Seiten {} bis {} wurden in '{}' extrahiert.",
        "unknown_error": "❌ Ein unerwarteter Fehler ist aufgetreten: {}"
    },
    "fr": {
        "intro": "Choisissez votre langue :",
        "ask_file": "📄 Nom du fichier PDF original (inclure .pdf) : ",
        "ask_start": "📘 Page de début : ",
        "ask_end": "📕 Page de fin : ",
        "ask_output": "💾 Nom du nouveau fichier PDF (inclure .pdf) : ",
        "error_range": "❌ Le PDF ne contient que {} pages.",
        "error_not_found": "❌ Fichier '{}' introuvable.",
        "success": "✅ Terminé ! Pages {} à {} extraites dans '{}'.",
        "unknown_error": "❌ Une erreur inattendue est survenue : {}"
    },
    "it": {
        "intro": "Scegli la tua lingua:",
        "ask_file": "📄 Nome del file PDF originale (includi .pdf): ",
        "ask_start": "📘 Pagina iniziale: ",
        "ask_end": "📕 Pagina finale: ",
        "ask_output": "💾 Nome per il nuovo PDF (includi .pdf): ",
        "error_range": "❌ Il PDF ha solo {} pagine.",
        "error_not_found": "❌ File '{}' non trovato.",
        "success": "✅ Fatto! Pagine da {} a {} estratte in '{}'.",
        "unknown_error": "❌ Si è verificato un errore imprevisto: {}"
    }
}

# === Menú de idiomas ===
print("Choose your language:")
print("1. English\n2. Spanish\n3. Swedish\n4. German\n5. French\n6. Italian")
opcion = input("👉 Option (1-6): ")

idioma = {
    "1": "en",
    "2": "es",
    "3": "sv",
    "4": "de",
    "5": "fr",
    "6": "it"
}.get(opcion, "en")

txt = mensajes[idioma]

# === Interfaz de usuario ===
try:
    archivo_origen = input(txt["ask_file"])
    pagina_inicio = int(input(txt["ask_start"]))
    pagina_fin = int(input(txt["ask_end"]))
    archivo_destino = input(txt["ask_output"])

    indice_inicio = pagina_inicio - 1
    indice_fin = pagina_fin

    with open(archivo_origen, "rb") as archivo:
        lector = PyPDF2.PdfReader(archivo)
        escritor = PyPDF2.PdfWriter()

        total_paginas = len(lector.pages)

        if indice_inicio < 0 or indice_fin > total_paginas:
            print(txt["error_range"].format(total_paginas))
        else:
            for i in range(indice_inicio, indice_fin):
                escritor.add_page(lector.pages[i])

            with open(archivo_destino, "wb") as salida:
                escritor.write(salida)

            print(txt["success"].format(pagina_inicio, pagina_fin, archivo_destino))

except FileNotFoundError:
    print(txt["error_not_found"].format(archivo_origen))
except Exception as e:
    print(txt["unknown_error"].format(e))

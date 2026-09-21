
import os
import sys

try:
    from openai import OpenAI
except ImportError:  # pragma: no cover
    OpenAI = None


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: no se encontró la variable de entorno OPENAI_API_KEY.")
        print("Configúrala así (Mac/Linux): export OPENAI_API_KEY='tu-clave'")
        print("En Windows (PowerShell): $env:OPENAI_API_KEY='tu-clave'")
        return None
    if OpenAI is None:
        print("Error: la librería 'openai' no está instalada.")
        print("Instálala con: pip install -r requirements.txt")
        return None
    return OpenAI(api_key=api_key)


def llamar_modelo(system_prompt, user_text, model="gpt-4o-mini", max_tokens=500):
    client = get_client()
    if client is None:
        return None
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text},
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error al llamar a la API de OpenAI: {e}")
        return None


def probar_conexion():
    print("Probando conexión con OpenAI...")
    resultado = llamar_modelo(
        "Eres un asistente útil que responde de forma breve.",
        "Responde solo con: 'Conexión exitosa'.",
        max_tokens=20,
    )
    if resultado:
        print(f"El modelo respondió: {resultado}")
        return True
    print("No se pudo verificar la conexión. Revisa tu API Key.")
    return False


def corregir_gramatica():
    texto = input("\nPega el texto a corregir: ").strip()
    if not texto:
        print("No ingresaste ningún texto.")
        return
    print("Revisando tu texto...")
    resultado = llamar_modelo(
        "Eres un corrector experto de español. Corrige gramática, "
        "ortografía y mejora el estilo. Devuelve solo el texto corregido.",
        texto,
    )
    if resultado:
        print("\n--- Texto corregido ---")
        print(resultado)


def generar_texto():
    tema = input("\n¿Sobre qué tema quieres escribir? ").strip()
    if not tema:
        print("No ingresaste ningún tema.")
        return
    print("Tonos: Profesional / Casual / Creativo / Persuasivo")
    tono = input("Elige el tono [Profesional]: ").strip() or "Profesional"
    print("Escribiendo...")
    resultado = llamar_modelo(
        f"Eres un redactor experto. Escribes con tono {tono.lower()}.",
        f"Escribe un texto completo sobre: '{tema}'.",
    )
    if resultado:
        print("\n--- Texto generado ---")
        print(resultado)


def sugerir_continuacion():
    texto = input("\nEscribe el inicio de tu texto: ").strip()
    if not texto:
        print("No ingresaste ningún texto.")
        return
    print("Pensando en ideas...")
    resultado = llamar_modelo(
        "Eres un asistente de escritura creativa. Continúa el texto del "
        "usuario de forma coherente agregando un párrafo más.",
        texto,
    )
    if resultado:
        print("\n--- Sugerencia de continuación ---")
        print(resultado)


def mostrar_menu():
    while True:
        print("\n=== Asistente de Escritura Automática ===")
        print("1. Corrección de gramática y estilo")
        print("2. Generación de texto completo a partir de un tema")
        print("3. Sugerencia de continuación de oraciones")
        print("4. Probar conexión con OpenAI")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            corregir_gramatica()
        elif opcion == "2":
            generar_texto()
        elif opcion == "3":
            sugerir_continuacion()
        elif opcion == "4":
            probar_conexion()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sys.exit(0 if probar_conexion() else 1)
    mostrar_menu()

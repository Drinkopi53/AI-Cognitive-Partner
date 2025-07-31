# -*- coding: utf-8 -*-

"""
AI Cognitive Partner (MVP)

Deskripsi:
Program ini adalah implementasi dari Produk Minimum yang Layak (MVP) untuk AI Cognitive Partner.
Tujuannya adalah untuk bertindak sebagai mitra kognitif yang membantu pengguna mempertajam ide,
mengidentifikasi bias kognitif, dan membangun model mental melalui debat interaktif.

Struktur Program:
- `main()`: Fungsi utama yang menjalankan loop aplikasi.
- `display_menu()`: Menampilkan menu utama kepada pengguna.
- `train_ai()`: Mengelola input teks dari pengguna untuk melatih AI.
- `start_debate()`: Memulai dan mengelola sesi debat interaktif antara pengguna dan AI.
- `detect_cognitive_biases(text)`: Menganalisis teks untuk mendeteksi bias kognitif.
- `generate_ai_response(user_input, history)`: Menghasilkan respons AI selama debat.
- `summarize_debate(history)`: Memberikan ringkasan sesi debat.
- `load_user_data()`: Memuat data pelatihan pengguna dari file.
- `save_user_data(data)`: Menyimpan data pelatihan pengguna ke file.
"""

import json
import random
import os
import re

# Nama file untuk menyimpan data pelatihan pengguna
USER_DATA_FILE = "user_data.json"

# Database sederhana untuk bias kognitif umum (MVP)
COGNITIVE_BIASES = {
    "Pemikiran Hitam-Putih": {
        "keywords": ["selalu", "tidak akan pernah", "semua orang", "tidak seorang pun", "sepenuhnya", "mustahil", "pasti"],
        "explanation": "Saya mendeteksi kemungkinan adanya 'Pemikiran Hitam-Putih' dalam argumen Anda. Ini adalah kecenderungan untuk melihat sesuatu secara absolut (misalnya, selalu/tidak pernah). Apakah ada kemungkinan lain atau pengecualian?"
    },
    "Bias Konfirmasi": {
        "keywords": ["seperti yang saya duga", "ini membuktikan bahwa", "sudah jelas bahwa", "tentu saja"],
        "explanation": "Pernyataan Anda mungkin menunjukkan 'Bias Konfirmasi', yaitu kecenderungan untuk fokus pada informasi yang mendukung keyakinan kita. Sudahkah Anda mempertimbangkan bukti yang mungkin bertentangan dengan pandangan Anda?"
    },
    "Generalisasi Berlebihan": {
        "keywords": ["setiap kali", "semua orang", "semuanya"],
        "explanation": "Ini terdengar seperti 'Generalisasi Berlebihan'. Anda mungkin mengambil satu atau beberapa contoh dan mengasumsikannya berlaku untuk semua kasus. Apakah ini benar-benar berlaku secara universal?"
    }
}

def load_user_data():
    """
    Memuat data (ide dan argumen) pengguna dari file JSON.
    Jika file tidak ada atau rusak, kembalikan data default.
    """
    default_data = {"training_text": ""}
    if not os.path.exists(USER_DATA_FILE):
        return default_data
    try:
        with open(USER_DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                return default_data
            data = json.loads(content)
            if "training_text" not in data or not isinstance(data["training_text"], str):
                data["training_text"] = ""
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return default_data

def save_user_data(data):
    """
    Menyimpan data pengguna ke dalam file JSON.
    """
    with open(USER_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def train_ai():
    """
    Memungkinkan pengguna untuk memasukkan teks untuk melatih AI.
    Teks ini akan disimpan dan digunakan untuk membentuk respons AI.
    """
    print("\n--- Pelatihan AI Personal ---")
    print("Masukkan teks, ide, atau argumen Anda. Ketik 'SELESAI' di baris baru untuk menyimpan.")

    user_input_lines = []
    while True:
        try:
            line = input("> ")
            if line.strip().upper() == 'SELESAI':
                break
            user_input_lines.append(line)
        except EOFError:
            print("\nInput stream berakhir, memproses teks yang dimasukkan...")
            break

    training_text = "\n".join(user_input_lines).strip()

    if training_text:
        user_data = load_user_data()

        if user_data.get("training_text"):
            user_data["training_text"] += "\n" + training_text
        else:
            user_data["training_text"] = training_text

        save_user_data(user_data)

        new_word_count = len(training_text.split())
        total_word_count = len(user_data["training_text"].split())

        print(f"\nTerima kasih! AI telah dilatih dengan {new_word_count} kata baru.")
        print(f"Total kata dalam data pelatihan sekarang: {total_word_count}.")

        if total_word_count >= 1000:
            print("INFO: Kriteria penerimaan (minimal 1000 kata pelatihan) telah terpenuhi.")
    else:
        print("\nTidak ada teks baru yang ditambahkan.")

def detect_cognitive_biases(text):
    """
    Mendeteksi bias kognitif umum dalam teks yang diberikan.
    Mengembalikan nama dan penjelasan bias pertama yang terdeteksi, jika tidak, None.
    """
    text_lower = text.lower()
    for bias, data in COGNITIVE_BIASES.items():
        for keyword in data["keywords"]:
            # Menggunakan word boundary untuk pencocokan yang lebih akurat
            if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                return bias, data["explanation"]
    return None, None

def generate_ai_response(user_input, history):
    """
    Menghasilkan respons AI berdasarkan input pengguna dan riwayat percakapan.
    Untuk MVP, ini akan menggunakan strategi sederhana:
    1. Cari kata kunci dari input pengguna dalam data pelatihan.
    2. Jika ditemukan, ajukan pertanyaan terkait kalimat yang cocok.
    3. Jika tidak, gunakan respons umum untuk memancing diskusi.
    """
    user_data = load_user_data()
    training_text = user_data.get("training_text", "")

    # 1. Gunakan respons umum jika tidak ada data pelatihan
    if not training_text:
        generic_responses = [
            "Mengapa Anda berpikir demikian?",
            "Bisakah Anda menjelaskan lebih lanjut tentang itu?",
            "Apa yang mendasari argumen Anda?",
            "Bagaimana jika kita melihatnya dari sudut pandang yang berbeda?",
            "Itu poin yang menarik. Apa buktinya?"
        ]
        return random.choice(generic_responses)

    # 2. Cari kalimat yang relevan dari data pelatihan
    user_words = set(user_input.lower().split())
    # Memisahkan teks menjadi kalimat dengan lebih baik, menangani beberapa tanda baca.
    sentences = [s.strip() for s in re.split(r'[.!?]+', training_text) if s]

    best_sentence = None
    max_overlap = 0

    for sentence in sentences:
        # Hindari kalimat yang sangat pendek
        if len(sentence.split()) < 4:
            continue

        sentence_words = set(sentence.lower().split())
        overlap = len(user_words.intersection(sentence_words))

        # Prioritaskan tumpang tindih yang lebih besar, tetapi juga acak jika tumpang tindihnya sama
        if overlap > max_overlap:
            max_overlap = overlap
            best_sentence = sentence.strip()

    # 3. Bentuk respons berdasarkan kalimat yang ditemukan
    if best_sentence and max_overlap > 1: # Membutuhkan setidaknya 2 kata yang cocok
        response_formats = [
            f"Anda pernah menyebutkan, \"{best_sentence}.\" Bagaimana ini berhubungan dengan argumen Anda saat ini?",
            f"Itu mengingatkan saya pada pemikiran Anda yang lain: \"{best_sentence}.\" Apakah ada kontradiksi di sini?",
            f"Terkait dengan \"{best_sentence}\", bagaimana Anda akan menanggapi kritik terhadap ide itu?"
        ]
        return random.choice(response_formats)
    else:
        # Gunakan respons umum jika tidak ada yang cocok
        generic_responses = [
            "Saya mengerti. Bagaimana Anda menghubungkan ini dengan ide-ide Anda sebelumnya?",
            "Coba kita gali lebih dalam. Apa asumsi utama Anda di sini?",
            "Menarik. Adakah perspektif lain yang belum kita pertimbangkan?",
            "Bagaimana Anda sampai pada kesimpulan itu?",
        ]
        return random.choice(generic_responses)

def summarize_debate(history):
    """
    Memberikan ringkasan sederhana dari sesi debat untuk membantu visualisasi model mental.
    """
    print("\n\n--- RINGKASAN SESI DEBAT ---")

    if not history:
        print("Tidak ada percakapan yang direkam dalam sesi ini.")
        print("--------------------------")
        return

    user_turns = [turn["message"] for turn in history if turn["speaker"] == "user"]
    ai_responses = [turn["message"] for turn in history if turn["speaker"] == "ai"]
    bias_feedback = [turn["message"] for turn in history if turn["speaker"] == "ai_feedback"]

    print(f"Total Pertukaran: {len(user_turns)} dari Anda, {len(ai_responses)} dari AI.")

    if user_turns:
        print("\nPokok Pikiran Utama Anda:")
        print(f"  - Argumen Pembuka: \"{user_turns[0]}\"")
        if len(user_turns) > 1:
            print(f"  - Argumen Penutup: \"{user_turns[-1]}\"")

    if bias_feedback:
        print("\nMomen Refleksi (Umpan Balik Bias Kognitif yang Diterima):")
        for i, feedback in enumerate(bias_feedback):
            print(f"  - Umpan Balik {i+1}: {feedback}")

    print("\nRingkasan ini dirancang untuk membantu Anda memetakan bagaimana argumen Anda berkembang dan area mana yang bisa direfleksikan.")
    print("--------------------------\n")

def start_debate():
    """
    Memulai sesi debat interaktif dengan AI.
    """
    print("\n--- Mode Debat Interaktif ---")
    print("Anda sekarang dalam mode debat. Ketik 'AKHIRI DEBAT' untuk menyelesaikan sesi.")

    debate_history = []

    while True:
        try:
            user_input = input("Anda: ")
        except EOFError:
            print("\nInput stream berakhir, mengakhiri debat...")
            break

        if user_input.strip().upper() == 'AKHIRI DEBAT':
            print("\nSesi debat telah berakhir.")
            summarize_debate(debate_history)
            break

        debate_history.append({"speaker": "user", "message": user_input})

        # Deteksi bias dan berikan umpan balik jika ada
        bias_name, bias_explanation = detect_cognitive_biases(user_input)
        if bias_name:
            print("\n--- UMPAN BALIK BIAS KOGNITIF ---")
            print(f"AI  : (Info) {bias_explanation}")
            print("---------------------------------\n")
            # Catat umpan balik bias dalam riwayat
            debate_history.append({"speaker": "ai_feedback", "message": bias_explanation})

        # Hasilkan respons AI
        ai_response = generate_ai_response(user_input, debate_history)
        print(f"AI  : {ai_response}")

        debate_history.append({"speaker": "ai", "message": ai_response})

def display_menu():
    """
    Menampilkan menu utama aplikasi.
    """
    print("\n--- AI Cognitive Partner (MVP) ---")
    print("1. Latih AI dengan ide-ide Anda")
    print("2. Mulai sesi debat dengan AI")
    print("3. Keluar")
    return input("Pilih opsi (1-3): ")

def main():
    """
    Fungsi utama untuk menjalankan aplikasi.
    """
    print("Selamat datang di AI Cognitive Partner.")

    while True:
        choice = display_menu()

        if choice == '1':
            train_ai()
        elif choice == '2':
            start_debate()
        elif choice == '3':
            print("Terima kasih telah menggunakan AI Cognitive Partner. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

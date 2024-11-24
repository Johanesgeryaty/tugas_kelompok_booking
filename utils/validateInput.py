def validate_input(prompt, valid_options):
    """Memvalidasi input user"""
    while True:
        value = input(prompt).lower().strip()
        if value in valid_options:
            return value
        print(f"Input tidak valid. Pilihan yang tersedia: {', '.join(valid_options).title()}")
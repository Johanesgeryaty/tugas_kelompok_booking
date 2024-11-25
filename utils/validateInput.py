def validate_input(prompt, valid_options):
    """Memvalidasi input user"""
    while True:
        value = input(prompt).lower().strip()
        
        for i in range(len(valid_options)):
            if value in valid_options[i] or value == valid_options[i] :
                return valid_options[i]
            continue
        print(f"Input tidak valid. Pilihan yang tersedia: {', '.join(valid_options).title()}")
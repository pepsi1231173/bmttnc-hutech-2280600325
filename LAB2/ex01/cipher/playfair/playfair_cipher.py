class PlayfairCipher:
    def __init__(self):
        pass

    def generate_key_matrix(self, key):
        key = key.upper().replace("J", "I")  # Replace 'J' with 'I' as per Playfair rules
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_matrix = []
        used_chars = set()

        # Add key characters to the matrix
        for char in key:
            if char not in used_chars and char in alphabet:
                key_matrix.append(char)
                used_chars.add(char)

        # Add remaining alphabet characters
        for char in alphabet:
            if char not in used_chars:
                key_matrix.append(char)

        # Convert to 5x5 matrix
        return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_position(self, char, key_matrix):
        for row in range(5):
            for col in range(5):
                if key_matrix[row][col] == char:
                    return row, col
        return None

    def encrypt(self, text, key):
        key_matrix = self.generate_key_matrix(key)
        text = text.upper().replace("J", "I").replace(" ", "")
        encrypted_text = ""

        # Prepare text in pairs
        i = 0
        while i < len(text):
            char1 = text[i]
            char2 = text[i + 1] if i + 1 < len(text) else "X"

            if char1 == char2:  # If both characters are the same, add 'X'
                char2 = "X"
                i += 1
            else:
                i += 2

            row1, col1 = self.find_position(char1, key_matrix)
            row2, col2 = self.find_position(char2, key_matrix)

            # Apply Playfair rules
            if row1 == row2:  # Same row
                encrypted_text += key_matrix[row1][(col1 + 1) % 5]
                encrypted_text += key_matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Same column
                encrypted_text += key_matrix[(row1 + 1) % 5][col1]
                encrypted_text += key_matrix[(row2 + 1) % 5][col2]
            else:  # Rectangle swap
                encrypted_text += key_matrix[row1][col2]
                encrypted_text += key_matrix[row2][col1]

        return encrypted_text

    def decrypt(self, text, key):
        key_matrix = self.generate_key_matrix(key)
        text = text.upper().replace(" ", "")
        decrypted_text = ""

        # Process text in pairs
        i = 0
        while i < len(text):
            char1 = text[i]
            char2 = text[i + 1] if i + 1 < len(text) else "X"
            i += 2

            row1, col1 = self.find_position(char1, key_matrix)
            row2, col2 = self.find_position(char2, key_matrix)

            # Apply Playfair rules
            if row1 == row2:  # Same row
                decrypted_text += key_matrix[row1][(col1 - 1) % 5]
                decrypted_text += key_matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Same column
                decrypted_text += key_matrix[(row1 - 1) % 5][col1]
                decrypted_text += key_matrix[(row2 - 1) % 5][col2]
            else:  # Rectangle swap
                decrypted_text += key_matrix[row1][col2]
                decrypted_text += key_matrix[row2][col1]

        return decrypted_text
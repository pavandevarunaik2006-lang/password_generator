import secrets
import string


class PasswordGenerator:
    """A secure password generator class."""
    
    def __init__(self):
        self.uppercase = string.ascii_uppercase
        self.lowercase = string.ascii_lowercase
        self.digits = string.digits
        self.special = string.punctuation
    
    def generate_password(self, length, use_uppercase, use_lowercase, use_digits, use_special):
        """
        Generate a secure password based on user preferences.
        
        Args:
            length (int): Desired password length
            use_uppercase (bool): Include uppercase letters
            use_lowercase (bool): Include lowercase letters
            use_digits (bool): Include numbers
            use_special (bool): Include special characters
            
        Returns:
            str: Generated password or error message
        """
        # Validate that at least one character type is selected
        if not any([use_uppercase, use_lowercase, use_digits, use_special]):
            return None, "Error: Please select at least one character type!"
        
        # Validate password length
        if length < 4:
            return None, "Error: Password length must be at least 4 characters!"
        
        if length > 128:
            return None, "Error: Password length must be 128 characters or less!"
        
        # Build character pool
        char_pool = ""
        required_chars = []
        
        if use_uppercase:
            char_pool += self.uppercase
            required_chars.append(secrets.choice(self.uppercase))
        
        if use_lowercase:
            char_pool += self.lowercase
            required_chars.append(secrets.choice(self.lowercase))
        
        if use_digits:
            char_pool += self.digits
            required_chars.append(secrets.choice(self.digits))
        
        if use_special:
            char_pool += self.special
            required_chars.append(secrets.choice(self.special))
        
        # Generate remaining characters
        remaining_length = length - len(required_chars)
        
        if remaining_length < 0:
            remaining_length = 0
            required_chars = required_chars[:length]
        
        password_chars = required_chars + [
            secrets.choice(char_pool) for _ in range(remaining_length)
        ]
        
        # Shuffle to ensure required characters aren't always at the start
        # Using secrets.SystemRandom for cryptographically secure shuffling
        random_gen = secrets.SystemRandom()
        random_gen.shuffle(password_chars)
        
        password = ''.join(password_chars)
        return password, None


def main():
    """Main function for command-line interface."""
    print("=" * 50)
    print("       SECURE PASSWORD GENERATOR")
    print("=" * 50)
    print()
    
    generator = PasswordGenerator()
    
    try:
        # Get password length
        length = int(input("Enter password length (4-128): "))
        
        # Get character type preferences
        print("\nSelect character types to include:")
        use_uppercase = input("Include uppercase letters (A-Z)? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters (a-z)? (y/n): ").lower() == 'y'
        use_digits = input("Include numbers (0-9)? (y/n): ").lower() == 'y'
        use_special = input("Include special characters (!@#$...)? (y/n): ").lower() == 'y'
        
        # Generate password
        password, error = generator.generate_password(
            length, use_uppercase, use_lowercase, use_digits, use_special
        )
        
        if error:
            print(f"\n❌ {error}")
        else:
            print("\n" + "=" * 50)
            print("✅ Your secure password:")
            print(f"\n    {password}\n")
            print("=" * 50)
            print("\n⚠️  Please store this password securely!")
    
    except ValueError:
        print("\n❌ Error: Please enter a valid number for password length!")
    except KeyboardInterrupt:
        print("\n\nPassword generation cancelled.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


if __name__ == "__main__":
    main()

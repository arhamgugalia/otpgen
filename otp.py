import random


def generate_otp(length=6):
    """Generate a numeric one-time password of the given length."""
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


if __name__ == "__main__":
    otp = generate_otp()
    print(f"Your OTP is: {otp}")

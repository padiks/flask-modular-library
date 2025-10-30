# Base configuration class that contains common settings for all environments.
class Config:
    # Secret key used by Flask for session management and encryption.
    # It should be kept secret in production to prevent security vulnerabilities.
    SECRET_KEY = "your_secret_key"

# Development-specific configuration class, which inherits from Config.
class DevelopmentConfig(Config):
    # Enable debug mode in development for better error messages and live reloading.
    DEBUG = True

# Production-specific configuration class, which also inherits from Config.
class ProductionConfig(Config):
    # Disable debug mode in production for performance and security reasons.
    DEBUG = False

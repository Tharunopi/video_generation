import logging
import sys
from datetime import datetime

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class ColoredFormatter(logging.Formatter):
    """Custom formatter with colors for different log levels"""
    
    FORMATS = {
        logging.DEBUG: Colors.CYAN + "%(asctime)s | DEBUG    | %(name)s | %(message)s" + Colors.ENDC,
        logging.INFO: Colors.GREEN + "%(asctime)s | INFO     | %(name)s | %(message)s" + Colors.ENDC,
        logging.WARNING: Colors.YELLOW + "%(asctime)s | WARNING  | %(name)s | %(message)s" + Colors.ENDC,
        logging.ERROR: Colors.RED + "%(asctime)s | ERROR    | %(name)s | %(message)s" + Colors.ENDC,
        logging.CRITICAL: Colors.RED + Colors.BOLD + "%(asctime)s | CRITICAL | %(name)s | %(message)s" + Colors.ENDC,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Get a configured logger for a module.
    
    Args:
        name: Name of the logger (usually __name__)
        level: Logging level (default: INFO)
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Avoid adding handlers multiple times
    if not logger.handlers:
        logger.setLevel(level)
        
        # Console handler with colors
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(ColoredFormatter())
        logger.addHandler(console_handler)
    
    return logger

def log_step(logger: logging.Logger, step_name: str, status: str = "started"):
    """Log a workflow step with visual formatting"""
    if status == "started":
        logger.info(f"{'='*50}")
        logger.info(f"STEP: {step_name}")
        logger.info(f"{'='*50}")
    elif status == "completed":
        logger.info(f"{step_name} completed successfully")
    elif status == "failed":
        logger.error(f"{step_name} failed")

def log_state(logger: logging.Logger, state: dict, keys: list = None):
    """Log specific state values for debugging"""
    logger.debug("Current state snapshot:")
    keys_to_log = keys or list(state.keys())
    for key in keys_to_log:
        if key in state:
            value = state[key]
            # Truncate long values
            if isinstance(value, str) and len(value) > 100:
                value = value[:100] + "..."
            elif isinstance(value, list) and len(value) > 3:
                value = f"[{len(value)} items]"
            logger.debug(f"  {key}: {value}")

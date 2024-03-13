# demonstrate the logging api in Python
import logging

# TODO: use the built-in logging module
logging.basicConfig(level=logging.DEBUG, filename='logoutput.log', filemode='w')

# TODO: Use basicConfig to configure logging

# TODO: Try out each of the log levels
logging.debug('This is debug level message....')
logging.info('This is info level message....')
logging.warning('This is warning level message....')
logging.error('This is error level message....')
logging.critical('This is critical level message....')

# TODO: Output formatted strings to the log

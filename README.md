Stepik TASK:
    Different interface languages

# INSTRUCTION:

You may use any language, that are in 'languages' dictionary (e.g.: 'en-gb', 'uk', 'es', 'fr', 'ar', 'ko' and so on)
    pytest -sv --language=uk test_items.py

Also ypu may use different browsers ('chrome' or 'firefox'). By default is used 'chrome' browser.
    pytest -sv --browser_name=firefox --language=uk test_items.py

By running script without '-sv' arguments will show the result, without showing 'print()' outputs in terminal
    pytest --language=uk test_items.py

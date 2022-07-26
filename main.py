#!/usr/bin/env python3
import sys
from sodoku_controller import SodokuController

def main():
    app = SodokuController()
    sys.exit(app.run())

if __name__ == '__main__':
    main()